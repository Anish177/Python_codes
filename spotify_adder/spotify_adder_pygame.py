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
import pygame
pygame.init()


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

screen = pygame.display.set_mode((410, 200))
pygame.display.set_caption("Add Random Songs to Queue")
img = pygame.image.load('spotify_adder\spotify_adder.png')
img = pygame.transform.scale(img, (150, 150))
screen.blit(img, (25, 25))
font = pygame.font.Font('Torus.ttf', 11)
song_text = font.render('Find song', True, (255, 255, 255))
screen.blit(song_text, (215, 35))
find_button = pygame.sprite.Sprite()
find_button.image = pygame.Surface((80, 30))
find_button.image.fill((142, 133, 255))
find_button.rect = find_button.image.get_rect()
find_button.rect.x = 215
find_button.rect.y = 130
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        if find_button.rect.collidepoint(pos):
            find()
        elif add_button.rect.collidepoint(pos):
            add_queue()

