#!/usr/bin/env python
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep

DEVICE_ID = "Your Device ID"
CLIENT_ID = "Your Client ID"
CLIENT_SECRET = "Your Client Secret"

# Spotify Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                client_secret=CLIENT_SECRET,
                                                redirect_uri="http://localhost:5000",
                                                scope="user-read-playback-state,user-modify-playback-state"))


# Transfer playback to the Raspberry Pi if music is playing on a different device
sp.transfer_playback(device_id=DEVICE_ID, force_play=False)

# Play the spotify track at URI with ID 45vW6Apg3QwawKzBi03rgD (you can swap this for a diff song ID below)
sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:7zK0PYW9JwQDEeczGPvcua'])
# https://open.spotify.com/track/7zK0PYW9JwQDEeczGPvcua?si=7309c0ddce2741ef

