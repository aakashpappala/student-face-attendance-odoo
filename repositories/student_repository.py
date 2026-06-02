from odoo import api, models


class StudentRepository(models.AbstractModel):
    _name = 'student.repository'
    _description = 'Student Repository'

    @api.model
    def get_by_id(self, student_id):

        return self.env[
            'student.student'
        ].browse(student_id)

    @api.model
    def get_by_roll_no(self, roll_no):

        return self.env[
            'student.student'
        ].search(
            [
                ('roll_no', '=', roll_no)
            ],
            limit=1
        )

    @api.model
    def get_registered_students(self):

        return self.env[
            'student.student'
        ].search(
            [
                ('face_registered', '=', True)
            ]
        )

    @api.model
    def get_active_students(self):

        return self.env[
            'student.student'
        ].search(
            [
                ('active', '=', True)
            ]
        )

    @api.model
    def create_student(self, values):

        return self.env[
            'student.student'
        ].create(values)

    @api.model
    def update_student(
        self,
        student,
        values
    ):

        student.write(values)

        return student

    @api.model
    def deactivate_student(
        self,
        student
    ):

        student.write({
            'active': False
        })

        return student