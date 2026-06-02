import cv2

from .camera_service import (
    CameraService
)

from .face_detection_service import (
    FaceDetectionService
)

from .quality_assessment_service import (
    QualityAssessmentService
)

from ..ai.recognition_engine import (
    RecognitionEngine
)

from ..utils.image_utils import (
    ImageUtils
)


class FaceRecognitionService:

    def __init__(self, env):

        self.env = env

        self.camera_service = (
            CameraService()
        )

        self.face_detection_service = (
            FaceDetectionService()
        )

        self.quality_service = (
            QualityAssessmentService()
        )

        self.recognition_engine = (
            RecognitionEngine()
        )

    def recognize_student(self):

        face_repository = self.env[
            'face.repository'
        ]

        face_records = (
            face_repository
            .get_registered_face_dataset()
        )

        if not face_records:

            return {
                "recognized": False,
                "message":
                    "No registered dataset found"
            }

        if not (
            self.camera_service
            .open_camera()
        ):

            return {
                "recognized": False,
                "message":
                    "Unable to open camera"
            }

        self.camera_service.create_window(
            "Face Recognition"
        )

        result = None

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
                    "Face Recognition",
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
                    "Face Recognition",
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

                quality_result = (
                    self.quality_service
                    .assess_quality(
                        frame,
                        face_detected=True,
                        eyes_visible=True,
                        face_centered=True,
                        face_angle_valid=True
                    )
                )

                if not (
                    quality_result[
                        "is_acceptable"
                    ]
                ):
                    continue

                result = (
                    self.recognition_engine
                    .recognize(
                        frame,
                        face_records
                    )
                )

                if not result:
                    continue

                if result.get(
                    "recognized"
                ):

                    print(
                        "Student Recognized"
                    )

                    break

        finally:

            self.camera_service.close()

        return result

    def identify_student(self):

        result = (
            self.recognize_student()
        )

        if not result:

            return None

        if not result.get(
            "recognized"
        ):

            return None

        return result.get(
            "student"
        )

    def verify_student(
        self,
        student
    ):

        face_repository = self.env[
            'face.repository'
        ]

        face_records = (
            face_repository
            .get_student_faces(
                student.id
            )
        )

        if not face_records:

            return {
                "verified": False,
                "message":
                    "No face data found"
            }

        if not (
            self.camera_service
            .open_camera()
        ):

            return {
                "verified": False,
                "message":
                    "Unable to open camera"
            }

        self.camera_service.create_window(
            "Face Verification"
        )

        result = None

        try:

            while True:

                success, frame = (
                    self.camera_service
                    .read_frame()
                )

                if not success:
                    break

                self.camera_service.show_frame(
                    "Face Verification",
                    frame
                )

                key = (
                    self.camera_service
                    .wait_key(1)
                )

                if key == 27:
                    break

                recognition_result = (
                    self.recognition_engine
                    .recognize(
                        frame,
                        face_records
                    )
                )

                if not recognition_result:
                    continue

                if recognition_result[
                    "recognized"
                ]:

                    result = {
                        "verified": True,
                        "student":
                            student,
                        "confidence_score":
                            recognition_result[
                                "confidence_score"
                            ]
                    }

                    break

        finally:

            self.camera_service.close()

        return result