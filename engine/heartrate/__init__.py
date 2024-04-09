from engine.require import *





__all__ = ("HeartRate",)





class HeartRate(RFT_Object):
	client = None

	sinceUpdate = time.time()



	@classmethod
	async def run(cls):
		if (Data.heartrate.address != None):
			cls.client = BleakClient(
				Data.heartrate.address
			)

			while not Data.qt.app.exiting:
				await asyncio.sleep(0.1)

				if (Tables.chatbox.spotify):
					await cls.connect()

					# If not update in 10 secs auto disconnect
					if (time.time() - cls.sinceUpdate > 10):
						await cls.disconnect()


			await cls.disconnect()



	@classmethod
	async def connect(cls):
		if (cls.client != None):
			while (not cls.client.is_connected and not Data.qt.app.exiting):
				Data.heartrate.value = None

				await cls.disconnect()


				try:
					await cls.client.connect()

					await cls.client.start_notify(
						Data.heartrate.char,
						cls.heartNotify
					)

					cls.sinceUpdate = time.time()
				except:
					...

				await asyncio.sleep(0.1)



	@classmethod
	async def disconnect(cls):
		await cls.client.unpair()
		await cls.client.disconnect()



	@classmethod
	async def heartNotify(cls, uuid, data):
		cls.sinceUpdate = time.time()

		if (len(data) == 2):
			Data.heartrate.value = (data[0] << 8) | data[1]




