from json import loads
from argparse import ArgumentParser
from datetime import datetime
from random import randint, choice
from modules.nasa_scrape import Scrape
from modules.config import _logos


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
print(choice(_logos)) # outputs a random logo from the config file

def client(nasa) -> None:
    if loads(client_args.build.lower()):
        nasa.build(start=True) # builds the header of the html page
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
                print('[  openNasa  ] Successfully added an article to the html page')
            else:
                print(output)
    else:
        if loads(client_args.build.lower()):
            nasa.build(end=True) # will finish the html page

if __name__ == "__main__":
    nasa = Scrape(api_key=client_args.key)
    client(nasa=nasa) # run a client