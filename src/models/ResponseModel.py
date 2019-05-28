from . import db
import datetime
import random
import string
from marshmallow import fields, Schema
from src.models.QuestionModel import QuestionModel, QuestionSchema






def randomStringDigits(stringLength=6):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))


class ResponseModel(db.Model):


    __tablename__ = "responses"

    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)
    answer = db.Column(db.String, nullable=False)
    

    def __init__(self, data):

        self.slug = randomStringDigits()
        self.question_id = data.get('question_id')
        self.answer = data.get('answer')
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, Item in data.items():
            setattr(self, key, item)
        self.modified_at = datetime.datetime.utcnow()
        db.session.commit()


    def delete(self):
        db.session.delete(self)
        db.session.commit()


    @staticmethod
    def get_all_responses():
        return ResponseModel.query.all()


    @staticmethod
    def get_one_answer(id):
        return AnswerModel.query.get(id)


    def __repr__(self):
        return '<id {}>'.format(self.id)



class ResponseSchema(Schema):

    id = fields.Int(dump_only=True)
    answer = fields.Str(required=True)
    question_id = fields.Int(required=True)  #Nested('QuestionModel', only=("id", "answer"))
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)


