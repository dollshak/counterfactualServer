from flask import Blueprint
from flask import request
import json

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


@urls_blueprint.route('/file', methods=['POST'])
def files():
    file = request.files['modelFile']
    data = file.read()
    print(data)
    return "succ"


@urls_blueprint.route('/algos')
def algos():
    # TODO need to implement
    # need to return values from DB
    algorithmsList = [
        {
            "_id": "1",
            "name": "Dummy_CF",
            "file_content": "from server.businessLayer...",
            "description": "dummy",
            "argument_lst": [
                {"param_name": "x", "description": "param desc", "accepted_types": "int"},
                {
                    "param_name": "y",
                    "description": "param desc",
                    "accepted_types": "string",
                },
            ],
            "additional_info": "some info",
            "output_example": ["6000 -> 1200", "4 -> 40"],
        },
        {
            "_id": "2",
            "name": "shaked",
            "file_content": "from server.businessLayer...",
            "description": "albidesc",
            "argument_lst": [
                {"param_name": "x", "description": "param desc", "accepted_types": "int"},
            ],
            "additional_info": "some info",
            "output_example": ["6000 -> 1200", "4 -> 40"],
        }]
    return algorithmsList


# file_content, name: str, argument_lst: list[dict], description: str,
#                           additional_info: str,
#                           output_example: list[str]
@urls_blueprint.route('/algorithm', methods=['POST'])
def add_new_algorithm():
    req = request.form
    file_name = req['name']
    arguments_list = req.get('argument_lst')
    arguments_list = json.loads(arguments_list)
    desc = req['description']
    output_exmaples = json.loads(req['output_example'])
    data = request.files["file_content"]
    additional_info = req['additional_info']
    algo_type = req.get('type')
    algo_type = json.loads(algo_type)
    file_content = data.read()
    return algorithm_service.add_new_algorithm(file_content, file_name, arguments_list, desc, additional_info,
                                               output_exmaples, algo_type)


@urls_blueprint.route('/runAlgorithm', methods=['POST'])
def run_algorithms():
    try:
        req = request.form
        algo_names = req.get('algo_names')
        if algo_names:
            algo_names = algo_names.split(',')

        arg_list = req.get('arg_list')
        if arg_list:
            arg_list = arg_list.split(',')
            arg_list = [int(arg) for arg in arg_list]  # TODO support all types

        modelFile = request.files['model_file']

        model_input = request.files['model_input']

        # model_input = request.form.get('model_input')
        # if model_input:
        #     model_input = model_input.split(',')
        #     model_input = [float(input) for input in model_input]
        #     print(model_input)  # Output: [6000.0, 10000.0, 200000.0]

        return algorithm_service.run_algorithms(algo_names, modelFile, arg_list, model_input)
    except:
        return "unknown model"


@urls_blueprint.route('/algorithm', methods=['DELETE'])
def remove_algorithm(name):
    return algorithm_service.remove_algorithm(name)


@urls_blueprint.route('/algorithmInfo', methods=['GET'])
def get_algorithm_info():
    name = request.args.get('name')
    return algorithm_service.get_algorithm_info(name)


@urls_blueprint.route('/algorithmCode', methods=['GET'])
def get_algorithm_code(name):
    return algorithm_service.get_algorithm_code(name)


@urls_blueprint.route('/getAllAlgorithms', methods=['GET'])
def get_all_algorithms():
    return algorithm_service.get_all_algorithms()


@urls_blueprint.route('/algorithm', methods=['PUT'])
def edit_algorithm(algorithm):
    req = request.form
    file_name = req['name']
    arguments_list = req.get('argument_lst')
    arguments_list = json.loads(arguments_list)
    desc = req['description']
    output_exmaples = json.loads(req['output_example'])
    data = request.files["file_content"]
    additional_info = req['additional_info']
    file_content = data.read()
    algo_type = req.get('type')
    algo_type = json.loads(algo_type)
    return algorithm_service.edit_algorithm(file_content, file_name, arguments_list, desc, additional_info, desc,
                                            output_exmaples, algo_type)


def dummy_predict(x):
    income = x[0]
    total = x[1]
    loan = x[2]
    ratio = (income * 6 + total) / loan
    return min(ratio, 1)

