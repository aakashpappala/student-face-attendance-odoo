import numpy as np


class SimilarityUtils:

    @staticmethod
    def cosine_similarity(
        embedding_1,
        embedding_2
    ):

        embedding_1 = np.array(
            embedding_1,
            dtype=np.float32
        )

        embedding_2 = np.array(
            embedding_2,
            dtype=np.float32
        )

        denominator = (
            np.linalg.norm(embedding_1)
            *
            np.linalg.norm(embedding_2)
        )

        if denominator == 0:

            return 0.0

        similarity = (
            np.dot(
                embedding_1,
                embedding_2
            )
            / denominator
        )

        return float(
            similarity
        )

    @staticmethod
    def euclidean_distance(
        embedding_1,
        embedding_2
    ):

        embedding_1 = np.array(
            embedding_1,
            dtype=np.float32
        )

        embedding_2 = np.array(
            embedding_2,
            dtype=np.float32
        )

        distance = np.linalg.norm(
            embedding_1 -
            embedding_2
        )

        return float(
            distance
        )

    @staticmethod
    def percentage_confidence(
        similarity_score
    ):

        confidence = (
            similarity_score * 100
        )

        confidence = max(
            0,
            min(
                confidence,
                100
            )
        )

        return round(
            confidence,
            2
        )

    @staticmethod
    def find_best_match(
        target_embedding,
        candidates
    ):

        best_score = 0.0

        best_record = None

        for candidate in candidates:

            similarity = (
                SimilarityUtils
                .cosine_similarity(
                    target_embedding,
                    candidate
                )
            )

            if similarity > best_score:

                best_score = similarity

                best_record = candidate

        return (
            best_record,
            best_score
        )

    @staticmethod
    def is_match(
        similarity_score,
        threshold
    ):

        return (
            similarity_score >=
            threshold
        )