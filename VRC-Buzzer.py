from engine.require import *
from engine.window import *
from engine.shocker import *
from engine.intiface import *
from engine.osc_server import *





async def intiface():
	# ~~~~~~~~~~~ Intiface ~~~~~~~~~~~
	await Intiface.start()
	await Intiface.connect()

	await asyncio.sleep(0.1)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~~~~~ Loop ~~~~~~~~~~~~~
	scan = False

	while not Data.qt.app.exiting:
		if (Data.intiface.scanning):
			if (not scan):
				await Intiface.startScan()
				scan = True

		else:
			if (scan):
				await Intiface.stopScan()
				scan = False



		config = Data.plugins.intiface
		level = config.level

		for k, v in Intiface.client.devices.items():
			for a in v.actuators:
				if (config.enabled):
					# Validate and multiply level
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
	await Intiface.stop()
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~





if (__name__ == "__main__"):
	# ~~~~ Kill Existing Instances ~~~
	e = Path(Data.intiface.executable)
	
	for p in psutil.process_iter():
		if (p.name() == e.name):
			p.kill()
			p.wait()
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~~~ Intiface ~~~~~~~~~~~
	intifaceThread = threading.Thread(
		target = asyncio.run,
		args = (intiface(),),
		kwargs = {},
		daemon = False
	)
	intifaceThread.start()
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~~ OSC Server ~~~~~~~~~~
	OSCServer.runThread()
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~~~~ Shocker ~~~~~~~~~~~
	Shocker.runThread()
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~~~~ Window ~~~~~~~~~~~~
	# Create window
	Data.qt.app.window = Window()
	Data.qt.app.window.show()

	# Run app
	Data.qt.app.app.exec()
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~~~ Finishing ~~~~~~~~~~
	# Wait for intiface to finish
	intifaceThread.join()

	# Save tables
	Tables_Obj.saveAll()
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


