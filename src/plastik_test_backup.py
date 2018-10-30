#import tkinter as tk
#import tkinter.ttk as ttk

from tkinter import *
import tkinter.ttk as ttk

import os
import plastik_theme

root = Tk()
plastik_theme.install('plastik_img')



scrollbar = ttk.Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

"""
listbox = Listbox(root)
listbox.pack()

for i in range(100):
    listbox.insert(END, i)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
"""

mainloop()