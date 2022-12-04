from tkinter import *

root = Tk()

blue = Label(root, text='Aylin', font=('Apple Chancery', 24, 'bold'), bg='blue', fg='white', width=20, height=5)
blue.grid(row=0, column=0)
red = Label(root, text='Aylin', font=('Apple Chancery', 24, 'bold'), bg='red', fg='white', width=20, height=5)
red.grid(row=0, column=1)
purple = Label(root, text='Aylin', font=('Apple Chancery', 24, 'bold'), bg='purple', fg='white', width=20, height=5)
purple.grid(row=0, column=2)

blue1 = Label(root, text='Aylin', font=('Apple Chancery', 24, 'bold'), bg='blue', fg='white', width=20, height=5)
blue1.grid(row=1, column=0)
red1 = Label(root, text='Aylin', font=('Apple Chancery', 24, 'bold'), bg='red', fg='white', width=20, height=5)
red1.grid(row=1, column=1)
purple1 = Label(root, text='Aylin', font=('Apple Chancery', 24, 'bold'), bg='purple', fg='white', width=20, height=5)
purple1.grid(row=1, column=2)

root.mainloop()