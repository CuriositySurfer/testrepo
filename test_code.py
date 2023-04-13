import tkinter as tk
from tkinter import ttk

def fun():
	print(label.configure())

root = tk.Tk()

label = ttk.Label(master = root, text = 'Hello')
label.pack()

print(label.configure())

root.mainloop()