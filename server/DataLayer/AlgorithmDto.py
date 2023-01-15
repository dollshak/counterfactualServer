from server.DataLayer.ArgumentDescriptionDto import ArgumentDescriptionDto

class AlgorithmDto:
    def __init__(self, file_content,  name: str, argument_lst: list[ArgumentDescriptionDto], description: str,
                 additional_info: str, output_example: list[str]):
        self.file_content = file_content
        self.name = name
        self.argument_lst = argument_lst
        self.description = description
        self.additional_info = additional_info
        self.output_example = output_example
