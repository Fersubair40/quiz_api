from flask import request, Response, json, Blueprint, flash
from src.models.ResponseModel import ResponseSchema, ResponseModel
from src.models.QuestionModel import QuestionModel, QuestionSchema





response_api = Blueprint('responses',__name__)
response_schema = ResponseSchema()



@response_api.route('/', methods=['POST'])

def create():
    req_data = request.get_json()
    data, error = response_schema.load(req_data)
    if error:
        return custom_response(error, 400)

    # correct_answer = QuestionModel.get_correct_answer(data.get('answer'))
    # question = QuestionModel.get_all_questions()
    # for answer in question:
    # correct_answer = QuestionModel.get_correct_answer(data.get('idp'))
    # if not correct_answer:
    def get_response(id):
        question_id = QuestionModel.get_one_question(id)
        response_id = ResponseModel.get_one_answer(id)

        if response_id == question_id:
            response = ResponseModel(data)
            response.save()
            data = response_schema.dump(response).data
            message1 = {"passed": "correct answer"}
            flash('correct answer')
        else:
            message = {'failed': 'incorrect answer'}
            return custom_response(message, 200)

            
        return custom_response(message1, 201)
        


@response_api.route('/', methods=['GET'])
def get_all():
    responses = ResponseModel.get_all_responses()
    ser_responses = response_schema.dump(responses, many=True).data
    return custom_response(ser_responses, 200)









def custom_response(res, status_code):

    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )