from odoo import models, fields


class FaceAttendanceSettings(models.Model):
    _name = 'face.attendance.settings'
    _description = 'Face Attendance Settings'

    name = fields.Char(
        string="Configuration Name",
        default="Default Configuration",
        required=True
    )

    # =========================
    # Camera Settings
    # =========================

    camera_index = fields.Integer(
        string="Camera Index",
        default=0
    )

    camera_width = fields.Integer(
        string="Camera Width",
        default=1280
    )

    camera_height = fields.Integer(
        string="Camera Height",
        default=720
    )

    # =========================
    # Registration Settings
    # =========================

    capture_count = fields.Integer(
        string="Capture Count",
        default=20
    )

    capture_interval = fields.Float(
        string="Capture Interval (Seconds)",
        default=1.0
    )

    quality_threshold = fields.Float(
        string="Quality Threshold",
        default=70.0
    )

    # =========================
    # Recognition Settings
    # =========================

    similarity_threshold = fields.Float(
        string="Similarity Threshold",
        default=0.80
    )

    recognition_interval = fields.Float(
        string="Recognition Interval (Seconds)",
        default=1.0
    )

    # =========================
    # Attendance Settings
    # =========================

    attendance_cooldown = fields.Integer(
        string="Attendance Cooldown (Minutes)",
        default=30
    )

    # =========================
    # Anti Spoofing
    # =========================

    enable_anti_spoofing = fields.Boolean(
        string="Enable Anti Spoofing",
        default=False
    )

    blink_threshold = fields.Float(
        string="Blink Threshold",
        default=0.25
    )

    # =========================
    # Logging
    # =========================

    enable_logging = fields.Boolean(
        string="Enable Logging",
        default=True
    )

    save_recognition_logs = fields.Boolean(
        string="Save Recognition Logs",
        default=True
    )

    save_registration_logs = fields.Boolean(
        string="Save Registration Logs",
        default=True
    )

    # =========================
    # Status
    # =========================

    active = fields.Boolean(
        string="Active",
        default=True
    )