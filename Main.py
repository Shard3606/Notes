import tkinter
import customtkinter

# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("black")

# App Setup/Frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Notes")

# Adding UI Elements
title = customtkinter.CTkLabel(app, text = "Welcome to Notes")
title.pack()

# Running the App
app.mainloop(padx = 10, pady = 10)
