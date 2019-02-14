import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import requests

# client credentials
client_id = "9cadcbe67a824c4f88857d0461cb88c9"
client_secret = "88860b25ed594d1aa0d1f9c9f7934dad"
redirect_uri='https://www.google.com/'


myURL = 'https://api.spotify.com/v1/search?q=one&type=artist&limit=50'

# user credentials
username='8fdw4l89zw0v8cfsx1dr28sh6'
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret) 
scope = 'user-library-read playlist-read-private'

# get authorization token
token = util.prompt_for_user_token(username, scope,client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
header = {'Authorization':'Bearer '+token}

#print(header)

# making a search request to the Spotify API to return
# any artist with 'OneRepublic' in their name
response = requests.get(myURL, headers=header)

# converts the response from a string to a json object that can be parsed in Python.
data = response.json()

print(data)