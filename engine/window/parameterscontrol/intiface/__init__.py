from engine.require import *
from engine.intiface import *

from .scanbox import *





__all__ = ("Window_ParametersControl_Intiface",)





class Window_ParametersControl_Intiface(QFrame, RFT_Object):
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



		# Title
		self.title = QLabel("Intiface")
		self.title.setAlignment(Qt.AlignmentFlag.AlignHCenter)
		self.title.setStyleSheet(Styles.parameters_control.title)
		self.layout.addWidget(self.title)



		# Vertical layout
		self.layoutH = QHBoxLayout()
		self.layoutH.setSpacing(5)
		self.layoutH.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
		
		self.layout.addLayout(self.layoutH)


		# Devices list label
		self.devicesLabel = QLabel()
		self.devicesLabel.setFixedWidth(125)
		self.devicesLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
		self.devicesLabel.setStyleSheet(Styles.parameters_control.device_list)
		self.layoutH.addWidget(self.devicesLabel)

		# Scan for devices checkbox
		self.scanBox = Window_ParametersControl_ScanBox(self)
		self.layoutH.addWidget(self.scanBox)



		# ~~~~~~~~~~~~~ Timer ~~~~~~~~~~~~
		self.timer = QTimer()
		self.timer.setInterval(100)
		self.timer.timeout.connect(self._timeout)
		self.timer.start()
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~~~~ Methods ~~~~~~~~~~~
	def _timeout(self):
		# Set scan box checked if scanning
		v = Data.intiface.scanning
		if (self.scanBox.isChecked() != v):
			self.scanBox.setChecked(v)



		# Display connected devices
		text = ""

		if (Intiface.client):
			for k, v in Intiface.client.devices.items():
				text += v.name + "\n"

			# Strip text
			text = text.strip()

		if (not text):
			text = "No Devices"

		# Set text
		self.devicesLabel.setText(text)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~





