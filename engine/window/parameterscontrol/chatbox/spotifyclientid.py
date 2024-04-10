from engine.require import *
from engine.spotify import *





__all__ = ("Window_ParametersControl_ChatBox_SpotifyClient",)





class Window_ParametersControl_ChatBox_SpotifyClient(QLineEdit, RFT_Object):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~~~~~ Variables ~~~~~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Options ~~~~~~~~~~~
		self.setText(Tables.spotify.clientId)
		self.setPlaceholderText("Client ID")
		self.setFixedSize(150, 25)
		# self.setEchoMode(QLineEdit.EchoMode.Password)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~ Stylesheet ~~~~~~~~~~
		self.setStyleSheet(Styles.window.field)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Signals ~~~~~~~~~~~
		self.editingFinished.connect(self._editingFinished)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def _editingFinished(self):
		t = self.text()
		t = t.strip()

		if (not t):
			t = None

		# Set ip in tables
		Tables.spotify.clientId = t

		self.setText(t)

		if (Tables.chatbox.spotify):
			# Intialize spotify
			Spotify.init()


		



