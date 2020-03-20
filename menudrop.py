import tkinter as tk
from tkinter import ttk 
from tkinter.messagebox import showinfo

win=tk.Tk()
win.title("dropdowm menu")

var=tk.StringVar(win)
var.set("fruits")
dropdown=tk.OptionMenu(win,var,"apple","bannana","pineapple")
dropdown.pack()
win.mainloop()