from tkinter import *

window = Tk()

def convert():
    tg.delete("1.0", END)
    tg.insert(END, float(val.get()) * 1000)
    tlb.delete("1.0", END)
    tlb.insert(END, float(val.get()) * 2.20462)
    toz.delete("1.0", END)
    toz.insert(END, float(val.get()) * 35.274)

l1 = Label(window, text = 'kg')
l1.grid(row = 0, column = 0)

b1 = Button(window, text = 'Convert', command = convert)
b1.grid(row = 0, column = 2)

val = StringVar()
e1 = Entry(window, textvariable = val)
e1.grid(row = 0, column = 1)

tg = Text(window, height = 1, width = 10)
tg.grid(row = 1, column = 0)

tlb = Text(window, height = 1, width = 10)
tlb.grid(row = 1, column = 1)

toz = Text(window, height = 1, width = 10)
toz.grid(row = 1, column = 2)

window.mainloop()