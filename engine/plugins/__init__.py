from engine.require import *





__all__ = ("Plugins",)





class Plugins(RFT_Object):
	# ~~~~~~~~ Default Plugins ~~~~~~~
	disabled = "disabled"


	plugins = RFT_Structure({
		disabled: None
	})
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~ Load Plugins ~~~~~~~~~
	for k, v in Plugins_Ext.items():
		if (hasattr(v, "Plugin")):
			# Get plugin class
			p = v.Plugin


			if (hasattr(p, "init")):
				# Get init function
				i = p.init

				if (callable(i)):
					# Call init function
					try:
						i()
					except:
						...


			if (hasattr(p, "entries")):
				# Get plugin entries
				e = p.entries

				if (isinstance(e, (dict, RFT_Structure))):
					# Iterate through entries
					for k_, v_ in e.items():
						plugins[k + " " + k_] = RFT_Structure(v_)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	@classmethod
	def findType(cls, text):
		v = None


		if (text):
			# Try convert to float/int
			try:
				v = float(text)

			except:
				if (text in ("true", "True", "on", "On")):
					v = True

				elif (text in ("false", "False", "off", "Off")):
					v = False

				elif (text in ("none", "None", "null", "nan", "-")):
					v = None


		return v



	@classmethod
	def newUID(cls):
		# Create new id
		uid_ = uuid.uuid4()
		hexId = uid_.hex.lower()

		return hexId


