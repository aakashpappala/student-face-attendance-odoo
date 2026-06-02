import math


class FaceAngleService:

    NOSE_TIP_INDEX = 1

    LEFT_FACE_INDEX = 234

    RIGHT_FACE_INDEX = 454

    FOREHEAD_INDEX = 10

    CHIN_INDEX = 152

    def get_face_angle_data(
        self,
        face_landmarks,
        frame_width,
        frame_height
    ):

        nose = self._get_landmark(
            face_landmarks,
            self.NOSE_TIP_INDEX,
            frame_width,
            frame_height
        )

        left_face = self._get_landmark(
            face_landmarks,
            self.LEFT_FACE_INDEX,
            frame_width,
            frame_height
        )

        right_face = self._get_landmark(
            face_landmarks,
            self.RIGHT_FACE_INDEX,
            frame_width,
            frame_height
        )

        forehead = self._get_landmark(
            face_landmarks,
            self.FOREHEAD_INDEX,
            frame_width,
            frame_height
        )

        chin = self._get_landmark(
            face_landmarks,
            self.CHIN_INDEX,
            frame_width,
            frame_height
        )

        yaw_angle = self.calculate_yaw(
            nose,
            left_face,
            right_face
        )

        pitch_angle = self.calculate_pitch(
            nose,
            forehead,
            chin
        )

        return {
            "yaw_angle": yaw_angle,
            "pitch_angle": pitch_angle,
            "is_straight": (
                abs(yaw_angle) <= 15 and
                abs(pitch_angle) <= 15
            )
        }

    def calculate_yaw(
        self,
        nose,
        left_face,
        right_face
    ):

        left_distance = abs(
            nose[0] - left_face[0]
        )

        right_distance = abs(
            right_face[0] - nose[0]
        )

        total_distance = (
            left_distance +
            right_distance
        )

        if total_distance == 0:

            return 0

        yaw = (
            (
                right_distance -
                left_distance
            )
            /
            total_distance
        ) * 100

        return round(
            yaw,
            2
        )

    def calculate_pitch(
        self,
        nose,
        forehead,
        chin
    ):

        upper_distance = abs(
            nose[1] - forehead[1]
        )

        lower_distance = abs(
            chin[1] - nose[1]
        )

        total_distance = (
            upper_distance +
            lower_distance
        )

        if total_distance == 0:

            return 0

        pitch = (
            (
                lower_distance -
                upper_distance
            )
            /
            total_distance
        ) * 100

        return round(
            pitch,
            2
        )

    def is_looking_left(
        self,
        yaw_angle
    ):

        return yaw_angle < -15

    def is_looking_right(
        self,
        yaw_angle
    ):

        return yaw_angle > 15

    def is_looking_up(
        self,
        pitch_angle
    ):

        return pitch_angle < -15

    def is_looking_down(
        self,
        pitch_angle
    ):

        return pitch_angle > 15

    def is_straight_face(
        self,
        yaw_angle,
        pitch_angle
    ):

        return (
            abs(yaw_angle) <= 15 and
            abs(pitch_angle) <= 15
        )

    def _get_landmark(
        self,
        face_landmarks,
        index,
        frame_width,
        frame_height
    ):

        landmark = (
            face_landmarks
            .landmark[index]
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