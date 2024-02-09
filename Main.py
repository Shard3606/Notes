import tkinter as tk

root = tk.Tk()

# System Settings


# App Setup/Frame
root.geometry("720x480")
root.title("Notes App")

# Adding UI Elements
label = tk.Label(root, text="Welcome to Notes!", font=('Times New Roman', 18))
label.pack()

# Running the App
root.mainloop()
