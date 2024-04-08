from engine.require import *
from engine.components import *

from .swapbox import *
from .componentsbox import *
from .componentsvalue import *





__all__ = ("Window_ComponentsItem",)





class Window_ComponentsItem(QFrame, RFT_Object):
	def __init__(self, parent, uid, param):
		super().__init__(parent)


		# ~~~~~~~~~~~ Variables ~~~~~~~~~~
		self.parent = parent

		self.uid = uid
		self.param = param
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Options ~~~~~~~~~~~
		self.setCursor(Qt.CursorShape.PointingHandCursor)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~ Stylesheet ~~~~~~~~~~
		self.setStyleSheet(Styles.components_item.main)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Layout ~~~~~~~~~~~~
		self.layout = QHBoxLayout()
		self.layout.setSpacing(10)
		self.layout.setContentsMargins(0, 0, 0, 0)
		self.layout.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

		self.setLayout(self.layout)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Plugins ~~~~~~~~~~~
		self.componentsBox = Window_ComponentsItem_ComponentsBox(self)
		self.layout.addWidget(self.componentsBox)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~~ Value ~~~~~~~~~~~~
		self.componentsValue = Window_ComponentsItem_ComponentsValue(self)
		self.layout.addWidget(self.componentsValue)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~ Swap Box ~~~~~~~~~~~
		self.swapBox = Window_ComponentsItem_SwapBox(self)
		self.layout.addWidget(self.swapBox)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		self.componentsBox.reload()



	@pyqtSlot(QMouseEvent)
	def mousePressEvent(self, event):
		if (event.button() == Qt.MouseButton.LeftButton):
			if (self.parent.selected):
				# Reset previously selected object to default stylesheet
				self.parent.selected.setStyleSheet(Styles.components_item.main)

			# Set selected to new stylesheet
			self.setStyleSheet(Styles.components_item.main_selected)

			# Set new selected
			self.parent.selected = self

			# Enable the buttons
			param = self.parent.parent.parametersControl.parametersWidget
			param.upButton.setEnabled(True)
			param.downButton.setEnabled(True)
			param.deleteButton.setEnabled(True)





