from engine.require import *
from engine.spotify import *





__all__ = ("Window_ParametersControl_ChatBox_EnableChatBox",)





class Window_ParametersControl_ChatBox_EnableChatBox(QCheckBox, RFT_Object):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~~~~~ Variables ~~~~~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Options ~~~~~~~~~~~
		self.setText("Enable")
		self.setFixedWidth(60)
		self.setChecked(Tables.chatbox.enabled)
		self.setCursor(Qt.CursorShape.PointingHandCursor)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~ Stylesheet ~~~~~~~~~~
		self.setStyleSheet(Styles.window.checkbox)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Signals ~~~~~~~~~~~
		self.toggled.connect(self._toggled)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def _toggled(self, checked):
		Tables.chatbox.enabled = checked







