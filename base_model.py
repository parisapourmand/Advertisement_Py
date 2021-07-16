class BaseAdvertising:
	"""docstring for BaseAdvertising"""
	_id = 0
	_clicks = 0
	_views = 0


	def __init__(self):
		super(BaseAdvertising, self).__init__()

	def getId():
		return self._id
	def setId(self, _id_):
		self._id = _id_
	def getClicks(self):
		return self._clicks
	def getViews(self):
		return self._views
	def incClicks(self):
		self._clicks += 1
	def incViews(self):
		self._views += 1
	def describeMe(self):
		return "BaseAdvertising: Class for basic functions needed for advertising"