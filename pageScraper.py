import urllib2

from bs4 import BeautifulSoup

url = "http://uk.gamespot.com/games.html?platform=1029&mode=all&sort=views&dlx_type=all&sortdir=asc&official=all&page="
games = []
pageCounter = 0
noResults = False

while !noResults:

	pageUrl = url + pageCounter
	pageSoup = BeautifulSoup(urllib2.urlopen(pageUrl))

	games = pageSoup.find("tbody").find_all("tr")

	# Extract games from table
	if(games == []):
		noResults = true
	else:
		for game in games:
			title = game.find("a").string
			gameUrl = game.find("a").get('href')
			details = game.find_all("td")
			genre = details[0].string
			score = details[1].string
			releaseDate = details[2].string
			if score :
				#print(title + " " + genre + " " + score + " " + releaseDate + gameUrl)
				games.push({title:title, genre: genre, score:score, url:gameUrl})

	# Loop through games and get more details
	#for game in games:
		#gameUrl = game[url];
		#gameDetailsSoup = BeautifulSoup(urllib2.urlopen(gameUrl))
