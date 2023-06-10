import os
import importlib
import datetime
from datetime import timedelta, datetime
import time
import ast
import pip

import multiprocess
from pathos.multiprocessing import ProcessingPool as Pool
from server.Tools.FailedCFException import FailedCFException
from server.Tools.Logger import Logger
from server.Tools.SystemConfig import SystemConfig
from server.businessLayer.Algorithms.CounterFactualAlgorithmDescription import CounterFactualAlgorithmDescription
from server.businessLayer.Engine.EngineAPI import EngineAPI
from server.businessLayer.FileManager import FileManager
from server.businessLayer.ML_Models.MlModel import MlModel
import json


class EnginePY(EngineAPI):

    def __init__(self, model, file_name, cf_params_list, config, feature_name_list: list):
        super().__init__(model, file_name, cf_params_list, config, feature_name_list)
        self.validate_arguments()

    def run_algorithm(self, model_input: list, algo_time_limit=-1):
        name, suffix = os.path.splitext(self.file_name)
        module_path = SystemConfig().ALGORITHMS_DIR_PATH_MODULES + name
        self.handleWithLibraries(module_path)
        try:
            cf_algo = self.import_cf_algo(module_path)
        except:
            raise FailedCFException(f'failed to import {name}')
        start_time = time.time()
        # start_time = timedelta(hours=start_time.hour, minutes=start_time.minute, seconds=start_time.second)
        if algo_time_limit > 0:
            pool = Pool(1)
            try:
                results = pool.apipe(cf_algo.explain, model_input).get(timeout=algo_time_limit)
            except multiprocess.context.TimeoutError:
                return f'{name} could not finish in time', algo_time_limit
            except Exception as e:
                return str(e), -1

        else:
            results = cf_algo.explain(model_input)
        end_time = time.time()
        # end_time = timedelta(hours=end_time.hour, minutes=end_time.minute, seconds=end_time.second)
        duration = end_time - start_time
        return results, duration

    def import_cf_algo(self, module_path):
        try:
            algo_module = importlib.import_module(module_path)
            cf_algo = algo_module.initAlgo(self.model, self.cf_params, self.feature_name_list)
        except:
            raise Exception(f'failed to import module {self.file_name}')
        return cf_algo

    def validate_arguments(self):
        file_manager = FileManager(self.config)
        name, suffix = os.path.splitext(self.file_name)

        algo_val = file_manager.get_algorithm(name)
        if algo_val is None or len(algo_val) == 0:
            raise FailedCFException(f'There is no CF algorithm named:{name}.py')
        arg_list = algo_val['argument_lst']
        arg_list = json.loads(arg_list)
        names = [arg['param_name'] for arg in arg_list]
        params = list(self.cf_params.keys())
        params.remove("time_limit")
        if len(names) < len(params):
            raise FailedCFException(f'too many arguments given for {name}')
        if len(names) > len(params):
            raise FailedCFException(f'not enough arguments given for {name}')
        for param_name in names:
            if param_name not in params:
                raise FailedCFException(f'{param_name} is missing for {name}')

    def extract_module_names(self, file_path):
        path = file_path.replace('.','/')
        with open(path+ ".py", 'r') as file:
            tree = ast.parse(file.read())

            module_names = set()

            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        module_names.add(alias.name.split('.')[0])
                elif isinstance(node, ast.ImportFrom):
                    module_names.add(node.module.split('.')[0])

            return module_names

    def install_package(self, package):
        pip.main(['install', package])

    def handleWithLibraries(self, module_path):
        module_names = self.extract_module_names(module_path)
        for module_name in module_names:
            try:
                module = importlib.import_module(module_name)
            except ImportError:
                # If the module is not found, install it using pip
                Logger().debug(f"Module '{module_name}' not found. Installing...")
                self.install_package(module_name)
