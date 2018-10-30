from tkinter import *

color_bg = "#181818"
color_text = "#B3B3B3"
color_green = "#1DB954"

def return_url(event):
    print(event.widget.get())

master = Tk()

master.overrideredirect(True) # important

canvas = Canvas(master, width = 0, height = 0, highlightthickness = 0) # width/height=0 is crazy right?

master.geometry('%dx%d+%d+%d' % (400, 24, 500, 1000))

master.wm_attributes("-topmost", 1) # keep entry always in front

entry_url = Entry(master,
				  font=('Verdana', 14, 'roman'),
				  bg=color_bg, # background color
				  fg=color_text, # text color
				  bd=0, # border width, 0
				  exportselection=False, # export selection to clipboard
				  justify=LEFT, # how to align the text inside the entry field
				  selectbackground=color_green, # selection background color
				  width=50, # width of chars
				  highlightthickness=0, # keep at 0, outer border coloring
				  insertbackground=color_green, # color used for the insertion cursor
				  insertborderwidth=2, # width of the insertion cursor’s border
				  insertofftime=200, # cursor blinking, ms
				  insertwidth=2 # width of the insertion cursor
				  #relief= #Border style. The default is SUNKEN. Other possible values are FLAT, RAISED, GROOVE, and RIDGE. (relief/Relief)
				  )
entry_url.pack(side = LEFT) # left within subwindow

entry_url.bind('<Return>', return_url)

master.mainloop()
