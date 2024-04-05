from engine.require import *





__all__ = ("GiggleTech",)





class GiggleTech(RFT_Object):
	# ~~~~~~~~~~~~ Client ~~~~~~~~~~~~
	client = OSC_Client(
		Tables.giggletech.ip,
		Data.giggletech.port
	)

	# ~~~~~~~~ Methods ~~~~~~~
	@classmethod
	def level(cls, level:float):
		if (isinstance(level, (int, float))):
			l = max(
				min(level, 1.0),
				0.0
			)

		else:
			l = 0.0


		cls.client.send_message(
			Data.giggletech.parameter_motor,
			round(l, 2)
		)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~~~~~~ Run ~~~~~~~~~~~~~
	@classmethod
	def run(cls):
		while True:
			# Get config
			c = Data.plugins.giggletech

			# Send command if enabled
			if (c.enabled):
				cls.level(c.level)

			# Wait
			time.sleep(0.01)


	@classmethod
	def runThread(cls):
		threading._start_new_thread(
			cls.run,
			(),
			{}
		)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



