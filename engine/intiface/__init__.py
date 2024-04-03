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
	async def startScan(cls):
		if (cls.client):
			await cls.client.start_scanning()

	@classmethod
	async def stopScan(cls):
		if (cls.client):
			await cls.client.stop_scanning()
