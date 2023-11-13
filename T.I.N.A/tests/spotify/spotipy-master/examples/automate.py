import os
import json
import time
import spotipy


client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
client_redirect_uri = os.environ["SPOTIPY_REDIRECT_URI"]

scope = 'user-read-current-playing'

oauth_object = spotipy.SpotifyOAuth(client_id=client_id, client_secret=client_secret,redirect_uri=client_redirect_uri, scope=scope)

current = spotify_object.current_playing