from engine.require import *
from engine.plugins import *





__all__ = ("Window_ParametersControl_NewButton",)





class Window_ParametersControl_NewButton(QPushButton, RFT_Object):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~~~~~ Variables ~~~~~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Options ~~~~~~~~~~~
		self.setText("New")
		self.setFixedSize(150, 25)
		self.setCursor(Qt.CursorShape.PointingHandCursor)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~ Stylesheet ~~~~~~~~~~
		self.setStyleSheet(Styles.window.button)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Signals ~~~~~~~~~~~
		self.pressed.connect(self._pressed)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def _pressed(self):
		# Get widgets
		pl = self.parent.parent.parent.parametersList
		pls = pl.selected

		cl = self.parent.parent.parent.componentsList
		clse = cl.selected


		# Create new uid
		uid = Plugins.newUID()


		if (clse):
			# Get components
			com = pls.param.components

			com[uid] = RFT_Structure({
				"component": None,
				"value": None,
				"swap": False
			})


		else:
			# Add new parameter
			Tables.parameters[uid] = RFT_Structure({
				"path": "/avatar/parameters/",
				"plugin": None,
				"enabled": False,
				"components": {}
			})


		# Reload parameters list
		pl.reload()
		cl.reload()



