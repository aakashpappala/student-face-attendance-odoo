from .face_recognition_service import (
    FaceRecognitionService
)

from .attendance_service import (
    AttendanceService
)


class AttendanceScannerService:

    def __init__(self, env):

        self.env = env

        self.recognition_service = (
            FaceRecognitionService(
                env
            )
        )

        self.attendance_service = (
            AttendanceService(
                env
            )
        )

    def scan_attendance(
        self,
        session
    ):

        if not session:

            return {
                "success": False,
                "message":
                    "Attendance session not found"
            }

        recognition_result = (
            self.recognition_service
            .recognize_student()
        )

        if not recognition_result:

            return {
                "success": False,
                "message":
                    "Recognition failed"
            }

        if not recognition_result.get(
            "recognized"
        ):

            return {
                "success": False,
                "message":
                    recognition_result.get(
                        "message",
                        "Unknown face"
                    )
            }

        student = (
            recognition_result.get(
                "student"
            )
        )

        confidence_score = (
            recognition_result.get(
                "confidence_score",
                0.0
            )
        )

        if not student:

            return {
                "success": False,
                "message":
                    "Student not found"
            }

        attendance_result = (
            self.attendance_service
            .mark_attendance(
                student=student,
                session=session,
                confidence_score=confidence_score
            )
        )

        return attendance_result

    def continuous_scan(
        self,
        session
    ):

        results = []

        while True:

            result = (
                self.scan_attendance(
                    session
                )
            )

            results.append(
                result
            )

            if not result.get(
                "success"
            ):
                break

        return results

    def scan_and_identify(
        self
    ):

        result = (
            self.recognition_service
            .recognize_student()
        )

        if not result:

            return {
                "success": False,
                "message":
                    "Recognition failed"
            }

        return result

    def verify_student(
        self,
        student
    ):

        return (
            self.recognition_service
            .verify_student(
                student
            )
        )

    def identify_student(
        self
    ):

        return (
            self.recognition_service
            .identify_student()
        )