from engine.require import *
from engine.spotify import *





__all__ = ("Window_ParametersControl_ChatBox_MuteBox",)





class Window_ParametersControl_ChatBox_MuteBox(QCheckBox, RFT_Object):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~~~~~ Variables ~~~~~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Options ~~~~~~~~~~~
		self.setText("Mute")
		self.setFixedWidth(55)
		self.setChecked(Tables.chatbox.mute)
		self.setCursor(Qt.CursorShape.PointingHandCursor)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~ Stylesheet ~~~~~~~~~~
		self.setStyleSheet(Styles.window.checkbox)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Signals ~~~~~~~~~~~
		self.toggled.connect(self._toggled)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def _toggled(self, checked):
		Tables.chatbox.mute = checked







