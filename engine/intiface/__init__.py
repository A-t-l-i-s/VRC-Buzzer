from engine.require import *





__all__ = ("Intiface",)





class Intiface(RFT_Object):
	process = None

	client = None
	connector = None



	@classmethod
	async def start(cls):
		nul = open("nul", "ab")

		# Create process
		cls.process = subprocess.Popen(
			(
				"",
				"--server-name", Data.qt.window.title,
				"--websocket-port", str(Data.intiface.port),
				"--use-bluetooth-le"
			),
			executable = Path(Data.intiface.executable),
			stdout = nul,
			stderr = nul,
			stdin = nul,
			close_fds = True,
			encoding = "utf-8",
			creationflags = subprocess.HIGH_PRIORITY_CLASS | subprocess.CREATE_NO_WINDOW
		)



	@classmethod
	async def stop(cls):
		if (cls.client != None):
			# Disconnect client
			await cls.client.disconnect()


		if (cls.process != None):
			# Terminate and wait for process to finish
			cls.process.kill()
			cls.process.wait()



	@classmethod
	async def connect(cls):
		# Create intiface client
		cls.client = Intiface_Client(
			Data.qt.window.title,
			Intiface_ProtocolSpec.v3
		)

		# Create intiface client connector
		cls.connector = Intiface_WebsocketConnector(f"ws://127.0.0.1:{Data.intiface.port}")

		# Connect client to server
		await cls.client.connect(cls.connector)



	@classmethod
	async def run(cls):
		# ~~~~~~~~~~~ Intiface ~~~~~~~~~~~
		await cls.start()
		await cls.connect()

		await asyncio.sleep(0.1)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~~ Loop ~~~~~~~~~~~~~
		scan = False

		while not Data.qt.app.exiting:
			if (Data.plugins.intiface.scanning):
				if (not scan):
					await cls.client.start_scanning()
					await asyncio.sleep(0.1)
					scan = True

			else:
				if (scan):
					# Stop scanning
					await cls.client.stop_scanning()
					await asyncio.sleep(0.1)

					# Stop application
					await cls.stop()
					await asyncio.sleep(0.1)

					# Restart application
					await cls.start()
					await cls.connect()
					await asyncio.sleep(0.1)

					scan = False



			config = Data.plugins.intiface
			level = config.level

			for k, v in cls.client.devices.items():
				for a in v.actuators:
					if (config.enabled):
						# Validate level
						l = max(
							min(level, 1.0),
							0.0
						)

					else:
						# No level
						l = 0.0


					try:
						# Send command
						await a.command(l)
					except:
						...

			
			await asyncio.sleep(0.01)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Finishing ~~~~~~~~~~
		# Disconnect and stop intiface
		await cls.stop()
		await asyncio.sleep(0.1)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


