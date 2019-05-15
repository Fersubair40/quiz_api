from . import db
import datetime
from marshmallow import fields, Schema






class AnswerModel(db.Model):


    __tablename__ = "answers"

    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)
    a = db.Column(db.String, nullable=False)
    b = db.Column(db.String, nullable=False)
    c = db.Column(db.String, nullable=False)
    d = db.Column(db.String, nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    answer = db.Column(db.String, nullable=False)
    response_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)
    
    

    def __init__(self, data):

        self.answer = data.get('answer')
        self.a = data.get('a')
        self.b = data.get('b')
        self.c = data.get('c')
        self.d = data.get('d')
        self.response_id = data.get('response_id')
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
    a = fields.Str(required=True)
    b = fields.Str(required=True)
    c = fields.Str(required=True)
    d = fields.Str(required=True)
    response_id = fields.Int(required=True)
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)


