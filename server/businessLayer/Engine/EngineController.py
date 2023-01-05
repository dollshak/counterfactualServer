import os.path

from server.businessLayer.Engine.EngineAPI import EngineAPI
from server.businessLayer.Engine.EngineInput import EngineInput
from server.businessLayer.Engine.EnginePY import EnginePY
from server.businessLayer.ML_Models.MlModel import MlModel


class EngineController:
    def __init__(self):
        self.cf_map: dict = {}
        self.init_cf_map()

    def run_algorithms(self, algo_names: list[str], model: MlModel, model_input: list, cf_inputs: list[list]) -> list[
        list]:
        results = [[] for i in range(len(algo_names))]
        for idx, algo_name in enumerate(algo_names):
            suffix: str = self.get_type_by_name(algo_name)
            engine = EnginePY(model, algo_name, [cf_inputs[idx]])
            # TODO implement here
            # engine: EngineAPI = self.cf_map[suffix](model, algo_name, cf_inputs[idx])
            result = engine.run_algorithm(model_input)
            results[idx] = result
        return results

    def get_type_by_name(self, algo_name) -> str:
        name, suffix = os.path.splitext(algo_name)
        return suffix

    def init_cf_map(self):
        self.cf_map['.py'] = EnginePY.__init__
