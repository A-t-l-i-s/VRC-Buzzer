from engine.require import *





__all__ = ("Window_ParametersControl_UpButton",)





class Window_ParametersControl_UpButton(QPushButton, RFT_Object):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~~~~~ Variables ~~~~~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Options ~~~~~~~~~~~
		self.setText("Move Up")
		self.setFixedSize(150, 25)
		self.setCursor(Qt.CursorShape.PointingHandCursor)
		self.setEnabled(False)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~ Stylesheet ~~~~~~~~~~
		self.setStyleSheet(Styles.window.button)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Signals ~~~~~~~~~~~
		self.pressed.connect(self._pressed)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	def _pressed(self):
		# Get widgets
		pl = self.parent.parent.parent.parametersList
		pls = pl.selected

		cl = self.parent.parent.parent.componentsList
		clse = cl.selected


		if (clse):
			# Get components
			com = pls.param.components

			if (len(com) > 1):
				self.parent.parent.parent.moveData(
					com,
					clse.uid,
					-1
				)


		elif (pls):
			if (len(Tables.parameters) > 1):
				self.parent.parent.parent.moveData(
					Tables.parameters,
					pls.uid,
					-1
				)




		# Reload lists
		pl.reload()
		cl.reload()




