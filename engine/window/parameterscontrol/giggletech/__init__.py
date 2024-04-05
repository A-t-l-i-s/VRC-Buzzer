from engine.require import *

from .ipfield import *





__all__ = ("Window_ParametersControl_GiggleTech",)





class Window_ParametersControl_GiggleTech(QFrame, RFT_Object):
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



		self.title = QLabel("GiggleTech")
		self.title.setAlignment(Qt.AlignmentFlag.AlignHCenter)
		self.title.setStyleSheet(Styles.parameters_control.title)
		self.layout.addWidget(self.title)


		self.ipField = Window_ParametersControl_GiggleTech_IPField(self)
		self.layout.addWidget(self.ipField)




