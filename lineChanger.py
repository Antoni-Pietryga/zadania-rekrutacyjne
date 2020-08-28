
class LineChanger:
    def __init__(self, number_of_chars_tab):
        self.editedLines = 0
        self.number_of_chars_tab = number_of_chars_tab

    def change(self, lines, parse_mode):
        if parse_mode == "tabs":
            return self.change_from_tabs(lines)
        else:
            return self.change_from_spaces(lines)

    def change_from_tabs(self, lines):
        change_lines = []
        for i in range(len(lines)):
            line_after_lstrip = lines[i].lstrip("	")

            if self.length_difference(lines[i], line_after_lstrip) > 0:
                self.editedLines += 1

            spaces_multiply = self.length_difference(lines[i], line_after_lstrip) * self.number_of_chars_tab
            line_after_change = spaces_multiply * " " + line_after_lstrip

            change_lines.append(line_after_change)

        return change_lines

    def change_from_spaces(self, lines):
        change_lines = []
        for i in range(len(lines)):
            line_after_lstrip = lines[i].lstrip(" ")

            if self.length_difference(lines[i], line_after_lstrip) > 0:
                self.editedLines += 1

            tab_multiply = self.length_difference(lines[i], line_after_lstrip) // self.number_of_chars_tab
            line_after_change = tab_multiply * "	" + line_after_lstrip

            change_lines.append(line_after_change)

        return change_lines

    def print_report(self):
        print("Edited lines: ", self.editedLines)

    @staticmethod
    def length_difference(string_1, string_2):
        return abs(len(string_1) - len(string_2))
