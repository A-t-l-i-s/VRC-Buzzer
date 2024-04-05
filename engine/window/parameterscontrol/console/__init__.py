from engine.require import *





__all__ = ("Window_ParametersControl_Console",)





class Window_ParametersControl_Console(QFrame, RFT_Object):
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



		self.title = QLabel("Console")
		self.title.setAlignment(Qt.AlignmentFlag.AlignHCenter)
		self.title.setStyleSheet(Styles.parameters_control.title)
		self.layout.addWidget(self.title)


		self.console = QLabel()
		self.console.setFixedWidth(150)
		self.console.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
		self.console.setStyleSheet(Styles.parameters_control.device_list)
		self.layout.addWidget(self.console)



		# ~~~~~~~~~~~~~ Timer ~~~~~~~~~~~~
		self.timer = QTimer()
		self.timer.setInterval(50)
		self.timer.timeout.connect(self._timeout)
		self.timer.start()
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~~~~ Methods ~~~~~~~~~~~
	def _timeout(self):
		# Create text for widget
		t = ""
		
		for k, v in Data.console.items():
			if (isinstance(v, RFT_Structure)):
				for k_, v_ in v.items():
					t += f"{v_}\n"

			else:
				t += f"{v_}\n"

			t += "\n"



		# Clean up text
		t = t.strip()

		# Add text to widget
		self.console.setText(t)
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




