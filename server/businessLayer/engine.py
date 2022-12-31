class Engine:
    def __init__(self):
        self.selected_algo_lst = list()

    def run_algorithm(self, algorithm):
        raise Exception("Not implemented.")

    def run_algorithms(self, model, inputs: list):
        raise Exception("Not implemented.")

    def import_(self):
        raise Exception("Not implemented.")

    def create_exec(self, name):
        raise Exception("Not implemented.")

    def delete_exec(self, name):
        raise Exception("Not implemented.")

    def run_exec(self, name):
        raise Exception("Not implemented.")

    def run_model(self):
        raise Exception("Not implemented.")
