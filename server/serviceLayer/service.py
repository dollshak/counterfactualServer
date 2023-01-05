from flask import Blueprint
from flask import request
import json
from server.Tools.Logger import Logger
from server.businessLayer.ML_Models.MlModel import MlModel
from server.serviceLayer.algorithmService import AlgorithmService
import os
from pymongo import MongoClient

urls_blueprint = Blueprint('urls', __name__, )
algorithm_service = AlgorithmService()


@urls_blueprint.route('/')
def index():
    # return algorithm_service.add_new_algorithm()
    return ("in index")


@urls_blueprint.route('/try')
def func():
    return "try"


# file_content, name: str, argument_lst: list[dict], description: str,
#                           additional_info: str,
#                           output_example: list[str]
@urls_blueprint.route('/algorithm', methods=['POST'])
def add_new_algorithm():
    req = request.form
    file_name = req['name']
    arguments_list = json.loads(req['argument_lst'])
    desc = req['description']
    output_exmaples = json.loads(req['output_example'])
    data = request.files["file_content"]
    additional_info = req['additional_info']
    file_content = data.read()
    return algorithm_service.add_new_algorithm(file_content, file_name, arguments_list, desc, additional_info,
                                               output_exmaples)
    return "ok"


@urls_blueprint.route('/runAlgorithm', methods=['POST'])
def run_algorithms():
    model = create_dummy_model()
    req = request.form
    algo_names = json.loads(req['algo_names'])
    arg_list = json.loads(req['arg_list'])
    model_input = json.loads(req['model_input'])
    return algorithm_service.run_algorithms(algo_names, model, arg_list, model_input)


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


def dummy_predict(x):
    income = x[0]
    total = x[1]
    loan = x[2]
    ratio = (income * 6 + total) / loan
    return min(ratio, 1)


def create_dummy_model():
    # dummy_loan_model = {'fit': lambda income, total, loan: loan < (income * 6 + total)}
    dummy_loan_model = MlModel()
    dummy_loan_model.predict = lambda x: dummy_predict(x)
    return dummy_loan_model
    # return lambda income, total, loan: loan < (income * 6 + total)
