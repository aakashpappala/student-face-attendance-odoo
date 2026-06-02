class QualityConfig:

    # =========================
    # Overall Quality
    # =========================

    MINIMUM_QUALITY_SCORE = 70

    EXCELLENT_QUALITY_SCORE = 90

    # =========================
    # Blur Detection
    # =========================

    MINIMUM_BLUR_SCORE = 100

    IDEAL_BLUR_SCORE = 200

    # =========================
    # Brightness
    # =========================

    MINIMUM_BRIGHTNESS = 80

    MAXIMUM_BRIGHTNESS = 200

    IDEAL_BRIGHTNESS = 140

    # =========================
    # Face Position
    # =========================

    MAX_FACE_CENTER_OFFSET = 50

    # Pixels

    # =========================
    # Face Size
    # =========================

    MINIMUM_FACE_WIDTH = 120

    MINIMUM_FACE_HEIGHT = 120

    # =========================
    # Face Angle
    # =========================

    MAX_FACE_ANGLE = 15

    # Degrees

    # =========================
    # Eye Validation
    # =========================

    REQUIRE_BOTH_EYES = True

    MINIMUM_EYE_DISTANCE = 30

    # Pixels

    # =========================
    # Registration Dataset
    # =========================

    MINIMUM_VALID_IMAGES = 20

    # =========================
    # Quality Weights
    # =========================

    FACE_DETECTION_WEIGHT = 40

    EYE_VISIBILITY_WEIGHT = 20

    BLUR_WEIGHT = 20

    BRIGHTNESS_WEIGHT = 20