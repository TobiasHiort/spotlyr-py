#import tkinter as tk
import tkinter as tk
from tkinter.font import Font

from tkinter import *
from tkinter.ttk import *

import psutil
import os

#import re # strip_accents?
import unicodedata

import json
import urllib3

import pywintypes # WIEEEEEEEEEEERD
import win32gui # windows specific

#from win32 import win32gui
#import win32ui, win32con, win32api

import time
import random

# internal modules
import spotipy_utils
import external_fonts
import azlyrics
import wikilyrics

from PIL import ImageTk, Image, ImageGrab, ImageFilter

# constants
ICON_WIDTH = 15
ICON_HEIGHT = 11

# vars
window_coords = [] # remove????
is_foreground = False
screenshot_show = True # remove? test

# REMOVE
#test_str = "spotify:local:Flume+And+Chet"
#print(test_str[:13] == "spotify:local")

# fps vars
#fps = 144
fps = 60
time_delta = 1./fps

x = 0
y = 0
w = 0
h = 0

test_text = None
current_track = None
current_track_prev = None

# colors
color_bg = "#181818"
color_text = "#B3B3B3"
color_text2 = "#B3B3B3"
color_green = "#1DB954"

# change name
def click(event):
    canvas.create_image(7, 5, image = icon_active)
    #spotipy_utils.create_playlist()
    sp = spotipy_utils.getClient()
    
    #print(sp)

    #testtt = spotipy_utils.getPlaylists(sp)
    #print(testtt)

    #playlist_id_current, playlist_name = spotipy_utils.currentPlaylist(sp)
    #print("hej")


    #print(playlist_id_current)
    
    current_track_json = spotipy_utils.currentTrack(sp)
    current_artist = current_track_json["item"]["album"]["artists"][0]["name"]
    current_track = current_track_json['item']['name'] # track name

    lyrics_test = azlyrics.get_lyrics(current_artist, current_track)
    print(lyrics_test)

    f = open("lyrics_test.txt","a") #opens file with name of "test.txt"
    f.write(lyrics_test)
    f.close()

    # wikilyrics!!! remove, is below?
    http = urllib3.PoolManager()
    response = http.request('GET', 'http://lyric-api.herokuapp.com/api/find/John%20Lennon/Imagine')
    #data = json.load(urllib2.urlopen('http://lyric-api.herokuapp.com/api/find/John%20Lennon/Imagine'))
    response.status
    wiki_lyric = response.data
    wiki_lyric_utf8 = wiki_lyric.decode('utf-8')
    d = json.loads(wiki_lyric_utf8)
    #print(d['lyric'])

    #print(wiki_lyric_utf8)
    #print(wiki_lyric_utf8['lyric'])
    #print(str(wiki_lyric_utf8['lyric']).split())

    #print(str(wiki_lyric['lyric']).split())

    #print(data['lyric'])
    #print(str(data['lyric']).split())

    #print(current_track_json['item']['artists']['name'])
    #print(current_track_json['item']['artists']['name'])

    """
    #print(playlist_name) # IMPORTANT FOR PLAYLIST NAME TRACEBACK. wont work with for example symbol here.
    #print(playlist_name[:3] == "[⤮]") # IF ALREADY SHUFFLED PLAYLIST, check for doubles if not shuffled active


    # REMOVE
    spotipy_utils.getPlaylists(sp)



    playlist_copy = spotipy_utils.getPlaylistTracks(sp, playlist_id_current)


    # STOP SHUFFLE
    spotipy_utils.shuffle(sp, False)

    if playlist_name[:3] != "[⤮]":

        #playlist_copy = spotipy_utils.getPlaylistTracks(sp, playlist_id_current)

        playlist_id_new = spotipy_utils.createPlaylist(sp, playlist_name)

        spotipy_utils.addTracksPlaylist(sp, playlist_id_new, playlist_copy)

        # STOP SHUFFLE
        #spotipy_utils.shuffle(sp, False)

        # PLAY
        spotipy_utils.playPlaylist(sp, playlist_id_new)


    elif playlist_name[:3] == "[⤮]":
        spotipy_utils.removeTracks(sp, playlist_id_current, playlist_copy)

        spotipy_utils.addTracksPlaylist(sp, playlist_id_current, playlist_copy)

        # STOP SHUFFLE
        #spotipy_utils.shuffle(sp, False)

        # PLAY, does not work here, probably because same active playlist
        #spotipy_utils.playPlaylist(sp, playlist_id_current)

        #spotipy_utils.getPlaylists(sp)

        # use playlist_id_current...



    #print(spotipy_utils.userPlaylists(sp))



    #is_foreground = True
    """

