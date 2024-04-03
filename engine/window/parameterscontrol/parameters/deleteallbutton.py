from engine.require import *
from engine.plugins import *
from engine.osc_server import *





__all__ = ("Window_ParametersControl_DeleteAllButton",)





class Window_ParametersControl_DeleteAllButton(QPushButton, RFT_Object):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~~~~~ Variables ~~~~~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Options ~~~~~~~~~~~
		self.setText("Delete All")
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


		if (clse):
			# Get components
			pls.param.components.clear()

			uid = Plugins.newUID()

			pls.param.components[uid] = RFT_Structure({
				"component": None,
				"value": None,
				"swap": False
			})

			# Unselect components
			cl.selected = None


		elif (pls):
			# Clear parameters list
			pl.clear()

			# Clear parameters
			Tables.parameters.clear()

			# Unselect plugin
			pl.selected = None



		# Reload lists
		pl.reload()
		cl.reload()

