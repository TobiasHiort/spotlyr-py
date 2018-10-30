# creates a playlist for a user

import pprint
import sys
import os
import subprocess
import math
import random

sys.path.append('../lib')
import spotipy
from spotipy import util

username = "taebmataz"
# SORT:
scope = "user-read-playback-state user-read-currently-playing playlist-modify-private user-modify-playback-state playlist-read-private"
client_id = "80c0eef01f1c417bbee21dfd3fe4e97d"
client_secret = "c92910e835774b42886ab782fc419718"
redirect_uri = "http://localhost/"

def getClient():
    token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
    if token:
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        return sp
    else:
        raise ValueError("Can't get token for", username)

# NOT NEEDED?
#def getIdFromURI(uri):
#    #return uri[-22:]
#    return uri

def currentTrack(sp):
    return sp.current_user_playing_track()
    #return sp.current_user()

def currentPlaylist(sp):
    #sp = spotipy.Spotify(auth=token)
    #sp.trace = False
    
    current_track = sp.current_user_playing_track()
    #print(current_track["item"])
    #print(current_track["item"]["name"]) # song name
    #print(current_track["item"]["album"]["name"]) # song name, compare above
    #print(current_track["item"]["album"]["artists"][0]["name"]) # artist name!!!
    #print(current_track["item"]["album"]["name"]) # album name!!!
    #print(current_track["item"]["popularity"]) # track popularity!!!
    
    #playlist_url = current_track["context"]["uri"] # playlist id!!!


    print(current_track)
    #print(current_track)
    #print(username)

    
    #playlist_object = sp.user_playlist(username, getIdFromURI(current_track["context"]["uri"]))
    playlist_object = sp.user_playlist(username, current_track["context"]["uri"])

    #return getIdFromURI(current_track["context"]["uri"]), playlist_object["name"] # return playlist_id, playlist_name
    return current_track["context"]["uri"], playlist_object["name"]

def createPlaylist(sp, playlist_name):
    #playlist_name_org = "hej"
    playlist_name_new = "[⤮] " + playlist_name

    #sp = spotipy.Spotify(auth=token)
    #sp.trace = False
    
    #playlists = sp.user_playlist_create(username, playlist_name_new, public=False) # remove left hand side?
    playlist_new = sp.user_playlist_create(username, playlist_name_new, public=False)
    
    print("createPlaylist() success")

    return playlist_new["id"]
    #pprint.pprint(playlists)


def addTracksPlaylist(sp, playlist_id, track_ids):


    with open("track_ids_tmp.txt", 'a') as out:
        out.write(str(track_ids))


    ################ insert/start
        # total tracks

    #playlist_iter, playlist_rem = getHundreds(playlist_tracks_tmp["total"])
    playlist_iter, playlist_rem = getHundreds(len(track_ids))
    print(playlist_iter)
    print(playlist_rem)

    # SHUFFLE
    random.shuffle(track_ids)

    track_limit = 100
    for idx in range(playlist_iter):
        #new_playlist_tracks = sp.user_playlist_tracks(username, playlist_id, limit=track_limit, offset=idx * track_limit)
    
        #for track in range(track_limit):
        #    #tracks_copy.append(getIdFromURI(playlist_tracks["items"][track]["track"]["uri"]))
        
        print(range(playlist_iter))
        print(idx)
        
        sp.user_playlist_add_tracks(username, playlist_id, track_ids[idx * 100:idx * 100 + track_limit])
        #print(len(track_ids[idx*100:idx*100+track_limit]))
    
    
    
    #tracks_copy.append(getIdFromURI(playlist_tracks["items"][track]["track"]["uri"]))
    
    print(len(track_ids[playlist_iter * 100:]))

    #print(track_ids[playlist_iter:])

    #print(track_ids)
    
    sp.user_playlist_add_tracks(username, playlist_id, track_ids[playlist_iter * track_limit:])
    #sp.user_playlist_add_tracks(username, playlist_id, track_ids[playlist_iter:])


    ######### insert/end



    #sp.user_playlist_add_tracks(username, playlist_id, track_ids)

    print("addTracksPlaylist() success")


def getHundreds(total_tracks):
    if total_tracks <= 0 or not isinstance(total_tracks, int):
        raise ValueError("only integers > 0")
    elif total_tracks > 0 and total_tracks <= 100:
        return 0, total_tracks
    else:
        return math.floor(total_tracks / 100), total_tracks % 100

