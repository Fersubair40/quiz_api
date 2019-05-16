from marshmallow import fields, Schema
from . import db
import datetime
from src.models.AnswerModel import AnswerModel, AnswerSchema
import random
import string
from sqlalchemy.dialects.postgresql import JSON

def randomStringDigits(stringLength=6):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

class QuestionModel(db.Model):

    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String)
    question = db.Column(db.Text, nullable=False, unique=True)
    options = db.relationship('AnswerModel', backref='questions', lazy=True)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)
    


    def __init__(self, data):
        self.id = data.get('id')
        self.slug = randomStringDigits()
        self.question = data.get('question')
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
    
    @staticmethod
    def get_question_by_name(value):
        return QuestionModel.query.filter_by(question=value).first()
    

    def _repr(self):
        return '<id {}>'.format(self.id)


class QuestionSchema(Schema):


    id = fields.Int(dump_only=True)
    questions = fields.Dict(reuired=True)
    slug = fields.String(dump_only=True)
    question = fields.Str(required=True)
    options = fields.Nested(AnswerSchema,  many=True)
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)

