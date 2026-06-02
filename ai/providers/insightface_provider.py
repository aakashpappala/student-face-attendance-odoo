import numpy as np
from insightface.app import FaceAnalysis


class InsightFaceProvider:

    _app = None

    @classmethod
    def get_app(cls):

        if cls._app is None:

            cls._app = FaceAnalysis(
                name="buffalo_l"
            )

            cls._app.prepare(
                ctx_id=0,
                det_size=(640, 640)
            )

        return cls._app

    def __init__(self):

        self.app = self.get_app()

    def get_embedding(self, image):

        if image is None:
            return None

        faces = self.app.get(image)

        if not faces:
            return None

        return (
            faces[0]
            .embedding
            .astype(np.float32)
            .tolist()
        )