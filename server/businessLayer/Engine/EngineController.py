import os.path

from server.businessLayer.Engine.EngineAPI import EngineAPI
from server.businessLayer.Engine.EngineInput import EngineInput
from server.businessLayer.Engine.EnginePY import EnginePY
from server.businessLayer.ML_Models.MlModel import MlModel


class EngineController:
    def __init__(self):
        self.cf_map: dir[str, EngineAPI] = {}
        self.init_cf_map()

    def run_algorithms(self, algo_names: list[str], model: MlModel, model_input: list, engine_config: EngineInput,
                       cf_inputs: list[list]):
        results = [[] for i in range(len(algo_names))]
        for idx, algo_name in enumerate(algo_names):
            suffix: str = self.get_type_by_name(algo_name)
            engine: EngineAPI = self.cf_map[suffix]
            result = engine.run_algorithm(model, algo_name, model_input, cf_inputs[idx])
            results[idx] = result

        return results

    def get_type_by_name(self, algo_name) -> str:
        name, suffix = os.path.splitext(algo_name)
        return suffix

    def init_cf_map(self):
        engine_py = EnginePY()
        self.cf_map['.py'] = engine_py
