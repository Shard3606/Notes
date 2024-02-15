import tkinter as tk

root = tk.Tk()

root.geometry("500x500")

root.title("Notes V2")

label = tk.Label(root, text="Welcome to your new notes!", font=('Arial', 18))
label.pack(padx=100, pady=100)

textbox = tk.Text(root, height=3, font=('Arial', 18))
textbox.pack(padx=100, pady=100)

button = tk.Button(root, text="Create Account", font=('Arial', 18))
button.place(x=100, y=200, height=100)

button = tk.Button(root, text="Sign In", font=('Arial', 18))
button.place(x=300, y=200, height=100)

root.mainloop()
