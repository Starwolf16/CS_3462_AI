# Name:         Jonathan Tarrant
# Assignment:   01
# Section:      01
# Due Date:     09/16/2022

# Library imports
import tkinter as tk
from tkinter import ttk

# Create Root Window
root = tk.Tk() 

# Set Window Attributes
root.title("Assignment 1")
root.geometry("500x360")
root.resizable(width=True, height=True)
root.configure(bg="#3f3f3f")

# Config Grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.columnconfigure(4, weight=1)


frame00 = ttk.Frame(root, borderwidth=1, )
frame00.grid(column=0, row=0, padx=5, pady=5)
frame00['borderwidth'] = 5


# Call Mainloop
root.mainloop()