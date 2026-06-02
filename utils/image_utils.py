import cv2
import base64
import numpy as np


class ImageUtils:

    @staticmethod
    def flip_horizontal(frame):

        return cv2.flip(
            frame,
            1
        )

    @staticmethod
    def convert_to_rgb(frame):

        return cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

    @staticmethod
    def convert_to_gray(frame):

        return cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2GRAY
        )

    @staticmethod
    def resize_image(
        frame,
        width,
        height
    ):

        return cv2.resize(
            frame,
            (width, height)
        )

    @staticmethod
    def image_to_base64(frame):

        success, buffer = cv2.imencode(
            '.jpg',
            frame
        )

        if not success:

            return None

        return base64.b64encode(
            buffer
        ).decode(
            'utf-8'
        )

    @staticmethod
    def base64_to_image(
        image_string
    ):

        image_bytes = base64.b64decode(
            image_string
        )

        image_array = np.frombuffer(
            image_bytes,
            dtype=np.uint8
        )

        return cv2.imdecode(
            image_array,
            cv2.IMREAD_COLOR
        )

    @staticmethod
    def get_image_height(
        frame
    ):

        return frame.shape[0]

    @staticmethod
    def get_image_width(
        frame
    ):

        return frame.shape[1]

    @staticmethod
    def get_image_size(
        frame
    ):

        return (
            frame.shape[1],
            frame.shape[0]
        )

    @staticmethod
    def crop_image(
        frame,
        x,
        y,
        width,
        height
    ):

        return frame[
            y:y + height,
            x:x + width
        ]

    @staticmethod
    def draw_rectangle(
        frame,
        x,
        y,
        width,
        height,
        color,
        thickness=2
    ):

        cv2.rectangle(
            frame,
            (x, y),
            (
                x + width,
                y + height
            ),
            color,
            thickness
        )

        return frame

    @staticmethod
    def draw_circle(
        frame,
        center_x,
        center_y,
        radius,
        color,
        thickness=2
    ):

        cv2.circle(
            frame,
            (
                center_x,
                center_y
            ),
            radius,
            color,
            thickness
        )

        return frame

    @staticmethod
    def put_text(
        frame,
        text,
        x,
        y,
        color,
        scale=0.7,
        thickness=2
    ):

        cv2.putText(
            frame,
            text,
            (x, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            scale,
            color,
            thickness
        )

        return frame