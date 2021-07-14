from base_model import BaseAdvertising
from advertiser import Advertiser

class Ad(BaseAdvertising):
	"""docstring for Ad"""

	__title__ = ""
	__imgURL__ = ""
	__link__ = ""
	__theAdveriser__ = None

	def __init__(self, _id, title, imgURL, link, theAdvertiser, clicks = 0, views = 0):
		super(Ad, self).__init__()
		self.__id__ = _id
		self.__title__ = title
		self.__clicks__ = clicks
		self.__views__ = views
		self.__imgURL__ = imgURL
		self.__link__ = link
		self.__theAdveriser__ = theAdvertiser

	def getTitle(self):
		return self.__title__

	def setTitle(self, title):
		self.__title__ = title

	def incClicks(self):
		self.__clicks__ += 1
		self.__theAdveriser__.incClicks()

	def describeMe(self):
		return "Ad: Class containing ad info and functions needed for each ad"
	
