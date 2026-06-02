from odoo import models, fields


class StudentFace(models.Model):
    _name = 'student.face'
    _description = 'Student Face'
    _order = 'capture_date desc'

    # =========================
    # Relationships
    # =========================

    student_id = fields.Many2one(
        'student.student',
        string="Student",
        required=True,
        ondelete='cascade'
    )

    # =========================
    # Face Data
    # =========================

    image = fields.Image(
        string="Face Image",
        required=True
    )

    embedding = fields.Text(
        string="Face Embedding"
    )

    # =========================
    # Quality Metrics
    # =========================

    quality_score = fields.Float(
        string="Quality Score"
    )

    brightness_score = fields.Float(
        string="Brightness Score"
    )

    blur_score = fields.Float(
        string="Blur Score"
    )

    face_angle = fields.Float(
        string="Face Angle"
    )

    # =========================
    # Recognition Metadata
    # =========================

    eyes_visible = fields.Boolean(
        string="Eyes Visible",
        default=False
    )

    face_centered = fields.Boolean(
        string="Face Centered",
        default=False
    )

    # =========================
    # Capture Information
    # =========================

    capture_date = fields.Datetime(
        string="Capture Date",
        default=fields.Datetime.now
    )

    active = fields.Boolean(
        string="Active",
        default=True
    )