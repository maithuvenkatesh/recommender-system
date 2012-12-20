from google.appengine.ext import db

class Game(db.Model):
	name = db.StringProperty(required=True)
	year = db.IntegerProperty
	genre = db.StringProperty
	userRating = db.FloatProperty
	localMultiplayer = db.BooleanProperty
	onlineMultiplayer = db.BooleanProperty
	developer = db.StringProperty
	publisher = db.StringProperty
	#Amend platform types
	platform = db.StringProperty(choices=set(["xbox360","playstation3","wii","pc","iOS","android"]))
	#Add in any other features required?