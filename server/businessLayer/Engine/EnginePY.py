import os
import importlib
from types import ModuleType
import signal
from server.Tools.FailedCFException import FailedCFException
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

    def run_algorithm(self, model_input: list, algo_time_limit, feature_list):
        name, suffix = os.path.splitext(self.file_name)
        module_path = SystemConfig().ALGORITHMS_DIR_PATH_MODULES + name
        try:
            cf_algo = self.import_cf_algo(module_path)
        except:
            raise FailedCFException(f'failed to import {name}')
        # TODO raz start time should be here
        if algo_time_limit > 0:
            results = self.run_with_timeout(cf_algo.explain, algo_time_limit, model_input)
        else:
            results = cf_algo.explain(model_input)
        # TODO raz end time should be here
        return results

    def timeout_handler(self, signum, frame):
        raise TimeoutError("Func timed out")

    def run_with_timeout(self, func, timeout, params):
        signal.signal(signal.SIGALRM, self.timeout_handler)
        signal.alarm(timeout)
        try:
            result = func(params)
        except TimeoutError:
            print("Func timed out")
            return []
        signal.alarm(0)
        return result

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
        # TODO raz need to fix validation here, time is an additional argument that makes the validation fail. need to remove it before it or decrease 1 in calculate
        if len(names) < len(params)-1:
            raise FailedCFException(f'too many arguments given for {name}')
        if len(names) > len(params)-1:
            raise FailedCFException(f'not enough arguments given for {name}')
        for param_name in names:
            if param_name not in params:
                raise FailedCFException(f'{param_name} is missing for {name}')
