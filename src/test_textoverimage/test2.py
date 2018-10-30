import tkinter
from PIL import Image, ImageDraw, ImageTk, ImageFont # only image, imagetk

# open a SPIDER image and convert to byte format    
im = Image.open('img.png')

root = tkinter.Tk()  # A root window for displaying objects

# Convert the Image object into a TkPhoto object
tkimage = ImageTk.PhotoImage(im)

tkinter.Label(root, image=tkimage, text="Update User\nhej", compound=tkinter.CENTER).pack() # Put it in the display window
#tkinter.Label(root, image=tkimage, text="Update User\nhej", compound=tkinter.CENTER).pack()

root.mainloop() # Start the GUI