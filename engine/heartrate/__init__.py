from engine.require import *





__all__ = ("HeartRate",)





class HeartRate(RFT_Object):
	client = None
	clientChar = None

	value = None

	sinceUpdate = time.time()



	@classmethod
	async def run(cls):
		while not Data.qt.app.exiting:
			if (Tables.heartrate.address != None):
				try:
					cls.client = BleakClient(
						Tables.heartrate.address
					)
				except:
					...

				else:
					while True:
						await asyncio.sleep(0.1)


						# If heartrate monitor address changes
						if (Tables.heartrate.address != cls.client.address):
							break


						if (Tables.chatbox.spotify):
							await cls.connect()

							# If not update in 10 secs auto disconnect
							if (time.time() - cls.sinceUpdate > 10):
								await cls.disconnect()


					await cls.disconnect()
			
				cls.client = None

			await asyncio.sleep(0.1)



	@classmethod
	async def connect(cls):
		if (cls.client != None):
			while (not cls.client.is_connected):
				cls.value = None

				await cls.disconnect()


				# If heartrate monitor address changes
				if (Tables.heartrate.address != cls.client.address):
					break


				try:
					# Connect to device
					await cls.client.connect()
					await cls.client.pair()


					# Get client characteristic
					cls.clientChar = None

					# Get services
					for s in cls.client.services:
						if (s.description == "Heart Rate"):

							# Get chars for heart rate service
							for c in s.characteristics:
								if (c.description == "Heart Rate Measurement"):
									cls.clientChar = c
									break


					if (cls.clientChar != None):
						# Start notify service
						await cls.client.start_notify(
							cls.clientChar,
							cls.heartNotify
						)

					else:
						await cls.disconnect()


					# Set last update to current
					cls.sinceUpdate = time.time()
				except:
					...

				await asyncio.sleep(0.1)



	@classmethod
	async def disconnect(cls):
		try:
			await cls.client.unpair()
		except:
			...

		await cls.client.disconnect()




	@classmethod
	async def heartNotify(cls, uuid, data):
		cls.sinceUpdate = time.time()

		if (len(data) == 2):
			cls.value = (data[0] << 8) | data[1]




