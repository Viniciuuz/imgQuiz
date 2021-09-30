from os import walk
from json import dump, dumps

filenames = next(walk("img/"), (None, None, []))[2]

data = []
for i in filenames:
    data.append(i.replace(".jpg", ""))


open("games.js", "w").write(f"var games = {data}")