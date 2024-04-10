from engine.require import *
from engine.spotify import *
from engine.heartrate import *
from engine.osc_server import *

from .mutebox import *
from .spotifybox import *
from .timezonebox import *
from .heartratebox import *
from .enablechatbox import *

from .spotifyclientid import *
from .spotifysecretid import *
from .heartrateaddress import *





__all__ = ("Window_ParametersControl_ChatBox",)





class Window_ParametersControl_ChatBox(QFrame, RFT_Object):
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



		self.title = QLabel("Chat Box")
		self.title.setAlignment(Qt.AlignmentFlag.AlignHCenter)
		self.title.setStyleSheet(Styles.parameters_control.title)
		self.layout.addWidget(self.title)


		self.enableChatBox = Window_ParametersControl_ChatBox_EnableChatBox(self)
		self.layout.addWidget(self.enableChatBox)


		# Seperator
		l = QLabel()
		l.setFixedHeight(3)
		self.layout.addWidget(l)


		self.spotifyBox = Window_ParametersControl_ChatBox_SpotifyBox(self)
		self.layout.addWidget(self.spotifyBox)

		self.spotifyClient = Window_ParametersControl_ChatBox_SpotifyClient(self)
		self.layout.addWidget(self.spotifyClient)

		self.spotifySecret = Window_ParametersControl_ChatBox_SpotifySecret(self)
		self.layout.addWidget(self.spotifySecret)


		# Seperator
		l = QLabel()
		l.setFixedHeight(3)
		self.layout.addWidget(l)


		self.timezoneBox = Window_ParametersControl_ChatBox_TimezoneBox(self)
		self.layout.addWidget(self.timezoneBox)


		# Seperator
		l = QLabel()
		l.setFixedHeight(3)
		self.layout.addWidget(l)


		self.heartrateBox = Window_ParametersControl_ChatBox_HeartRateBox(self)
		self.layout.addWidget(self.heartrateBox)

		self.heartrateAddress = Window_ParametersControl_ChatBox_HeartRateAddress(self)
		self.layout.addWidget(self.heartrateAddress)


		# Seperator
		l = QLabel()
		l.setFixedHeight(3)
		self.layout.addWidget(l)


		self.muteBox = Window_ParametersControl_ChatBox_MuteBox(self)
		self.layout.addWidget(self.muteBox)


		# Seperator
		l = QLabel()
		l.setFixedHeight(3)
		self.layout.addWidget(l)


		self.chatbox = QLabel()
		self.chatbox.setFixedWidth(150)
		self.chatbox.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
		self.chatbox.setStyleSheet(Styles.parameters_control.device_list + "\n*{font-size: 11px;}")
		self.layout.addWidget(self.chatbox)



		# ~~~~~~~~~~~~~ Loop ~~~~~~~~~~~~~
		threading._start_new_thread(
			self.loop,
			(),
			{}
		)
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


		# ~~~~~~~~~~~~~ Timer ~~~~~~~~~~~~
		self.timer = QTimer()
		self.timer.setInterval(50)
		self.timer.timeout.connect(self._timeout)
		self.timer.start()
		# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	# ~~~~~~~~~~~~ Methods ~~~~~~~~~~~
	def _timeout(self):
		for w, e in (
			(self.enableChatBox, Tables.chatbox.enabled),
			(self.spotifyBox, Tables.chatbox.spotify),
			(self.timezoneBox, Tables.chatbox.timezone),
			(self.heartrateBox, Tables.chatbox.heartrate),
			(self.muteBox, Tables.chatbox.mute),
		):
			if (w.isChecked() != e):
				w.setChecked(e)






	def loop(self):
		while not Data.qt.app.exiting:
			if (Tables.chatbox.enabled):
				t = time.time()
				text = ""


				if (Tables.chatbox.spotify):
					# Get currently playing song
					p = Spotify.playing()

					if (p):
						if (p.playing):
							# Display song and artists
							arts = ", ".join(p.artists)

							text += f"\v♫ {p.title} ᵇʸ {arts}"


							# Display progress
							pSecs = p.progress[0] / 1000
							dSecs = p.progress[1] / 1000

							pMins = math.floor(pSecs / 60)
							dMins = math.floor(dSecs / 60)

							pSecs = round(pSecs % 60)
							dSecs = round(dSecs % 60)

							text += "\v⏳ " + f"{pMins}:{pSecs}s - ".lstrip("0:") + f"{dMins}:{dSecs}s".lstrip("0:")



				if (Tables.chatbox.timezone):
					# Get current time
					now = datetime.datetime.now()
					text += "\v🕜 " + now.strftime("%I:%M:%S %p")



				if (Tables.chatbox.heartrate):
					# Get heart rate
					v = HeartRate.value

					if (v):
						text += f"\v❤︎ {v}"



				if (Tables.chatbox.mute):
					# Get is muted
					text += "\v🔇"



				text = text.strip("\v")
				textOut = text.replace("\v", "\n")

				if (not Data.qt.app.exiting):
					self.chatbox.setText(textOut)


				# Get difference delay
				dif = time.time() - t

				# Wait
				time.sleep(
					max(
						1.6 - dif,
						0
					)
				)


				# Send text to chatbox
				OSCServer.send(
					"/chatbox/input",
					(
						text,
						True,
						False
					)
				)

			else:
				time.sleep(1)

				if (not Data.qt.app.exiting):
					self.chatbox.setText("")
	# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




