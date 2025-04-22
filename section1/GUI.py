# Importing GUI libraries
import tkinter as tk

# Window initializing
root = tk.Tk()
root.title("Differentiation")

# GUI settings
root.geometry("500x500")
root.iconbitmap("img/derivative.ico")

# Label for the calculus
label_introduction = tk.Label(root, text = "You can calculate derivative of a function here!")
label_introduction.pack(pady = 10)

# GUI's Main loop
root.mainloop()