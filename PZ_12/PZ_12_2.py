from tkinter import *
import secrets
import string


def generate_string():
    a = string.ascii_letters + string.digits
    b = ''.join(secrets.choice(a) for i in range(int(n.get())))
    c['text'] = 'Сгенерированный пароль', b


root = Tk()
root.title('Генерация пароля')
root.geometry("500x120")
Label(text='Количество символов:').grid(row=1, column=0)
n = Entry()
n.grid(row=1, column=1)
button1 = Button(text="Сгенерировать")
button1.grid(row=4, column=1)
c = Label()
c.grid(row=5, column=1)
button1.bind('<Button-1>', generate_string)
root.mainloop()
