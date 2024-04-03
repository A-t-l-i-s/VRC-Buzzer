from engine.require import *





__all__ = ("Window_ParametersItem_ParameterPath",)





class Window_ParametersItem_ParameterPath(QLineEdit, RFT_Object):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~~~~~ Variables ~~~~~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Options ~~~~~~~~~~~
		self.setText(self.parent.param.path)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~ Stylesheet ~~~~~~~~~~
		self.setStyleSheet(Styles.parameters_item.parameter_path)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Signals ~~~~~~~~~~~
		self.textChanged.connect(self._textChanged)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def _textChanged(self, event):
		self.parent.param.path = self.text()


