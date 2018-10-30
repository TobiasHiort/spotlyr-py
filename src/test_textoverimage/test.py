import io
import base64

from tkinter import Tk, Label, Entry, Toplevel, Canvas

from PIL import Image, ImageDraw, ImageTk, ImageFont


root = Tk()

#image_file = io.BytesIO(base64.b64decode(BASE64_BACKGROUND))
image = Image.open('img.png')

width, height = image.size

# I disallow window to resizing and I make the size of the window the same than the size of the background image
root.resizable(width=False, height=False)
root.geometry("%sx%s"%(width, height))

draw = ImageDraw.Draw(image)

text_x = 55
text_y = 45

text = "Neil Young - Heart of Gold\nNeil Young - Heart of Gold\nNeil Young - Heart of Gold"

# Use here a nice ttf font
font = ImageFont.truetype("Metropolis-Regular.otf", 35)
#width_text, height_text = font.getsize(text)
draw.text((text_x, text_y), text, fill="white", font=font)

#width_text, height_text = draw.textsize(text)

photoimage = ImageTk.PhotoImage(image)
Label(root, image=photoimage).place(x=-2,y=-2)

root.mainloop()