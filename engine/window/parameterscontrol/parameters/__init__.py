from engine.require import *
from engine.plugins import *

from .upbutton import *
from .newbutton import *
from .downbutton import *
from .deletebutton import *
from .deleteallbutton import *
from .enableallbutton import *
from .disableallbutton import *
from .importparametersbutton import *





__all__ = ("Window_ParametersControl_Parameter",)





class Window_ParametersControl_Parameter(QFrame, RFT_Object):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~~~~~ Variables ~~~~~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Options ~~~~~~~~~~~
		self.setEnabled(True)
		self.setVisible(True)

		self.setFixedWidth(150)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~ Stylesheet ~~~~~~~~~~
		self.setStyleSheet(Styles.parameters_control.frame)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Layout ~~~~~~~~~~~~
		self.layout = QVBoxLayout()
		self.layout.setSpacing(3)
		self.layout.setContentsMargins(0, 0, 0, 3)
		self.layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
		
		self.setLayout(self.layout)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



		# New parameter/component button
		self.newButton = Window_ParametersControl_NewButton(self)
		self.layout.addWidget(self.newButton)

		# Delete parameter/component button
		self.deleteButton = Window_ParametersControl_DeleteButton(self)
		self.layout.addWidget(self.deleteButton)

		# Delete all parameters/components
		self.deleteAllButton = Window_ParametersControl_DeleteAllButton(self)
		self.layout.addWidget(self.deleteAllButton)

		# Move up parameters/components
		self.upButton = Window_ParametersControl_UpButton(self)
		self.layout.addWidget(self.upButton)

		# Move down parameters/components
		self.downButton = Window_ParametersControl_DownButton(self)
		self.layout.addWidget(self.downButton)



		# Seperator
		l = QLabel()
		l.setStyleSheet(Styles.parameters_control.seperator)
		self.layout.addWidget(l)



		# Enable all parameters		
		self.enableAllButton = Window_ParametersControl_EnableAllButton(self)
		self.layout.addWidget(self.enableAllButton)

		# Disable all parameters		
		self.disableAllButton = Window_ParametersControl_DisableAllButton(self)
		self.layout.addWidget(self.disableAllButton)

		# Import new parameters		
		self.importParametersButton = Window_ParametersControl_ImportParametersButton(self)
		self.layout.addWidget(self.importParametersButton)











