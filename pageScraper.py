import urllib2
import urllib
import re

from bs4 import BeautifulSoup

#Base url of gamespot.com
baseurl1 = "http://uk.gamespot.com/games.html?platform="
baseurl2 = "&mode=all&sort=views&dlx_type=all&sortdir=asc&official=all&page="

#List of platforms
platforms = {"xbox360":1029}# "pc":5, "playstation3":1028}

for platform in platforms:
	print platform
	games = []
	pageCounter = 0
	noResults = False

	while pageCounter < 60:
		print pageCounter
		pageUrl = baseurl1 + str(platforms[platform]) + baseurl2 + str(pageCounter)
		pageCounter += 1

		#Get page
		pageSoup = BeautifulSoup(urllib2.urlopen(pageUrl))
		
		#Get table of games
		gamesTableSoup = pageSoup.find("tbody").find_all("tr")

		#Extract games from table
		if(gamesTableSoup == []):
			noResults = True
		else:
			out = {}
			for game in gamesTableSoup:
				out["title"] = game.find("a").string
				out["url"] = game.find("a").get('href')
				details = game.find_all("td")
				out["genre"] = details[0].string
				out["gamespotScore"] = details[1].string
				releaseDate = details[2].string
				out["year"] = releaseDate[-4:]
				out["platform"] = platform
				if out["gamespotScore"]:
					#Create page url
					gameUrl = out["url"]
					techUrl = re.sub("platform", "techinfo/platform", gameUrl)

					#Get the table of statistics
					gameSoup = BeautifulSoup(urllib2.urlopen(techUrl))
					gameStatsSoup = gameSoup.find("div", {"id": "gamestats"})
					imgTag = gameStatsSoup.find("img")
					out["imgUrl"] = imgTag["src"]
					out["publisher"] = gameStatsSoup.find("li", {"class": "publisher"}).find("a").string
					developerSoup = gameStatsSoup.find("li", {"class": "developer"})
					if developerSoup is not None:
						out["developer"] = developerSoup.find("a").string
					else:
						out["developer"] = out["publisher"]
					# ratingDetails = gameStatsSoup.find("li", {"class": "maturity"})
					# if ratingDetails.find("span", {"class": "data"}).string is not None:
					# 	out["rating"] = ratingDetails.find("span", {"class": "data"}).string
					# else:
					# 	out["rating"] = "TBC"

					urllib2.urlopen("http://localhost:8081/saveGame",urllib.urlencode(out))
