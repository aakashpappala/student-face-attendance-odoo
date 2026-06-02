class CameraConfig:

    # =========================
    # Camera Source
    # =========================

    DEFAULT_CAMERA_INDEX = 0

    CAMERA_SOURCE_TYPE = "webcam"

    # webcam
    # usb
    # ip_camera
    # rtsp

    # =========================
    # Resolution
    # =========================

    FRAME_WIDTH = 1280

    FRAME_HEIGHT = 720

    # =========================
    # Performance
    # =========================

    FPS = 30

    BUFFER_SIZE = 1

    # =========================
    # Timeouts
    # =========================

    CAMERA_STARTUP_TIMEOUT = 10

    FRAME_READ_TIMEOUT = 5

    # =========================
    # Registration
    # =========================

    REGISTRATION_WINDOW_NAME = (
        "Face Registration"
    )

    # =========================
    # Recognition
    # =========================

    RECOGNITION_WINDOW_NAME = (
        "Face Recognition"
    )

    # =========================
    # Display
    # =========================

    SHOW_FPS = True

    SHOW_GUIDE_OVERLAY = True

    SHOW_FACE_BOX = True

    SHOW_LANDMARKS = True

    # =========================
    # Face Guide
    # =========================

    GUIDE_CIRCLE_RADIUS = 150

    GUIDE_COLOR = (
        255,
        255,
        255
    )

    SUCCESS_COLOR = (
        0,
        255,
        0
    )

    ERROR_COLOR = (
        0,
        0,
        255
    )