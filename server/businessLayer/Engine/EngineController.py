import os.path

from server.businessLayer.Engine.EnginePY import EnginePY
from server.businessLayer.ML_Models.MlModel import MlModel
from server.Tools.Logger import Logger

logger = Logger()


class EngineController:
    def __init__(self):
        self.cf_map: dict = {}
        self.init_cf_map()

    def run_algorithms(self, algo_names: list[str], model: MlModel, model_input: dict, cf_inputs: dict) -> list[
        list]:
        # init result array for each cf
        results = [[] for i in range(len(algo_names))]
        # for each cf
        logger.debug(f'Starting run algorithms.')
        for idx, algo_name in enumerate(algo_names):
            try:
                logger.debug(f'running {algo_name}')
                name, suffix = os.path.splitext(algo_name)
                inputs = cf_inputs[name]
                result = self.get_cf_results(algo_name, inputs, model, model_input)
                results[idx] = result
            except:
                logger.error(f'{algo_name} failed to run, returned empty results')
                results[idx] = []
        logger.debug(f'Finished to run algorithms.')
        return results

    def get_cf_results(self, algo_name, cf_inputs, model, model_input):
        suffix: str = self.get_type_by_name(algo_name)
        # TODO implement here -> bring engine by suffix instead of hard coded enginePY -> should create a function
        engine = EnginePY(model, algo_name, cf_inputs)
        result = engine.run_algorithm(model_input)
        logger.debug(f'Algorithm {algo_name} ran successfully.')
        return result

    def get_type_by_name(self, algo_name) -> str:
        name, suffix = os.path.splitext(algo_name)
        return suffix

    def init_cf_map(self):
        self.cf_map['.py'] = EnginePY.__init__
