# *** КОТРЕЖ (tuple) ***

# неизменяемый (immutable) тип коллекций (структур данных)

my_tuple = (10, 20, 30, 30, 30)

# чтение данных из кортежи

num = my_tuple[0]

# нельзя менять значения
# my_tuple[0] = 100  - это ошибка!!!!

# нелзя удалять значения
# нельзя добавлять значения  


# **** МЕТОДЫ ****

# метод, который возвращает кол-во элементов определенного значения 
# n = my_tuple.count(30)
# print(n)

# метод который возвращает индекс с определенным значением
idx = my_tuple.index(30)

# срезы 
my_slice = my_tuple[1:]
# print(my_slice)

# длина 
lenght = len(my_slice)

print(lenght)