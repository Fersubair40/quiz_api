from marshmallow import fields, Schema

from . import db
import datetime

from src.models.AnswerModel import AnswerModel, AnswerSchema
import random
import string



def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

class QuestionModel(db.Model):

    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String)
    question = db.Column(db.Text, nullable=False, unique=True)
    answers = db.relationship('AnswerModel', backref='answers', lazy=True)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)
    


    def __init__(self, data):
        self.id = data.get('id')
        self.slug = randomString()
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
    def get_question_by_id(value):
        return QuestionModel.query.filter_by(question=value).first()
    

    def _repr(self):
        return '<id {}>'.format(self.id)


class QuestionSchema(Schema):


    id = fields.Int(dump_only=True)
    slug = fields.String(dump_only=True)
    question = fields.Str(required=True)
    questions = fields.Nested(AnswerSchema, one=True)
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)

