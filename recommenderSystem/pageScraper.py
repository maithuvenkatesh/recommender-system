import urllib2

from bs4 import BeautifulSoup

url = "http://uk.gamespot.com/games.html?platform=1029&mode=all&sort=views&dlx_type=all&sortdir=asc&official=all"
soup = BeautifulSoup(urllib2.urlopen(url))

gamesTable = soup.find("tbody").find_all("tr")

for game in gamesTable:
	title = game.find("a").string
	details = game.find_all("td")
	genre = details[0].string
	score = details[1].string
	releaseDate = details[2].string
	print(title + " " + genre + " " + score + " " + releaseDate)
