from tkinter import *

def clicked():
    lbl.configure(text="Это интересно!")



window = Tk()
window.title("Численое интегрирование!")
window.geometry('800x600')

lbl = Label(window, text="Численное интегрирование!")  
lbl.grid(column=0, row=0)


btn = Button(window, text="Нажимать!", command=clicked)
btn.grid(column=1, row=0)






window.mainloop()









print("Численное интегрирование")
print("Сравнение точности известных методов")
print("И проверка их алгебраического порядка точности")




















