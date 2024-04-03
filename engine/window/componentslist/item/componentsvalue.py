from engine.require import *
from engine.plugins import *





__all__ = ("Window_ComponentsItem_ComponentsValue",)





class Window_ComponentsItem_ComponentsValue(QLineEdit, RFT_Object):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~~~~~ Variables ~~~~~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Options ~~~~~~~~~~~
		self.setText("")
		self.setPlaceholderText("None")
		self.setFixedWidth(140)

		self.setPlaceholder(self.parent.param.value)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~ Stylesheet ~~~~~~~~~~
		self.setStyleSheet(Styles.components_item.components_value)
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

			# Set value
			self.parent.param.value = v

			# Reset text
			self.setText("")

			# Set placeholder text
			self.setPlaceholder(v)





	def setPlaceholder(self, value):
		# If boolean
		if (isinstance(value, bool)):
			strValue = f"{value}"

		# If int/float
		elif (isinstance(value, (int, float))):
			strValue = f"{round(value, 2)}"

		# If anything else (NoneType)
		else:
			strValue = "None"


		# Set placeholder text
		self.setPlaceholderText(strValue)

