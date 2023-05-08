from server.DataLayer.ArgumentDescriptionDto import ArgumentDescriptionDto

class AlgorithmDto:
    def __init__(self, file_content, param_name: str, argument_lst: list[ArgumentDescriptionDto], description: str,
                 additional_info: str, output_example: list[str], algo_type):
        self.file_content = file_content
        self.param_name = param_name
        self.argument_lst = argument_lst
        self.description = description
        self.additional_info = additional_info
        self.output_example = output_example
        self.algo_type = algo_type