def motion_hit(event):
    canvas.create_image(7, 5, image = icon_hover)

def motion_leave(event):
    canvas.create_image(7, 5, image = icon_blank)

def calc_pos(window_coords, x_padding, y_padding):
    x = window_coords[0] + round(window_coords[2]/2) - x_padding
    y = window_coords[3] + window_coords[1] - y_padding
    return x, y

# quit below if spotify is not running!
def callback(hwnd, extra):
    global is_foreground
    global window_coords
    global x
    global y
    global w
    global h


    #rect = win32gui.GetWindowRect(hwnd)
    #x = rect[0]
    #y = rect[1]
    #w = rect[2] - x
    #h = rect[3] - y
    #print(x)

    # remove? Look below. only getforegroundwindow???
    class_name = win32gui.GetClassName(hwnd)
    #print(class_name)

    #with open("test.txt", 'a') as out:
    #    out.write(class_name + '\n')

    foreground_window_hwnd = win32gui.GetForegroundWindow()

    #with open("test.txt", 'a') as out:
    #    out.write(str(foreground_window_hwnd) + '\n')

    if win32gui.IsWindow(foreground_window_hwnd):
        foreground_window_class = win32gui.GetClassName(foreground_window_hwnd)
        #print(foreground_window_class)
        #with open("test.txt", 'a') as out:
        #    out.write(foreground_window_class + '\n')

        #if foreground_window_class == "Chrome_WidgetWin_0" or foreground_window_class == "TkTopLevel":
        if foreground_window_class == "Chrome_WidgetWin_0" or foreground_window_class == "ConsoleWindowClass":
        #if foreground_window_class == "Chrome_WidgetWin_0":

            rect = win32gui.GetWindowRect(foreground_window_hwnd)
            x = rect[0]
            y = rect[1]
            w = rect[2] - x
            h = rect[3] - y
            #print(x,y,w,h)

            #print("hej")
            is_foreground = True

        else:
            is_foreground = False

    if class_name == "Chrome_WidgetWin_0":
        window_coords = [x, y, w, h]
        #print("---")
        #print(window_coords)
        #print("---")

# tk borderless window
root = tk.Tk()
root.overrideredirect(True) # important

canvas = tk.Canvas(root, width = ICON_WIDTH, height = ICON_HEIGHT, highlightthickness = 0) # width, height, does not affect visible here
canvas.grid(row = 0, column = 0) # ???

canvas.bind('<Motion>', motion_hit)
canvas.bind('<Leave>', motion_leave)
canvas.bind("<Button 1>", click) # prints for just shuffle button

icon_hover = tk.PhotoImage(file = os.path.join("icons", "icon_hover.png"))
icon_active = tk.PhotoImage(file = os.path.join("icons", "icon_active.png"))
icon_blank = tk.PhotoImage(file = os.path.join("icons", "icon_blank.png"))
canvas.create_image(7, 5, image = icon_blank) # important for first view, blank otherwise

root.wm_attributes("-topmost", 1) # keep icon always in front

font_bool = external_fonts.loadFont('Metropolis-Regular.otf', private=True, enumerable=False)
print(font_bool)
#print(font.families())

#--- texttest
master = Tk()
master.overrideredirect(True) # important
#master.attributes('-alpha', 0.3)

#???
#canvas2 = Canvas(master, width = 0, height = 0, highlightthickness = 0) # width/height=0 is crazy right?
master.geometry('%dx%d+%d+%d' % (800, 900, 400, 400))

master.wm_attributes("-topmost", 1) # always in front

