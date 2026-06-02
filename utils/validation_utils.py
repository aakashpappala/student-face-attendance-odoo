class ValidationUtils:

    @staticmethod
    def is_not_empty(value):

        return (
            value is not None and
            value != ""
        )

    @staticmethod
    def is_positive_number(value):

        return (
            isinstance(
                value,
                (int, float)
            )
            and value > 0
        )

    @staticmethod
    def is_between(
        value,
        minimum,
        maximum
    ):

        return (
            minimum <= value <= maximum
        )

    @staticmethod
    def is_valid_quality_score(
        score
    ):

        return (
            0 <= score <= 100
        )

    @staticmethod
    def is_valid_similarity_score(
        score
    ):

        return (
            0 <= score <= 1
        )

    @staticmethod
    def is_single_face_detected(
        detections
    ):

        if not detections:
            return False

        return len(
            detections
        ) == 1

    @staticmethod
    def are_both_eyes_visible(
        left_eye_detected,
        right_eye_detected
    ):

        return (
            left_eye_detected and
            right_eye_detected
        )

    @staticmethod
    def is_face_centered(
        face_center_x,
        face_center_y,
        frame_center_x,
        frame_center_y,
        max_offset
    ):

        x_diff = abs(
            face_center_x -
            frame_center_x
        )

        y_diff = abs(
            face_center_y -
            frame_center_y
        )

        return (
            x_diff <= max_offset and
            y_diff <= max_offset
        )

    @staticmethod
    def is_face_size_valid(
        face_width,
        face_height,
        min_width,
        min_height
    ):

        return (
            face_width >= min_width and
            face_height >= min_height
        )

    @staticmethod
    def is_face_angle_valid(
        angle,
        max_angle
    ):

        return abs(
            angle
        ) <= max_angle

    @staticmethod
    def can_mark_attendance(
        already_marked
    ):

        return not already_marked

    @staticmethod
    def is_registration_complete(
        captured_count,
        required_count
    ):

        return (
            captured_count >=
            required_count
        )