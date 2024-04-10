from engine.require import *
from engine.plugins.base import *





__all__ = ("Plugin",)





class Plugin(Plugins_Base):
	def init(cls):
		cls.config = Tables.chatbox



	def enabled(cls, path, value):
		cls.config.enabled = bool(value)

	def spotify(cls, path, value):
		cls.config.spotify = bool(value)

	def timezone(cls, path, value):
		cls.config.timezone = bool(value)

	def heartrate(cls, path, value):
		cls.config.heartrate = bool(value)

	def mute(cls, path, value):
		cls.config.mute = bool(value)




	entries = {
		"chatbox enabled": {
			"callback": enabled
		},

		"chatbox spotify": {
			"callback": spotify
		},

		"chatbox timezone": {
			"callback": timezone
		},

		"chatbox heartrate": {
			"callback": heartrate
		},

		"chatbox mute": {
			"callback": mute
		}
	}





