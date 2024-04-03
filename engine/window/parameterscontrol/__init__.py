from engine.require import *
from engine.intiface import *

from .shocker import *
from .intiface import *
from .parameters import *





__all__ = ("Window_ParametersControl",)





class Window_ParametersControl(QFrame, RFT_Object):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~~~~~ Variables ~~~~~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Options ~~~~~~~~~~~
		self.setEnabled(True)

		self.setFixedWidth(170)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~ Stylesheet ~~~~~~~~~~
		self.setStyleSheet(Styles.parameters_control.main)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~ Main Layout ~~~~~~~~~
		self.mainLayout = QVBoxLayout()
		self.mainLayout.setSpacing(0)
		self.mainLayout.setContentsMargins(0, 0, 0, 0)

		self.setLayout(self.mainLayout)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Layout ~~~~~~~~~~~~
		self.layout = QVBoxLayout()
		self.layout.setSpacing(0)
		self.layout.setContentsMargins(0, 0, 0, 0)
		self.layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
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
		

		# ~~~~~~~~~~~~ Parameters ~~~~~~~~
		self.parametersWidget = Window_ParametersControl_Parameter(self)
		self.layout.addWidget(self.parametersWidget)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Shocker ~~~~~~~~~~~
		self.shockerWidget = Window_ParametersControl_Shocker(self)
		self.layout.addWidget(self.shockerWidget)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Intiface ~~~~~~~~~~~
		self.intifaceWidget = Window_ParametersControl_Intiface(self)
		self.layout.addWidget(self.intifaceWidget)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



		# ~~~~~~~~~~~~~ Timer ~~~~~~~~~~~~
		self.timer = QTimer()
		self.timer.setInterval(100)
		self.timer.timeout.connect(self._timeout)
		self.timer.start()
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~~~~ Methods ~~~~~~~~~~~
	def _timeout(self):
		text = ""

		if (Intiface.client):
			for k, v in Intiface.client.devices.items():
				text += v.name + "\n"

			# Strip text
			text = text.strip()

		if (not text):
			text = "No Devices Connected"

		# Set text
		self.intifaceWidget.devicesConnectedLabel.setText(text)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
