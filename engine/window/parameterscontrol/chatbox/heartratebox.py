from engine.require import *
from engine.spotify import *





__all__ = ("Window_ParametersControl_ChatBox_HeartRateBox",)





class Window_ParametersControl_ChatBox_HeartRateBox(QCheckBox, RFT_Object):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~~~~~ Variables ~~~~~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Options ~~~~~~~~~~~
		self.setText("Heart Rate")
		self.setFixedWidth(85)
		self.setChecked(Tables.chatbox.heartrate)
		self.setCursor(Qt.CursorShape.PointingHandCursor)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~ Stylesheet ~~~~~~~~~~
		self.setStyleSheet(Styles.window.checkbox)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Signals ~~~~~~~~~~~
		self.toggled.connect(self._toggled)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def _toggled(self, checked):
		Tables.chatbox.heartrate = checked







