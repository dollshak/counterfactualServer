from flask import Blueprint
from server.serviceLayer.algorithmService import AlgorithmService

urls_blueprint = Blueprint('urls', __name__,)
algorithm_service = AlgorithmService()

@urls_blueprint.route('/')
def index():
    return algorithm_service.add_new_algorithm()

@urls_blueprint.route('/try')
def func():
    return "new duct"