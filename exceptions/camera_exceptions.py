class CameraException(Exception):
    pass


class CameraOpenException(
    CameraException
):
    pass


class CameraReadException(
    CameraException
):
    pass


class CameraDisconnectedException(
    CameraException
):
    pass