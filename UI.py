##b1 = bPar
##b2 = bPaste
##b3 = bCancel
##l1 = lSchool
##e1 = eSchool
##l2 = lProject
##e2 = eProject

from tkinter import *
import tkfont

mas = ['']*7

# Кнопки

def cancel():
    bPaste.grid()
    bCancel.grid_remove()
    print("bCancel")
def paste():
    bPaste.grid_remove()
    bCancel.grid(row=51, column=3)
    mas.append(t.get('1.0','end'))
    print("bPaste")
def par():
    bPaste.grid(row=51, column=3)
    print("bPar")
def point():
    bPaste.grid(row=51, column=3)
    print("bPoint")
def contents():
    mas[0]=eSchool.get()
    mas[1]=eProject.get()
    mas[2]=eName.get()
    mas[3]=eTeacher.get()
    mas[4]=eClass.get()   
    mas[5]=eCity.get()
    mas[6]=eYear.get()
    lSchool.grid_remove()
    eSchool.grid_remove()
    lProject.grid_remove()
    eProject.grid_remove()
    lName.grid_remove()
    eName.grid_remove()
    lTeacher.grid_remove()
    eTeacher.grid_remove()
    lClass.grid_remove()
    eClass.grid_remove()
    lCity.grid_remove()
    eCity.grid_remove()
    lYear.grid_remove()
    eYear.grid_remove()
    bText.grid_remove()
    t.grid(row=0, column=0, rowspan=50, columnspan=50)
    bPar.grid(row=51, column=0, sticky=E)
    bPoint.grid(row=51, column=1)
    bTitle.grid(row=51, column=2, sticky=W)
    print("bText")
def title():
    print(mas)
    t.grid_remove()
    bTitle.grid_remove()
    bPar.grid_remove()
    bPaste.grid_remove()
    bCancel.grid_remove()
    bPoint.grid_remove()
    lSchool.grid(row=1, column=0, sticky=E)
    eSchool.grid(row=1, column=1, columnspan=3)
    lProject.grid(row=1, column=0, sticky=E)
    eProject.grid(row=1, column=1, columnspan=3)
    lName.grid(row=2, column=0, sticky=E)
    eName.grid(row=2, column=1, columnspan=3)
    lTeacher.grid(row=3, column=0, sticky=E)
    eTeacher.grid(row=3, column=1, columnspan=3)
    lClass.grid(row=4, column=0, sticky=E)
    eClass.grid(row=4, column=1, sticky=W)
    lCity.grid(row=5, column=0, sticky=E)
    eCity.grid(row=5, column=1, sticky=W)
    lYear.grid(row=6, column=0, sticky=E)
    eYear.grid(row=6, column=1, sticky=W)
    bText.grid(row=51, column=1, sticky=W)
    canvas.grid(row=52, column=0)
    print("bTitle")
    
# Окно

root = Tk()
root.title("ПРОЕКТ")
root.geometry(str(root.winfo_screenwidth())+"x"+str(root.winfo_screenheight()))
canvas = Canvas(root, width=200, height=200)
helv = Font(family='Helvica', size=36, weight=BOLD)

# Титульник

lSchool = Label(text="Название образовательного учреждения:")
eSchool = Entry(width=30)
lProject = Label(text="Название проекта:")
eProject = Entry(width=30)
lName = Label(text="ФИО ученика:")
eName = Entry(width=30)
lTeacher = Label(text="ФИО классного руководителя:")
eTeacher = Entry(width=30)
lClass = Label(text="Класс ученика:")
eClass = Entry(width=3)
lCity = Label(text="Город:")
eCity = Entry(width=30)
lYear = Label(text="Год сдачи:")
eYear = Spinbox(width=10, from_=1999, to=2099)
bText = Button(root, text="Вперёд", font = helv, height = 20, width = 20, command=contents)

# Основная часть

bPar = Button(root, text="Абзац", command=par)
bPoint = Button(root, text='Пункт', command=point)
bPaste = Button(root, text="Вставить", command=paste)
bCancel = Button(root, text="Отменить", command=cancel)
bTitle = Button(root, text='Назад', command=title)

t = Text()

title()
root.mainloop()
