import argparse


class ParametersResolver:

    def __init__(self):
        self.parser = argparse.ArgumentParser()

    def parse_arguments(self):
        self.parser.add_argument('file_path')
        self.parser.add_argument('-f', '--from', dest="from_", required=False, default="ToCheck")
        self.parser.add_argument('-r', '--replace', dest="replace", required=False, action='store_false')
        self.parser.add_argument('-t', '--tab-chars', dest="number_of_chars_tab", type=int, default=4, required=False)

        args = self.parser.parse_args()

        return OperationDetailsDTO(args.file_path, args.from_, args.replace, args.number_of_chars_tab)


class OperationDetailsDTO:
    def __init__(self, file_path, parse_mode, replace, number_of_chars_tab):
        self.file_path = file_path
        self.parse_mode = parse_mode
        self.replace_mode = replace
        self.number_of_chars_tab = number_of_chars_tab

    def get_argument_list(self):
        return [self.file_path, self.parse_mode, self.replace_mode, self.number_of_chars_tab]
