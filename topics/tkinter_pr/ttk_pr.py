from tkinter import *
from tkinter import ttk

root = Tk()

frame = ttk.Frame(root, width=200, height=300, padding=5)
frame['padding'] = (5, 10)
frame['borderwidth'] = 5
frame['relief'] = 'raised'
frame.grid()

label = ttk.Label(frame, text='First Label')
label.grid()

new_content = StringVar()
label['textvariable'] = new_content
new_content.set('Second Title')

root.mainloop()
