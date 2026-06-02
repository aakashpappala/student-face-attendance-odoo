import mediapipe as mp

from ..utils.validation_utils import (
    ValidationUtils
)


class EyeDetectionService:

    LEFT_EYE_INDEX = 33
    RIGHT_EYE_INDEX = 263

    def __init__(self):

        self.face_mesh = (
            mp.solutions.face_mesh
            .FaceMesh(
                static_image_mode=False,
                max_num_faces=1,
                refine_landmarks=True,
                min_detection_confidence=0.5,
                min_tracking_confidence=0.5
            )
        )

    def detect_landmarks(
        self,
        rgb_frame
    ):

        return self.face_mesh.process(
            rgb_frame
        )

    def get_primary_face_landmarks(
        self,
        mesh_results
    ):

        if not (
            mesh_results and
            mesh_results.multi_face_landmarks
        ):
            return None

        return (
            mesh_results
            .multi_face_landmarks[0]
        )

    def get_left_eye(
        self,
        face_landmarks,
        frame_width,
        frame_height
    ):

        landmark = (
            face_landmarks
            .landmark[
                self.LEFT_EYE_INDEX
            ]
        )

        return (
            int(
                landmark.x *
                frame_width
            ),
            int(
                landmark.y *
                frame_height
            )
        )

    def get_right_eye(
        self,
        face_landmarks,
        frame_width,
        frame_height
    ):

        landmark = (
            face_landmarks
            .landmark[
                self.RIGHT_EYE_INDEX
            ]
        )

        return (
            int(
                landmark.x *
                frame_width
            ),
            int(
                landmark.y *
                frame_height
            )
        )

    def get_eye_distance(
        self,
        left_eye,
        right_eye
    ):

        x1, y1 = left_eye
        x2, y2 = right_eye

        distance = (
            (
                (x2 - x1) ** 2 +
                (y2 - y1) ** 2
            ) ** 0.5
        )

        return distance

    def are_eyes_visible(
        self,
        face_landmarks,
        frame_width,
        frame_height,
        minimum_distance
    ):

        left_eye = self.get_left_eye(
            face_landmarks,
            frame_width,
            frame_height
        )

        right_eye = self.get_right_eye(
            face_landmarks,
            frame_width,
            frame_height
        )

        eye_distance = (
            self.get_eye_distance(
                left_eye,
                right_eye
            )
        )

        return (
            ValidationUtils
            .are_both_eyes_visible(
                eye_distance >=
                minimum_distance,
                eye_distance >=
                minimum_distance
            )
        )

    def get_eye_data(
        self,
        face_landmarks,
        frame_width,
        frame_height
    ):

        left_eye = self.get_left_eye(
            face_landmarks,
            frame_width,
            frame_height
        )

        right_eye = self.get_right_eye(
            face_landmarks,
            frame_width,
            frame_height
        )

        eye_distance = (
            self.get_eye_distance(
                left_eye,
                right_eye
            )
        )

        return {
            "left_eye": left_eye,
            "right_eye": right_eye,
            "eye_distance": eye_distance
        }