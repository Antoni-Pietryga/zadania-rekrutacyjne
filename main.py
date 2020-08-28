from parametersResolver import ParametersResolver
from modeAnalyzer import ModeAnalyzer
from lineChanger import LineChanger
from fileBackingUpCreator import FileBackingUpCreator
from file import File

REPLACE_FILE = True
CHECK_MODE = "ToCheck"

if __name__ == "__main__":

    parametersResolver = ParametersResolver()
    args = parametersResolver.parse_arguments()

    file = File(args.file_path, "r")
    lines = file.read_lines()

    if args.parse_mode == CHECK_MODE:
        modeAnalyzer = ModeAnalyzer(args.number_of_chars_tab)
        mode = modeAnalyzer.check_mode(lines)
        print("Most lines in the file begin with a", mode)
        exit()

    lineChanger = LineChanger(args.number_of_chars_tab)
    change_lines = lineChanger.change(lines, args.parse_mode)

    if args.replace_mode == REPLACE_FILE:
        fileBackingUpCreator = FileBackingUpCreator()
        new_file_name = fileBackingUpCreator.get_next_available_file_name(args.file_path)

        new_file = File(new_file_name, "w")
        new_file.write_lines(change_lines)

    else:
        file = File(args.file_path, "w")
        file.write_lines(change_lines)

    lineChanger.print_report()
