from odoo import api, models


class AttendanceRepository(models.AbstractModel):
    _name = 'attendance.repository'
    _description = 'Attendance Repository'

    @api.model
    def create_attendance(
        self,
        values
    ):

        return self.env[
            'student.attendance'
        ].create(values)

    @api.model
    def get_by_id(
        self,
        attendance_id
    ):

        return self.env[
            'student.attendance'
        ].browse(attendance_id)

    @api.model
    def get_student_attendance(
        self,
        student_id
    ):

        return self.env[
            'student.attendance'
        ].search(
            [
                ('student_id', '=', student_id),
                ('active', '=', True)
            ]
        )

    @api.model
    def get_session_attendance(
        self,
        session_id
    ):

        return self.env[
            'student.attendance'
        ].search(
            [
                ('session_id', '=', session_id),
                ('active', '=', True)
            ]
        )

    @api.model
    def attendance_exists(
        self,
        student_id,
        session_id
    ):

        return bool(

            self.env[
                'student.attendance'
            ].search(
                [
                    ('student_id', '=', student_id),
                    ('session_id', '=', session_id)
                ],
                limit=1
            )

        )

    @api.model
    def get_today_attendance(
        self,
        student_id,
        attendance_date
    ):

        return self.env[
            'student.attendance'
        ].search(
            [
                ('student_id', '=', student_id),
                ('attendance_date', '=', attendance_date)
            ]
        )

    @api.model
    def update_attendance(
        self,
        attendance_record,
        values
    ):

        attendance_record.write(values)

        return attendance_record

    @api.model
    def deactivate_attendance(
        self,
        attendance_record
    ):

        attendance_record.write({
            'active': False
        })

        return attendance_record

    @api.model
    def delete_attendance(
        self,
        attendance_record
    ):

        attendance_record.unlink()

        return True

    @api.model
    def get_attendance_count_by_session(
        self,
        session_id
    ):

        return self.env[
            'student.attendance'
        ].search_count(
            [
                ('session_id', '=', session_id),
                ('active', '=', True)
            ]
        )

    @api.model
    def get_attendance_count_by_student(
        self,
        student_id
    ):

        return self.env[
            'student.attendance'
        ].search_count(
            [
                ('student_id', '=', student_id),
                ('active', '=', True)
            ]
        )