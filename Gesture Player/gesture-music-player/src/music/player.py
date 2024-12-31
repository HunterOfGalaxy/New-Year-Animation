class MusicPlayer:
    def __init__(self):
        self.volume = 0.5  # Default volume level
        self.is_playing = False

    def play_music(self, track):
        if not self.is_playing:
            print(f"Playing music: {track}")
            self.is_playing = True
        else:
            print("Music is already playing.")

    def stop_music(self):
        if self.is_playing:
            print("Stopping music.")
            self.is_playing = False
        else:
            print("No music is currently playing.")

    def set_volume(self, volume):
        if 0 <= volume <= 1:
            self.volume = volume
            print(f"Volume set to: {self.volume * 100}%")
        else:
            print("Volume must be between 0 and 1.")