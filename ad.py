from base_model import BaseAdvertising
from advertiser import Advertiser

class Ad(BaseAdvertising):
	"""docstring for Ad"""

	_title = ""
	_imgURL = ""
	_link = ""
	_theAdveriser = None

	def __init__(self, _id, title, imgURL, link, theAdvertiser, clicks = 0, views = 0):
		super(Ad, self).__init__()
		self._id = _id
		self._title = title
		self._clicks = clicks
		self._views = views
		self._imgURL = imgURL
		self._link = link
		self._theAdveriser = theAdvertiser

	def getTitle(self):
		return self._title

	def setTitle(self, title):
		self._title = title

	def incClicks(self):
		self._clicks += 1
		self._theAdveriser.incClicks()

	def describeMe(self):
		return "Ad: Class containing ad info and functions needed for each ad"
	
