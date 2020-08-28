import sys

from parametersResolver import *
from modeAnalyzer import ModeAnalyzer
from lineChanger import LineChanger
from fileBackingUpCreator import FileBackingUpCreator


def test_parameters_resolver():
    input_list = [
        [sys.argv[0], "file_name.txt", "-f", "tabs"],
        [sys.argv[0], "file_name.txt", "--from", "tabs"],
        [sys.argv[0], "file.txt-copy", "-f", "spaces"],
        [sys.argv[0], "file_name.txt", "-f", "tabs", "-r"],
        [sys.argv[0], "file_name.txt", "--from", "tabs", "-r", "-t", "6"],
        [sys.argv[0], "my_data.txt", "-r", "-f", "spaces"],
        [sys.argv[0], "file_name.txt", "--tab-char", "8", "-f", "spaces", "-r"],
        [sys.argv[0], "file_name.txt"],
        [sys.argv[0], "file_name.txt-copy", "-r", "-t", "10"],
        [sys.argv[0], "data.txt", "--from", "spaces", "--replace"],
    ]

    result_list = [
        ["file_name.txt", "tabs", True, 4],
        ["file_name.txt", "tabs", True, 4],
        ["file.txt-copy", "spaces", True, 4],
        ["file_name.txt", "tabs", False, 4],
        ["file_name.txt", "tabs", False, 6],
        ["my_data.txt", "spaces", False, 4],
        ["file_name.txt", "spaces", False, 8],
        ["file_name.txt", "ToCheck", True, 4],
        ["file_name.txt-copy", "ToCheck", False, 10],
        ["data.txt", "spaces", False, 4],
    ]

    for i in range(len(input_list)):
        sys.argv = input_list[i]
        dto = ParametersResolver().parse_arguments()

        assert dto.get_argument_list() == result_list[i]


def test_file_backing_up_creator():

    fileBackingUpCreator = FileBackingUpCreator()

    input_list = [
        "testDirectory/data-copy.txt",
        "testDirectory/file.txt",
        "testDirectory/my_favorite_file-copy-2000.txt",
        "testDirectory/test.py",
        "testDirectory/file_150.rtf",
        "testDirectory/file_150.odt",
        "testDirectory/file_150.docx"
    ]

    result_list = [
        "testDirectory/data-copy-1.txt",
        "testDirectory/file-copy.txt",
        "testDirectory/my_favorite_file-copy-2001.txt",
        "testDirectory/test-copy.py",
        "testDirectory/file_150-copy.rtf",
        "testDirectory/file_150-copy.odt",
        "testDirectory/file_150-copy.docx"
    ]

    for i in range(len(input_list)):
        assert fileBackingUpCreator.get_next_available_file_name(input_list[i]) == result_list[i]


def test_mode_analyzer_4_chars():

    modeAnalyzer = ModeAnalyzer(4)
    input_list = [
        ['\t\tlllll', '\taaaa', '    Napis', '    Napis', '      Cos tam'],
        ['\t\tlllll', '\taaaa', '    Napis', '\t    Napis', '      Cos tam'],
        ['       Pies lubi kota', '       Kot lubi psa', '      Pociag do domu', '    Odjezdza za', '     15 minut'],
        ['\t\t\t\t\tSzlachetne', '\t\t\t\t\t\tZdrowie', '\t\t\t\t\t\tNikt się', '\tnie', '\t\tdowie']
    ]

    result_list = [
        "spaces",
        "tabs",
        "spaces",
        "tabs",
    ]

    for i in range(len(input_list)):
        assert modeAnalyzer.check_mode(input_list[i]) == result_list[i]


