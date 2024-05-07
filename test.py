import serial
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify Authentication
DEVICE_ID = "bdfa920fb519288b10b8012fdc9789bc33beaac7"
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
ser = serial.Serial('COM3', 9600)  # Adjust the serial port as needed

while True:
    if ser.in_waiting > 0:
        card_id = ser.readline().strip().decode('utf-8')
        # Replace 'your_rfid_tag_id_here' with the actual RFID tag ID you want to trigger playback
        if card_id == "d3e2bc15":
            # Start playback on Spotify
            sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:5CE1ynhZ3PUWrj10mw2w0d'])
        elif card_id == "c3b2a615":
            sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:2gug6MRv4xQFYi9LA3PJCS'])
        elif card_id == "534e9b3":
            sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:0yc6Gst2xkRu0eMLeRMGCX'])
        elif card_id == "43699715":
            sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:4PogoNNiWpyonhZxaypK60'])
        elif card_id == "f3cc315":
            sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:0m23lLeRzSmqPbFu62pQ5b'])
        elif card_id == "13da9115":
            sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:5ueYZaFc4RMyJYkDg9GzVJ'])
        elif card_id == "435b9015":
            sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:52eIcoLUM25zbQupAZYoFh'])   
        elif card_id == "1376a215":
            sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:4kjI1gwQZRKNDkw1nI475M'])
        elif card_id == "734fb115":
            sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:3KkXRkHbMCARz0aVfEt68P'])
                         
