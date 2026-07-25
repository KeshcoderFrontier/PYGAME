from tkinter import *
from  datetime import date 

root = Tk()
root.title("Lets get started with widgets")
root.geometry("500x600")


lbl = Label(text="Hey there", fg = "white", bg = "blue", height = 1 , width = 300)

name_lbl = Label(text = " Full name ", bg = "dark blue")
name_entry = Entry()

def display():
    name = name_entry.get()
    global message
    message = "Welcome to the App \n the Date today is:"
    greet = "hello!"+name+"\n"
    text_box.insert(END, greet)
    text_box.insert(END, message )
    text_box.insert(END, date.today())

text_box = Text(height=3)


btn = Button(text = "Begin", command = display , height = 1, bg = "green", fg = "white")

lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

root.mainloop()