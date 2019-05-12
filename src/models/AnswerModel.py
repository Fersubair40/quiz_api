from . import db


import datetime
from marshmallow import fields, Schema

from .QuestionModel import QuestionSchema


class AnswerModel(db.Model):


    __tablename__ = "answers"

    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.String, nullable=False)
    questions = db.relationship('QuestionModel', backref='answers', lazy=True)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)
    

    def __init__(self, data):

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
    def get_all_answers():
        return AnswerModel.query.all()


    @staticmethod
    def get_one_answer(id):
        return AnswerModel.query.get(id)


    def __repr__(self):
        return '<id {}>'.format(self.id)



class AnswerSchema(Schema):

    id = fields.Int(dump_only=True)
    answer = fields.Str(required=True)
    questions = fields.Nested(QuestionSchema, one=True)
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)


