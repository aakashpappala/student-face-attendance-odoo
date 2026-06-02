import mediapipe as mp

from ..utils.validation_utils import (
    ValidationUtils
)


class FaceDetectionService:

    def __init__(self):

        self.face_detector = (
            mp.solutions.face_detection
            .FaceDetection(
                model_selection=0,
                min_detection_confidence=0.7
            )
        )

    def detect_faces(
        self,
        rgb_frame
    ):

        return self.face_detector.process(
            rgb_frame
        )

    def get_face_count(
        self,
        detection_results
    ):

        if not detection_results.detections:

            return 0

        return len(
            detection_results.detections
        )

    def is_single_face_detected(
        self,
        detection_results
    ):

        return (
            ValidationUtils
            .is_single_face_detected(
                detection_results.detections
            )
        )

    def get_primary_face(
        self,
        detection_results
    ):

        if not detection_results.detections:

            return None

        return (
            detection_results
            .detections[0]
        )

    def get_face_bounding_box(
        self,
        detection,
        frame_width,
        frame_height
    ):

        bbox = (
            detection
            .location_data
            .relative_bounding_box
        )

        x = int(
            bbox.xmin *
            frame_width
        )

        y = int(
            bbox.ymin *
            frame_height
        )

        width = int(
            bbox.width *
            frame_width
        )

        height = int(
            bbox.height *
            frame_height
        )

        return {
            "x": x,
            "y": y,
            "width": width,
            "height": height
        }

    def get_face_center(
        self,
        bounding_box
    ):

        center_x = (
            bounding_box["x"] +
            bounding_box["width"] // 2
        )

        center_y = (
            bounding_box["y"] +
            bounding_box["height"] // 2
        )

        return (
            center_x,
            center_y
        )

    def get_face_size(
        self,
        bounding_box
    ):

        return (
            bounding_box["width"],
            bounding_box["height"]
        )

    def is_face_size_valid(
        self,
        bounding_box,
        minimum_width,
        minimum_height
    ):

        width = (
            bounding_box["width"]
        )

        height = (
            bounding_box["height"]
        )

        return (
            ValidationUtils
            .is_face_size_valid(
                width,
                height,
                minimum_width,
                minimum_height
            )
        )

    def get_detection_confidence(
        self,
        detection
    ):

        if not detection.score:

            return 0.0

        return float(
            detection.score[0]
        )