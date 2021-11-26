class Plugin(object):
	"""
	The most simple interface to be inherited when creating a plugin.
	"""

	def __init__(self):
		self.is_activated = False

	def activate(self):
		"""
		Called at plugin activation.
		"""
		self.is_activated = True
		print("The " + self.__class__.__name__ + " has been activated")

	def deactivate(self):
		"""
		Called when the plugin is disabled.
		"""
		self.is_activated = False
		print("The " + self.__class__.__name__ + " has been deactivated")

	def run(self):
		"""
		This function executes the plugin if it is activated
		"""