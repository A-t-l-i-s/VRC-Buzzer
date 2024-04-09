from engine.require import *
from engine.spotify import *





__all__ = ("Window_ParametersControl_TimezoneBox",)





class Window_ParametersControl_TimezoneBox(QCheckBox, RFT_Object):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~~~~~ Variables ~~~~~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Options ~~~~~~~~~~~
		self.setText("Timezone")
		self.setFixedWidth(80)
		self.setChecked(Tables.chatbox.timezone)
		self.setCursor(Qt.CursorShape.PointingHandCursor)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~ Stylesheet ~~~~~~~~~~
		self.setStyleSheet(Styles.window.checkbox)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Signals ~~~~~~~~~~~
		self.toggled.connect(self._toggled)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def _toggled(self, checked):
		Tables.chatbox.timezone = checked







