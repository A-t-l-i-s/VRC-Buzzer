from engine.require import *
from engine.spotify import *





__all__ = ("Window_ParametersControl_SpotifyBox",)





class Window_ParametersControl_SpotifyBox(QCheckBox, RFT_Object):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~~~~~ Variables ~~~~~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Options ~~~~~~~~~~~
		self.setText("Spotify")
		self.setFixedWidth(65)
		self.setChecked(Tables.chatbox.spotify)
		self.setCursor(Qt.CursorShape.PointingHandCursor)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~ Stylesheet ~~~~~~~~~~
		self.setStyleSheet(Styles.window.checkbox)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Signals ~~~~~~~~~~~
		self.toggled.connect(self._toggled)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def _toggled(self, checked):
		Tables.chatbox.spotify = checked







