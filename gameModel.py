from google.appengine.ext import db

class Game(db.Model):
	Title = db.StringProperty()
	Year = db.IntegerProperty()
	Genre = db.StringProperty()
	Platform = db.StringProperty(choices=set(["xbox360","playstation3","pc"]))
	GamespotScore = db.FloatProperty()
	Url = db.LinkProperty()
	Developer = db.StringProperty()
	Publisher = db.StringProperty()
	ImageUrl = db.LinkProperty()
	PEGIRating = db.StringProperty()
	#localMultiplayer = db.BooleanProperty
	#onlineMultiplayer = db.BooleanProperty
	#Amend platform types
	#Add in any other features required?