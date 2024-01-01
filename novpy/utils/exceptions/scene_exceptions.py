


class NoPreviousScenes(Exception):
	"""
	Raised when an attempt is made to call a previous scene, when the list of previous scenes is empty
	"""

	def __init__(*args, **kwargs):
		Exception.__init__(*args, **kwargs)




class NoNextScenes(Exception):
	"""
	Raised when an attempt is made to call a previous scene, when the list of previous scenes is empty
	"""

	def __init__(*args, **kwargs):
		Exception.__init__(*args, **kwargs)





class IncorrectSceneIndex(Exception):
	"""
	Raised when an attempt is made to call a previous scene, when the list of previous scenes is empty
	"""

	def __init__(*args, **kwargs):
		Exception.__init__(*args, **kwargs)


