from base_model import BaseAdvertising

class Advertiser(BaseAdvertising):
	"""docstring for Advertiser"""

	_name = ""
	_totalclicks = 0

	def __init__(self, _id, name, clicks = 0, views = 0):
		super(Advertiser, self).__init__()
		self._id = _id
		self._name = name
		self._clicks = clicks
		self._views = views
		Advertiser._totalclicks += clicks


	def getName(self):
		return self._name

	def setName(self, name):
		self._name = name

	@staticmethod
	def help():
		return "Help: id is the Advertiser id, name is the Advertiser name, clicks and views are the number of clicks and views of this Advertisers ads. The field total clicks is the sum of all Advertisers clicks."

	@staticmethod
	def getTotalClicks():
		return Advertiser._totalclicks

	def incClicks(self):
		self._clicks += 1
		Advertiser._totalclicks += 1

	def describeMe(self):
		return "Advertiser: Class containing advertiser info and functions needed for each advertiser"