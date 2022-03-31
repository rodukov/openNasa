from json import loads
from argparse import ArgumentParser
from datetime import datetime
from random import randint, choice
from modules.nasa_scrape import Scrape
from modules import config
from time import sleep


"""Getting user arguments"""
parser = ArgumentParser(description='Information about using the openNasa software')
parser.add_argument('-k', '--key', help="NASA API key")
parser.add_argument('-b', '--build', help="If True the script will create an html page, if False it will output the results to the terminal")
parser.add_argument('-y', '--year', help="Enter the desired year, for random results write 'random'")
parser.add_argument('-m', '--month', help="Enter the desired month, for random results write 'random'")
parser.add_argument('-d', '--day', help="Enter the desired day, for random results write 'random'")
parser.add_argument('-c', '--count', help="Enter the number of articles, for example, '30', without quotes")
client_args = parser.parse_args()

_history = [] # stores all requests
print(choice(config._logos)) # outputs a random logo from the config file

"""You can edit modules/config.py"""
print(config._neutral_c + "Author:" + config._reset_c, config._author_a)
print(config._neutral_c + "openNasa repository pages:" + config._reset_c)
for _item in config._link_to_openNasa_repository_a.items():
    print(config._main_indent+f"{_item[0]}: {_item[1]}")
print(config._neutral_c + "Author's Social Media:" + config._reset_c)
for _item in config._link_to_social_media_a.items():
    print(config._main_indent+f"{_item[0]}: {_item[1]}")
else:
    print("\n")
    sleep(config._sleep_time_after_starting_program) # Resting while the user looks at the welcome screen

def client(nasa) -> None:
    if loads(client_args.build.lower()):
        nasa.build(start=True) # builds the header of the html page
        print(config._successfully_build_header_d)
    for i in range(int(client_args.count)):
        request_data = [] # this list will generate a request for NASA API

        if (client_args.year == "random"): request_data.append(randint(1996, int((str(datetime.now()).split(" ")[0]).split("-")[0])))
        else: request_data.append(client_args.year)
        if (client_args.month == "random"): request_data.append(randint(1, 12))
        else: request_data.append(client_args.year)
        if (client_args.day == "random"): request_data.append(randint(1, 31))
        else: request_data.append(client_args.year)
        
        output = nasa.request(year=str(request_data[0]), month=str(request_data[1]), day=str(request_data[2])) # sending a request
        if output not in _history: # check if there was such a request in the history
            _history.append(output)
            if loads(client_args.build.lower()):
                nasa.build(output) # add an article to an html page
                print(config._successfully_d)
            else:
                print(output)
                print(config._fence)
    else:
        if loads(client_args.build.lower()):
            nasa.build(end=True) # will finish the html page
            print(config._successfully_build_d)

if __name__ == "__main__":
    nasa = Scrape(api_key=client_args.key)
    client(nasa=nasa) # run a client