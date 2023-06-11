from flask import Blueprint
from flask import request
import json

from server.Tools.SystemConfig import SystemConfig
from server.businessLayer.ML_Models.MlModel import MlModel
from server.serviceLayer.algorithmService import AlgorithmService
import os
from pymongo import MongoClient

urls_blueprint = Blueprint('urls', __name__, )
algorithm_service = AlgorithmService(SystemConfig())


@urls_blueprint.route('/file', methods=['POST'])
def files():
    file = request.files['modelFile']
    data = file.read()
    print(data)
    return "succ"


@urls_blueprint.route('/algorithm', methods=['POST'])
def add_new_algorithm():
    """
    argument_lst : [
                {"param_name": "features", "description": "", "accepted_types": ["list"], default_value},
                {"param_name": "outcome_name", "description": "", "accepted_types": ["string"], default_value},
                {"param_name": "total_CFs", "description": "", "accepted_types": ["float"], default_value},
                {"param_name": "desired_class", "description": "", "accepted_types": ["float"], default_value},
                {"param_name": "desired_range", "description": "", "accepted_types": ["list"], default_value},
                {"param_name": "is_classifier", "description": "", "accepted_types": ["boolean"], default_value},
            ]
    :return:
    """
    req = request.form
    file_name = req['name']
    if file_name is None or file_name == "":
        return "File name has to be filled ", 400
    arguments_list = req.get('argument_lst')
    if arguments_list is None:
        return "Argument list cannot be none ", 400
    arguments_list = json.loads(arguments_list)
    desc = req['description']
    if desc is None:
        return "Description cannot be none ", 400
    output_exmaples = req['output_example']
    if output_exmaples is None:
        return "Output examples cannot be none ", 400
    data = request.files["file_content"]
    if data is None:
        return "File content cannot be none ", 400
    additional_info = req['additional_info']
    if additional_info in None:
        return "The algorithm additional info cannot be none ", 400
    algo_type = req.get('type')
    if additional_info in None:
        return "The algorithm type cannot be none ", 400
    algo_type = json.loads(algo_type)
    file_content = data.read()
    try:
        return algorithm_service.add_new_algorithm(file_content, file_name, arguments_list, desc, additional_info,
                                                   output_exmaples, algo_type)
    except Exception as e:
        return str(e), 400


@urls_blueprint.route('/runAlgorithm', methods=['POST'])
def run_algorithms():
    """
    request should be as following ::
        {
            "algo_names":   ["algo_1","algo_2"],\n
            "arg_list": {
                            "algo_1":{
                                        "param1": value,\n
                                        "param2":value2
                                        "time_limit" : -1

                            },
                            "algo_2":{
                                        "param1_algo2" : 1,\n
                                        "param2_algo2" : 1
                                        "time_limit" : 1
                            }
            },\n
            "model_file": <model_code_file>,\n
            "model_input" : <json file> as following :{
                                                        values: [9562, 5060, 81991, 374286],
                                                        names: ["income", "outcome", "total", "loan"]
            }
        }

    :return:
    """
    try:
        req = request.form
        algo_names = json.loads(req.get('algo_names'))
        if algo_names is None:
            return "Chosen algorithms list cannot be None ", 400
        arg_list = req.get('arg_list')
        if arg_list is None:
            return "Arguments list cannot be None ", 400
        arg_list = json.loads(arg_list)
        modelFile = request.files['model_file']
        if modelFile is None:
            return "Model file cannot be None ", 400
        model_input = json.load(request.files['model_input'])
        if model_input is None:
            return "The input for the model cannot be None ", 400
        return algorithm_service.run_algorithms(algo_names, modelFile, arg_list, model_input)
    except Exception as e:
        return str(e), 400


@urls_blueprint.route('/algorithm', methods=['DELETE'])
def remove_algorithm(name):
    if name is None:
        return "Algorithm cannot be none ", 400
    return algorithm_service.remove_algorithm(name)


@urls_blueprint.route('/algorithmInfo', methods=['GET'])
def get_algorithm_info():
    name = request.args.get('name')
    if name is None:
        return "Algorithm cannot be none ", 400
    return algorithm_service.get_algorithm_info(name)


@urls_blueprint.route('/algorithmCode', methods=['GET'])
def get_algorithm_code(name):
    if name is None:
        return "Algorithm cannot be none ", 400
    return algorithm_service.get_algorithm_code(name)


@urls_blueprint.route('/getAllAlgorithms', methods=['GET'])
def get_all_algorithms():
    try:
        results = algorithm_service.get_all_algorithms()
        return results
    except Exception as e:
        return str(e), 400


@urls_blueprint.route('/clearDB', methods=['POST'])
def clear_db():
    algorithm_service.clear_db()
    return "DB cleared", 400


@urls_blueprint.route('/algorithm', methods=['PUT'])
def edit_algorithm():
    try:
        req = request.form
        file_name = req['name']
        if file_name is None:
            return "The file name has to be filled and cannot be None ", 400
        origin_name = req['origin_name']
        if origin_name is None:
            return "Origin name has to be filled and cannot be None ", 400
        arguments_list = req.get('argument_lst')
        if arguments_list is None:
            return "Argument list cannot be none ", 400
        arguments_list = json.loads(arguments_list)
        desc = req['description']
        if desc is None:
            return "Description cannot be none ", 400
        output_exmaples = req['output_example']
        if output_exmaples is None:
            return "Output examples cannot be none ", 400
        if "file_content" in request.files and request.files["file_content"] is not None:
            data = request.files["file_content"]
            file_content = data.read()
        else:
            file_content = None
        additional_info = req['additional_info']
        algo_type = req.get('type')
        if additional_info in None:
            return "The algorithm type cannot be none ", 400
        algo_type = json.loads(algo_type)
        return algorithm_service.edit_algorithm(file_content, file_name, arguments_list, desc, additional_info,
                                                output_exmaples, algo_type, origin_name)
    except Exception as e:
        return str(e), 400
