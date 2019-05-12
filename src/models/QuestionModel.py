from marshmallow import fields, Schema

from . import db
import datetime






class QuestionModel(db.Model):

    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    answer_id = db.Column(db.Integer, db.ForeignKey('answers.id'), nullable=False)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)
    


    def __init__(self, data):
        

        self.question = data.get('question')
        self.answer_id = data.get('answer_id')
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()


    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self,data):
        for key, item in data.items():
            setattr(self, key, item)
        self.modified_at = datetime.datetime.utcnow()
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


    @staticmethod
    def get_all_questions():
        return QuestionModel.query.all()

    @staticmethod
    def get_one_question(id):
        return QuestionModel.query.get(id)
    

    def _repr(self):
        return '<id {}>'.format(self.id)


class QuestionSchema(Schema):


    id = fields.Int(dump_only=True)
    question = fields.Str(required=True)
    answer_id = fields.Int(required=True)
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)

