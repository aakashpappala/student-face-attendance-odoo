import json

from ..ai.providers.insightface_provider import (
    InsightFaceProvider
)

from ..config.recognition_config import (
    RecognitionConfig
)


class EmbeddingService:

    def __init__(self):

        self.provider = (
            InsightFaceProvider()
        )

    def generate_embedding(
        self,
        image
    ):

        return (
            self.provider
            .get_embedding(
                image
            )
        )

    def serialize_embedding(
        self,
        embedding
    ):

        if not embedding:

            return None

        return json.dumps(
            embedding
        )

    def deserialize_embedding(
        self,
        embedding_string
    ):

        if not embedding_string:

            return None

        try:

            return json.loads(
                embedding_string
            )

        except Exception:

            return None

    def validate_embedding(
        self,
        embedding
    ):

        if not embedding:

            return False

        return (
            len(embedding)
            ==
            RecognitionConfig
            .EMBEDDING_VECTOR_SIZE
        )

    def generate_serialized_embedding(
        self,
        image
    ):

        embedding = (
            self.generate_embedding(
                image
            )
        )

        if not self.validate_embedding(
            embedding
        ):

            return None

        return (
            self.serialize_embedding(
                embedding
            )
        )

    def compare_embeddings(
        self,
        embedding_1,
        embedding_2
    ):

        from ..utils.similarity_utils import (
            SimilarityUtils
        )

        return (
            SimilarityUtils
            .cosine_similarity(
                embedding_1,
                embedding_2
            )
        )

    def get_embedding_dimension(
        self
    ):

        return (
            RecognitionConfig
            .EMBEDDING_VECTOR_SIZE
        )