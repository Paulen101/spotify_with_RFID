#!/usr/bin/env python
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep

DEVICE_ID = "1377d4deeff9d04fb01c24b39848de962186e626"
CLIENT_ID = "3cd0d7c1827e45409647d94ae3e8ba41"
CLIENT_SECRET = "a50770c16dde48b4aa9cf2e7bce5e7d5"

# Spotify Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                client_secret=CLIENT_SECRET,
                                                redirect_uri="http://localhost:5000",
                                                scope="user-read-playback-state,user-modify-playback-state"))


# Transfer playback to the Raspberry Pi if music is playing on a different device
sp.transfer_playback(device_id=DEVICE_ID, force_play=False)

# Play the spotify track at URI with ID 45vW6Apg3QwawKzBi03rgD (you can swap this for a diff song ID below)
sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:3Y4za64Zc5vE5bZHJJAbej'])


