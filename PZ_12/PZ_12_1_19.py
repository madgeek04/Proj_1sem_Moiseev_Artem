from tkinter import *
from tkinter.font import BOLD
root = Tk()
root.geometry('1391x646')
root['bg'] = '#9dd7ed'
var = IntVar()
Canvas(root, width=950, height=646, bg='#ffffff').place(x=205, y=0)
Label(text='Регистрация', width=10, bg='#FFFFFF', fg='#11b4f0', font='arial 15').place(x=234, y=10)
Label(text='Создание нового сайта', width=60, bg='#00b0ef', fg='#FFFFFF', font='arial 19').place(x=230, y=50)
Label(text='Email', width=10, bg='#FFFFFF', fg='#11b4f0', font=('arial', 13, BOLD)).place(x=450, y=120)
Entry(textvariable=StringVar(value='@gmail.com'), fg='gray', width=27, bd='2', font='arial 15').place(x=544, y=118)
Label(text='Пароль', width=10, bg='#FFFFFF', fg='#11b4f0', font=('arial', 13, BOLD)).place(x=445, y=160)
Entry(textvariable=StringVar(value='********'),fg='gray', width=27, bd='2', font='arial 15').place(x=544, y=158)
Label(text='Имя', width=10, bg='#FFFFFF', fg='#11b4f0', font=('arial', 13, BOLD)).place(x=453, y=200)
Entry(textvariable=StringVar(value='Руслан'),fg='gray', width=27, bd='2', font='arial 15').place(x=544, y=198)
Label(text='Фамилия', width=10, bg='#FFFFFF', fg='#11b4f0', font=('arial', 13, BOLD)).place(x=440, y=240)
Entry(textvariable=StringVar(value='Тертышный'),fg='gray', width=27, bd='2', font='arial 15').place(x=544, y=238)
Label(text='Никнейм', width=10, bg='#FFFFFF', fg='#11b4f0', font=('arial', 13, BOLD)).place(x=440, y=280)
Entry(textvariable=StringVar(value='Tros'),fg='gray', width=27, bd='2', font='arial 15').place(x=544, y=278)
Label(text='Дата рождения', width=13, bg='#FFFFFF', fg='#11b4f0', font=('arial', 13, BOLD)).place(x=400, y=320)
Spinbox(root, from_=0, to=31, width=6).place(x=544, y=323)
Spinbox(root, from_=0, to=12, width=6).place(x=604, y=323)
Spinbox(root, from_=1980, to=2004, width=6).place(x=664, y=323)
Label(text='Пол', width=6, bg='#FFFFFF', fg='#11b4f0', font=('arial', 13, BOLD)).place(x=474, y=360)
Radiobutton(text='Мужчина', bg='white', variable=var, value=1).place(x=544, y=361)
Radiobutton(text='Женщина', bg='white', variable=var, value=2).place(x=644, y=361)
root.mainloop()
