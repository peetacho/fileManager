import os
import shutil
from var import *

os.chdir(Downloads)

if not os.path.exists(Image):
    os.mkdir(Image)

if not os.path.exists(Video):
    os.mkdir(Video)

if not os.path.exists(Audio):
    os.mkdir(Audio)

if not os.path.exists(Compressed):
    os.mkdir(Compressed)

if not os.path.exists(Adobe):
    os.mkdir(Adobe)

if not os.path.exists(Microsoft):
    os.mkdir(Microsoft)

if not os.path.exists(Developer):
    os.mkdir(Developer)

if not os.path.exists(Others):
    os.mkdir(Others)

for path in os.listdir(Downloads):
    full_path = os.path.join(Downloads, path)
    if os.path.isfile(full_path):
        if(full_path.__contains__("/.")):
            print("Hidden files found: ", full_path)

        else:
            ext = os.path.splitext(full_path)[1].lower()

            if img_ext.__contains__(ext):
                img_paths.append(full_path)
                shutil.move(full_path, Image)

            elif video_ext.__contains__(ext):
                video_paths.append(full_path)
                shutil.move(full_path, Video)

            elif audio_ext.__contains__(ext):
                audio_paths.append(full_path)
                shutil.move(full_path, Audio)

            elif compressed_ext.__contains__(ext):
                compressed_paths.append(full_path)
                shutil.move(full_path, Compressed)

            elif adobe_ext.__contains__(ext):
                adobe_paths.append(full_path)
                shutil.move(full_path, Adobe)

            elif microsoft_ext.__contains__(ext):
                microsoft_paths.append(full_path)
                shutil.move(full_path, Microsoft)

            elif developer_ext.__contains__(ext):
                developer_paths.append(full_path)
                shutil.move(full_path, Developer)

            else:
                other_paths.append(full_path)
                shutil.move(full_path, Others)
