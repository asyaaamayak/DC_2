# *** Работа с файлами ****

# ***  Создание файла и запись в этот файл 
# контектстный менеджер with
# Режимы функции open:
# w - write (записи)
# a - append (добавление)
# r - read (чтение)

# with open("hello.txt", "w") as f:
#     f.write("Hello, world!\n")
#     f.write("How do u do?\n")

# *** Добавление новой записи без удаления старых
# with open("hello.txt", "a") as f:
#     f.write("Привет, Земляне!!\n")

# *** Чтение всего файла 
# with open("hello.txt",) as f:
#     text = f.read()
#     print(text)

# *** Чтение отдельных строк
# with open("hello.txt",) as f:
#     row = f.readline()
#     print(row, end="")
#     row = f.readline()
#     print(row, end="")

# *** Создаине списка из строк файла
# with open("hello.txt",) as f:
#     row_list = f.readlines()
#     # print(row_list)
#     print(row_list[-1])
    