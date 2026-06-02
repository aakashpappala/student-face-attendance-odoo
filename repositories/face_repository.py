from odoo import api, models


class FaceRepository(models.AbstractModel):
    _name = 'face.repository'
    _description = 'Face Repository'

    @api.model
    def create_face(
        self,
        values
    ):

        return self.env[
            'student.face'
        ].create(values)

    @api.model
    def get_by_id(
        self,
        face_id
    ):

        return self.env[
            'student.face'
        ].browse(face_id)

    @api.model
    def get_student_faces(
        self,
        student_id
    ):

        return self.env[
            'student.face'
        ].search(
            [
                ('student_id', '=', student_id),
                ('active', '=', True)
            ]
        )

    @api.model
    def get_all_faces(self):

        return self.env[
            'student.face'
        ].search(
            [
                ('active', '=', True)
            ]
        )

    @api.model
    def get_high_quality_faces(
        self,
        minimum_score=70
    ):

        return self.env[
            'student.face'
        ].search(
            [
                ('quality_score', '>=', minimum_score),
                ('active', '=', True)
            ]
        )

    @api.model
    def get_registered_face_dataset(self):

        return self.env[
            'student.face'
        ].search(
            [
                ('active', '=', True),
                ('embedding', '!=', False)
            ]
        )

    @api.model
    def update_face(
        self,
        face_record,
        values
    ):

        face_record.write(values)

        return face_record

    @api.model
    def deactivate_face(
        self,
        face_record
    ):

        face_record.write({
            'active': False
        })

        return face_record

    @api.model
    def delete_face(
        self,
        face_record
    ):

        face_record.unlink()

        return True

    @api.model
    def get_best_face(
        self,
        student_id
    ):

        faces = self.env[
            'student.face'
        ].search(
            [
                ('student_id', '=', student_id),
                ('active', '=', True)
            ],
            order='quality_score desc',
            limit=1
        )

        return faces