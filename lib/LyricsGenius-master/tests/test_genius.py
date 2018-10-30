import os
import unittest
#import lyricsgenius
import lyricsgenius as genius
from lyricsgenius.song import Song
from lyricsgenius.artist import Artist

# Import client access token from environment variable
#client_access_token = os.environ.get("GENIUS_CLIENT_ACCESS_TOKEN", None)
client_access_token = "dGA2Gf-7SjaEyJARHaHcQFBxPi0NP9gRfuBktGtjpwqzhyNoXRWApYZLEzVzqSBH"
assert client_access_token is not None, "Must declare environment variable: GENIUS_CLIENT_ACCESS_TOKEN"
#api = lyricsgenius.Genius(client_access_token, sleep_time=1)


api = genius.Genius('dGA2Gf-7SjaEyJARHaHcQFBxPi0NP9gRfuBktGtjpwqzhyNoXRWApYZLEzVzqSBH')
artist = api.search_artist('Andy Shauf', max_songs=3)

print(artist)

song = api.search_song('To You',artist.name)
print(song)