import serial
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify Authentication
DEVICE_ID = "Your Device ID"
CLIENT_ID = "Your Client ID"
CLIENT_SECRET = "Your Client Secret"

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
        command = ser.readline().strip().decode('utf-8')
        
        if command == "b30959fb": 
            sp.pause_playback(device_id=DEVICE_ID)
        elif command == "d3e2bc15":
            sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:1dGr1c8CrMLDpV6mPbImSI'])
        elif command == "c3b2a615":
            sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:5XeFesFbtLpXzIVDNQP22n'])
        elif command == "534e9b3":
            sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:2WqdR6WZkndY8aCUQrHBLe'])
        elif command == "43699715":
            sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:42VsgItocQwOQC3XWZ8JNA'])
        elif command == "f3cc315":
            sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:7CyPwkp0oE8Ro9Dd5CUDjW'])
        elif command == "13da9115":
            sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:1V8s51MOKlmES1Vc9Erm89'])
        elif command == "435b9015":
            sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:2qSkIjg1o9h3YT9RAgYN75'])   
        elif command == "1376a215":
            sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:3XgGQ1wjo5khvq2UImjyNF'])
        elif command == "734fb115":
            sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:0s7Z1RtnsmiYOfSIbB3btD'])