#print(wikilyrics.get_lyrics("beyonce", "drunk in love"))

###


test_text = Text(master, wrap=WORD)
ScrollBar = Scrollbar(master)
ScrollBar.config(command=test_text.yview)
ScrollBar.pack(side=RIGHT, fill=Y)
test_text.config(yscrollcommand=ScrollBar.set)
test_text.pack(expand=YES, fill=BOTH)
test_text.configure(
    #font=("Proxima Nova Rg", 35, "bold"),
    font=("Metropolis", 35, "bold"),
    bg=color_bg, # background color
    fg=color_green # text color
    )

test_text.tag_config(
    'artist',
    #background = color_bg,
    #bgstipple = ?,
    #borderwidth = ?,
    #fgstipple = ?,
    #font = ("Proxima Nova Rg", 22, "normal"),
    font = ("Metropolis", 22, "normal"),
    foreground = color_text,
    #justify = ?,
    #lmargin1 = ?,
    #lmargin2 = ?,
    #offset = ?,
    #overstrike = ?,
    #relief = ?,
    #rmargin = ?,
    #spacing1 = ?,
    #spacing2 = ?,
    #spacing3 = ?,
    #tabs = ?,
    #underline = ?,
    #wrap = ?,
    )

test_text.tag_config(
    'artist_inline',
    #background = color_bg,
    #bgstipple = ?,
    #borderwidth = ?,
    #fgstipple = ?,
    #font = ("Proxima Nova Rg", 22, "bold"),
    font = ("Metropolis", 22, "bold"),
    foreground = color_text2,
    #justify = ?,
    #lmargin1 = ?,
    #lmargin2 = ?,
    #offset = ?,
    #overstrike = ?,
    #relief = ?,
    #rmargin = ?,
    #spacing1 = ?,
    #spacing2 = ?,
    #spacing3 = ?,
    #tabs = ?,
    #underline = ?,
    #wrap = ?,
    )

test_text.tag_config(
    'top_row',
    #background = color_bg,
    #bgstipple = ?,
    #borderwidth = ?,
    #fgstipple = ?,
    #font = ("Proxima Nova Rg", 50, "bold"),
    font = ("Metropolis", 50, "bold"),
    foreground = color_green,
    #justify = ?,
    #lmargin1 = ?,
    #lmargin2 = ?,
    #offset = ?,
    #overstrike = ?,
    #relief = ?,
    #rmargin = ?,
    #spacing1 = ?,
    #spacing2 = ?,
    #spacing3 = ?,
    #tabs = ?,
    #underline = ?,
    #wrap = ?,
    )

def addLyrics(lyrics):
    global test_text

    test_text.delete(1.0, END)

    lyrics_rows = lyrics.splitlines()
    lyrics_rows_flipped = lyrics_rows[::-1]

    #print(lyrics_rows_flipped)

    #for row in lyrics_rows:
    #    test_text.insert("1.0", row + '\n')
    #    test_text.tag_add("center", "1.0", "end")
    #    test_text.pack()
    

    

    # refactorrrrrrrrrr ifses and elses
    for row in lyrics_rows_flipped:
        #print(row)
        #print(row)https://open.spotify.com/user/spotifycharts/playlist/37i9dQZEVXbMDoHDwVN2tF
        #change to 4, include [ etcccc...
        if row[:3] == "<i>" and row[-4:] == "</i>":
            #print(row[4:-6])
            #test_text.configure(font=("Proxima Nova Rg", 35, "bold"),
            #        bg=color_bg, # background color
            #        fg="#B3B3B3") # text color
            #test_text.tag_configure("center", justify='center')
            test_text.insert("1.0", '[' + row[4:-5] + ']'+ '\n', 'artist')
            #test_text.tag_add("center", "1.0", "end")
            
        elif row[:5] == '(<i>[':
            #print("ÖPPPPPPÖ")
            inline_end = row.find(':]</i>')
            #print(row[5:inline_end])
            #test_text.insert("1.0", '(', 'artist')
            #test_text.insert("1.0", '(        ', 'artist')
            
            test_text.insert("1.0", '[' + row[5:inline_end] + ']:' + row[inline_end + 6:] + '\n', 'artist_inline')
            #test_text.insert("1.0", ')\n')
            #test_text.insert("1.0", row[inline_end:] + ']:')
        
        #for inline artist highlist, see no brainer justin beiber dj khaled
        #elif row[:3] == "(<i>" and row[-4:] == "</i>":
        #    test_text.tag_configure("center", justify='center')
        #    test_text.insert("1.0", row[4:-6] + '\n', 'artist_inline')
        #    test_text.tag_add("center", "1.0", "end")
        else:
            test_text.tag_configure("center", justify='center')
            test_text.insert("1.0", row + '\n')
            #test_text.tag_add("center", "1.0", "end")
    
    # top row. FIX FOR PRIVATE MODE, should not be visible then
    test_text.insert("1.0", 'Hej - Hej\n', 'top_row')
    test_text.tag_add("center", "1.0", "end")
    #test_text.pack() ??????????????

    #return test_text
    lyrics_once = False


