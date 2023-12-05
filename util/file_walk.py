import os


def file_walk(folder_path):
    files_list = os.listdir(folder_path)
    files_list = [file for file in files_list if os.path.isfile(os.path.join(folder_path, file))]
    return files_list



