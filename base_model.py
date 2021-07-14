class BaseAdvertising:
	"""docstring for BaseAdvertising"""
	__id__ = 0
	__clicks__ = 0
	__views__ = 0


	def __init__(self):
		super(BaseAdvertising, self).__init__()

	# def __init__(self, _id, clicks = 0, views = 0):
	# 	super(BaseAdvertising, self).__init__()
	# 	self.__id__ = _id
	# 	self.__clicks__ = clicks
	# 	self.__views__ = views

	def getClicks(self):
		return self.__clicks__
	def getViews(self):
		return self.__views__
	def incClicks(self):
		self.__clicks__ += 1
	def incViews(self):
		self.__views__ += 1
	def describeMe(self):
		return "BaseAdvertising: Class for basic functions needed for advertising"
	
