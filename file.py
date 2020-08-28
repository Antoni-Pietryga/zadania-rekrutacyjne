class File:
    def __init__(self, file_name, option):
        self.file = open(file_name, option)

    def read_lines(self):
        return self.file.readlines()

    def write_lines(self, lines):
        return self.file.writelines(lines)

    def __del__(self):
        self.file.close()