# REMOVE?
# tempory
#def listDuplicates(seq):
#  seen = set()
#  seen_add = seen.add
#  # adds all elements it doesn't know yet to seen and all other to seen_twice
#  seen_twice = set( x for x in seq if x in seen or seen_add(x) )
#  # turn the set into a list (as requested)
#  return list( seen_twice )

def getPlaylistTracks(sp, playlist_id):
    # all track details in playlist
    
    def getTrackURI(playlist_tracks):
        #return getIdFromURI(playlist_tracks["items"][track]["track"]["uri"])
        return playlist_tracks["items"][track]["track"]["uri"]

    tracks_copy = []

    playlist_tracks_tmp = sp.user_playlist_tracks(username, playlist_id, limit = 1, offset = 0) # just for total tracks
    #playlist_tracks = sp.user_playlist_tracks(username, playlist_id, limit=100, offset=0, market=None)
    
    # total tracks
    playlist_iter, playlist_rem = getHundreds(playlist_tracks_tmp["total"])


    track_limit = 100
    for idx in range(playlist_iter):
        playlist_tracks = sp.user_playlist_tracks(username, playlist_id, limit=track_limit, offset=idx * track_limit)

        for track in range(track_limit):
            tracks_copy.append(getTrackURI(playlist_tracks))

    playlist_tracks = sp.user_playlist_tracks(username, playlist_id, limit = track_limit, offset = playlist_iter * track_limit)
    for track in range(playlist_rem):
        tracks_copy.append(getTrackURI(playlist_tracks))

    #print(playlist_iter)
    #print(playlist_rem)

    #print(len(tracks_copy))

    prefix = "spotify:local" # move to ~constants
    newlist = [x for x in tracks_copy if not x.startswith(prefix)]
    #print("newlist len: " + str(len(newlist)))

    #with open("track_ids_tmp2.txt", 'a') as out:
    #    out.write(str(newlist))


    print("getPlaylistTracks() success")

    #return tracks_copy
    return newlist


#def userPlaylists(sp):
#    #sp.current_user_playlists(sp, limit=50, offset=0)
#    sp.current_user_playlists(sp)

#def user_playlist_remove_all_occurrences_of_tracks(self, user, playlist_id, tracks, snapshot_id=None)
def removeTracks(sp, playlist_id, tracks):
    playlist_iter, playlist_rem = getHundreds(len(tracks))

    #print(playlist_iter)

    track_limit = 100 # move globally upwards...
    
    for idx in range(playlist_iter):
        sp.user_playlist_remove_all_occurrences_of_tracks(username, playlist_id, tracks[idx * track_limit:idx * track_limit + track_limit])
        #print(str(idx * track_limit) + "-----"  + str(idx * track_limit + track_limit))

    #print(len(tracks[playlist_iter*100:]))
    

    sp.user_playlist_remove_all_occurrences_of_tracks(username, playlist_id, tracks[playlist_iter * track_limit:]) # WORKS < 100!!!!


    #for idx in range(playlist_iter):
    #    playlist_tracks = sp.user_playlist_tracks(username, playlist_id, limit=track_limit, offset=idx * track_limit)
    #
    #    for track in range(track_limit):
    #        tracks_copy.append(getTrackURI(playlist_tracks))

    
    #playlist_tracks = sp.user_playlist_tracks(username, playlist_id, limit = track_limit, offset = playlist_iter * track_limit)
    #for track in range(playlist_rem):
    #    tracks_copy.append(getTrackURI(playlist_tracks))



    #sp.user_playlist_remove_all_occurrences_of_tracks(username, playlist_id, tracks)



# shady shit... view gui_xx.py
def getPlaylists(sp):

    user_playlists = sp.user_playlists(username, limit = 50, offset = 0)
    #print(user_playlists["items"][0]["name"])

    print(user_playlists["total"])

    
    playlists_iter, playlists_rem = getHundreds(user_playlists["total"])
    print("playlists 100s: " + str(playlists_iter) + " | playlists_rem: " + str(playlists_rem))


def shuffle(sp, state):
    sp.shuffle(state)

def playPlaylist(sp, playlist):
    #sp.start_playback(device_id = None, context_uri = None, uris = None, offset = None)
    #print("spotify:playlist:" + playlist)
    sp.start_playback(context_uri = "spotify:user:" + username + ":playlist:" + playlist)