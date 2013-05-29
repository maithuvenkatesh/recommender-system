import webapp2
import os
import logging

from google.appengine.ext.webapp import template
from google.appengine.ext import db

from gameModel import Game

class SaveGameHandler(webapp2.RequestHandler):
    def post(self):
		logging.info("Title of the game is %s", self.request.get('title'))
		newGame = Game()
		try:
			newGame.Title = self.request.get('title')
			newGame.Year = int(self.request.get('year'))
			newGame.Genre = self.request.get('genre')
			newGame.Platform = self.request.get('platform')
			newGame.GamespotScore = float(self.request.get('gamespotScore'))
			newGame.Url = self.request.get('url')
			newGame.ImageUrl = self.request.get('imgUrl')
			newGame.Rating = self.request.get('rating')
			newGame.Publisher = self.request.get('publisher')
			newGame.Developer = self.request.get('developer')
			newGame.put()			
		except ValueError:
			print 'Could not convert year to int'

app = webapp2.WSGIApplication([('/saveGame', SaveGameHandler)], debug=True)

