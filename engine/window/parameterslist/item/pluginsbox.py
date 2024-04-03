from engine.require import *
from engine.plugins import *





__all__ = ("Window_ParametersItem_PluginsBox",)





class Window_ParametersItem_PluginsBox(QComboBox, RFT_Object):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~~~~~ Variables ~~~~~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Options ~~~~~~~~~~~
		self.setFixedSize(180, 25)
		self.setCursor(Qt.CursorShape.PointingHandCursor)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~ Stylesheet ~~~~~~~~~~
		self.setStyleSheet(Styles.parameters_item.plugins_box)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Signals ~~~~~~~~~~~
		self.textActivated.connect(self._textActivated)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~~~~ Events ~~~~~~~~~~~~
	def _textActivated(self, text):
		# If disabled plugin selected
		if (text == Plugins.disabled):
			text = None

		self.parent.param.plugin = text



	def wheelEvent(self, event):
		event.ignore()
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def reload(self):
		prev = None

		# Add plugin ids to combobox
		for k, v in Plugins.plugins.items():
			self.addItem(k)


			p = k.split(" ")[0]

			if (p != prev and prev != None):
				self.insertSeparator(self.count() - 1)

			prev = p



		# Get current plugin
		pl = self.parent.param.plugin
		if (Plugins.plugins.contains(pl)):
			# Set current plugin
			self.setCurrentText(pl)

		else:
			self.setCurrentText(Plugins.disabled)