def getLyrics(artist, track):
    print(artist)
    print(track)

    lyrics_az = azlyrics.get_lyrics(artist, track)
    if lyrics_az != '!found':
        print("az working!")
        return lyrics_az
    
    else:
        print('az fail, doing wiki...')
        lyrics_wiki = wikilyrics.get_lyrics(artist, track)
        if lyrics_wiki != '!found':
            print("wiki success!")
            #print(lyrics_wiki)
            return lyrics_wiki
        else:
            print("az and wiki fail :(")
            return "az and wiki fail :("
           
# go for num 1, wiki kinda sucks 
def getLyrics2(artist, track):
        lyrics_wiki = wikilyrics.get_lyrics(artist, track)
        
        if lyrics_wiki != '!found':
            print("wiki working!")
            return lyrics_wiki
        
        else:
            print('az fail, doing wiki...')
            lyrics_az = azlyrics.get_lyrics(artist, track)
            #lyrics_wiki = wikilyrics.get_lyrics(artist, track)
            if lyrics_az != '!found':
                print("az success!")
                #print(lyrics_wiki)
                return lyrics_az
            else:
                print("az and wiki fail :(")
                return "az and wiki fail :("

def strip_accents(text):
    """
    Strip accents from input String.

    :param text: The input string.
    :type text: String.

    :returns: The processed String.
    :rtype: String.
    """
    try:
        text = unicode(text, 'utf-8')
    except (TypeError, NameError): # unicode is a default on python 3 
        pass
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore')
    text = text.decode("utf-8")
    return str(text)

def replace_special_chars_in_string(string):
    def replace_special_chars(char):
        desc = unicodedata.name(str(char))
        cutoff = desc.find(' WITH ')
        if cutoff != -1:
            desc = desc[:cutoff]
        return unicodedata.lookup(desc)

    string_tmp = ""

    for char in range(len(string)):
        string_tmp += replace_special_chars(string[char])
    return string_tmp

#master.mainloop()



#master.mainloop()




#text = Text(master, height=0, font="Helvetica 12")
#text.tag_configure("bold", font="Helvetica 12 bold")
#text.insert(END, "Hello, ") 
#text.insert("end", "world", "bold") 
#text.configure(state="disabled")


#myFont = Font(family="Airbornebgbgbgb", size=42)
#test_text.configure(font=myFont)
#myFont = Font(family="Arial", size=24)
#text = Text(master, height=0, font="Proxima Nova Rg 52")
#test_text.insert(INSERT, "1234567890!\n")
#test_text.insert(END, "This is a phrase.\n")
#test_text.insert(END, "Bye bye...")
#test_text.pack(expand=1, fill=BOTH)
#test_text.configure(state='disabled')
#test_text.configure(font=myFont)


