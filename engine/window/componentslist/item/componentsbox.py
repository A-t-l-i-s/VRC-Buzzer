from engine.require import *
from engine.components import *





__all__ = ("Window_ComponentsItem_ComponentsBox",)





class Window_ComponentsItem_ComponentsBox(QComboBox, RFT_Object):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~~~~~ Variables ~~~~~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Options ~~~~~~~~~~~
		self.setFixedSize(90, 25)
		self.setCursor(Qt.CursorShape.PointingHandCursor)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~ Stylesheet ~~~~~~~~~~
		self.setStyleSheet(Styles.components_item.components_box)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Signals ~~~~~~~~~~~
		self.textActivated.connect(self._textActivated)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~~~~ Events ~~~~~~~~~~~~
	def _textActivated(self, text):
		# If disabled plugin selected
		if (text == Components.disabled):
			text = None


		# Set invisible if single component
		single = (text in Components.componentsSingle)
		
		self.parent.componentsValue.setVisible(not single)
		self.parent.swapBox.setVisible(not single)


		self.parent.param.component = text



	def wheelEvent(self, event):
		event.ignore()
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def reload(self):
		# Add plugin ids to combobox
		for k, v in Components.components.items():
			self.addItem(k)



		# Get current plugin
		com = self.parent.param.component
		if (Components.components.contains(com)):
			# Set current component
			self.setCurrentText(com)


		else:
			self.setCurrentText(Components.disabled)


		# Set value visible
		single = (com in Components.componentsSingle)
		
		self.parent.componentsValue.setVisible(not single)
		self.parent.swapBox.setVisible(not single)




