from engine.require import *





__all__ = ("Spotify",)





class Spotify(RFT_Object):
	try:
		client = spotipy.Spotify(
			auth_manager = SpotifyOAuth( # Spotify OAuth Authentication
				client_id = Data.spotify.clientId, # Client ID
				client_secret = Data.spotify.secretId, # Secret Client ID
				redirect_uri = "http://localhost:8080", # Redirect URI
				scope = "user-read-playback-state user-read-currently-playing" # Access Scopes
			)
		)
		
	except:
		client = None



	@classmethod
	def playing(cls):
		if (cls.client):
			# Get currently playing
			try:
				current = cls.client.current_playback()
			except:
				current = None


			if (current):
				data = RFT_Structure(current)

				if (data.contains(("item", "is_playing", "progress_ms"))):
					# Get item
					item = data.item

					if (item.contains(("name", "artists", "duration_ms"))):
						# Get all artists
						artists = []

						for a in data.item.artists:
							artists.append(
								a["name"]
							)


						# Build and retrun data
						return RFT_Structure({
							"title": item.name,
							"artists": artists,
							"playing": data.is_playing,

							"progress": (
								data.progress_ms,
								item.duration_ms
							)
						})

		return None




