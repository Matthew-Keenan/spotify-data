import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt 

# Retrieved client id and client secret from Spotify app dashboard
cli_id = '21357e5761f84b0397e2b26cb9a8fbc7'
cli_secret = '965431eaa09e49bd9e1e17393ec10312'

# Uses client id and client secret to create client credentials object
client_cred_manager = SpotifyClientCredentials(client_id=cli_id, client_secret=cli_secret)

# Creates spotify object to use spotipy methods to use with Spotify api, using client credentials 
# for authorization
spotify = spotipy.Spotify(client_credentials_manager=client_cred_manager)

# Playlist id for Spotify's "Top Songs of 2019" playlist
playlistID = '37i9dQZF1DWVRSukIED0e9'

# Creates dictionary with the playlist id to return entire playlist data
top_hits_2019 = spotify.playlist(playlistID)

# Creates list with track data for every track
tracks = top_hits_2019['tracks']['items']

# Initalize an empty list to hold ids of all tracks in the playlist
track_ids = []

# Initalize an empty list to hold popularity value of every track in 'track_ids'
track_popularity = []

# For loop to retrieve id and popularity of every track in list 'tracks', append it to lists 'track_ids'
# and 'track_popularity'
for i in range(len(tracks)):
    track_ids.append(tracks[i]['track']['id'])
    track_popularity.append(tracks[i]['track']['popularity'])

# Creates a list of the audio features for every track in 'track_ids'
audio_features = spotify.audio_features(track_ids)

# Creates pandas data frame with audio features, drops unnecessary columns
audio_df = pd.DataFrame(audio_features)
audio_df = audio_df.drop(['duration_ms', 'track_href', 'type', 'analysis_url', 'uri', 'id'], axis=1)

# Add track_popularity as a column in audio_df
audio_df['popularity'] = track_popularity

danceability = audio_df['danceability']
energy = audio_df['energy']
instrumentalness = audio_df['instrumentalness']
loudness = audio_df['loudness']
valence = audio_df['valence']
tempo = audio_df['tempo']
popularity = audio_df['popularity']

plt.scatter(danceability, popularity, label='Danceability', s=75, c='#00fa58')
plt.scatter(valence, popularity, label='Valence', s=75, c='#000000')
plt.scatter(energy, popularity, label='Energy', s=75, c='#00802d')

plt.title('Spotify Top Songs of 2019')
plt.xlabel('Audio Features')
plt.ylabel('Popularity')

plt.legend()
plt.style.use('grayscale')
plt.show()
