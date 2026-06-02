class RecognitionConfig:

    # =========================
    # Recognition Engine
    # =========================

    DEFAULT_PROVIDER = (
        "insightface"
    )

    SUPPORTED_PROVIDERS = [
        "insightface",
        "facenet",
        "arcface"
    ]

    # =========================
    # Similarity Thresholds
    # =========================

    MINIMUM_SIMILARITY_SCORE = 0.75

    HIGH_CONFIDENCE_SCORE = 0.85

    VERY_HIGH_CONFIDENCE_SCORE = 0.95

    # =========================
    # Recognition Timing
    # =========================

    RECOGNITION_INTERVAL = 1.0

    # Seconds

    MAX_RECOGNITION_ATTEMPTS = 5

    # =========================
    # Embedding
    # =========================

    EMBEDDING_VECTOR_SIZE = 512

    # InsightFace Standard

    # =========================
    # Dataset Requirements
    # =========================

    MINIMUM_FACE_SAMPLES = 20

    MAXIMUM_FACE_SAMPLES = 100

    # =========================
    # Candidate Selection
    # =========================

    TOP_MATCHES_TO_COMPARE = 5

    # =========================
    # Unknown Face Detection
    # =========================

    ENABLE_UNKNOWN_FACE_REJECTION = True

    UNKNOWN_FACE_THRESHOLD = 0.70

    # =========================
    # Attendance Recognition
    # =========================

    AUTO_MARK_ATTENDANCE = True

    PREVENT_DUPLICATE_ATTENDANCE = True

    # =========================
    # Logging
    # =========================

    SAVE_RECOGNITION_HISTORY = True

    SAVE_CONFIDENCE_SCORES = True

    # =========================
    # Performance
    # =========================

    MAX_PARALLEL_RECOGNITIONS = 1

    CACHE_EMBEDDINGS = True

    CACHE_TIMEOUT = 300