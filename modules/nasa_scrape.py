from requests import get
from json import loads
from time import time
from random import randint, choice


class Scrape:
    def __init__(self, api_key:str) -> None:
        "Initialization of a class"
        self.api_key = api_key
        self.time = round(time(),0)
    def request(self, year:str, month:str, day:str) -> dict:
        """Request to NASA servers"""
        linksrc = f"https://api.nasa.gov/planetary/apod?date={year}-{month}-{day}&hd=True&api_key={self.api_key}"
        data = loads(get(linksrc).text)
        return data
    def build(self, data:dict={}, start:bool=False, end:bool=False) -> bool:
        """This function builds an HTML page based on the server response"""
        CHOICE = [["45A6C1", "46C2A3"], ["4671C2", "8246C2"], ["C24646", "FFA630"]]
        COLOR = choice(CHOICE)

        URL = str(data["url"]) if "url" in data else ""
        TITLE = str(data["title"]) if "title" in data else ""
        EXPLANATION = str(data["explanation"]) if "explanation" in data else ""
        DATE = str(data["date"]) if "date" in data else ""

        with open(f"index-{self.time}.html", "a") as htmlpage:
            if start:
                htmlpage.write("""<!DOCTYPE HTML>
            <html>
            <head>
                <title>NASA Pictures</title>
            </head>
            <body>
                """)
            elif end:
                htmlpage.write("""
            </body>
                </html>""")
            else:
                htmlpage.write("""
                <div style="border-radius: 10px; background: white; border: 1px solid #""" + COLOR[0] + """; padding: 25px; margin: 10px;">
                    <div><p style="text-align: center; margin: 20px;"><img style="border-radius: 5px;" src='""" + URL + """'></p></div>
                    <div><h1 style="font-family: arial; text-align: center; color: #282828;">""" + TITLE + """</h1><h3 style="font-family: arial; text-align: center; color: #868686;">""" + DATE + """</h3></div>
                    <div style="color: white; padding: 10px; margin: 10px; border-radius: 20px; box-shadow: 0px 5px 13px #AFAFAF; font-family: arial; background: linear-gradient(45deg, #""" + COLOR[0] + """, #""" + COLOR[1] + """)"><p>""" + EXPLANATION + """</p></div>
                </div>
                """)