from engine.require import *
from engine.giggletech import *





__all__ = ("Window_ParametersControl_GiggleTech_IPField",)





class Window_ParametersControl_GiggleTech_IPField(QLineEdit, RFT_Object):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~~~~~ Variables ~~~~~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Options ~~~~~~~~~~~
		self.setText(Tables.giggletech.ip)
		self.setPlaceholderText("Device IP")
		self.setFixedSize(150, 25)
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
		Tables.giggletech.ip = t

		# Set ip in client
		GiggleTech.client._address = t

		self.setText(t)

		



