from engine.require import *
from engine.window import *
from engine.plugins import *
from engine.shocker import *
from engine.intiface import *
from engine.components import *
from engine.giggletech import *
from engine.osc_server import *





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
		args = (Intiface.run(),),
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


	# ~~~~~~~~~~ GiggleTech ~~~~~~~~~~
	GiggleTech.runThread()
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~~~~ Plugins ~~~~~~~~~~~
	Plugins.loadPlugins()
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~~~~ Window ~~~~~~~~~~~~
	try:
		# Create window
		Data.qt.app.window = Window()
		Data.qt.app.window.show()

		# Run app
		Data.qt.app.app.exec()
	
	except:
		print(traceback.format_exc())


	Data.qt.app.exiting = True
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~~~ Finishing ~~~~~~~~~~
	# Wait for intiface to finish
	intifaceThread.join()

	# Save tables
	Tables_Obj.saveAll()
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


