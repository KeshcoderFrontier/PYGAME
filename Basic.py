from tkinter import *
from tkinter import messagebox


window = Tk()
window.title("Basic script")
window.geometry('500x500')


def show_message():
    messagebox.showinfo("Button clicked")



Basic_Text = Label(window, text='Basic', bg='white',fg='purple')
Basic_Button = Button(window,text='Click me', bg='green',fg='black',command=show_message)
Basic_Button.pack()
Basic_Text.pack()
window.mainloop()


