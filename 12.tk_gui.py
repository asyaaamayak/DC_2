# *** Генератор паролей ***
from tkinter import Tk, StringVar, Label, Entry, Button
import hashlib as h

def hashing():
    """ 
    Функция шифрования (хэширования)
    """
    # строка пароли
    origin_str = pwd.get()

    # кодирование в байт-строку 
    byte_str = origin_str.encode()
    # шифрование - пропускание байт-строки через хэш-функцию
    hash_str = h.sha256(byte_str)
    # преобразование в строку шестьнадцатеричного числа (hex - числа)
    hex_str = hash_str.hexdigest()[:8]

    # передача хеш - строки
    pwd_hash.set(hex_str)
    # print(type(byte_str))

    # запись в файл


# объект окна 
window = Tk()
# заголовок окна 
window.title("** Password generator** ")
# переменные с объектами класса StringVar
pwd = StringVar()
pwd_hash = StringVar()

# текстовая метка, созданная виджетом (компонентом, элементов) Label
label = Label(text="Пароль:")

# позиционирование виджета методом grid(сетка)
label.grid(row=0, column=0, padx=5, pady=5)

# поле ввода строки, созданная виджетом Entry
Entry(textvariable=pwd).grid(row=0, column=1, padx=5, pady=5)

# кнопка
Button(text="Click me", command=hashing).grid(row=1, column=0, padx=5, pady=5)
# поле вывода хэш-строки
Entry(textvariable=pwd_hash).grid(row=1, column=1, padx=5, pady=5)

window.mainloop()
