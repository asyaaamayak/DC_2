# **** СЛОВАРЬ ****

# ПАРЫ "ключ:значение"
my_dict = {10:100, 1:100, 2:400, "A":5.14, 'abc':[1, 2, 3]}

a = [
    ['A', 1000],
    ["B", 2000]
]

# a = [ ['A', 1000],['B',2000] ]
my_dict_2 = dict(a)
# print(my_dict_2)

# ЧТЕНИЕ ДАННЫХ
item = my_dict['abc']  #10]
# print(item)

# ИЗМЕНЕНИЕ ЗНАЧЕНИЯ
my_dict[10] = 777
# print(my_dict)

# ДОБАВЛЕНИЕ НОВОГО ЭЛЕМЕНТА
my_dict["hello"] = 1000
# print(my_dict)

# *** ПРОБЛЕМЫ СО ЧТЕНИЕМ ЗНАЧЕНИЯ 
d = {"key_1":100, "key_2":300}
k = "key_3"
# val = d[10]


# ПЕРВЫЙ ВАРИАНТ РЕШЕНИЯ
# if k in d:
#     val = d[k]
# else:
#     val = "такого ключа нет"

# ВТОРОЙ ВАРИАНТ РЕШЕНИЯ
# val = d.get(k) # None - пустота
# val = d.get(k, 0) # "пусто")
# print(val)

# *** ПРОБЕЛЕМЫ ПРИ УДАЛЕНИИ ПО НЕСУЩЕСТВУЮЩЕМУ КЛЮЧЮ ***

# del d[k]

k = "key_1"
# РЕШЕНИЕ ЭТОЙ ПРОБЛЕМЫ
# val = d.pop(k, None) # метод удаляет элемент если ключ существует и при этом значение можно присвоить переменной 

# print(val, d)


# *** ОБНОВЛЕНИЕ ЗНАЧЕНИЙ ***

d_1 = {"key_1":100, "key_2":300}

d_2 = {"key_1":777, "key_3":200}

d_1.update(d_2)

print(d_1)