from base_model import BaseAdvertising

class Advertiser(BaseAdvertising):
	"""docstring for Advertiser"""

	__name__ = ""
	__totalclicks__ = 0

	def __init__(self, _id, name, clicks = 0, views = 0):
		super(Advertiser, self).__init__()
		self.__id__ = _id
		self.__name__ = name
		self.__clicks__ = clicks
		self.__views__ = views
		Advertiser.__totalclicks__ += clicks


	def getName(self):
		return self.__name__

	def setName(self, name):
		self.__name__ = name

	@staticmethod
	def help():
		return "Help: id is the Advertiser id, name is the Advertiser name, clicks and views are the number of clicks and views of this Advertisers ads. The field total clicks is the sum of all Advertisers clicks."

	@staticmethod
	def getTotalClicks():
		return Advertiser.__totalclicks__

	def incClicks(self):
		self.__clicks__ += 1
		Advertiser.__totalclicks__ += 1

	def describeMe(self):
		return "Advertiser: Class containing advertiser info and functions needed for each advertiser"