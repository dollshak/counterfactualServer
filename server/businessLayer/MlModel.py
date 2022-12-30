from abc import abstractmethod


class MlModel:

    @abstractmethod
    def predict(self, x: list):
        pass
