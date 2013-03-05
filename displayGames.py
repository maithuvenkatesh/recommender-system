import webapp2
import os

from google.appengine.ext.webapp import template
from google.appengine.ext import db

from gameModel import Game

class DisplayGamesHandler(webapp2.RequestHandler):
    def get(self):
    	platform = self.request.get("platform")

    	#Get games for this platform from database
    	query = db.GqlQuery("SELECT * FROM Game WHERE Platform = '" + platform + "'")

    	gamesList = []

    	for game in query.run():
    		gamesList.append(game)


    	path = os.path.join(os.path.dirname(__file__), 'games.html')
    	self.response.out.write(template.render(path, {'games' : gamesList}))

app = webapp2.WSGIApplication([('/games', DisplayGamesHandler)], debug=True)
