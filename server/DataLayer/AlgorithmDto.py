from server.DataLayer.ArgumentDescriptionDto import ArgumentDescriptionDto


class AlgorithmDto:
    def __init__(self, file, name: str, args_lst: list[ArgumentDescriptionDto]):
        self.file = file
        self.name = name
        self.args_lst = args_lst
