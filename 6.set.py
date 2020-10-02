# **** МНОЖЕСТВО(set) *****

# ОСОБЕННОЧТИ: 
# - неупорядоченная коллекция 
# - нет индексов 
# - при создании множетсва, автоматически удаляются все дублирующие объекты

# **** СОЗДАНИЕ МНОЖЕСТВА *****

# первый способ
my_set = {"a", "b", "c"}

# второй способ
s = "hello"
my_list = [100, 200, 200, 300, 500]

my_set_2 = set(my_list)

# **** добавление элементов ****

my_set.add(777)

# **** удаление элемнтов ****

my_set = {10, 35, 40, 50, 200}

# my_set.remove(200)

# проблемы при удалении
# my_set.remove(1020)

# решение проблемы 
my_set.discard(40)

# **** ОБЪЕДЕНИЕ МНОЖЕСТВ ****

users = {"John", "Antony", "Chris"}
new_users = {"John", "Jack", "Maria"}

# users = users.union(new_users) # union() позволяет создать новое множество и при этом сохранить исходные множ-ва
users_2 = users |  new_users # короткий аналог union()
# users.update(new_users) # тоже самое, что и union(), но нвоое множ-во создается внутри первой переменной 

 # *** ОПРДЕЛЕНИЕ пересечений (схождений)

intersect_user = users.intersection(new_users)

# короткий аналог метода intersection()
intersect_user = users & new_users

# ***  опрделение разности ***
# diff_user = users.difference(new_users)  # разност только из пегвого множества

# короткий аналог метода difference)
# diff_user = users - new_users

# sd_users = users.symmetric_difference(new_users) # симметричная разность

# print(diff_user)

# import this 