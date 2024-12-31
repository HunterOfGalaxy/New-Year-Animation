# Gesture Music Player

This project is a gesture-controlled music player that plays music based on hand movements. It utilizes gesture recognition to interpret hand gestures and control music playback.

## Project Structure

```
gesture-music-player
├── src
│   ├── gesture_player.py       # Main entry point of the application
│   ├── music
│   │   └── player.py           # Music player functionality
│   └── utils
│       └── gesture_recognition.py # Gesture recognition functionality
├── requirements.txt             # Project dependencies
└── README.md                    # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd gesture-music-player
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage Guidelines

1. Run the main application:
   ```
   python src/gesture_player.py
   ```

2. Make hand gestures to control the music playback:
   - Specific gestures will correspond to different music commands (e.g., play, pause, next track).

## Overview

The project consists of three main components:

- **Gesture Recognition**: The `GestureRecognition` class in `src/utils/gesture_recognition.py` captures and interprets hand movements to determine gestures.
  
- **Music Playback**: The `MusicPlayer` class in `src/music/player.py` handles music playback, including methods to play, stop, and adjust volume based on gestures received.

- **Integration**: The `gesture_player.py` file integrates the gesture recognition system with the music player, allowing for seamless control of music through hand movements.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.