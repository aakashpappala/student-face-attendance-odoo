import cv2

from ..config.quality_config import (
    QualityConfig
)

from ..utils.validation_utils import (
    ValidationUtils
)


class QualityAssessmentService:

    def calculate_brightness(
        self,
        frame
    ):

        gray = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2GRAY
        )

        return float(
            gray.mean()
        )

    def calculate_blur_score(
        self,
        frame
    ):

        gray = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2GRAY
        )

        return float(
            cv2.Laplacian(
                gray,
                cv2.CV_64F
            ).var()
        )

    def is_brightness_valid(
        self,
        brightness
    ):

        return (
            QualityConfig.MINIMUM_BRIGHTNESS
            <= brightness <=
            QualityConfig.MAXIMUM_BRIGHTNESS
        )

    def is_blur_valid(
        self,
        blur_score
    ):

        return (
            blur_score >=
            QualityConfig.MINIMUM_BLUR_SCORE
        )

    def calculate_quality_score(
        self,
        face_detected,
        eyes_visible,
        brightness,
        blur_score,
        face_centered,
        face_angle_valid
    ):

        score = 0

        # Face Detection
        if face_detected:

            score += (
                QualityConfig
                .FACE_DETECTION_WEIGHT
            )

        # Eyes
        if eyes_visible:

            score += (
                QualityConfig
                .EYE_VISIBILITY_WEIGHT
            )

        # Blur
        if self.is_blur_valid(
            blur_score
        ):

            score += (
                QualityConfig
                .BLUR_WEIGHT
            )

        # Brightness
        if self.is_brightness_valid(
            brightness
        ):

            score += (
                QualityConfig
                .BRIGHTNESS_WEIGHT
            )

        # Face Center
        if face_centered:

            score += 10

        # Face Angle
        if face_angle_valid:

            score += 10

        return min(
            score,
            100
        )

    def assess_quality(
        self,
        frame,
        face_detected,
        eyes_visible,
        face_centered,
        face_angle_valid
    ):

        brightness = (
            self.calculate_brightness(
                frame
            )
        )

        blur_score = (
            self.calculate_blur_score(
                frame
            )
        )

        quality_score = (
            self.calculate_quality_score(
                face_detected,
                eyes_visible,
                brightness,
                blur_score,
                face_centered,
                face_angle_valid
            )
        )

        return {
            "quality_score":
                quality_score,

            "brightness_score":
                round(
                    brightness,
                    2
                ),

            "blur_score":
                round(
                    blur_score,
                    2
                ),

            "brightness_valid":
                self.is_brightness_valid(
                    brightness
                ),

            "blur_valid":
                self.is_blur_valid(
                    blur_score
                ),

            "is_acceptable":
                quality_score >=
                QualityConfig
                .MINIMUM_QUALITY_SCORE
        }

    def validate_registration_frame(
        self,
        quality_result
    ):

        return (
            quality_result[
                "is_acceptable"
            ]
        )