from ttkthemes import themed_tk as tk # Also imports the normal tk definitions, such as Button, Label, etc.
import tkinter.ttk as ttk # Imports the themed extensions for Tkinter

window = tk.ThemedTk()

window.get_themes()                 # Returns a list of all themes that can be set
window.set_theme("clearlooks")         # Sets an available theme

label = ttk.Label(window, text="This is a themed label")
label2 = ttk.Label(window, text="This is not a themed label")
button = ttk.Button(window, text="Themed exit button", command=window.destroy)
button2 = ttk.Button(window, text="This is not a themed exit button", command=window.destroy)


root = ttk.Tk()
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )

mylist = Listbox(root, yscrollcommand = scrollbar.set )
for line in range(100):
   mylist.insert(END, "This is line number " + str(line))

mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )


label.pack()
label2.pack()
button.pack()
button2.pack()



window.mainloop()