#Python file search engine

import os

fileType = ".png"
anyFile = os.listdir(".") #search path {/home/user_name/folder}

for file in anyFile:
    if file.endswith(fileType):
        print(file)
