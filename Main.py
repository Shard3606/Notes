import tkinter

# System Settings
tkinter.set_appearance_mode("System")
tkinter.set_default_color_theme("black")

# App Setup/Frame
app = tkinter.tk()
app.geometry("720x480")
app.title("Notes")

# Adding UI Elements
title = tkinter.tkLabel(app, text = "Welcome to Notes")
title.pack()

# Running the App
app.mainloop(padx = 10, pady = 10)
