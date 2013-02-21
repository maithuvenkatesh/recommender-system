import game
import webapp2
import os
import logging

from google.appengine.ext.webapp import template
from google.appengine.ext import db

class SaveGameHandler(webapp2.RequestHandler):
    def post(self):
		self.response.write(self.request.get('title'))
		newGame = game.Game()
		newGame.title = self.request.get('title')
		newGame.year = self.request.get('year')
		newGame.genre = self.request.get('genre')
		newGame.platform = self.request.get('platform')
		newGame.gamespotScore = self.request.get('gamespotScore')
		newGame.url = self.request.get('url')

		#TODO parse string -> float and string -> year
		newGame.put()


app = webapp2.WSGIApplication([('/saveGame', SaveGameHandler)], debug=True)

