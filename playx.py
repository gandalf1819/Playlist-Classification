import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import requests

client_id = "9cadcbe67a824c4f88857d0461cb88c9"
client_secret = "88860b25ed594d1aa0d1f9c9f7934dad"

myUrl = 'https://api.spotify.com/v1/search?q=dua%20lipa&type=artist&limit=50'
myToken = 'BQC-zTLqmPLDYeX_8GdFIAbUelm1-M0QdFLqnaoPEEk_DYFO7EUwkmM-8v-yIckCIIyzpC3XHXXG6_-R9VFuLkCWZNqzPPzB5gblxfFSjZvbC3ozb9OGtt6LKDUEOtOpavR3NDWK_jkMA0pkKZmdC1LpMs7fmwdo80AyqV5e6LnGjk4uaDxS86vLEIw'
head = {'Authorization': 'token {}'.format(myToken)}

# username='8fdw4l89zw0v8cfsx1dr28sh6'
# client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret) 
# scope = 'user-library-read playlist-read-private'

response = requests.get(myUrl, headers={'Authorization': 'TOK:BQC-zTLqmPLDYeX_8GdFIAbUelm1-M0QdFLqnaoPEEk_DYFO7EUwkmM-8v-yIckCIIyzpC3XHXXG6_-R9VFuLkCWZNqzPPzB5gblxfFSjZvbC3ozb9OGtt6LKDUEOtOpavR3NDWK_jkMA0pkKZmdC1LpMs7fmwdo80AyqV5e6LnGjk4uaDxS86vLEIw'})
#response = requests.get(myUrl, headers=head)
print(response)

# try:
#     token=util.prompt_for_user_token(username, scope,client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri) 

#     response = requests.get(url)
#     print(response)
# except:
#     print('Token is not accesible for ' + username)


#body_params = {'grant_type' : grant_type}

#url = 'https://accounts.spotify.com/api/token'
#url = 'https://api.spotify.com/v1/search?q=dua%20lipa&type=artist&limit=50'

#response = requests.get(url, data=body_params, auth = (client_id, client_secret))
#print(response)