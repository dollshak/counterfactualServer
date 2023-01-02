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

@urls_blueprint.route('/algorithm', methods=['POST'])
def add_new_algorithm():
    return algorithm_service.add_new_algorithm()

@urls_blueprint.route('/runAlgorithm', methods=['POST'])
def run_algorithms():
    return algorithm_service.run_algorithms()

@urls_blueprint.route('/algorithm', methods=['DELETE'])
def remove_algorithm(name):
    return algorithm_service.remove_algorithm(name)

@urls_blueprint.route('/algorithmInfo', methods=['GET'])
def get_algorithm_info(name):
    return algorithm_service.get_algorithm_info((name))

@urls_blueprint.route('/algorithmCode', methods=['GET'])
def get_algorithm_code(name):
    return algorithm_service.get_algorithm_code(name)

@urls_blueprint.route('/algorithm', methods=['GET'])
def get_all_algorithms():
    return algorithm_service.get_all_algorithms()

@urls_blueprint.route('/algorithm', methods=['PUT'])
def edit_algorithm(algorithm):
    return algorithm_service.edit_algorithm(algorithm)