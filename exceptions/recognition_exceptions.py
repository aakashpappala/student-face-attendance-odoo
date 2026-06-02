class RegistrationException(
    Exception
):
    pass


class FaceNotDetectedException(
    RegistrationException
):
    pass


class MultipleFacesDetectedException(
    RegistrationException
):
    pass


class LowQualityFaceException(
    RegistrationException
):
    pass


class RegistrationTimeoutException(
    RegistrationException
):
    pass