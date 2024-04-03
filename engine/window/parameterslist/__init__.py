from engine.require import *
from engine.plugins import *
from engine.osc_server import *

from .item import *





__all__ = ("Window_ParametersList", "Window_ParametersItem")





class Window_ParametersList(QFrame, RFT_Object):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~~~~~ Variables ~~~~~~~~~~
		self.parent = parent

		self.selected = None
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Options ~~~~~~~~~~~
		self.setEnabled(True)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~ Stylesheet ~~~~~~~~~~
		self.setStyleSheet(Styles.parameters_list.main)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~ Main Layout ~~~~~~~~~
		self.mainLayout = QVBoxLayout()
		self.mainLayout.setSpacing(0)
		self.mainLayout.setContentsMargins(0, 0, 0, 0)

		self.setLayout(self.mainLayout)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Layout ~~~~~~~~~~~~
		self.layout = QVBoxLayout()
		self.layout.setSpacing(5)
		self.layout.setContentsMargins(3, 3, 3, 3)
		self.layout.setAlignment(Qt.AlignmentFlag.AlignTop)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~ Scroll Area ~~~~~~~~~
		self.scroll = QScrollArea()
		self.scroll.setWidgetResizable(True)

		self.mainLayout.addWidget(self.scroll)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~ Scroll Widget ~~~~~~~~
		self.widget = QWidget()
		self.widget.setLayout(self.layout)
		self.scroll.setWidget(self.widget)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~~~~ Methods ~~~~~~~~~~~
	def clear(self):
		while (self.layout.count()):
			c = self.layout.takeAt(0)
			w = c.widget()

			# Unregister old handle if its bound
			if (w.handle != None):
				OSCServer.unregister(
					w.handlePath,
					w.handle
				)


			if (w):
				w.deleteLater()



	def reload(self):
		self.clear()

		# Disable delete button
		self.parent.parametersControl.parametersWidget.deleteButton.setEnabled(False)


		# If previous selected exists then get uid
		if (self.selected):
			uid = self.selected.uid

		else:
			uid = None


		for k, v in Tables.parameters.items():
			if (len(v.components) == 0):
				uid = Plugins.newUID()

				v.components[uid] = RFT_Structure({
					"component": None,
					"value": None,
					"swap": False
				})


			# Create new item
			w = Window_ParametersItem(self, k)
			w.update()


			# If id has already been selected
			if (k == uid):
				self.selected = w

				# Set to selected stylesheet
				w.setStyleSheet(Styles.parameters_item.main_selected)

				# Enable delete button
				self.parent.parametersControl.parametersWidget.deleteButton.setEnabled(True)


			# Add item to layout
			self.layout.addWidget(w)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

