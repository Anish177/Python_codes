import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Initialize Spotipy with your credentials
auth_manager = SpotifyOAuth(client_id='f59c9a80334c45a7912961907a464fee', client_secret='5dbdc1b9868d4832a3301a68f860bc24', redirect_uri='http://localhost:8888/callback/', scope='user-read-playback-state,user-modify-playback-state')
sp = spotipy.Spotify(auth_manager=auth_manager)

# Create the main window
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Spotify Player')

# Create the buttons
play_pause_button = QPushButton('Play/Pause')
next_button = QPushButton('Next')
prev_button = QPushButton('Previous')

# Create the label for displaying the currently playing track
now_playing_label = QLabel('No song playing')

# Create the label for displaying the album art
album_art_label = QLabel()

# Create the layout for the window and add the widgets
layout = QVBoxLayout()
layout.addWidget(play_pause_button)
layout.addWidget(next_button)
layout.addWidget(prev_button)
layout.addWidget(now_playing_label)
layout.addWidget(album_art_label)
window.setLayout(layout)

# Define the SpotifyPlayer class
class SpotifyPlayer:
    def __init__(self):
        self.album_art_data = None

    # Update the GUI with the currently playing track and album art
    def update_gui(self):
        current_track = sp.current_playback()
        if current_track is not None:
            now_playing_label.setText(current_track['item']['name'] + ' - ' + current_track['item']['artists'][0]['name'])
            album_art_url = "https://assets.leetcode.com/uploads/2021/02/05/bst1.jpg"
            self.album_art_data = QPixmap(album_art_url)
            if self.album_art_data is not None:
                album_art_label.setPixmap(self.album_art_data)
            else:
                album_art_label.clear()
        else:
            now_playing_label.setText('No song playing')
            album_art_label.clear()

# Create an instance of the SpotifyPlayer class
player = SpotifyPlayer()

# Set a timer to update the GUI every second
timer = QTimer()
timer.timeout.connect(player.update_gui)
timer.start(1000)

# Set the button actions
play_pause_button.clicked.connect(lambda: sp.pause_playback() if sp.current_playback()['is_playing'] else sp.start_playback())
next_button.clicked.connect(lambda: sp.next_track())
prev_button.clicked.connect(lambda: sp.previous_track())

# Show the window
window.show()
sys.exit(app.exec_())
