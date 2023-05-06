import pickle


# TODO we could use joblib instead of pickle to allow multiple files support
class PickleModel:

    @staticmethod
    def from_pickle_file(pickle_file_path):
        with open(pickle_file_path, 'rb') as file:
            model = pickle.load(file)
        return model

    @staticmethod
    def to_pickle_file(model, name="model_packed", directory='server/businessLayer/ML_Models'):
        filename = f'{directory}/{name}.pkl'
        with open(filename, 'wb') as file:
            pickle.dump(model, file)

    @staticmethod
    def from_pickle_content(pickle_content):
        return pickle.load(pickle_content)
