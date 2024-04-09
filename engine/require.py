import sys
sys.path = [".", "lib", "lib.zip", "bin", "bin.zip", "engine.zip"]

import os
import io
import json
import math
import time
import uuid
import yaml
import types
import psutil
import random
import asyncio
import zipfile
import datetime
import requests
import traceback
import threading
import subprocess

from pathlib import Path

import spotipy
from spotipy.oauth2 import SpotifyOAuth

from bleak import BleakClient, BleakScanner

from buttplug import (
	Client as Intiface_Client,
	WebsocketConnector as Intiface_WebsocketConnector,
	ProtocolSpec as Intiface_ProtocolSpec
)

from pythonosc.dispatcher import Dispatcher as OSC_Dispatcher
from pythonosc.udp_client import SimpleUDPClient as OSC_Client
from pythonosc.osc_server import BlockingOSCUDPServer as OSC_BlockingServer

from PyQt6.QtGui import (
	QFontDatabase, QFontMetrics, QAction,
	QImage, QPixmap, QIcon,
	QPainter, QColor, QPen,
	QBrush, QMouseEvent, QCursor,
	QFont
)

from PyQt6.QtCore import (
	Qt, pyqtSlot, QSize, QEvent, QTimer
)

from PyQt6.QtWidgets import (
	QApplication, QMainWindow,
	QWidget, QVBoxLayout, QHBoxLayout,
	QScrollArea, QLabel, QFrame,
	QLineEdit, QCheckBox, QPushButton,
	QComboBox, QFileDialog
)

from RFTLib.Core.Object import *
from RFTLib.Core.Buffer import *
from RFTLib.Core.Structure import *

from RFTLib.Config import *
from RFTLib.Config.qt import *
from RFTLib.Config.nil import *
from RFTLib.Config.yaml import *
from RFTLib.Config.text import *
from RFTLib.Config.python import *

from RFTLib.Tables import *





# ~~~~~~~~~~~~~~ Qt ~~~~~~~~~~~~~~
qtApp = QApplication([""])
qtApp.setStyle("Fusion")

QFontDatabase.addApplicationFont("./res/fonts/Dosis-Bold.ttf")
QFontDatabase.addApplicationFont("./res/fonts/Dosis-ExtraBold.ttf")
QFontDatabase.addApplicationFont("./res/fonts/Dosis-ExtraLight.ttf")
QFontDatabase.addApplicationFont("./res/fonts/Dosis-Light.ttf")
QFontDatabase.addApplicationFont("./res/fonts/Dosis-Medium.ttf")
QFontDatabase.addApplicationFont("./res/fonts/Dosis-Regular.ttf")
QFontDatabase.addApplicationFont("./res/fonts/Dosis-SemiBold.ttf")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



# ~~~~~~~~~~~~~ Data ~~~~~~~~~~~~~
Data_Obj = RFT_Config(
	"./res/data",
	(RFT_Config_NIL, RFT_Config_YAML)
)

Data = Data_Obj.data

Data.qt.app.app = qtApp

Data.elevate("Data")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ~~~~~~~~~~~~~ Icons ~~~~~~~~~~~~
Icons_Obj = RFT_Config(
	"./res/icons",
	(RFT_Config_QT_ICON,)
)

Icons = Icons_Obj.data

Icons.elevate("Icons")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ~~~~~~~~~~~~ Styles ~~~~~~~~~~~~
Styles_Obj = RFT_Config(
	"./res/styles",
	(RFT_Config_QT_QSS,)
)

Styles = Styles_Obj.data

Styles.elevate("Styles")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ~~~~~~~~~~~~ Plugins ~~~~~~~~~~~
Plugins_Ext_Obj = RFT_Config(
	"./res/plugins",
	(RFT_Config_PYTHON,)
)

Plugins_Ext = Plugins_Ext_Obj.data

Plugins_Ext.elevate("Plugins_Ext")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ~~~~~~~~~~~~ Tables ~~~~~~~~~~~~
Tables_Obj = RFT_Tables(
	"./res/tables"
)

Tables = Tables_Obj.data


Tables.window.default( # Allocate window table
	{
		"width": Data.qt.window.width,
		"height": Data.qt.window.height,

		"x": 0,
		"y": 0
	}
)

Tables.parameters.default( # Allocate parameters table
	{}
)

Tables.shocker.default( # Allocate shocker table
	{
		"username": None,
		"code": None,
		"token": None
	}
)

Tables.giggletech.default( # Allocate giggletech table
	{
		"ip": None
	}
)

Tables.chatbox.default( # Allocate chatbox table
	{
		"enabled": False,
		"spotify": False,
		"timezone": False,
		"heartrate": False
	}
)


Tables.elevate("Tables")
Tables_Obj.saveEvery(30)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
