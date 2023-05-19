import os.path
from typing import Tuple, List, Any, Dict

from server.Tools.FailedCFException import FailedCFException
from server.Tools.ModelException import ModelException
from server.businessLayer.Engine.EnginePY import EnginePY
from server.businessLayer.ML_Models.MlModel import MlModel
from server.Tools.Logger import Logger
from datetime import timedelta
from datetime import datetime, date
import time

logger = Logger()


class EngineController:
    def __init__(self, config):
        self.cf_map: dict = {}
        self.init_cf_map()
        self.config = config

    def run_algorithms(self, algo_names: list[str], model: MlModel, model_input: dict, cf_inputs: dict,algos_time_limit) -> tuple[
        list[list[Any]], dict[str, float]]:
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
                result, duration = self.get_cf_results(algo_name, inputs, model, model_input)
                algo_runtimes[algo_name] = duration.total_seconds()
                results[idx] = result
            except FailedCFException as e:
                logger.error(f'{algo_name} failed to run, returned empty results')
                results[idx] = []
            except ModelException as e:
                # TODO need to decide how to return the error to client
                logger.error(f'model failed')
                results[idx] = []
        logger.debug(f'Finished to run algorithms.')
        return results, algo_runtimes

    def get_cf_results(self, algo_name, cf_inputs, model, model_input):
        suffix: str = self.get_type_by_name(algo_name)
        # TODO implement here -> bring engine by suffix instead of hard coded enginePY -> should create a function
        engine = EnginePY(model, algo_name, cf_inputs, self.config)
        start_time = datetime.now().time()
        start_time = timedelta(hours=start_time.hour, minutes=start_time.minute, seconds=start_time.second)
        result = engine.run_algorithm(model_input)
        end_time = datetime.now().time()
        end_time = timedelta(hours=end_time.hour, minutes=end_time.minute, seconds=end_time.second)
        duration = start_time - end_time
        logger.debug(f'Algorithm {algo_name} ran successfully.')
        return result,duration

    def get_type_by_name(self, algo_name) -> str:
        name, suffix = os.path.splitext(algo_name)
        return suffix

    def init_cf_map(self):
        self.cf_map['.py'] = EnginePY.__init__
