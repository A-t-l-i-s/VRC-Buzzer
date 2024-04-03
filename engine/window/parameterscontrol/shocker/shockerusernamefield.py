from engine.require import *





__all__ = ("Window_ParametersControl_ShockerUsernameField",)





class Window_ParametersControl_ShockerUsernameField(QLineEdit, RFT_Object):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~~~~~ Variables ~~~~~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Options ~~~~~~~~~~~
		self.setText(Tables.shocker.username)
		self.setPlaceholderText("Username")
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

		# Set username
		Tables.shocker.username = t

		



