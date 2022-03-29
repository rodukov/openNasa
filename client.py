import argparse
from datetime import datetime

from aiohttp import request
from nasa_scrape import Scrape
from random import randint, choice


parser = argparse.ArgumentParser(description='NASA Scraper argument parser')
parser.add_argument('-k', '--key', type=str)
parser.add_argument('-b', '--build', type=bool)
parser.add_argument('-y', '--year')
parser.add_argument('-m', '--month')
parser.add_argument('-d', '--day')
parser.add_argument('-c', '--count')
client_args = parser.parse_args()

_logos = [""""
 _______  _______  _______  __    _  __    _  _______  _______  _______ 
|       ||       ||       ||  |  | ||  |  | ||   _   ||       ||   _   |
|   _   ||    _  ||    ___||   |_| ||   |_| ||  |_|  ||  _____||  |_|  |
|  | |  ||   |_| ||   |___ |       ||       ||       || |_____ |       |
|  |_|  ||    ___||    ___||  _    ||  _    ||       ||_____  ||       |
|       ||   |    |   |___ | | |   || | |   ||   _   | _____| ||   _   |
|_______||___|    |_______||_|  |__||_|  |__||__| |__||_______||__| |__|

""","""
  ____                _  __             
 / __ \___  ___ ___  / |/ /__ ____ ___ _
/ /_/ / _ \/ -_) _ \/    / _ `(_-</ _ `/
\____/ .__/\__/_//_/_/|_/\_,_/___/\_,_/ 
    /_/                     
""", """
   ___                 _  _               
  / _ \ _ __  ___ _ _ | \| |__ _ ___ __ _ 
 | (_) | '_ \/ -_) ' \| .` / _` (_-</ _` |
  \___/| .__/\___|_||_|_|\_\__,_/__/\__,_|
       |_|                                

"""]
_history = []
print(choice(_logos))
nasa = Scrape(api_key=client_args.key)
if client_args.build:
    nasa.build(start=True)
for i in range(int(client_args.count)):
    request_data = []
    if (client_args.year == "random"): request_data.append(randint(1996, int((str(datetime.now()).split(" ")[0]).split("-")[0])))
    else: request_data.append(client_args.year)
    if (client_args.month == "random"): request_data.append(randint(1, 12))
    else: request_data.append(client_args.year)
    if (client_args.day == "random"): request_data.append(randint(1, 31))
    else: request_data.append(client_args.year)
    
    output = nasa.request(year=str(request_data[0]), month=str(request_data[1]), day=str(request_data[2]))
    if output not in _history:
        _history.append(output)
        if client_args.build:
            nasa.build(output)
            print('[  openNasa  ] Successfully added an article to the html page')
        else:
            print(output)
else:
    if client_args.build:
        nasa.build(end=True)
