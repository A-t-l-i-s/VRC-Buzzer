from engine.require import *
from engine.plugins import *

from .newbutton import *
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



		self.newButton = Window_ParametersControl_NewButton(self)
		self.layout.addWidget(self.newButton)

		self.deleteButton = Window_ParametersControl_DeleteButton(self)
		self.layout.addWidget(self.deleteButton)

		self.deleteAllButton = Window_ParametersControl_DeleteAllButton(self)
		self.layout.addWidget(self.deleteAllButton)


		l = QLabel()
		l.setStyleSheet(Styles.parameters_control.seperator)
		self.layout.addWidget(l)

		
		self.enableAllButton = Window_ParametersControl_EnableAllButton(self)
		self.layout.addWidget(self.enableAllButton)

		self.disableAllButton = Window_ParametersControl_DisableAllButton(self)
		self.layout.addWidget(self.disableAllButton)

		self.importParametersButton = Window_ParametersControl_ImportParametersButton(self)
		self.layout.addWidget(self.importParametersButton)











