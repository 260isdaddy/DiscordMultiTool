import requests
from bs4 import BeautifulSoup


def rsItem(item_name):
    OSRS_url = "https://oldschool.runescape.wiki/w/" + item_name
    data = requests.get(OSRS_url)
    soup = BeautifulSoup(data.content, "html.parser")
    OSRS_price = str(soup.find('span', attrs={'class':"infobox-quantity-replace"}))

    RS3_url = "https://runescape.wiki/w/" + item_name
    data = requests.get(RS3_url)
    soup = BeautifulSoup(data.content, "html.parser")
    RS3_price = str(soup.find('span', attrs={'class':"infobox-quantity-replace"}))

    osrs = OSRS_price[39:-7]
    rs3 = RS3_price[39:-7]

    if osrs == '':
        osrs = 'Item not in this game or not on GE.'

    if rs3 == '':
        rs3 = 'Item not in this game or not on GE.'

    return(item_name.capitalize() +
           "\nOSRS: " + osrs +
           "\nRS3: " + rs3)

#<span class="infobox-quantity-replace">6</span>