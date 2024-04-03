from engine.require import *





__all__ = ("OSCServer",)





class OSCServer(RFT_Object):
	# ~~~~~~~~~~ Dispatcher ~~~~~~~~~~
	dispatcher = OSC_Dispatcher()

	# ~~~~~~~~ Methods ~~~~~~~
	@classmethod
	def register(cls, path:str, function):
		return cls.dispatcher.map(
			path,
			function
		)


	@classmethod
	def unregister(cls, path:str, handler):
		cls.dispatcher.unmap(
			path,
			handler
		)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~~~~ Client ~~~~~~~~~~~~
	client = OSC_Client(
		Data.osc.client.ip,
		Data.osc.client.port
	)

	# ~~~~~~~~ Methods ~~~~~~~
	@classmethod
	def send(cls, path:str, value):
		cls.client.send_message(
			path,
			value
		)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~~~~ Server ~~~~~~~~~~~~
	server = OSC_BlockingServer(
		(
			Data.osc.server.ip,
			Data.osc.server.port
		),
		dispatcher
	)


	# ~~~~~~~~ Methods ~~~~~~~
	@classmethod
	def run(cls):
		cls.server.serve_forever()


	@classmethod
	def runThread(cls):
		threading._start_new_thread(
			cls.run,
			(),
			{}
		)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


