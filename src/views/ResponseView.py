from flask import request, Response, json, Blueprint, g
from src.models.ResponseModel import ResponseSchema, ResponseModel
from src.models.QuestionModel import QuestionModel





response_api = Blueprint('responses',__name__)
response_schema = ResponseSchema()



@response_api.route('/', methods=['POST'])

def create():
    req_data = request.get_json()
    data, error = response_schema.load(req_data)
    if error:
        return custom_error(error, 400)
    response = ResponseModel(data)
    response.save()
    data = response_schema.dump(response).data
    return custom_response(data, 201)



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