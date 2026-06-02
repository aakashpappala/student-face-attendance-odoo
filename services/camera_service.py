import cv2

from ..config.camera_config import (
    CameraConfig
)


class CameraService:

    def __init__(self):

        self.camera = None

    def open_camera(self):

        self.camera = cv2.VideoCapture(
            CameraConfig.DEFAULT_CAMERA_INDEX,
            cv2.CAP_DSHOW
        )

        if not self.camera.isOpened():
            return False

        self.camera.set(
            cv2.CAP_PROP_FRAME_WIDTH,
            CameraConfig.FRAME_WIDTH
        )

        self.camera.set(
            cv2.CAP_PROP_FRAME_HEIGHT,
            CameraConfig.FRAME_HEIGHT
        )

        self.camera.set(
            cv2.CAP_PROP_FPS,
            CameraConfig.FPS
        )

        return True
    
    def read_frame(self):

        if not self.camera:

            return (
                False,
                None
            )

        return self.camera.read()

    def is_camera_opened(self):

        if not self.camera:

            return False

        return self.camera.isOpened()

    def create_window(
            self,
            window_name
    ):

        cv2.namedWindow(
            window_name,
            cv2.WINDOW_NORMAL
        )

        cv2.setWindowProperty(
            window_name,
            cv2.WND_PROP_TOPMOST,
            1
        )

    def show_frame(
        self,
        window_name,
        frame
    ):

        cv2.imshow(
            window_name,
            frame
        )

    def wait_key(
        self,
        delay=1
    ):

        return cv2.waitKey(delay)

    def release_camera(self):

        if self.camera:

            self.camera.release()

            self.camera = None

    def destroy_all_windows(self):

        cv2.destroyAllWindows()

    def close(self):

        self.release_camera()

        self.destroy_all_windows()

    def get_frame_size(self):

        if not self.camera:

            return (
                0,
                0
            )

        width = int(
            self.camera.get(
                cv2.CAP_PROP_FRAME_WIDTH
            )
        )

        height = int(
            self.camera.get(
                cv2.CAP_PROP_FRAME_HEIGHT
            )
        )

        return (
            width,
            height
        )

    def get_fps(self):

        if not self.camera:

            return 0

        return int(
            self.camera.get(
                cv2.CAP_PROP_FPS
            )
        )