def test_line_changer_4_chars():

    input_list = [
        ['			lllll', '		aaaa', '		Napis', '	Napis', '      Cos tam'],
        ['\t\t\tlllll', '\t\taaaa', '\t\tNapis', '	Napis', '      Cos tam'],
        ['\t	\tlllll', '	\taaaa', '\t	Napis', '	Napis', '      Cos tam'],
        ['        Pies lubi kota', '    Kot lubi psa', 'Pociag do domu', '        Odjezdza za', '    15 minut'],
        ['        Pies lubi kota', '    Kot lubi psa', 'Pociag do domu', '        Odjezdza za', '    15 minut'],
        ['\t\t\t\tSzlachetne', '\t\t\tZdrowie', '\t\tNikt się', '\tnie', 'dowie'],
        ['\t\t\t\tSzlachetne', '\t\t\tZdrowie', '\t\tNikt się', '\tnie', 'dowie']
    ]
    modes_list = [
        "tabs",
        "tabs",
        "tabs",
        "spaces",
        "tabs",
        "tabs",
        "spaces"
    ]
    result_list = [
        ['            lllll', '        aaaa', '        Napis', '    Napis', '      Cos tam'],
        ['            lllll', '        aaaa', '        Napis', '    Napis', '      Cos tam'],
        ['            lllll', '        aaaa', '        Napis', '    Napis', '      Cos tam'],
        ['\t\tPies lubi kota', '\tKot lubi psa', 'Pociag do domu', '\t\tOdjezdza za', '\t15 minut'],
        ['        Pies lubi kota', '    Kot lubi psa', 'Pociag do domu', '        Odjezdza za', '    15 minut'],
        ['                Szlachetne', '            Zdrowie', '        Nikt się', '    nie', 'dowie'],
        ['\t\t\t\tSzlachetne', '\t\t\tZdrowie', '\t\tNikt się', '\tnie', 'dowie']
    ]
    lineChanger = LineChanger(4)

    for i in range(len(input_list)):
        assert lineChanger.change(input_list[i], modes_list[i]) == result_list[i]

def test_line_changer_6_chars():

    input_list = [
        ['			lllll', '		aaaa', '		Napis', '	Napis', '      Cos tam'],
        ['\t\t\tlllll', '\t\taaaa', '\t\tNapis', '	Napis', '      Cos tam'],
        ['\t	\tlllll', '	\taaaa', '\t	Napis', '	Napis', '      Cos tam'],
        ['            Pies lubi kota', '      Kot lubi psa', 'Pociag do domu', '            Odjezdza za', '      15 minut'],
        ['            Pies lubi kota', '      Kot lubi psa', 'Pociag do domu', '            Odjezdza za', '      15 minut'],
        ['\t\t\t\tSzlachetne', '\t\t\tZdrowie', '\t\tNikt się', '\tnie', 'dowie'],
        ['\t\t\t\tSzlachetne', '\t\t\tZdrowie', '\t\tNikt się', '\tnie', 'dowie']
    ]
    modes_list = [
        "tabs",
        "tabs",
        "tabs",
        "spaces",
        "tabs",
        "tabs",
        "spaces"
    ]
    result_list = [
        ['                  lllll', '            aaaa', '            Napis', '      Napis', '      Cos tam'],
        ['                  lllll', '            aaaa', '            Napis', '      Napis', '      Cos tam'],
        ['                  lllll', '            aaaa', '            Napis', '      Napis', '      Cos tam'],
        ['\t\tPies lubi kota', '\tKot lubi psa', 'Pociag do domu', '\t\tOdjezdza za', '\t15 minut'],
        ['            Pies lubi kota', '      Kot lubi psa', 'Pociag do domu', '            Odjezdza za', '      15 minut'],
        ['                        Szlachetne', '                  Zdrowie', '            Nikt się', '      nie', 'dowie'],
        ['\t\t\t\tSzlachetne', '\t\t\tZdrowie', '\t\tNikt się', '\tnie', 'dowie']
    ]
    lineChanger = LineChanger(6)

    for i in range(len(input_list)):
        assert lineChanger.change(input_list[i], modes_list[i]) == result_list[i]