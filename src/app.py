from flask import request, json, Response, Flask
from src.models import QuestionModel
from src.models import AnswerModel
from src.config import app_config
from src.models import db


from src.views.QuestionView import question_api as question_blueprnt


def create_app(env_name):


    app = Flask(__name__)

    app.config.from_object(app_config[env_name])
    
    db.init_app(app)

    app.register_blueprint(question_blueprnt, url_prefix='/api/v1/questions')

    @app.route('/', methods=['GET'])

    def index():
        # question = QuestionModel.get_all_question()
        # #  testing endpoint
        # req_data = request.get_json()
        return 'endpoint is workin'
    
    return app


