import os.path
from typing import Tuple, List, Any, Dict
from server.Tools.FailedCFException import FailedCFException
from server.Tools.ModelException import ModelException
from server.businessLayer.Engine.EnginePY import EnginePY
from server.businessLayer.ML_Models.MlModel import MlModel
from server.Tools.Logger import Logger

logger = Logger()


class EngineController:
    def __init__(self, config):
        self.config = config

    def run_algorithms(self, algo_names: list[str], model: MlModel, model_input, feature_names: list,
                       cf_inputs: dict):
        # init result array for each cf
        algo_runtimes = {}
        results = [[] for i in range(len(algo_names))]
        # for each cf
        logger.debug(f'Starting run algorithms.')
        for idx, algo_name in enumerate(algo_names):
            try:
                logger.debug(f'running {algo_name}')
                name, suffix = os.path.splitext(algo_name)
                inputs = cf_inputs[name]
                algo_time_limit = inputs["time_limit"]
                if algo_time_limit is not None:
                    algo_time_limit = int(algo_time_limit)
                result, duration = self.get_cf_results(algo_name, inputs, model, model_input, algo_time_limit,
                                                       feature_names)
                algo_runtimes[name] = duration
                results[idx] = result
            except FailedCFException as e:
                logger.error(f'{algo_name} failed to run, returned empty results . error message is : {e.message}')
                results[idx] = e.message
        logger.debug(f'Finished to run algorithms.')
        return results, algo_runtimes

    def get_cf_results(self, algo_name, cf_inputs, model, model_input, algo_time_limit, feature_list: list):
        suffix: str = self.get_type_by_name(algo_name)
        engine = EnginePY(model, algo_name, cf_inputs, self.config, feature_list)
        result, duration = engine.run_algorithm(model_input, algo_time_limit)
        # duration = duration.seconds
        if algo_time_limit > 0:
            duration = min(duration, algo_time_limit)

        logger.debug(f'Algorithm {algo_name} ran successfully.')
        return result, duration

    def get_type_by_name(self, algo_name) -> str:
        name, suffix = os.path.splitext(algo_name)
        return suffix
