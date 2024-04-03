from engine.require import *





__all__ = ("Window_ParametersControl_ImportParametersButton",)





class Window_ParametersControl_ImportParametersButton(QPushButton, RFT_Object):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~~~~~ Variables ~~~~~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Options ~~~~~~~~~~~
		self.setText("Import Parameters")
		self.setFixedSize(150, 25)
		self.setCursor(Qt.CursorShape.PointingHandCursor)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~ Stylesheet ~~~~~~~~~~
		self.setStyleSheet(Styles.window.button)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Signals ~~~~~~~~~~~
		self.pressed.connect(self._pressed)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def _pressed(self):
		# Open file dialog
		file, type_ = QFileDialog.getOpenFileName(
			self,
			"Open File",
			"./res/parameters",
			"YAML (*.yaml *.yml);;JSON (*.json)"
		)


		if (file):
			# Convert to path
			path = Path(file)
			d = {}

			with path.open("rb") as file:
				if (path.suffix in (".yaml", ".yml")):
					try:
						# Load yaml file
						d = yaml.load(file, yaml.FullLoader)
					except:
						...

				elif (path.suffix == ".json"):
					try:
						# Load json file
						d = json.load(file)
					except:
						...



			if (isinstance(d, dict)):
				# Convert to structure
				d_ = RFT_Structure(d)

				for k, v in d_.items():
					# If contains correct keys
					if (v.contains(("path", "plugin", "enabled"))):
						# If parameter doesn't exist
						if (not Tables.parameters.contains(k)):
							Tables.parameters[k] = v


			# Reload parameters list
			self.parent.parent.parent.parametersList.reload()