"""
#MOVE
color_bg = "#181818"
color_text = "#B3B3B3"
color_green = "#1DB954"

entry_url = Entry(master,
                  font=('Proxima Nova Rg', 34, 'bold'),
                  #bg=color_bg, # background color
                  #fg=color_green, # text color
                  #bd=0, # border width, 0
                  exportselection=False, # export selection to clipboard
                  justify=LEFT, # how to align the text inside the entry field
                  #selectbackground=color_green, # selection background color
                  width=24, # width of chars
                  #highlightthickness=0, # keep at 0, outer border coloring
                  #insertbackground=color_green, # color used for the insertion cursor
                  #insertborderwidth=2, # width of the insertion cursor’s border
                  #insertofftime=200, # cursor blinking, ms
                  #insertwidth=2 # width of the insertion cursor
                  #relief= #Border style. The default is SUNKEN. Other possible values are FLAT, RAISED, GROOVE, and RIDGE. (relief/Relief)
                  )
entry_url.pack(side = LEFT) # left within subwindow
entry_url.insert(INSERT, "Neil Young - \n")
entry_url.insert(END, "This is a phrase.\n")
entry_url.config(state='readonly')
"""

#master.mainloop()

#test_text.tag_add("start", "1.0", "5.0")
#test_text.tag_config("start", background="black", foreground="green")
#/-- texttest


# shuffling, REMOVE
#list_tmp = [1, 2, 3, 4, 5, 6]
#list_tmp_shuffled = random.sample(list_tmp, k=len(list_tmp))

# only certain updatable elements, clean!


### should be outside!!! But what if change account?
sp = spotipy_utils.getClient()
# gui loop
while True:

    is_foreground = False

    win32gui.EnumWindows(callback, None) # must be here!

    #print(is_foreground)
    

    #"""
    if is_foreground:
        #new
        if screenshot_show:
            screenshot = ImageGrab.grab((x, y, x + w, y + h))
            screenshot = screenshot.filter(ImageFilter.GaussianBlur(radius=25))
            screenshot = screenshot.convert("RGBA")

            exit_rect = Image.new("RGBA", (135, 31), (255, 255, 255, 0))
            screenshot.paste(exit_rect, (w - 135, 0))
            screenshot.save(os.path.join("tmp", "background_gauss.png"))

            #screenshot.show()

            screenshot_show = False
        #print(window_coords)
        if window_coords[0] == -8 and window_coords[1] == -8: # fullscreen
            x_pos, y_pos = calc_pos(window_coords, 156, 64)
            root.geometry('%dx%d+%d+%d' % (ICON_WIDTH, ICON_HEIGHT, x_pos, y_pos))
        elif window_coords[3] <= 823: # small
            x_pos, y_pos = calc_pos(window_coords, 156, 50)
            root.geometry('%dx%d+%d+%d' % (ICON_WIDTH, ICON_HEIGHT, x_pos, y_pos))
        elif window_coords[3] > 823: # large
            x_pos, y_pos = calc_pos(window_coords, 156, 56)
            root.geometry('%dx%d+%d+%d' % (ICON_WIDTH, ICON_HEIGHT, x_pos, y_pos))
        else:
            raise ValueError("invalid window_coords")
    elif not is_foreground:
        root.geometry('%dx%d+%d+%d' % (ICON_WIDTH, ICON_HEIGHT, -ICON_WIDTH, -ICON_HEIGHT))
    #"""
    

    #window_coords = [] # must be here!

    ###
    
    #current_track_json = None
    current_track_json = spotipy_utils.currentTrack(sp)

    # also maybe fix nonplaying here?
    if current_track_json == None:
        #print("dont use privatez")
        addLyrics("Dont use privatez")
    else:
        current_artist = replace_special_chars_in_string(current_track_json["item"]["album"]["artists"][0]["name"])
        current_track = replace_special_chars_in_string(current_track_json['item']['name']) # track name

    #print(current_track)
    #print(current_track_prev)
    #if current_track != None and current_track != current_track_prev: # track id instead, see above
    

    if current_track != current_track_prev: # track id instead, see above
        print("update")
        
        lyrics = getLyrics(current_artist, current_track)

        addLyrics(lyrics)
        current_track_prev = current_track
        ###
    

    #root.mainloop() #warning
    root.update_idletasks() # maybe not needed? seems to be faster with this
    root.update()

    # fps limit for performace
    #t0 = time.clock()
    time.sleep(time_delta) # true fps
    #t1 = time.clock()
