import os
import shutil
from var import *

os.chdir(Downloads)


for var in Type_List:
    if not os.path.exists(var):
        os.mkdir(var)

for path in os.listdir(Downloads):
    full_path = os.path.join(Downloads, path)
    if os.path.isfile(full_path):
        if(full_path.__contains__("/.")):
            # print("Hidden files found: ", full_path)
            pass

        else:
            ext = os.path.splitext(full_path)[1].lower()

            for l, t in zip(List_List, Type_List):
                if l.__contains__(ext):
                    shutil.move(full_path, t)

            # elif video_ext.__contains__(ext):
            #     video_paths.append(full_path)
            #     shutil.move(full_path, Video)

            # elif audio_ext.__contains__(ext):
            #     audio_paths.append(full_path)
            #     shutil.move(full_path, Audio)

            # elif compressed_ext.__contains__(ext):
            #     compressed_paths.append(full_path)
            #     shutil.move(full_path, Compressed)

            # elif adobe_ext.__contains__(ext):
            #     adobe_paths.append(full_path)
            #     shutil.move(full_path, Adobe)

            # elif microsoft_ext.__contains__(ext):
            #     microsoft_paths.append(full_path)
            #     shutil.move(full_path, Microsoft)

            # elif developer_ext.__contains__(ext):
            #     developer_paths.append(full_path)
            #     shutil.move(full_path, Developer)

            # else:
            #     other_paths.append(full_path)
            #     shutil.move(full_path, Others)
