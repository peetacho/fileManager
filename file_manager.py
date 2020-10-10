import os
import shutil
import datetime
from var import *

os.chdir(Downloads)

recent_time = 1800


def get_time_difference(full_path):
    birth_time = datetime.datetime.fromtimestamp(
        os.stat(full_path).st_birthtime)
    now_time = datetime.datetime.now()
    diff = now_time-birth_time

    return diff.total_seconds()


for var in Type_List:
    if not os.path.exists(var):
        os.mkdir(var)

# moves to recent folder
for path in os.listdir(Downloads):
    full_path = os.path.join(Downloads, path)
    if os.path.isfile(full_path):
        if(full_path.__contains__("/.")):
            # print("Hidden files found: ", full_path)
            # ignores hidden files
            pass

        else:
            ext = os.path.splitext(full_path)[1].lower()
            # move to recents folder
            shutil.move(full_path, Recent)

# move out of recents folder
for path in os.listdir(Recent):
    full_path = os.path.join(Recent, path)

    if os.path.isfile(full_path):
        # if file was created within 30 mins
        # print(get_time_difference(full_path))
        if get_time_difference(full_path) >= recent_time:
            if(full_path.__contains__("/.")):
                # print("Hidden files found: ", full_path)
                # ignores hidden files
                pass

            else:
                ext = os.path.splitext(full_path)[1].lower()

                for l, t in zip(List_List, Type_List):
                    if l.__contains__(ext):
                        shutil.move(full_path, t)
