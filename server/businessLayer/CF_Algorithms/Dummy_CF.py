from server.businessLayer.ML_Models import MlModel
from server.businessLayer.Algorithms.Algorithm import Algorithm
from server.businessLayer.Algorithms.ArgumentDescription import ArgumentDescription


def initAlgo(model, arg_lst):
    return Dummy_CF(arg_lst, model=model)


class Dummy_CF(Algorithm):
    def __init__(self, arg_lst: list, model: MlModel):
        super().__init__(arg_lst, model)

    def explain(self, model_input):
        # total
        to_change_index = 1
        curr_input = model_input
        if self.model.predict(curr_input) == 1:
            return curr_input
        temp_input = curr_input.copy()
        temp_input[to_change_index] = temp_input[to_change_index] * 2
        up = self.model.predict(curr_input) < self.model.predict(temp_input)
        if up:
            print("higher the better")
        else:
            print("lower the better")
        low = curr_input[to_change_index]
        high = curr_input[2] if up else curr_input[0]
        mid = low
        last_correct = curr_input.copy()
        while low < high if up else high < low:
            mid = (low + high) / 2
            curr_input[to_change_index] = mid
            val = self.model.predict(curr_input)
            if val >= 1:
                if up:
                    # not loan case
                    high = mid - 1
                else:
                    # loan case
                    high = mid + 1
                last_correct = curr_input.copy()
            else:
                # loan case
                if not up:
                    low = mid - 1
                else:
                    low = mid + 1

        return last_correct