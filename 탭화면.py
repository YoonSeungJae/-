from tkinter import *
from tkinter import ttk

window = Tk()
window.iconbitmap('python.ico')

baseTab = ttk.Notebook(window)

tabDog = ttk.Frame(baseTab)
baseTab.add(tabDog, text='강아지')
tabCat = ttk.Frame(baseTab)
baseTab.add(tabCat, text='고양이')

baseTab.pack(expand=1, fill="both")

photoDog = PhotoImage(file="C:/Users/윤/PycharmProjects/6주차/gif/dog.gif")
labelDog = Label(tabDog, image=photoDog)
labelDog.pack()
#2019038050_윤승재
photoCat = PhotoImage(file="C:/Users/윤/PycharmProjects/6주차/gif/cat2.gif")
labelCat = Label(tabCat, image=photoCat)
labelCat.pack()

window.mainloop()
