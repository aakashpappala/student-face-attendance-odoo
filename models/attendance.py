from odoo import models, fields


class StudentAttendance(models.Model):
    _name = 'student.attendance'
    _description = 'Student Attendance'

    student_id = fields.Many2one(
        'student.student',
        string='Student',
        required=True
    )

    session_id = fields.Many2one(
        'attendance.session',
        string='Attendance Session'
    )

    attendance_datetime = fields.Datetime(
        string='Attendance Time',
        default=fields.Datetime.now
    )

    status = fields.Selection(
        [
            ('present', 'Present'),
            ('absent', 'Absent'),
            ('late', 'Late')
        ],
        default='present'
    )

    confidence_score = fields.Float(
        string='Confidence Score'
    )

    recognition_method = fields.Selection(
        [
            ('face', 'Face'),
            ('manual', 'Manual'),
            ('qr', 'QR'),
            ('rfid', 'RFID')
        ],
        default='face'
    )

    active = fields.Boolean(
        string='Active',
        default=True
    )