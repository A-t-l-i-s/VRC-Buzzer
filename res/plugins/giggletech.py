from engine.require import *
from engine.plugins.base import *





__all__ = ("Plugin",)





class Plugin(Plugins_Base):
	def init(cls):
		cls.config = Data.plugins.giggletech



	def enabled(cls, path, value):
		cls.config.enabled = bool(value)



	def level(cls, path, value):
		if (isinstance(value, (int, float, bool))):
			cls.config.level = float(value)




	entries = {
		"giggletech enabled": {
			"callback": enabled
		},

		"giggletech level": {
			"callback": level
		}
	}





