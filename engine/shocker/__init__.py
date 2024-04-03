from engine.require import *





__all__ = ("Shocker",)





class Shocker(RFT_Object):
	queue = []


	# ~~~~~~~~~~~~~~ Run ~~~~~~~~~~~~~
	@classmethod
	def run(cls):
		while True:
			while cls.queue:
				v = cls.queue.pop(0)
				cls.send(*v)

			time.sleep(0.01)


	@classmethod
	def runThread(cls):
		threading._start_new_thread(
			cls.run,
			(),
			{}
		)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~~~~~ Send ~~~~~~~~~~~~~
	@classmethod
	def send(cls, op, intensity, duration):
		req = requests.post(
			"https://do.pishock.com/api/apioperate",
			json = {
				"Username": Tables.shocker.username,
				"Name": Data.qt.window.title,
				"ApiKey": Tables.shocker.token,
				"Code": Tables.shocker.code,

				"Op": op,
				"Intensity": intensity,
				"Duration": duration
			},
			headers = {
				"Content-Type": "application/json"
			}
		)

		return req.status_code == 200
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~~~ Commands ~~~~~~~~~~~
	@classmethod
	def shock(cls, intensity, duration):
		return cls.send(
			0,
			intensity,
			duration
		)

	@classmethod
	def vibrate(cls, intensity, duration):
		return cls.send(
			1,
			intensity,
			duration
		)

	@classmethod
	def beep(cls, intensity, duration):
		return cls.send(
			2,
			intensity,
			duration
		)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~ Commands Queue ~~~~~~~~
	@classmethod
	def addShock(cls, intensity, duration):
		cls.queue.append((
			0,
			intensity,
			duration
		))

	@classmethod
	def addVibrate(cls, intensity, duration):
		cls.queue.append((
			1,
			intensity,
			duration
		))

	@classmethod
	def addBeep(cls, intensity, duration):
		cls.queue.append((
			2,
			intensity,
			duration
		))
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


