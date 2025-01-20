import json
from os import listdir
from os.path import isfile

def getAllFiles(path: str) -> list[str]:
    if path[-1] == "/" or path[:-1] == "\\":
        path = path[:-1]
    path = path.replace("/", "\\")
    files = []
    for item in listdir(path):
        if isfile(f"{path}\\{item}"):
            files.append(f"{path}\\{item}")
        else:
            files.extend(getAllFiles(f"{path}\\{item}"))
    return files

reslist = list(map(lambda x: x[4:], getAllFiles("res")))
json.dump(reslist, open("reslist.json", "w", encoding="utf-8"), ensure_ascii=False, indent=4)