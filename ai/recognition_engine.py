from .similarity_engine import (
    SimilarityEngine
)

from .providers.insightface_provider import (
    InsightFaceProvider
)


class RecognitionEngine:

    def __init__(self):

        self.provider = (
            InsightFaceProvider()
        )

        self.similarity_engine = (
            SimilarityEngine()
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

    def recognize(
        self,
        image,
        face_records
    ):

        embedding = (
            self.generate_embedding(
                image
            )
        )

        if not embedding:

            return {
                "recognized": False,
                "message": (
                    "No face detected"
                ),
                "student": None,
                "confidence_score": 0,
                "similarity_score": 0
            }

        result = (
            self.similarity_engine
            .find_best_match(
                embedding,
                face_records
            )
        )

        if (
            not result["is_match"]
            or
            not result["face_record"]
        ):

            return {
                "recognized": False,
                "message": (
                    "Unknown face"
                ),
                "student": None,
                "confidence_score":
                    result[
                        "confidence_score"
                    ],
                "similarity_score":
                    result[
                        "similarity_score"
                    ]
            }

        student = (
            result[
                "face_record"
            ]
            .student_id
        )

        return {
            "recognized": True,
            "message":
                "Student recognized",
            "student":
                student,
            "face_record":
                result[
                    "face_record"
                ],
            "confidence_score":
                result[
                    "confidence_score"
                ],
            "similarity_score":
                result[
                    "similarity_score"
                ]
        }

    def verify_face(
        self,
        image,
        reference_embedding
    ):

        embedding = (
            self.generate_embedding(
                image
            )
        )

        if not embedding:

            return {
                "verified": False,
                "similarity_score": 0
            }

        similarity = (
            self.similarity_engine
            .calculate_similarity(
                embedding,
                reference_embedding
            )
        )

        return {
            "verified":
                self.similarity_engine
                .is_match(
                    similarity
                ),

            "similarity_score":
                similarity,

            "confidence_score":
                self.similarity_engine
                .calculate_confidence(
                    similarity
                )
        }

    def identify_student(
        self,
        image,
        face_records
    ):

        result = self.recognize(
            image,
            face_records
        )

        if not result[
            "recognized"
        ]:

            return None

        return result[
            "student"
        ]