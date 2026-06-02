import time


class AntiSpoofingService:

    def __init__(self):

        self.blink_count = 0

        self.last_eye_state = True

        self.head_movements = 0

        self.previous_yaw = 0

        self.previous_pitch = 0

        self.start_time = (
            time.time()
        )

    def detect_blink(
        self,
        left_eye_open,
        right_eye_open
    ):

        current_eye_state = (
            left_eye_open and
            right_eye_open
        )

        if (
            self.last_eye_state
            and
            not current_eye_state
        ):

            self.blink_count += 1

        self.last_eye_state = (
            current_eye_state
        )

        return (
            self.blink_count > 0
        )

    def detect_head_movement(
        self,
        yaw_angle,
        pitch_angle
    ):

        yaw_diff = abs(
            yaw_angle -
            self.previous_yaw
        )

        pitch_diff = abs(
            pitch_angle -
            self.previous_pitch
        )

        if (
            yaw_diff > 5
            or
            pitch_diff > 5
        ):

            self.head_movements += 1

        self.previous_yaw = (
            yaw_angle
        )

        self.previous_pitch = (
            pitch_angle
        )

        return (
            self.head_movements >= 2
        )

    def validate_live_face(
        self,
        left_eye_open,
        right_eye_open,
        yaw_angle,
        pitch_angle
    ):

        blink_detected = (
            self.detect_blink(
                left_eye_open,
                right_eye_open
            )
        )

        movement_detected = (
            self.detect_head_movement(
                yaw_angle,
                pitch_angle
            )
        )

        is_live = (
            blink_detected
            or
            movement_detected
        )

        return {

            "is_live":
                is_live,

            "blink_detected":
                blink_detected,

            "movement_detected":
                movement_detected,

            "blink_count":
                self.blink_count,

            "head_movements":
                self.head_movements
        }

    def validate_liveness_timeout(
        self,
        timeout_seconds=10
    ):

        elapsed_time = (
            time.time()
            -
            self.start_time
        )

        return (
            elapsed_time <=
            timeout_seconds
        )

    def get_liveness_score(
        self
    ):

        score = 0

        if self.blink_count > 0:

            score += 50

        if self.head_movements > 0:

            score += 50

        return min(
            score,
            100
        )

    def reset(self):

        self.blink_count = 0

        self.head_movements = 0

        self.previous_yaw = 0

        self.previous_pitch = 0

        self.last_eye_state = True

        self.start_time = (
            time.time()
        )