from engine.require import *
from engine.plugins import *





__all__ = ("Window_ParametersItem_ParameterValue",)





class Window_ParametersItem_ParameterValue(QLineEdit, RFT_Object):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~~~~~ Variables ~~~~~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Options ~~~~~~~~~~~
		self.setText("")
		self.setPlaceholderText("None")
		self.setFixedWidth(120)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~ Stylesheet ~~~~~~~~~~
		self.setStyleSheet(Styles.parameters_item.parameter_value)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Signals ~~~~~~~~~~~
		self.editingFinished.connect(self._editingFinished)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def _editingFinished(self):
		t = self.text()
		t = t.strip()


		if (t):
			# Find type of value
			v = Plugins.findType(t)

			# Reset text
			self.setText("")

			if (isinstance(v, (int, float, bool))):
				# Call osc callback
				self.parent.callback(
					self.parent.param.path,
					v
				)


