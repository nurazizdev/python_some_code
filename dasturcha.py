from datetime import datetime
from tkinter import *

oyna = Tk()
oyna.title('Dasturcha :) ')
oyna.geometry('700x500')

bosh = Label(text="Bu dastur yoshingizni yoki bu yil to'ladigan yoshingizni chiqaradi!!!", bg="white")
bosh.place(x=110, y=30, width=480, height=40)
boshi = Label(text="Tug'ilgan yilingizni kiriting", bg="white")
boshi.place(x=250, y=110, width=200, height=40)
natija = Label(text="Natija", bg="white")
natija.place(x=275, y=250, width=150, height=40)

yil = Entry()
yil.place(x=275, y=160, width=150, height=30)

def farq():
	bugun = datetime.today()
	natija.config(text=bugun.year - int(yil.get()))

tugma = Button(text="Hisoblash", command=farq)
tugma.place(x=260, y=200, width=180, height=40)

oyna.mainloop()