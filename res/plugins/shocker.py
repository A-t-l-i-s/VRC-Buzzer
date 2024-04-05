from engine.require import *
from engine.shocker import *





__all__ = ("Plugin",)





class Plugin:
	def enabled(path, value):
		Data.plugins.shocker.enabled = bool(value)



	def level(path, value):
		config = Data.plugins.shocker
		if (isinstance(value, (int, float, bool))):
			value = float(value)
			config.sinceReset = time.time()

			if (value):
				config.level = value
				config.levelDefault = value

			else:
				config.level = 0
				config.levelDefault = 0



	def duration(path, value):
		config = Data.plugins.shocker
		if (isinstance(value, (int, float, bool))):
			value = float(value)
			config.sinceReset = time.time()

			if (value):
				config.duration = value * 15
				config.durationDefault = config.duration

			else:
				config.duration = 0
				config.durationDefault = 0



	def punish(path, value):
		config = Data.plugins.shocker
		if (config.enabled):
			if (value):
				t = time.time()

				if ((config.duration / 5) <= (t - config.sinceBoop)):
					# Shock as punishment
					Shocker.addShock(
						round(config.level * 100),
						round(config.duration * 1000)
					)

					# Step up level and duration as punishment
					config.level = min(
						config.level + config.levelStep,
						1
					)

					config.duration = min(
						config.duration + config.durationStep,
						15
					)

					# Time since last boop
					config.sinceBoop = t
					config.sinceReset = t



	def reward(path, value):
		config = Data.plugins.shocker
		if (config.enabled):
			if (value):
				t = time.time()

				if (.2 <= (t - config.sinceHeadpat)):
					# Vibrate as reward
					Shocker.addVibrate(
						10,
						400
					)

					# Set default shock level/duration
					config.level = config.levelDefault
					config.duration = config.durationDefault
					
					# Time since last headpat
					config.sinceHeadpat = t
					config.sinceReset = t





	entries = {
		"enabled": {
			"callback": enabled
		},

		"level": {
			"callback": level
		},

		"duration": {
			"callback": duration
		},


		"punish": {
			"callback": punish
		},

		"reward": {
			"callback": reward
		}
	}







