# FILE: /gesture-music-player/gesture-music-player/src/gesture_player.py

import time
from utils.gesture_recognition import GestureRecognition
from music.player import MusicPlayer

class GestureMusicPlayer:
    def __init__(self):
        self.gesture_recognition = GestureRecognition()
        self.music_player = MusicPlayer()
        self.is_running = False

    def start(self):
        self.is_running = True
        self.gesture_recognition.start_recognition()
        print("Gesture recognition started. Listening for gestures...")

        while self.is_running:
            gesture = self.gesture_recognition.get_gesture()
            self.handle_gesture(gesture)
            time.sleep(0.1)  # Prevent busy waiting

    def handle_gesture(self, gesture):
        if gesture == "play":
            self.music_player.play_music()
        elif gesture == "stop":
            self.music_player.stop_music()
        elif gesture == "volume_up":
            self.music_player.set_volume(self.music_player.volume + 10)
        elif gesture == "volume_down":
            self.music_player.set_volume(self.music_player.volume - 10)

    def stop(self):
        self.is_running = False
        self.gesture_recognition.stop_recognition()
        print("Gesture recognition stopped.")

if __name__ == "__main__":
    player = GestureMusicPlayer()
    try:
        player.start()
    except KeyboardInterrupt:
        player.stop()