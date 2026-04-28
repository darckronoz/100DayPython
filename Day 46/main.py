#Learning python and skipping the days of the 100 days course because
#I already know a little bit of python haha
import json
from dataclasses import dataclass

#music time machine to spotify.

import requests
from bs4 import BeautifulSoup


@dataclass
class Song:
    title: str
    artist: str

#url sample https://www.billboard.com/charts/hot-100/2000-01-01/
# H3 title-of-a-story
# DIV o - chart - results - list - row - container
# SPAN
year_songs_dict = {}

#Falta usar la api de spotify y arreglar el error al obtener la info.
for year in range(2000, 2025):
    content = requests.get(f"https://www.billboard.com/charts/hot-100/{year}-01-01/")
    page = BeautifulSoup(content.content, "html.parser")
    divs = page.find_all("div", {"class": "o-chart-results-list-row-container"})
    music_list = []
    for div in divs:
        song = div.find("h3").text
        artists = div.select_one("li span").text
        music_list.append(Song(song, artists))
    year_songs_dict[year] = music_list

print(year_songs_dict)

# with open("music_list.json", "w") as f:
#     json.dump(year_songs_dict, f)