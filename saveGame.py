import webapp2
import os
import logging

from google.appengine.ext.webapp import template
from google.appengine.ext import db

class Game(db.Model):
	title = db.StringProperty
	year = db.IntegerProperty
	genre = db.StringProperty
	platform = db.StringProperty(choices=set(["xbox360","playstation3","pc"]))
	gamespotScore = db.FloatProperty
	url = db.LinkProperty
	#userRating = db.FloatProperty
	#localMultiplayer = db.BooleanProperty
	#onlineMultiplayer = db.BooleanProperty
	#developer = db.StringProperty
	#publisher = db.StringProperty
	#Amend platform types
	#Add in any other features required?

class SaveGameHandler(webapp2.RequestHandler):
    def post(self):
		logging.info("Title of the game is %s", self.request.get('title'))
		newGame = Game()
		newGame.title = self.request.get('title')
		newGame.year = int(self.request.get('year'))
		newGame.genre = self.request.get('genre')
		newGame.platform = self.request.get('platform')
		newGame.gamespotScore = float(self.request.get('gamespotScore'))
		newGame.url = self.request.get('url')

		newGame.put()


app = webapp2.WSGIApplication([('/saveGame', SaveGameHandler)], debug=True)

