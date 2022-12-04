from tkinter import *

root = Tk()
root.geometry('500x300+100+100')
# set width/height to center an elem

# blue = Label(root, text='Aylin relheight=0.3', font=('Apple Chancery', 24, 'bold'), bg='blue', fg='white')
# blue.place(relheight=0.3)
# red = Label(root, text='Aylin relwidth=0.7', font=('Apple Chancery', 24, 'bold'), bg='red', fg='white')
# red.place(relwidth=0.7)
# purple = Label(root, text='Aylin relx=0.2', font=('Apple Chancery', 24, 'bold'), bg='purple', fg='white')
# purple.place(relx=0.2)
# green = Label(root, text='Aylin rely=0.4', font=('Apple Chancery', 24, 'bold'), bg='green', fg='white')
# green.place(rely=0.4)

label = Label(root, text='Aylin', font=('Apple Chancery', 24, 'bold'), bg='blue', fg='white')
label.place(width=400, height=100, x=50, y=100)
button = Button(root, text='Aylin\' button', font=('Apple Chancery', 24, 'bold'), highlightbackground='red', fg='white')
button.place(in_=label, relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
