from engine.require import *

from .componentslist import *
from .parameterslist import *
from .parameterscontrol import *





__all__ = ("Window",)





class Window(QMainWindow, RFT_Object):
	def __init__(self):
		super().__init__()


		# ~~~~~~~~~~~ Variables ~~~~~~~~~~
		self.selectedPlugin = None
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Options ~~~~~~~~~~~
		self.setWindowIcon(Icons.icon)
		self.setWindowTitle(Data.qt.window.title)

		self.setWindowFlags(
			self.windowFlags() & ~Qt.WindowType.WindowMinimizeButtonHint & ~Qt.WindowType.WindowMaximizeButtonHint
		)

		self.resize(
			Tables.window.width,
			Tables.window.height
		)

		self.setMinimumSize(
			Data.qt.window.width,
			Data.qt.window.height
		)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~ Stylesheet ~~~~~~~~~
		self.setStyleSheet(Styles.window.main)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~ Central Widget ~~~~~~~~
		self.widget = QWidget()

		self.setCentralWidget(self.widget)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Layout ~~~~~~~~~~~~
		self.layout = QHBoxLayout()
		self.layout.setSpacing(0)
		self.layout.setContentsMargins(0, 0, 0, 0)
		self.layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

		self.widget.setLayout(self.layout)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~~ Body ~~~~~~~~~~~~~
		self.bodyLayout = QHBoxLayout()
		self.bodyLayout.setSpacing(0)
		self.bodyLayout.setContentsMargins(0, 0, 0, 0)


		self.parametersControl = Window_ParametersControl(self)
		self.bodyLayout.addWidget(self.parametersControl)


		self.parametersList = Window_ParametersList(self)
		self.bodyLayout.addWidget(self.parametersList)


		self.componentsList = Window_ComponentsList(self)
		self.bodyLayout.addWidget(self.componentsList)


		self.layout.addLayout(self.bodyLayout)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~ Load Parameters ~~~~~~~
		self.parametersList.reload()
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~~~~ Events ~~~~~~~~~~~~
	def closeEvent(self, event):
		self.hide()

		event.ignore()

		self.exit()



	def resizeEvent(self, event):
		size = event.size()

		Tables.window.width = size.width()
		Tables.window.height = size.height()

		event.accept()



	def keyPressEvent(self, event):
		key = event.key()
		modifiers = event.modifiers()

		if (modifiers == Qt.KeyboardModifier.ControlModifier):
			if (key == Qt.Key.Key_S):
				# Save tables
				Tables_Obj.saveAll()

			elif (key == Qt.Key.Key_R):
				# Reload parameters
				Tables.pop("parameters")
				self.parametersList.reload()

			elif (key == Qt.Key.Key_E):
				# Enable all parameters
				self.parametersControl.enableAllButton._pressed()

			elif (key == Qt.Key.Key_D):
				# Disable all parameters
				self.parametersControl.disableAllButton._pressed()
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	# ~~~~~~~~~~~~ Methods ~~~~~~~~~~~
	def exit(self):
		# Exit app
		Data.qt.app.app.quit()

		Data.qt.app.exiting = True
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


