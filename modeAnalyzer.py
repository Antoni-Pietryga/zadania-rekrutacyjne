class ModeAnalyzer:
    def __init__(self, number_of_chars_tab):
        self.number_of_chars_tab = number_of_chars_tab

    def check_mode(self, lines):
        tabs, spaces = 0, 0

        for line in lines:
            for char in line:

                if char == " ":
                    spaces += 1
                elif char == "\t":
                    tabs += 1

                break

        if spaces > tabs:
            return "spaces"
        else:
            return "tabs"