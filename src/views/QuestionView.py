from flask import request, json, Response, Blueprint

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












def custom_response(res, status_code):

    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )













