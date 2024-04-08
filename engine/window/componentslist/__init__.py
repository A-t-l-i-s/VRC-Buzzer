from engine.require import *
from engine.plugins import *

from .item import *





__all__ = ("Window_ComponentsList",)





class Window_ComponentsList(QFrame, RFT_Object):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~~~~~ Variables ~~~~~~~~~~
		self.parent = parent

		self.selected = None
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Options ~~~~~~~~~~~
		self.setEnabled(True)
		self.setFixedWidth(210)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~ Stylesheet ~~~~~~~~~~
		self.setStyleSheet(Styles.components_list.main)
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

			if (w):
				w.deleteLater()



	def reload(self):
		self.clear()

		sel = self.parent.parametersList.selected
		selC = self.selected


		if (sel):
			if (sel.param.plugin not in (Plugins.disabled, Plugins.seperator, None)):
				com = sel.param.components

				if (len(com) == 0):
					uid = Plugins.newUID()

					com[uid] = RFT_Structure({
						"component": None,
						"value": None,
						"swap": False
					})


				for k, v in com.items():
					# Create new item
					w = Window_ComponentsItem(self, k, v)


					# If id has already been selected
					if (selC != None and k == selC.uid):
						self.selected = w

						# Set to selected stylesheet
						w.setStyleSheet(Styles.components_item.main_selected)

						# Enable the buttons
						param = self.parent.parametersControl.parametersWidget
						param.upButton.setEnabled(True)
						param.downButton.setEnabled(True)
						param.deleteButton.setEnabled(True)


					# Add item to layout
					self.layout.addWidget(w)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

