from tkinter import *
from tkinter import font

root = Tk()
root.geometry('200x200')
root.title('Welcome screen')

Label(root, text='Welcome!', font=('Apple Chancery', 24, 'bold'), fg='#a541e0', bg='#92e3ef', relief='ridge').pack()
# relief: solid, flat, sunken, raised, ridge, groove
# tk.Button(root, text='Hello, Aylin!').grid()
# print(font.families())    # to check out list of fonts

tkinter_version = TkVersion
# tk.Label(root, text=f'Version {tkinter_version}').place(x=10, y=50)
Label(root, text=f'Version {tkinter_version}').pack()

Button(root, text='Hello, Aylin!', highlightbackground='#a6cef4', relief=RAISED).pack()

root.mainloop()
