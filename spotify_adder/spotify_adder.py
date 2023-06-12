'''
From an idea to a script to a GUI
Docstring to be written here
'''
from io import BytesIO
import os
import random
import tkinter as tk
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from PIL import Image, ImageTk
import requests
from requests_file import FileAdapter

# Setting environment variables
os.environ["SPOTIPY_CLIENT_ID"] = " " # redacted for privacy reasons
os.environ["SPOTIPY_CLIENT_SECRET"] = " " # redacted for privacy reasons
os.environ["SPOTIPY_REDIRECT_URI"] = " " # redacted for privacy reasons

# Setting up the Spotify client
sp = spotipy.Spotify(auth_manager = SpotifyOAuth(scope = 'user-library-read, user-modify-playback-state'))


def get_tracks(sp: spotipy.client.Spotify) -> list[str]:
    '''
    Returns a list of tracks
    '''
    # Fetching saved tracks (i.e., Liked Songs)
    results = sp.current_user_saved_tracks(limit = 50, offset = 0)
    tracks = results['items']

    # Fetch all of the user's Liked Songs
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    
    return tracks

try:
    tracks = get_tracks(sp)
except requests.exceptions.ReadTimeout:
    print('Unable to get list of tracks. Restart the program.')

track_uri = ''

def find():
    '''
    Finds the song
    '''
    if len(tracks) > 0:
        global track_uri
        chosen_track = random.choice(tracks)
        track = chosen_track['track']
        track_uri = track['uri']

        tracks.remove(chosen_track)
        # Get the album cover art URL for the track
        album_cover_url = track['album']['images'][0]['url']

        # Load the album cover art image and resize it
        try:
            response = requests.get(album_cover_url, timeout = 1)
            img = Image.open(BytesIO(response.content))
            img = img.resize((150, 150))

            # Display the album cover art in the GUI
            album_cover = ImageTk.PhotoImage(img)
            album_cover_label.config(image = album_cover)
            album_cover_label.image = album_cover

            song_label.config(text = track['name'])
            album_label.config(text = track['album']['name'])
            artist_label.config(text = track['artists'][0]['name'])
            added_song_label.config(text = '')
        except Exception:
            added_song_label.config(text = 'Timed out, try again')

    else:
        song_label.config(text='No saved tracks found.')

def add_queue():
    '''
    Adds the track to the user's queue
    '''
    sp.add_to_queue(track_uri)
    added_song_label.config(text='Added')

# Create the GUI
root = tk.Tk()
root.geometry("410x200")
root.configure(bg = '#7d7ced')
root.title("Add Random Songs to Queue")

# cover art
album_cover_label = tk.Label(root, bg = '#7d7ced')
album_cover_label.place(x = 25, y = 25)

s = requests.Session()
s.mount('file://', FileAdapter())
resp = s.get('file:///' + full path + '/spotify_adder.png')
img = Image.open(BytesIO(resp.content))
img = img.resize((150, 150))

# Display the temporary cover art in the GUI
temp_cover = ImageTk.PhotoImage(img)
album_cover_label.config(image = temp_cover)
album_cover_label.image = temp_cover

song_label = tk.Label(root, text = 'Find song', bg = '#7d7ced', font = ('Torus', 11, 'bold'))
song_label.place(x = 215, y = 35)

album_label = tk.Label(root, text = 'Then add it', bg = '#7d7ced', font = ('Torus', 9))
album_label.place(x = 218, y = 55)

artist_label = tk.Label(root, text = '', bg = '#7d7ced', font = ('Torus', 9))
artist_label.place(x = 218, y = 75)

added_song_label = tk.Label(root, text = '', bg = '#7d7ced', font = ('Torus', 10, 'bold'))
added_song_label.place(x = 215, y = 105)

find_button = tk.Button(root, text = "Find song", command = find,
                        bg = '#8e85ff', activebackground = '#716acc')
add_button = tk.Button(root, text = "Add song", command = add_queue,
                        bg = '#8e85ff', activebackground = '#716acc')

# add the buttons to one line
find_button.place(x = 215, y = 130)
add_button.place(x = 305, y = 130)

root.mainloop()
