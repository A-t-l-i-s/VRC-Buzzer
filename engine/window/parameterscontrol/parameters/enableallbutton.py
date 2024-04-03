from engine.require import *





__all__ = ("Window_ParametersControl_EnableAllButton",)





class Window_ParametersControl_EnableAllButton(QPushButton, RFT_Object):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~~~~~ Variables ~~~~~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Options ~~~~~~~~~~~
		self.setText("Enable All")
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
		# Set all parameters to enabled
		for k, v in Tables.parameters.items():
			v.enabled = True

		# Reload all parameters
		self.parent.parent.parent.parametersList.reload()

