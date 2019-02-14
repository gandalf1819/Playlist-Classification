import requests

# making a search request to the Spotify API to return
# any artist with 'OneRepublic' in their name
#response = requests.get('https://api.spotify.com/v1/search?query=OneRepublic&type=artist&limit=50&market=US')
#response = requests.get('https://api.spotify.com/v1/search?q=dua%20lipa&type=artist&limit=50')
response = requests.get('https://api.spotify.com/v1/search?q=one&type=artist&limit=50')
#response = requests.get('https://api.spotify.com/v1/artists/5Pwc4xIPtQLFEnJriah9YJ/top-tracks?country=SE')

# converts the response from a string to a json object that can be parsed in Python.
data = response.json()

#visit this url: in order to see what the json object that is returned looks like:
# https://api.spotify.com/v1/artists/5Pwc4xIPtQLFEnJriah9YJ/top-tracks?country=SE
# looking at the 'items' returned for 'artists' in this request

#lil_artists = data['artists']['items'] 
print(data)
# iterating through each artist and their items
# items contains the information we would like to recieve for each artist.