from engine.require import *
from engine.plugins import *
from engine.components import *
from engine.osc_server import *

from .enablebox import *
from .pluginsbox import *

from .parameterpath import *
from .parametervalue import *





__all__ = ("Window_ParametersItem",)





class Window_ParametersItem(QFrame, RFT_Object):
	def __init__(self, parent, uid):
		super().__init__(parent)


		# ~~~~~~~~~~~ Variables ~~~~~~~~~~
		self.parent = parent

		self.uid = uid
		self.param = Tables.parameters[uid]

		self.handle = None
		self.handlePath = None
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Options ~~~~~~~~~~~
		self.setCursor(Qt.CursorShape.PointingHandCursor)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~ Stylesheet ~~~~~~~~~~
		self.setStyleSheet(Styles.parameters_item.main)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Layout ~~~~~~~~~~~~
		self.layout = QHBoxLayout()
		self.layout.setSpacing(10)
		self.layout.setContentsMargins(0, 0, 0, 0)
		self.layout.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

		self.setLayout(self.layout)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~~ Path ~~~~~~~~~~~~~
		self.parameterPath = Window_ParametersItem_ParameterPath(self)
		self.layout.addWidget(self.parameterPath)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~~ Value ~~~~~~~~~~~~
		self.parameterValue = Window_ParametersItem_ParameterValue(self)
		self.layout.addWidget(self.parameterValue)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~ Plugins ~~~~~~~~~~~
		self.pluginsBox = Window_ParametersItem_PluginsBox(self)
		self.pluginsBox.reload()
		self.layout.addWidget(self.pluginsBox)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~ Enable Box ~~~~~~~~~~
		self.enableBox = Window_ParametersItem_EnableBox(self)
		self.layout.addWidget(self.enableBox)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	@pyqtSlot(QMouseEvent)
	def mousePressEvent(self, event):
		if (event.button() == Qt.MouseButton.LeftButton):
			if (self.parent.selected):
				# Reset previously selected object to default stylesheet
				self.parent.selected.setStyleSheet(Styles.parameters_item.main)

			# Set selected to new stylesheet
			self.setStyleSheet(Styles.parameters_item.main_selected)
			
			# Set new selected
			self.parent.selected = self

			# Enable the delete button
			self.parent.parent.parametersControl.parametersWidget.deleteButton.setEnabled(True)


			# Unselect components
			self.parent.parent.componentsList.selected = None
	
			# Reload components
			self.parent.parent.componentsList.reload()




	# ~~~~~~~~~~~~ Methods ~~~~~~~~~~~
	def update(self):
		# Get path
		path = self.param.path

		# Get enabled
		enabled = self.param.enabled


		# Set enabled
		self.pluginsBox.setEnabled(not enabled)
		self.parameterPath.setEnabled(not enabled)
		# self.parameterValue.setEnabled(not enabled)


		# Unregister old handle if its bound
		if (self.handle != None):
			OSCServer.unregister(
				self.handlePath,
				self.handle
			)

			self.handle = None
			self.handlePath = None


		# Register new handle if its enabled
		if (enabled):
			self.handle = OSCServer.register(
				path,
				self.callback
			)

			self.handlePath = path





	def callback(self, path, value):
		if (isinstance(value, (bool, int, float))):
			# Process value with components
			com = self.param.components


			for k, v in com.items():

				c = v.component

				# If component exists
				if (Components.components.contains(c)):
					func = Components.components[c]

					if (value != None):
						if (v.value != None or c in Components.componentsSingle):
							if (func):
								# Call function
								try:
									v = func(
										value,
										v.value,
										v.swap
									)

								except:
									print(traceback.format_exc())
									v = None


								# If function returned correct value
								if (isinstance(v, (int, float, bool))):
									value = v



			if (isinstance(value, bool)):
				strValue = f"{value}"

			elif (isinstance(value, (int, float))):
				strValue = f"{round(value, 2)}"

			else:
				strValue = "None"
				value = None



			# Set parameter value widget
			self.parameterValue.setPlaceholderText(strValue)


			# Get plugin id
			pl = self.param.plugin

			# Get plugin
			if (Plugins.plugins.contains(pl)):
				plugin = Plugins.plugins[pl]
				
				# Get plugin callback
				func = plugin.callback

				if (func):
					try:
						# Call function
						func(path, value)

					except:
						print(traceback.format_exc())


		elif (isinstance(value, types.NoneType)):
			# Set parameter value widget
			self.parameterValue.setPlaceholderText("None")
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




