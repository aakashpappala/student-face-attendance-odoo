from odoo import models, fields, api

class Student(models.Model):
    _name = 'student.student'
    _description = 'Student'
    _rec_name = 'name'

    # =========================
    # Basic Information
    # =========================

    name = fields.Char(
        string="Student Name",
        required=True
    )

    roll_no = fields.Char(
        string="Roll Number",
        required=True
    )

    branch = fields.Char(
        string="Branch",
        required=True
    )

    year = fields.Integer(
        string="Year",
        required=True
    )

    image = fields.Image(
        string="Profile Photo"
    )

    # =========================
    # Face Registration
    # =========================

    face_registered = fields.Boolean(
        string="Face Registered",
        default=False
    )

    registration_date = fields.Datetime(
        string="Registration Date"
    )

    face_count = fields.Integer(
        string="Face Samples",
        compute="_compute_face_count",
        store=False
    )

    # =========================
    # Status
    # =========================

    active = fields.Boolean(
        string="Active",
        default=True
    )

    # =========================
    # Relationships
    # =========================

    face_ids = fields.One2many(
        'student.face',
        'student_id',
        string="Face Images"
    )

    attendance_ids = fields.One2many(
        'student.attendance',
        'student_id',
        string="Attendance Records"
    )

    # =========================
    # Computed Fields

    @api.depends('face_ids')
    def _compute_face_count(self):
        for record in self:
            record.face_count = len(
                record.face_ids
            )

    # =========================

    def action_capture_face(self):
        self.ensure_one()

        from ..services.face_registration_service import (
            FaceRegistrationService
        )

        service = FaceRegistrationService(
            self.env
        )

        service.register_student(
            self
        )

        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Success',
                'message': 'Face Registration Completed',
                'type': 'success',
                'sticky': False,
            }
        }