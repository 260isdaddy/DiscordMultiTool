import json
import os
from urllib.request import urlopen

os.chdir("../venv")

steam_string = open('C:/Users/bmood/PycharmProjects/testing/steamstuff.json','r',encoding='utf-8')

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