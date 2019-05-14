# from flask import json, Response, request, g

# from src.models.QuestionModel import QuestionModel
# from functools import wraps



# class Auth():

#     @staticmethod
#     def auth_required(func):
#         @wraps(func)
#         def decorated_auth(*args, **kwargs):

#             question_id = ['question_id']
#             check_question = QuestionModel.get_one_question(question_id)
#             if not check_question:
#                 return Response(
#                     mimetype="application/json",
#                     response=json.dumps({'error': 'question does not exist, invalid token'}),
#                     status=400
#                     )
#             g.question = {'id': question_id}
#             return func(*args, **kwargs)
#         return decorated_auth