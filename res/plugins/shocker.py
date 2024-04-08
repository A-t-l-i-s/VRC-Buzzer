from engine.require import *
from engine.shocker import *
from engine.plugins.base import *





__all__ = ("Plugin",)





class Plugin(Plugins_Base):
	def init(cls):
		cls.config = Data.plugins.shocker



	def enabled(cls, path, value):
		cls.config.enabled = bool(value)



	def level(cls, path, value):
		if (isinstance(value, (int, float, bool))):
			value = float(value)
			cls.config.sinceReset = time.time()

			if (value):
				cls.config.level = value
				cls.config.levelDefault = value

			else:
				cls.config.level = 0
				cls.config.levelDefault = 0



	def duration(cls, path, value):
		if (isinstance(value, (int, float, bool))):
			value = float(value)
			cls.config.sinceReset = time.time()

			if (value):
				cls.config.duration = value * 15
				cls.config.durationDefault = cls.config.duration

			else:
				cls.config.duration = 0
				cls.config.durationDefault = 0



	def punish(cls, path, value):
		if (cls.config.enabled):
			if (value):
				t = time.time()

				if ((cls.config.duration / 5) <= (t - cls.config.sinceBoop)):
					# Shock as punishment
					Shocker.addShock(
						round(cls.config.level * 100),
						round(cls.config.duration * 1000)
					)

					# Step up level and duration as punishment
					cls.config.level = min(
						cls.config.level + cls.config.levelStep,
						1
					)

					cls.config.duration = min(
						cls.config.duration + cls.config.durationStep,
						15
					)

					# Time since last boop
					cls.config.sinceBoop = t
					cls.config.sinceReset = t



	def reward(cls, path, value):
		if (cls.config.enabled):
			if (value):
				t = time.time()

				if (.2 <= (t - cls.config.sinceHeadpat)):
					# Vibrate as reward
					Shocker.addVibrate(
						10,
						400
					)

					# Set default shock level/duration
					cls.config.level = cls.config.levelDefault
					cls.config.duration = cls.config.durationDefault
					
					# Time since last headpat
					cls.config.sinceHeadpat = t
					cls.config.sinceReset = t




	entries = {
		"shocker enabled": {
			"callback": enabled
		},

		"shocker level": {
			"callback": level
		},

		"shocker duration": {
			"callback": duration
		},


		"shocker punish": {
			"callback": punish
		},

		"shocker reward": {
			"callback": reward
		}
	}







