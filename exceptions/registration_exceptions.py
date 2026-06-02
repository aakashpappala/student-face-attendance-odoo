class RecognitionException(
    Exception
):
    pass


class UnknownFaceException(
    RecognitionException
):
    pass


class EmbeddingGenerationException(
    RecognitionException
):
    pass


class DatasetEmptyException(
    RecognitionException
):
    pass