from ..utils.similarity_utils import (
    SimilarityUtils
)

from ..config.recognition_config import (
    RecognitionConfig
)


class SimilarityEngine:

    def calculate_similarity(
        self,
        embedding_1,
        embedding_2
    ):

        return (
            SimilarityUtils
            .cosine_similarity(
                embedding_1,
                embedding_2
            )
        )

    def calculate_confidence(
        self,
        similarity_score
    ):

        return (
            SimilarityUtils
            .percentage_confidence(
                similarity_score
            )
        )

    def is_match(
        self,
        similarity_score
    ):

        return (
            SimilarityUtils
            .is_match(
                similarity_score,
                RecognitionConfig
                .MINIMUM_SIMILARITY_SCORE
            )
        )

    def find_best_match(
        self,
        target_embedding,
        face_records
    ):

        best_face = None

        best_similarity = 0.0

        for face_record in face_records:

            if not face_record.embedding:

                continue

            try:

                stored_embedding = eval(
                    face_record.embedding
                )

            except Exception:

                continue

            similarity = (
                self.calculate_similarity(
                    target_embedding,
                    stored_embedding
                )
            )

            if similarity > best_similarity:

                best_similarity = similarity

                best_face = face_record

        confidence = (
            self.calculate_confidence(
                best_similarity
            )
        )

        return {
            "face_record": best_face,
            "similarity_score": round(
                best_similarity,
                4
            ),
            "confidence_score": confidence,
            "is_match": self.is_match(
                best_similarity
            )
        }

    def find_top_matches(
        self,
        target_embedding,
        face_records,
        limit=5
    ):

        matches = []

        for face_record in face_records:

            if not face_record.embedding:

                continue

            try:

                stored_embedding = eval(
                    face_record.embedding
                )

            except Exception:

                continue

            similarity = (
                self.calculate_similarity(
                    target_embedding,
                    stored_embedding
                )
            )

            matches.append({
                "face_record":
                    face_record,

                "similarity_score":
                    similarity,

                "confidence_score":
                    self.calculate_confidence(
                        similarity
                    )
            })

        matches.sort(
            key=lambda item:
            item["similarity_score"],
            reverse=True
        )

        return matches[:limit]