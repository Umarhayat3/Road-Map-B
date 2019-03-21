# Road-Map-B/Task+01

import pathlib
import datetime

if __name__ == '__main__':
    date_string = datetime.date.today().strftime("%d-%m-%y")
    cur_path = pathlib.Path(".")
    File_PATTERN = "*.txt"
    paths = cur_path.glob(File_PATTERN)
    ARCHIVE = pathlib.Path("Archive")
    new_path = cur_path.joinpath(ARCHIVE, date_string)
    new_path.mkdir()
    for path in paths:
        path.rename(new_path.joinpath(path.name))


