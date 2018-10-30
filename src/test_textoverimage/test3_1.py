import tkinter as tk
from random import randint
import azlyrics
from PIL import ImageTk, Image

lyrics = azlyrics.get_lyrics("Neil Young", "Heart of gold")
lyrics_rows = lyrics.splitlines()
lyrics_rows_flipped = lyrics_rows[::-1]

print(lyrics_rows_flipped)

#_HEX = list('0123456789ABCDEF')
#def random_color():
#    return '#' + ''.join(_HEX[randint(0, len(_HEX)-1)] for _ in range(6))

def create_text(y, color, font_size, text_row):
	canvas.create_text(
		WIDTH/2,
		y,
		fill=color,
		font="Metropolis " + str(font_size),
		#font="Arial " + str(font_size),
		text=text_row,
		anchor='center',
		width = WIDTH,
		justify = tk.CENTER
	)

# const
WIDTH = 1149
HEIGHT = 1131
#TRANSCOLOUR = "#666666"
TRANSCOLOUR = "#555555"
COLOR_GREEN_TEXT = "#1DB954"
PADDING = 50
FONT_SIZE = 18
ROW_DIST = 45

# root
root = tk.Tk()
#root2 = tk.Tk()
#root.overrideredirect(True)
#root.lift() #?
#root.wm_attributes("-topmost", True)
root.wm_attributes("-transparentcolor", TRANSCOLOUR)

vscrollbar = tk.Scrollbar(root)



#background_gauss = ImageTk.PhotoImage(Image.open("background_gauss.png"))
#panel = tk.Label(root, image = background_gauss)
#panel.pack(side = "top", fill = "both", expand = "yes")



# text canvas
#canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, highlightthickness = 0, background = "#FF0000", yscrollcommand=vscrollbar.set)
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, highlightthickness = 0, yscrollcommand=vscrollbar.set)
#canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.create_rectangle(0, 0, WIDTH, PADDING+ROW_DIST*len(lyrics_rows_flipped), fill=TRANSCOLOUR, outline=TRANSCOLOUR)
canvas.pack(side="left", fill="both", expand=True)

# scrollwheel

# scrollbar conf
vscrollbar.config(command=canvas.yview)
vscrollbar.pack(side=tk.RIGHT, fill=tk.Y) 

# text example
text_example = "Test "
for i in range(len(lyrics_rows_flipped)):
	create_text(PADDING+ROW_DIST*i, COLOR_GREEN_TEXT, 30, lyrics_rows_flipped[i])

# updates and mainloops
#canvas2.update()
canvas.config(scrollregion = canvas.bbox("all"))
#canvas2.config(scrollregion = canvas.bbox("all"))
#root.update() #?

#canvas2.mainloop()
root.mainloop()
#root2.mainloop()