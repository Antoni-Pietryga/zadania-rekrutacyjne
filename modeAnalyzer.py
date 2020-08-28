class ModeAnalyzer:
    def __init__(self, number_of_chars_tab):
        self.number_of_chars_tab = number_of_chars_tab

    def check_mode(self, lines):
        tabs, spaces, spaces_in_line, tabs_in_line = 0, 0, 0, 0

        for line in lines:
            spaces_in_line, tabs_in_line = 0, 0

            for char in line:

                if char == " ":
                    spaces_in_line += 1
                elif char == "\t":
                    tabs_in_line += 1
                else:
                    break

            spaces_in_line //= self.number_of_chars_tab

            if spaces_in_line > tabs_in_line:
                spaces += 1
            elif spaces_in_line < tabs_in_line:
                tabs += 1

        if spaces > tabs:
            return "spaces"
        else:
            return "tabs"