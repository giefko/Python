
from Tkinter import *
import math

root = Tk()
top = Frame(root) 
top.pack(side='top')

hwtext = Label(top, text='Hello, World! The sine of')
hwtext.pack(side='top')

r = StringVar() 
r.set('1.2')    
r_entry = Entry(top, width=6, textvariable=r)
r_entry.pack(side='top')

s = StringVar() 
def comp_s(event):
    global s
    s.set('%g' % math.sin(float(r.get()))) # construct string

r_entry.bind('<Return>', comp_s)

compute = Label(top, text=' equals ')
compute.pack(side='top')

s_label = Label(top, textvariable=s, width=18)
s_label.pack(side='top')

import tkMessageBox
def quit(event):
    if tkMessageBox.askokcancel('Quit','Do you really want to quit?'):
        root.destroy()

root.bind('<q>', quit)

root.mainloop()
