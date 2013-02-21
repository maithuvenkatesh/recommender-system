import urllib2
import urllib

from bs4 import BeautifulSoup

#Base url of gamespot.com
baseurl1 = "http://uk.gamespot.com/games.html?platform="
baseurl2 = "&mode=all&sort=views&dlx_type=all&sortdir=asc&official=all&page="

#List of platforms
platforms = {"xbox360":1029, "pc":5, "playstation3":1028}

for platform in platforms:
	games = []
	pageCounter = 0
	noResults = False

	while pageCounter < 1:
		pageUrl = baseurl1 + str(platforms[platform]) + baseurl2 + str(pageCounter)
		pageCounter += 1

		#Get page
		pageSoup = BeautifulSoup(urllib2.urlopen(pageUrl))
		
		#Get table of games
		gamesSoup = pageSoup.find("tbody").find_all("tr")

		#Extract games from table
		if(gamesSoup == []):
			noResults = True
		else:
			out = {}
			for game in gamesSoup:
				out["title"] = game.find("a").string
				out["url"] = game.find("a").get('href')
				details = game.find_all("td")
				out["genre"] = details[0].string
				out["gamespotScore"] = details[1].string
				releaseDate = details[2].string
				out["year"] = releaseDate[8:12]
				if out["gamespotScore"]:
					print urllib2.urlopen("http://localhost:8081/saveGame",urllib.urlencode(out))
					#games.push({title: title, genre: genre, score:score, url:gameUrl})

	# Loop through games in page and get more details
	#for game in games:
		#gameurl = game[url]
		#gameDetailsSoup = BeautifulSoup(urllib2.urlopen(gameUrl))
		#userScoreLabel = gameDetailSoup.get("label")
		#if userScoreLabel == "User Score":
			#userScore = gameDetailSoup.get("a")
			#print("userScore" + userScore)

		# Pass each game to appengine app
		#for game in games:
			#urllib2.urlopen("http://localhost:8081/saveGame")
