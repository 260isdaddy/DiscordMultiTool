import json
import os
from urllib.request import urlopen
from pathlib import Path

# Path logic
path = Path(os.getcwd())
levels_up = 1

#print(path)

#rootDir = str(path.parents[levels_up-1])

#print(rootDir)

steam_string = open(str(path) + '\\json\\' + 'steamstuff.json','r',encoding='utf-8')

#print(steam_string)

# Path Logic End

# BINGOOOOO print(data['app'])
data = json.load(steam_string)


def steamGameSearch(game_name):
    id = 1

    for game in data["app"]:
        #print(game['name'])

        if game_name.lower() == str(game['name']).lower():
            id = game['appid']
            official_name = str(game['name'])

    if id == 1:
        return "Game not found."

    embed = ("https://store.steampowered.com/app/" + str(id))
    return embed