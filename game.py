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