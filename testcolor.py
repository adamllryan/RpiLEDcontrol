#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# colorPicker.py

from tkinter import *
import tkinter.colorchooser, tkinter.messagebox

win = Tk()
win.title(string = "Color Dialog")

# Open a color dialog box
def openColorDialog():
    # display color dialog box
    color = colorDialog.show()
    # show the chosen RBG value
    tkinter.messagebox.showinfo("Notice", "The color you chose is: " + color[1] + "n" + 
        "R = " + str(color[0][0]) + " G = " + str(color[0][1]) + " B = " + str(color[0][2]))
        
Button(win, text="Open color dialog box", command=openColorDialog).pack(side=LEFT)

# create a color dialog
colorDialog = tkinter.colorchooser.Chooser(win)

win.mainloop()