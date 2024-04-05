from engine.require import *

from .shockercodefield import *
from .shockertokenfield import *
from .shockerusernamefield import *





__all__ = ("Window_ParametersControl_Shocker",)





class Window_ParametersControl_Shocker(QFrame, RFT_Object):
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
		self.layout.setContentsMargins(0, 20, 0, 3)
		self.layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
		
		self.setLayout(self.layout)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



		self.title = QLabel("Shocker")
		self.title.setAlignment(Qt.AlignmentFlag.AlignHCenter)
		self.title.setStyleSheet(Styles.parameters_control.title)
		self.layout.addWidget(self.title)


		self.shockerUsernameField = Window_ParametersControl_ShockerUsernameField(self)
		self.layout.addWidget(self.shockerUsernameField)

		self.shockerCodeField = Window_ParametersControl_ShockerCodeField(self)
		self.layout.addWidget(self.shockerCodeField)

		self.shockerTokenField = Window_ParametersControl_ShockerTokenField(self)
		self.layout.addWidget(self.shockerTokenField)




