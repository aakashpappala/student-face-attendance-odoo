from odoo import fields


class AttendanceService:

    def __init__(self, env):

        self.env = env

        self.attendance_repository = (
            self.env[
                'attendance.repository'
            ]
        )

    def mark_attendance(
        self,
        student,
        session,
        confidence_score
    ):

        if not student:

            return {
                "success": False,
                "message":
                    "Student not found"
            }

        if not session:

            return {
                "success": False,
                "message":
                    "Attendance session not found"
            }

        already_marked = (
            self.attendance_repository
            .attendance_exists(
                student.id,
                session.id
            )
        )

        if already_marked:

            return {
                "success": False,
                "message":
                    "Attendance already marked"
            }

        attendance = (
            self.attendance_repository
            .create_attendance({

                'student_id':
                    student.id,

                'session_id':
                    session.id,

                'attendance_datetime':
                    fields.Datetime.now(),

                'confidence_score':
                    confidence_score,

                'recognition_method':
                    'face',

                'status':
                    'present'
            })
        )

        return {
            "success": True,
            "message":
                "Attendance marked successfully",

            "attendance":
                attendance
        }

    def mark_manual_attendance(
        self,
        student,
        session
    ):

        if not student:

            return {
                "success": False,
                "message":
                    "Student not found"
            }

        if not session:

            return {
                "success": False,
                "message":
                    "Attendance session not found"
            }

        already_marked = (
            self.attendance_repository
            .attendance_exists(
                student.id,
                session.id
            )
        )

        if already_marked:

            return {
                "success": False,
                "message":
                    "Attendance already marked"
            }

        attendance = (
            self.attendance_repository
            .create_attendance({

                'student_id':
                    student.id,

                'session_id':
                    session.id,

                'attendance_datetime':
                    fields.Datetime.now(),

                'recognition_method':
                    'manual',

                'status':
                    'present'
            })
        )

        return {
            "success": True,
            "message":
                "Manual attendance marked",

            "attendance":
                attendance
        }

    def mark_absent_students(
        self,
        session,
        students
    ):

        absent_records = []

        if not session:

            return absent_records

        for student in students:

            exists = (
                self.attendance_repository
                .attendance_exists(
                    student.id,
                    session.id
                )
            )

            if exists:
                continue

            attendance = (
                self.attendance_repository
                .create_attendance({

                    'student_id':
                        student.id,

                    'session_id':
                        session.id,

                    'attendance_datetime':
                        fields.Datetime.now(),

                    'recognition_method':
                        'manual',

                    'status':
                        'absent'
                })
            )

            absent_records.append(
                attendance
            )

        return absent_records

    def get_student_attendance(
        self,
        student
    ):

        if not student:
            return []

        return (
            self.attendance_repository
            .get_student_attendance(
                student.id
            )
        )

    def get_session_attendance(
        self,
        session
    ):

        if not session:
            return []

        return (
            self.attendance_repository
            .get_session_attendance(
                session.id
            )
        )

    def has_attendance(
        self,
        student,
        session
    ):

        if not student or not session:
            return False

        return (
            self.attendance_repository
            .attendance_exists(
                student.id,
                session.id
            )
        )

    def get_attendance_summary(
            self,
            session
    ):

        records = (
            self.get_session_attendance(
                session
            )
        )

        present_count = 0
        absent_count = 0

        for record in records:

            if record.status == 'present':
                present_count += 1

            elif record.status == 'absent':
                absent_count += 1

        return {
            "total":
                len(records),

            "present":
                present_count,

            "absent":
                absent_count
        }