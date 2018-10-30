import urllib3
import json

def get_lyrics(artist, song_title):
    print(artist)
    print(song_title)
    def webSubSplit(split_string):
    	mergedSplit = ''
    	for substring in split_string:
    		if substring != split_string[-1]:
    			mergedSplit = mergedSplit + substring + '%20'
    		else:
    			mergedSplit = mergedSplit + substring
    	return mergedSplit


    artist = artist.lower()
    song_title = song_title.lower()

    artist = artist.split()
    song_title = song_title.split()

    # artist
    artist = webSubSplit(artist)
    song_title = webSubSplit(song_title)

    print(artist)
    print(song_title)

    http = urllib3.PoolManager()
    #response = http.request('GET', 'http://lyric-api.herokuapp.com/api/find/John%20Lennon/Imagine')
    response = http.request('GET', 'http://lyric-api.herokuapp.com/api/find/' + str(artist) +'/'+ str(song_title))

    test = ((response.data).decode('utf-8'))
    test_error = json.loads(test)
    if test_error['err'] == "not found":
    	return('!found')
    else:
	    wiki_lyric = response.data
	    wiki_lyric_utf8 = wiki_lyric.decode('utf-8')
	    d = json.loads(wiki_lyric_utf8)
	    return(d['lyric'])

get_lyrics('Håkan Hellström', 'En Midsommarnattsdröm')