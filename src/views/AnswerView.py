from flask import request, Response, json, Blueprint, g
from src.models.AnswerModel import AnswerModel, AnswerSchema
from src.models.QuestionModel import QuestionModel





answer_api = Blueprint('answers',__name__)
answer_schema = AnswerSchema()



@answer_api.route('/', methods=['POST'])

def create():
    req_data = request.get_json()
    data, error = answer_schema.load(req_data)
    if error:
        return custom_error(error, 400)
    answer = AnswerModel(data)
    answer.save()
    data = answer_schema.dump(answer).data
    return custom_response(data, 201)



@answer_api.route('/', methods=['GET'])
def get_all():
    answers = AnswerModel.get_all_answers()
    ser_answers = answer_schema.dump(answers, many=True).data
    return custom_response(ser_answers, 200)









def custom_response(res, status_code):

    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )