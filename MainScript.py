import tkinter as tk
import time
import tkinter.colorchooser
import os
from datetime import datetime
import numpy as np
r = 17
g = 22
b = 24
enabled = True
f_speed = 10
gmax = 255
global fade
fade = False
mode = False
sto = [[255,0,0], [0,255,0], [0,0,255], [255,100,50], [255,0,130], [165,0,190], [255,150,255], [0,255,255], [255,60,0], [255,255,255], [0,0,0]]
#Main Window
root = tk.Tk()
root.geometry('435x300')
root.resizable(width=False, height=False)
#Container Main
coFr = tk.Frame(root, background = 'gray', highlightbackground='black', highlightthickness=1)
timerFrame = tk.Frame(root, background = 'gray', highlightbackground='black', highlightthickness=1)
presFr = tk.Frame(root, background = 'gray', highlightbackground='black', highlightthickness=1)
preFr = tk.Frame(root, background = 'gray', highlightbackground='black', highlightthickness=1)
coFr.grid(row=0,column=0)
timerFrame.grid(row=0,column=1)
presFr.grid(row=1, column=1)
preFr.grid(row=1,column=0)

#Color Editor
redFrame = tk.Frame(coFr, background = 'red')
greenFrame = tk.Frame(coFr, background = 'green')
blueFrame = tk.Frame(coFr, background = 'blue')
slr1 = tk.Frame(coFr, background = 'red')
slr2 = tk.Frame(coFr, background = 'green')
slr3 = tk.Frame(coFr, background = 'blue')
#CE Labels
redLbl= tk.Label(redFrame, text="Red", background='red')
blueLbl = tk.Label(greenFrame, text="Green", background='green')
greenLbl= tk.Label(blueFrame , text="Blue", background='blue')
#Draw Frames
redFrame.grid(row=0,column=0, padx=14, pady=10)
greenFrame.grid(row=0,column=1, padx=10, pady=10)
blueFrame.grid(row=0,column=2, padx=15, pady=10)
slr1.grid(row=1,column=0, padx=5, pady=5)
slr2.grid(row=1,column=1, padx=5, pady=5)
slr3.grid(row=1,column=2, padx=5, pady=5)

#Sliders
slider_r = tk.Scale(slr1, from_=0, to=255, background='red')
slider_g = tk.Scale(slr2, from_=0, to=255, background='green')
slider_b = tk.Scale(slr3, from_=0, to=255, background='blue')
slider_r.grid()
slider_g.grid()
slider_b.grid()
slider_r.set(255)
slider_g.set(100)
slider_b.set(50)
#draw labels
redLbl.grid()
blueLbl.grid()
greenLbl.grid()

#Timer Editor
sunBox = tk.Frame(timerFrame, background = 'gray')
monBox = tk.Frame(timerFrame, background = 'gray')
tueBox = tk.Frame(timerFrame, background = 'gray')
wedBox = tk.Frame(timerFrame, background = 'gray')
thuBox = tk.Frame(timerFrame, background = 'gray')
friBox = tk.Frame(timerFrame, background = 'gray')
satBox = tk.Frame(timerFrame, background = 'gray')

sunBox.grid(row = 0)
monBox.grid(row = 0)
tueBox.grid()
wedBox.grid()
thuBox.grid()
friBox.grid()
satBox.grid()

sunLbl = tk.Label(sunBox, text = "Sunday", background = 'light blue')
monLbl = tk.Label(sunBox, text = "Monday", background = 'light blue')
tueLbl = tk.Label(sunBox, text = "Tuesday", background = 'light blue')
wedLbl = tk.Label(sunBox, text = "Wednesday", background = 'light blue')
thuLbl = tk.Label(sunBox, text = "Thursday", background = 'light blue')
friLbl = tk.Label(sunBox, text = "Friday", background = 'light blue')
satLbl = tk.Label(sunBox, text = "Saturday", background = 'light blue')

sunLbl.grid()
monLbl.grid()
tueLbl.grid()
wedLbl.grid()
thuLbl.grid()
friLbl.grid()
satLbl.grid()

#Preset Editor
p1 = tk.Frame(presFr, background = 'white')
p2 = tk.Frame(presFr, background = 'white')
p3 = tk.Frame(presFr, background = 'white')
p4 = tk.Frame(presFr, background = 'white')
p5 = tk.Frame(presFr, background = 'white')
p6 = tk.Frame(presFr, background = 'white')
p7 = tk.Frame(presFr, background = 'white')
p8 = tk.Frame(presFr, background = 'white')
p9 = tk.Frame(presFr, background = 'white')
p10 = tk.Frame(presFr, background = 'white')
p11 = tk.Frame(presFr, background = 'white')
p12 = tk.Frame(presFr, background = 'white')
p1.grid(column = 0, row = 0, padx = 5, pady = 5)
p2.grid(column = 1, row = 0, padx = 5, pady = 5)
p3.grid(column = 2, row = 0, padx = 5, pady = 5)
p4.grid(column = 0, row = 1, padx = 5, pady = 5)
p5.grid(column = 1, row = 1, padx = 5, pady = 5)
p6.grid(column = 2, row = 1, padx = 5, pady = 5)
p7.grid(column = 0, row = 2, padx = 5, pady = 5)
p8.grid(column = 1, row = 2, padx = 5, pady = 5)
p9.grid(column = 2, row = 2, padx = 5, pady = 5)
p10.grid(column = 3, row = 0, padx = 5, pady = 5)
p11.grid(column = 3, row = 1, padx = 5, pady = 5)
p12.grid(column = 3, row = 2, padx = 5, pady = 5)
print(f'#{sto[0][0]:02x}{sto[0][1]:02x}{sto[0][2]:02x}')
print(sto[0])
def animation():
    rcmd =slider_r.get()
    gcmd =slider_g.get()
    bcmd =slider_b.get()
    heks = str(f'#{rcmd:02x}{gcmd:02x}{bcmd:02x}')
    coFr.config(bg=heks)
    os.system( 'pigs p 17 ' + str(rcmd))
    os.system( 'pigs p 22 ' + str(gcmd))
    os.system( 'pigs p 24 ' + str(bcmd))
    root.update()
def fadeTo(r2, g2, b2):
    r1 =slider_r.get()
    g1 =slider_g.get()
    b1 =slider_b.get()
    while r1 != r2 or g1 != g2 or b1 != b2:
        f_speed = 100 / slider_s.get()
        animation()
        r1 =slider_r.get()
        g1 =slider_g.get()
        b1 =slider_b.get()
        if g1 > gmax:
            g1 = gmax
        if r1 > r2:
            slider_r.set(np.clip(np.floor(r1 - (r1 - r2) / f_speed),r2,255))
        elif r1 < r2:
            slider_r.set(np.clip(np.ceil(r1 + (r2 - r1) / f_speed + 1),0,r2))
        if g1 > g2:
            slider_g.set(np.clip(np.floor(g1 - (g1 - g2) / f_speed),g2,188))
        elif g1 < g2:
            slider_g.set(np.clip(np.ceil(g1 + (g2 - g1) / f_speed + 1),0,g2))
        if b1 > b2:
            slider_b.set(np.clip(np.floor(b1 - (b1 - b2) / f_speed),b2,255))
        elif b1 < b2:
            slider_b.set(np.clip(np.ceil(b1 + (b2 - b1) / f_speed + 1),0,b2))
        
def chgclr(bruh):
    fadeTo(sto[bruh][0],sto[bruh][1],sto[bruh][2])
    global fade 
    fade = False
def toggle():
    global fade
    fade = True
    global mode
    mode = not mode
def chgmd(i):
    global mode
    mode = i
b1 = tk.Button(p1, width = 2, height = 1, bg = f'#{sto[0][0]:02x}{sto[0][1]:02x}{sto[0][2]:02x}', bd = 5, relief = 'ridge', command=lambda:chgclr(0))
b1.grid()
b2 = tk.Button(p2, width = 2, height = 1, bg = f'#{sto[1][0]:02x}{sto[1][1]:02x}{sto[1][2]:02x}', bd = 5, relief = 'ridge', command=lambda:chgclr(1))
b2.grid()
b3 = tk.Button(p3, width = 2, height = 1, bg = f'#{sto[2][0]:02x}{sto[2][1]:02x}{sto[2][2]:02x}', bd = 5, relief = 'ridge', command=lambda:chgclr(2))
b3.grid()
b4 = tk.Button(p4, width = 2, height = 1, bg = f'#{sto[3][0]:02x}{sto[3][1]:02x}{sto[3][2]:02x}', bd = 5, relief = 'ridge', command=lambda:chgclr(3))
b4.grid()
b5 = tk.Button(p5, width = 2, height = 1, bg = f'#{sto[4][0]:02x}{sto[4][1]:02x}{sto[4][2]:02x}', bd = 5, relief = 'ridge', command=lambda:chgclr(4))
b5.grid()
b6 = tk.Button(p6, width = 2, height = 1, bg = f'#{sto[5][0]:02x}{sto[5][1]:02x}{sto[5][2]:02x}', bd = 5, relief = 'ridge', command=lambda:chgclr(5))
b6.grid()
b7 = tk.Button(p7, width = 2, height = 1, bg = f'#{sto[6][0]:02x}{sto[6][1]:02x}{sto[6][2]:02x}', bd = 5, relief = 'ridge', command=lambda:chgclr(6))
b7.grid()
b8 = tk.Button(p8, width = 2, height = 1, bg = f'#{sto[7][0]:02x}{sto[7][1]:02x}{sto[7][2]:02x}', bd = 5, relief = 'ridge', command=lambda:chgclr(7))
b8.grid()
b9 = tk.Button(p9, width = 2, height = 1, bg = f'#{sto[8][0]:02x}{sto[8][1]:02x}{sto[8][2]:02x}', bd = 5, relief = 'ridge', command=lambda:chgclr(8))
b9.grid()
toggleon = tk.Button(p10, width = 2, height = 1, bg = 'gray', bd = 5, relief = 'ridge', command=lambda:chgclr(9))
toggleon.grid()
toggleoff = tk.Button(p11, width = 2, height = 1, bg = 'black', bd = 5, relief = 'ridge', command=lambda:chgclr(10))
toggleoff.grid()
b10 = tk.Button(p12, width = 2, height = 1, bg = f'#{sto[8][0]:02x}{sto[8][1]:02x}{sto[8][2]:02x}', bd = 5, relief = 'ridge', command=lambda:toggle())
b10.grid()

#Setting Frame
mode1f = tk.Frame(preFr, background = 'red')
mode2f = tk.Frame(preFr, background = 'green')
mode3f = tk.Frame(preFr, background = 'blue')
mode4f = tk.Frame(preFr, background = 'red')
mode5f = tk.Frame(preFr, background = 'green')
mode6f = tk.Frame(preFr, background = 'blue')

slide1f = tk.Frame(preFr, background = 'gray')
slide1f.grid(row=0,column=0, padx=5, pady=5, rowspan=3)
slideL = tk.Label(slide1f, text = 'Speed')
mode1f.grid(row=0,column=1, padx=5, pady=5)
mode2f.grid(row=0,column=2, padx=5, pady=5)
mode3f.grid(row=1,column=1, padx=5, pady=5)
mode4f.grid(row=1,column=2, padx=5, pady=5)
mode5f.grid(row=2,column=1, padx=5, pady=5)
mode6f.grid(row=2,column=2, padx=5, pady=5)
slider_s = tk.Scale(slide1f, from_=1, to=100, background='red')
mode_1 = tk.Button(mode1f, width = 2, height = 1, bg = f'#{sto[0][0]:02x}{sto[0][1]:02x}{sto[0][2]:02x}', bd = 5, relief = 'ridge', command=lambda:chgmd(0))
mode_2 = tk.Button(mode2f, width = 2, height = 1, bg = f'#{sto[0][0]:02x}{sto[0][1]:02x}{sto[0][2]:02x}', bd = 5, relief = 'ridge', command=lambda:chgmd(1))
mode_3 = tk.Button(mode3f, width = 2, height = 1, bg = f'#{sto[0][0]:02x}{sto[0][1]:02x}{sto[0][2]:02x}', bd = 5, relief = 'ridge', command=lambda:chgmd(2))
mode_4 = tk.Button(mode4f, width = 2, height = 1, bg = f'#{sto[0][0]:02x}{sto[0][1]:02x}{sto[0][2]:02x}', bd = 5, relief = 'ridge', command=lambda:chgmd(3))
mode_5 = tk.Button(mode5f, width = 2, height = 1, bg = f'#{sto[0][0]:02x}{sto[0][1]:02x}{sto[0][2]:02x}', bd = 5, relief = 'ridge', command=lambda:chgmd(4))
mode_6 = tk.Button(mode6f, width = 2, height = 1, bg = f'#{sto[0][0]:02x}{sto[0][1]:02x}{sto[0][2]:02x}', bd = 5, relief = 'ridge', command=lambda:chgmd(5))

slider_s.grid()
mode_1.grid()
mode_2.grid()
mode_3.grid()
mode_4.grid()
mode_5.grid()
mode_6.grid()
#timer thing
def timer():
    n = datetime.now()
    t = n.timetuple()
    y, m, d, h, min, sec, wd, yd, i = t
    if h == 5 and min == 30 and sec == 0:
        chgclr(9)
    elif h == 22 and min == 30 and sec == 0:
        chgclr(10)

#main loop
while True:
    animation()
    if fade == True:
        rand1 = np.round(np.random.random_sample()*255)
        rand2 = np.round(np.random.random_sample()*255)
        rand3 = np.round(np.random.random_sample()*255) 
        if mode == True:
            fadeTo(rand1, rand2, rand3)
        else:
            fadeTo(rand1, rand1, rand1)
    timer()
    time.sleep(.1)

