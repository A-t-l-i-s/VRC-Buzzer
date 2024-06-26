from engine.require import *
from engine.spotify import *





__all__ = ("Window_ParametersControl_ChatBox_SpotifyBox",)





class Window_ParametersControl_ChatBox_SpotifyBox(QCheckBox, RFT_Object):
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


		if (Tables.chatbox.spotify):
			Spotify.init()



	def _toggled(self, checked):
		Tables.chatbox.spotify = checked

		if (checked):
			# Intialize spotify client
			Spotify.init()







