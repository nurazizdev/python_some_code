from datetime import datetime
from tkinter import *

oyna = Tk()
oyna.title('Dasturcha :) ')
oyna.geometry('700x500')

bosh = Label(text="TUB SON ", bg="white")
bosh.place(x=110, y=30, width=480, height=40)
boshi = Label(text="Son kiriting", bg="white")
boshi.place(x=250, y=110, width=200, height=40)
natija = Label(text="Natija", bg="white")
natija.place(x=275, y=250, width=150, height=40)

yil = Entry()
yil.place(x=275, y=160, width=150, height=30)

def IsPrime():
  k=int(pow(int(yil.get()),1/2))
  for i in range(2,k+1):
    if int(yil.get())%i==0:
      return natija.config(text="Tub son emas")
  return natija.config(text="Tub son")
tugma = Button(text="Hisoblash", command=IsPrime)
tugma.place(x=260, y=200, width=180, height=40)

oyna.mainloop()


