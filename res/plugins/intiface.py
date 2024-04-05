from engine.require import *
from engine.plugins.base import *





__all__ = ("Plugin",)





class Plugin(Plugins_Base):
	def init(cls):
		cls.config = Data.plugins.intiface

		Data.console.allocate("intiface")



	def enabled(cls, path, value):
		cls.config.enabled = bool(value)
		
		# Update console values
		cls.updateConsole()



	def scanning(cls, path, value):
		cls.config.scanning = bool(value)
		
		# Update console values
		cls.updateConsole()



	def level(cls, path, value):
		if (isinstance(value, (int, float, bool))):
			cls.config.level = float(value)

		# Update console values
		cls.updateConsole()



	@classmethod
	def updateConsole(cls):
		Data.console.intiface.enabled = f"Intiface Enabled: {cls.config.enabled}"
		Data.console.intiface.scanning = f"Intiface Scanning: {cls.config.scanning}"
		Data.console.intiface.level = f"Intiface Level: {cls.config.level * 100:.2f}%"




	entries = {
		"intiface enabled": {
			"callback": enabled
		},

		"intiface scanning": {
			"callback": scanning
		},

		"intiface level": {
			"callback": level
		}
	}





