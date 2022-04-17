from tkinter import *
from tkinter.filedialog import *

#함수선언

def func_open() :
    global filename
    filename = askopenfilename(parent=window, filetypes=(("GIF 파일", "*.gif"),("모든파일","*.*")))
    photo = PhotoImage(file=filename)
    pLabel.configure(image = photo)
    pLabel.image = photo

def func_exit() :
    window.quit()
    window.destroy()

def zoom(event):
    #global photo
    photo = PhotoImage(file=filename)
    photo = photo.zoom(2, 2)
    pLabel.configure(image = photo)
    pLabel.image = photo

def subsample(event):
    #global photo
    photo = PhotoImage(file=filename)
    photo = photo.subsample(2, 2)
    pLabel.configure(image = photo)
    pLabel.image = photo

#def KeyEvent(event):
#    global key
#    key = event.keysym
#    #print("키보드이벤트"+key)
#    if key == "Up" :
#        zoom()
#    if key == "Down" :
#        subsample()


#메인코드
window = Tk()
window.geometry("400x400")
window.title("연습문제")

#2019038050_윤승재
photo = PhotoImage()
pLabel = Label(window, image= photo)
pLabel.pack(expand=1, anchor=CENTER)

mainMenu = Menu(window)
window.config(menu=mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="파일열기", command=func_open)
fileMenu.add_separator()
fileMenu.add_command(label="프로그램 종료",command=func_exit)

#window.bind("<Key>", KeyEvent)
window.bind("<Up>", zoom)
window.bind("<Down>", subsample)

window.mainloop()