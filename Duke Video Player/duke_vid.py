import tkinter as tk
from tkinter import filedialog, ttk
from ffpyplayer.player import MediaPlayer
import cv2
from PIL import Image, ImageTk

class VideoPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Enhanced Video Player")
        
        # Variables
        self.file_path = None
        self.cap = None
        self.player = None
        self.playing = False
        self.volume = 0.5
        self.frame_image = None  # Holds the current frame to avoid garbage collection

        # Create GUI
        self.create_gui()

    def create_gui(self):
        # Video Display
        self.canvas = tk.Canvas(self.root, width=800, height=450, bg="black")
        self.canvas.pack()

        # Open File Button
        self.open_button = tk.Button(self.root, text="Open Video", command=self.open_video)
        self.open_button.pack(pady=10)

        # Play/Pause Button
        self.play_button = tk.Button(self.root, text="Play", command=self.toggle_play_pause, state="disabled")
        self.play_button.pack(pady=5)

        # Volume Control
        self.volume_label = tk.Label(self.root, text="Volume")
        self.volume_label.pack(pady=5)
        self.volume_slider = ttk.Scale(self.root, from_=0, to=1, value=self.volume, orient='horizontal', command=self.change_volume)
        self.volume_slider.pack()

        # Stop Button
        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_video, state="disabled")
        self.stop_button.pack(pady=5)

    def open_video(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4 *.avi *.mkv *.mov *.flv *.wmv")])
        if self.file_path:
            # Load Video
            self.cap = cv2.VideoCapture(self.file_path)
            self.player = MediaPlayer(self.file_path)
            self.play_button.config(state="normal")
            self.stop_button.config(state="normal")
            self.playing = True
            self.play_video()

    def play_video(self):
        if not self.cap or not self.cap.isOpened():
            return

        ret, frame = self.cap.read()
        if ret:
            # Convert frame for display
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            self.frame_image = ImageTk.PhotoImage(image=img)

            # Display on Canvas
            self.canvas.create_image(0, 0, anchor="nw", image=self.frame_image)

            # Sync with audio
            audio_frame, val = self.player.get_frame()
            if val != 'eof' and audio_frame is not None:
                self.player.set_volume(self.volume)

            # Continue playing if video is active
            if self.playing:
                self.root.after(10, self.play_video)
        else:
            self.stop_video()

    def toggle_play_pause(self):
        if not self.cap or not self.player:
            return
        if self.playing:
            self.playing = False
            self.player.pause()
            self.play_button.config(text="Play")
        else:
            self.playing = True
            self.player.set_pause(False)  # Resume audio playback
            self.play_button.config(text="Pause")
            self.play_video()

    def change_volume(self, value):
        self.volume = float(value)
        if self.player:
            self.player.set_volume(self.volume)

    def stop_video(self):
        self.playing = False
        self.play_button.config(text="Play", state="disabled")
        self.stop_button.config(state="disabled")
        if self.cap:
            self.cap.release()
            self.cap = None
        if self.player:
            self.player.close()
            self.player = None
        self.canvas.delete("all")

    def run(self):
        self.root.mainloop()
        if self.cap:
            self.cap.release()
        if self.player:
            self.player.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoPlayer(root)
    app.run()
