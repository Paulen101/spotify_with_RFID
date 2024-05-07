import serial
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify Authentication
DEVICE_ID = "66a07b1a0e587b0a0dee891b2e1e369e861ff3a8"
CLIENT_ID = "3cd0d7c1827e45409647d94ae3e8ba41"
CLIENT_SECRET = "a50770c16dde48b4aa9cf2e7bce5e7d5"

sp_oauth = SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri="http://localhost:5000",
    scope="user-read-playback-state,user-modify-playback-state"
)

sp = spotipy.Spotify(auth_manager=sp_oauth)

# Establish serial connection with Arduino
ser = serial.Serial('COM13', 9600)  # Adjust the serial port as needed

while True:
    if ser.in_waiting > 0:
        card_id = ser.readline().strip().decode('utf-8')
        # Replace 'your_rfid_tag_id_here' with the actual RFID tag ID you want to trigger playback
        if card_id == "d3e2bc15":
            # Start playback on Spotify
            sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:2dHHgzDwk4BJdRwy9uXhTO'])
            # https://open.spotify.com/track/2dHHgzDwk4BJdRwy9uXhTO?si=7b17341b0e17495d
