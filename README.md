# Spotify with RFID

Spotify with RFID is a Python project that integrates RFID technology with the Spotify Web API. The goal is to enable users to control Spotify playback—such as starting playlists, skipping tracks, or triggering other actions—by simply scanning RFID tags. This project uses the [Spotipy](https://spotipy.readthedocs.io/) library to interact with Spotify, and it leverages RFID hardware for a unique, physical interaction with your music streaming experience.

## Features

- **RFID-Triggered Actions:**  
  Each RFID tag can be mapped to a specific Spotify action, for example, playing a favorite playlist or controlling playback.
- **Spotify API Integration:**  
  Uses Spotipy to manage authentication and execute commands on your Spotify account.
- **Modular Design:**  
  Organized into separate modules, including the main application logic, API interaction tests, and RFID-specific tests.
- **Arduino Integration:**  
  An Arduino board assists in reading RFID tags and sending the data to the Python application in real time.
- **Testing Suite:**  
  Includes tests (e.g., `test_api.py` and contents within the `test_rfid` folder) to verify communication with both Spotify and the RFID reader.

## Hardware Integration

In addition to the RFID reader, this project utilizes an Arduino microcontroller to capture RFID scans and assist the Python application with real-time data input.

### Requirements

- **Arduino Board:** (e.g., Arduino Uno)
- **RFID Reader Module:** Compatible with Arduino (e.g., RC522)
- **RFID Tags**
- **USB Cable:** To connect the Arduino to your computer

### Setup Steps for Arduino

1. **Hardware Setup:**  
   Connect the RFID reader to the Arduino following the wiring diagram provided by your RFID module’s documentation. [Last Minute Engineering](https://lastminuteengineers.com/how-rfid-works-rc522-arduino-tutorial/)

2. **Arduino Code:**  
   Upload the provided Arduino sketch (located in the `arduino` folder) to your Arduino board. This sketch reads RFID tags and sends the tag data over serial communication to the connected computer.

3. **Python Integration:**  
   The Python application listens for incoming serial data from the Arduino. Ensure that your Arduino is connected to your computer and configure the correct serial port in your Python script.

4. **Customization:**  
   Both the Arduino sketch and the Python script can be modified to change how RFID scans are handled. Future changes and enhancements are expected as the project evolves.

## Installation

### Prerequisites

- **Python 3.12+**  
  Ensure you are running Python 3.12 or later.
- **RFID Hardware:**  
  An RFID reader and tags are required to fully test the RFID functionality.
- **Spotify Developer Account:**  
  Create a Spotify Developer account to obtain your Client ID, Client Secret, and Redirect URI. You can sign in by using your default Spotify account.  

### Setup Steps

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Paulen101/spotify_with_RFID.git
   cd spotify_with_RFID
   ```

2. **Create a Virtual Environment:**
  
   ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Independencies:**

   ```bash
    pip install -r requirement.txt
   ```

4. **Configure Spotify Credentials:**

     Setup your Spotify Credentials as environment variables or in configuration file (e.g., `config.py`)
     
     ```python
      SPOTIFY_CLIENT_ID = 'your_client_id'
      SPOTIFY_CLIENT_SECRET = 'your_client_secret'
      SPOTIFY_REDIRECT_URI = 'your_redirect_uri'
     ```

## Usage
After setting up your environment and configuring your credentials, run the main application with:

```bash
  python main.py
```
The application will wait for RFID tag scans (received via the Arduino) and then perform the associated spotify action. Modify the mapping of RFID tags to action as needed for your project.

## Testing
Run the included tests to verify your setup:

- ### API Tests:

      python test_api.py

- ### RFID Tests: 
    Check the `test_rfid` folder for additional test scripts that help ensure your RFID hardware is correctly intergrated. These tests ensure that the RFID reader correctly captures the RFID card's ID. Make sure you get the correct ID from your RFID card. After scanning, the application will trigger playback on the device specified by the device ID in your Python code. You no longer need the RFID scanner to be physically connected to that playback device; simply connect the scanner to your computer and configure the correct port in your code. This way, playback can occur on any device (e.g., your phone or tablet) as long as its device ID is correctly set.

## Future Improvement
This project is under active development. Future updates may includes:
- Enhanced scanning functionality
- Additional Arduino and sensor integration
- Expanded mapping options for RFID tags
- Improved error handling and user feedback
- __Integration with Apple Music:__ Expanding the platform support to include Apple Music
- __Wireless Operation:__ Transitioning to a wireless solution so that the RFID scanner doesn't need to be physically connected to your computer. Instead, the scanner will operate on a normal power supply, while your Python code directs playback to the device specified in the configuration.

## Contributing 

Contributions are welcome! If you have any ideas for improvements or additional features, please feel free to open an issue or submit a pull request.
        
    


