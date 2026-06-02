from odoo import models, fields

from ..services.attendance_scanner_service import (
    AttendanceScannerService
)


class AttendanceSession(models.Model):
    _name = 'attendance.session'
    _description = 'Attendance Session'
    _rec_name = 'name'
    _order = 'start_datetime desc'

    # =========================
    # Basic Information
    # =========================

    name = fields.Char(
        string="Session Name",
        required=True
    )

    description = fields.Text(
        string="Description"
    )

    # =========================
    # Schedule
    # =========================

    start_datetime = fields.Datetime(
        string="Start Time",
        required=True
    )

    end_datetime = fields.Datetime(
        string="End Time",
        required=True
    )

    # =========================
    # Status
    # =========================

    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('active', 'Active'),
            ('completed', 'Completed'),
            ('cancelled', 'Cancelled')
        ],
        string="Status",
        default='draft'
    )

    active = fields.Boolean(
        string="Active",
        default=True
    )

    # =========================
    # Statistics
    # =========================

    attendance_count = fields.Integer(
        string="Attendance Count",
        compute="_compute_attendance_count"
    )

    # =========================
    # Relationships
    # =========================

    attendance_ids = fields.One2many(
        'student.attendance',
        'session_id',
        string="Attendance Records"
    )

    # =========================
    # Computed Fields
    # =========================

    def _compute_attendance_count(self):

        for record in self:

            record.attendance_count = len(
                record.attendance_ids
            )

    # =========================
    # Actions
    # =========================

    def action_activate(self):

        self.ensure_one()

        self.state = 'active'

    def action_complete(self):

        self.ensure_one()

        self.state = 'completed'

    def action_start_scan(self):

        self.ensure_one()

        scanner = (
            AttendanceScannerService(
                self.env
            )
        )

        result = (
            scanner.scan_attendance(
                self
            )
        )

        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Attendance Scanner',
                'message': result.get(
                    'message',
                    'Attendance Processed'
                ),
                'type': 'success',
                'sticky': False,
            }
        }