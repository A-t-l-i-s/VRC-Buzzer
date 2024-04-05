from engine.require import *





__all__ = ("Plugin",)





class Plugin:
	def enabled(path, value):
		Data.plugins.intiface.enabled = bool(value)



	def scan(path, value):
		Data.intiface.scanning = bool(value)



	def level(path, value):
		if (isinstance(value, (int, float, bool))):
			Data.plugins.intiface.level = float(value)





	entries = {
		"enabled": {
			"callback": enabled
		},

		"scan": {
			"callback": scan
		},

		"level": {
			"callback": level
		}
	}





