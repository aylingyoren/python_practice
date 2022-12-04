from tkinter import *

root = Tk()
# root.geometry('800x600+50+50')

# blue = Label(root, text='Aylin', font=('Apple Chancery', 48, 'bold'), bg='blue', fg='white')
# blue.pack(fill=BOTH, expand=1, padx=20)    # fill=X / fill=Y, expand=1
# red = Label(root, text='Aylin', font=('Apple Chancery', 48, 'bold'), bg='red', fg='white')
# red.pack(fill=BOTH, expand=1, pady=20)
# purple = Label(root, text='Aylin', font=('Apple Chancery', 48, 'bold'), bg='purple', fg='white')
# purple.pack(fill=BOTH, expand=1, padx=10, pady=10)

# listbox = Listbox(root)
# listbox.pack(fill=BOTH, expand=1)
# for i in range(1, 21):
#     listbox.insert(END, str(i))

# blue = Label(root, text='Aylin', font=('Apple Chancery', 48, 'bold'), bg='blue', fg='white')
# blue.pack(ipadx=20)
# red = Label(root, text='Aylin', font=('Apple Chancery', 48, 'bold'), bg='red', fg='white')
# red.pack(ipady=20)
# purple = Label(root, text='Aylin', font=('Apple Chancery', 48, 'bold'), bg='purple', fg='white')
# purple.pack(ipadx=10, ipady=10)

blue = Label(root, text='Aylin', font=('Apple Chancery', 48, 'bold'), bg='blue', fg='white')
blue.pack(ipadx=20, side=LEFT)    # or side=RIGHT
red = Label(root, text='Aylin', font=('Apple Chancery', 48, 'bold'), bg='red', fg='white')
red.pack(ipady=20, side=LEFT)
purple = Label(root, text='Aylin', font=('Apple Chancery', 48, 'bold'), bg='purple', fg='white')
purple.pack(ipadx=10, ipady=10, side=LEFT)

root.mainloop()