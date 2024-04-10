from engine.require import *





__all__ = ("Window_ParametersControl_ChatBox_HeartRateAddress",)





class Window_ParametersControl_ChatBox_HeartRateAddress(QLineEdit, RFT_Object):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~~~~~ Variables ~~~~~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Options ~~~~~~~~~~~
		self.setText(Tables.heartrate.address)
		self.setPlaceholderText("Address")
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
		Tables.heartrate.address = t

		self.setText(t)

		



