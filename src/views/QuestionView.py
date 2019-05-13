from flask import request, json, Response, Blueprint, g

from src.models.QuestionModel import QuestionModel, QuestionSchema



question_api = Blueprint('questions', __name__)
question_schema = QuestionSchema()


@question_api.route('/', methods=['POST'])

def create():

    req_data = request.get_json()
    data, error = question_schema.load(req_data)

    if error:
        return custom_response(error, 400)


    question_in_db = QuestionModel.get_question_by_id(data.get('question'))
    if question_in_db:
        message = {'error': 'question already exists, please add another question'}
        return custom_response(message, 400)

    question = QuestionModel(data)
    question.save()

    ser_data = question_schema.dump(question).data
    return custom_response(ser_data, 201)


@question_api.route('/', methods=['GET'])
def get_all():
    questions = QuestionModel.get_all_questions()
    ser_questions = question_schema.dump(questions, many=True).data
    return custom_response(ser_questions, 200)




    

@question_api.route('/<int:question_id>', methods=['GET'])
def get_one_question(question_id):
    quesion = QuestionModel.get_one_question(question_id)
    if not quesion:
        return custom_response({'error':'question not found'}, 400)

    ser_question = question_schema.dump(quesion).data
    return custom_response(ser_question, 200)





@question_api.route('/<int:question_id>', methods=['PUT'])
def update(question_id):
    req_data = request.get_json()
    question = QuestionModel.get_one_question(question_id)
    if not question:
        return custom_response({'error':'question not found'}, 400)

    data, error = question_schema.load(req_data, partial=True)
    if error:
        return custom_response(error, 400)

    question.update(data)
    ser_question = question_schema.dump(question).data
    return custom_response(ser_question, 200)




@question_api.route('<int:question_id>', methods=['DELETE'])
def delete(question_id):
    question = QuestionModel.get_one_question(question_id)
    if not question:
        return custom_response({'error':'question not found'}, 400)
    
    question.delete()
    question = question_schema.dump(question).data
    return custom_response(question, 204)





def custom_response(res, status_code):

    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )













