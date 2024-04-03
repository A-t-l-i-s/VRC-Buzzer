from engine.require import *





__all__ = ("Window_ParametersControl_DeleteButton",)





class Window_ParametersControl_DeleteButton(QPushButton, RFT_Object):
	def __init__(self, parent):
		super().__init__(parent)


		# ~~~~~~~~~~~ Variables ~~~~~~~~~~
		self.parent = parent
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Options ~~~~~~~~~~~
		self.setText("Delete")
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
				# If component exists then delete it
				if (com.contains(clse.uid)):
					com.pop(clse.uid)

				# Unselect components
				cl.selected = None


		elif (pls):
			# Disable param before deletion
			pls.param.enabled = False
			pls.update()

			# Delete parameter
			Tables.parameters.pop(pls.uid)

			# Unselect plugin
			pl.selected = None



		# Reload lists
		pl.reload()
		cl.reload()


		self.setEnabled(False)




