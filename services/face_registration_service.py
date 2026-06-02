import cv2

from odoo import fields

from .camera_service import (
    CameraService
)

from .face_detection_service import (
    FaceDetectionService
)

from .eye_detection_service import (
    EyeDetectionService
)

from .face_angle_service import (
    FaceAngleService
)

from .quality_assessment_service import (
    QualityAssessmentService
)

from .embedding_service import (
    EmbeddingService
)

from ..utils.image_utils import (
    ImageUtils
)

from ..config.quality_config import (
    QualityConfig
)


class FaceRegistrationService:

    def __init__(self, env):

        self.env = env

        self.camera_service = (
            CameraService()
        )

        self.face_detection_service = (
            FaceDetectionService()
        )

        self.eye_detection_service = (
            EyeDetectionService()
        )

        self.face_angle_service = (
            FaceAngleService()
        )

        self.quality_service = (
            QualityAssessmentService()
        )

        self.embedding_service = (
            EmbeddingService()
        )

    def register_student(
        self,
        student
    ):

        target_images = 20

        captured_count = 0

        if not (
            self.camera_service
            .open_camera()
        ):

            raise Exception(
                "Unable to open camera"
            )

        self.camera_service.create_window(
            "Face Registration"
        )

        try:

            while True:

                success, frame = (
                    self.camera_service
                    .read_frame()
                )

                if not success:
                    break

                cv2.putText(
                    frame,
                    f"Captured: {captured_count}/{target_images}",
                    (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2
                )

                cv2.putText(
                    frame,
                    "Press ESC to Exit",
                    (20, 80),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 255, 255),
                    2
                )

                self.camera_service.show_frame(
                    "Face Registration",
                    frame
                )

                key = (
                    self.camera_service
                    .wait_key(1)
                )

                if key == 27:
                    break

                rgb_frame = (
                    ImageUtils
                    .convert_to_rgb(
                        frame
                    )
                )

                detection_results = (
                    self.face_detection_service
                    .detect_faces(
                        rgb_frame
                    )
                )

                if not (
                    self.face_detection_service
                    .is_single_face_detected(
                        detection_results
                    )
                ):
                    continue

                mesh_results = (
                    self.eye_detection_service
                    .detect_landmarks(
                        rgb_frame
                    )
                )

                landmarks = (
                    self.eye_detection_service
                    .get_primary_face_landmarks(
                        mesh_results
                    )
                )

                if not landmarks:
                    continue

                angle_data = (
                    self.face_angle_service
                    .get_face_angle_data(
                        landmarks,
                        frame.shape[1],
                        frame.shape[0]
                    )
                )

                eyes_visible = (
                    self.eye_detection_service
                    .are_eyes_visible(
                        landmarks,
                        frame.shape[1],
                        frame.shape[0],
                        QualityConfig
                        .MINIMUM_EYE_DISTANCE
                    )
                )

                quality_result = (
                    self.quality_service
                    .assess_quality(
                        frame,
                        True,
                        eyes_visible,
                        True,
                        angle_data[
                            "is_straight"
                        ]
                    )
                )

                if not (
                    quality_result[
                        "is_acceptable"
                    ]
                ):
                    continue

                embedding = (
                    self.embedding_service
                    .generate_serialized_embedding(
                        frame
                    )
                )

                if not embedding:
                    continue

                image_base64 = (
                    ImageUtils
                    .image_to_base64(
                        frame
                    )
                )

                self.env[
                    'face.repository'
                ].create_face({

                    'student_id':
                        student.id,

                    'image':
                        image_base64,

                    'embedding':
                        embedding,

                    'quality_score':
                        quality_result[
                            'quality_score'
                        ],

                    'brightness_score':
                        quality_result[
                            'brightness_score'
                        ],

                    'blur_score':
                        quality_result[
                            'blur_score'
                        ],

                    'face_angle':
                        angle_data[
                            'yaw_angle'
                        ],

                    'eyes_visible':
                        eyes_visible,

                    'face_centered':
                        True
                })

                if captured_count == 0:

                    student.write({

                        'image':
                            image_base64
                    })

                captured_count += 1

                print(
                    f"Captured "
                    f"{captured_count}/"
                    f"{target_images}"
                )

                if captured_count >= target_images:

                    student.write({

                        'face_registered':
                            True,

                        'registration_date':
                            fields.Datetime.now()
                    })

                    print(
                        "Face Registration "
                        "Completed"
                    )

                    break

        finally:

            self.camera_service.close()

        return True