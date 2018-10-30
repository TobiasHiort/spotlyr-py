import tkinter as tk
from random import randint

_HEX = list('0123456789ABCDEF')
def random_color():
    return '#' + ''.join(_HEX[randint(0, len(_HEX)-1)] for _ in range(6))

def create_text(y, color, font_size, text):
	canvas.create_text(
		WIDTH/2,
		y,
		fill=color,
		font="Metropolis " + str(font_size),
		text=text,
		anchor='center',
		width = WIDTH,
		justify = tk.CENTER
	)

# const
WIDTH = 1024
HEIGHT = 768
TRANSCOLOUR = "#000000"
COLOR_GREEN_TEXT = "#1DB954"

# root
root = tk.Tk()
#root.overrideredirect(True) # important
#root.lift() #?
#root.wm_attributes("-topmost", True) # keep window always in front
root.wm_attributes("-transparentcolor", TRANSCOLOUR)
#root.attributes('alpha', 0.30)

vscrollbar = tk.Scrollbar(root)

# text canvas
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, highlightthickness = 0, background = "#FF0000", yscrollcommand=vscrollbar.set)
#canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, highlightthickness = 0, yscrollcommand=vscrollbar.set)
#canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill=TRANSCOLOUR, outline=TRANSCOLOUR)
canvas.pack(side="left", fill="both", expand=True)

# scrollbar conf
vscrollbar.config(command=canvas.yview)
vscrollbar.pack(side=tk.RIGHT, fill=tk.Y) 


text_example = "Test "
for i in range(20):
	create_text(50+50*i, random_color(), 35, text_example + str(i))


#frame = tk.Frame(canvas) #Create the frame which will hold the widgets
#Updated the window creation
#canvas.create_window(0, 0, window = frame)
#canvas.place(relx=0.5, rely=0.5)

#Added more content here to activate the scroll
#for i in range(100):
#    tk.Label(frame, text='Neil Young - ' + str(i), font=("Metropolis", 35), fg="red", bg="black").pack()

#Removed the frame packing
#f.pack()

#Updated the screen before calculating the scrollregion

canvas.update()
canvas.config(scrollregion = canvas.bbox("all")) #vvvvry important for scroll
root.update() #?

canvas.mainloop()
root.mainloop()