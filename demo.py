import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import numpy as np

client_id = "9cadcbe67a824c4f88857d0461cb88c9"
client_secret = "88860b25ed594d1aa0d1f9c9f7934dad"
redirect_uri='https://www.google.com/'

username='8fdw4l89zw0v8cfsx1dr28sh6'
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret) 
scope = 'user-library-read playlist-read-private'
try:
    token = util.prompt_for_user_token(username, scope,client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)  
    sp=spotipy.Spotify(auth= token) # use sp to acceess spotify data

    songLibrary = sp.current_user_saved_tracks()
    playlist = sp.user_playlist(username,
    playlist_id='13ibm09SWMbyzrfPdEtSgI')

    playlists = sp.user_playlists(username)
    print("success")
    print(playlist)
except:
    print('Token is not accesible for ' + username)
