from pathlib import Path
import re


def change_name_on_dir(directory: str):
    path_start = './' + directory + '/'
    path = Path('./' + directory + '/')
    for currentFile in path.iterdir():             
        if currentFile is not dir:
            file_name = currentFile.name
            full_path = re.sub('-', r"/", file_name)
            new_file_name = re.search(r"\d+.txt", full_path).group(0)
            path_to_new_file = re.search(r"\d{4}/\d+/", full_path).group(0)
            Path(path_start + path_to_new_file).mkdir(parents=True, exist_ok=True)
            Path(path_start + path_to_new_file + new_file_name).touch()
            currentFile.unlink()

