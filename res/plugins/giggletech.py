from engine.require import *
from engine.plugins.base import *





__all__ = ("Plugin",)





class Plugin(Plugins_Base):
	def init(cls):
		cls.config = Data.plugins.giggletech

		Data.console.allocate("giggletech")



	def enabled(cls, path, value):
		cls.config.enabled = bool(value)
		
		# Update console values
		cls.updateConsole()



	def level(cls, path, value):
		if (isinstance(value, (int, float, bool))):
			cls.config.level = float(value)

		# Update console values
		cls.updateConsole()



	@classmethod
	def updateConsole(cls):
		Data.console.giggletech.enabled = f"GiggleTech Enabled: {cls.config.enabled}"
		Data.console.giggletech.level = f"GiggleTech Level: {cls.config.level * 100:.2f}%"




	entries = {
		"giggletech enabled": {
			"callback": enabled
		},

		"giggletech level": {
			"callback": level
		}
	}





