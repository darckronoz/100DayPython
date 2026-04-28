#Learning python and skipping the days of the 100 days course because
#I already know a little bit of python haha
from dataclasses import dataclass

#webscrapping with beautifullsoup
from bs4 import BeautifulSoup

import requests

@dataclass
class Movie:
    title: str
    rank: int
    genre: str

my_page = requests.get('https://www.bfi.org.uk/sight-and-sound/greatest-films-all-time#rank-25')

soup = BeautifulSoup(my_page.content, 'html.parser')

movies = []

for m in soup.select("article a"):
    movies.append(Movie(title=m.find("h1").text, rank=int(m.select_one("div p").text.replace('=','')), genre=m.find("p", class_="PreviewCard__description").text))

print(movies[1].title) #done.


