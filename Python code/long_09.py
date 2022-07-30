import string
from tkinter import*
from tkinter .ttk import*

from time import strftime

root = Tk()
root.title = ("clock")

def time():
    string = strftime(' %H:%M:%5 %p')
    