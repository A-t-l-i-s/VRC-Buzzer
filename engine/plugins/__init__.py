from engine.require import *

from .base import *





__all__ = ("Plugins",)





class Plugins(RFT_Object):
	# ~~~~~~~~ Default Plugins ~~~~~~~
	disabled = "disabled"


	plugins = RFT_Structure({
		disabled: None
	})

	groups = []
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~ Load Plugins ~~~~~~~~~
	@classmethod
	def loadPlugins(cls):
		for k, v in Plugins_Ext.items():
			if (hasattr(v, "Plugin")):
				# Get plugin class
				p = v.Plugin


				if (issubclass(p, Plugins_Base)):
					try:
						cls.groups.append(len(cls.plugins))

						p.init(p)
					
						# Iterate through entries
						for k_, v_ in p.entries.items():
							s = RFT_Structure(v_)
							s.inst = p

							cls.plugins[k_] = s
					
					except:
						print(traceback.format_exc())
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


