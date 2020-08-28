import os


class FileBackingUpCreator:

    def get_next_available_file_name(self, file_path):
        path, file_name, extension = self.separate_file_path(file_path)
        file_name_after_split = file_name.split("-")

        if len(file_name_after_split) == 1:
            new_file_name = file_name_after_split[0] + "-copy"
        elif len(file_name_after_split) == 2:
            new_file_name = file_name_after_split[0] + "-copy-1"
        else:
            new_file_name = file_name_after_split[0] + "-copy-" + str(int(file_name_after_split[2]) + 1)

        new_file_name += extension
        if path == "":
            new_file_path = new_file_name
        else:
            new_file_path = path + "\\" + new_file_name

        if self.file_name_existing_check(new_file_name, path):
            return self.get_next_available_file_name(new_file_path)
        else:
            return new_file_path

    @staticmethod
    def file_name_existing_check(new_file_name, path):
        if path == "":
            file_names_dir_list = os.listdir()
        else:
            file_names_dir_list = os.listdir(path)
        for dir_file_name in file_names_dir_list:
            if dir_file_name == new_file_name:
                return True
        return False

    @staticmethod
    def separate_file_path(file_path):
        split_path = file_path.split('\\')
        file_name_split = split_path[-1].split(".")
        return file_path[:len(file_path)-len(split_path[-1])], file_name_split[0], "." + file_name_split[1]
