# **** Списки (Lists) ****

#  создание пустого списка

# my_list = []
# my_list_2 = list()

# # метод append 

# my_list.append(100)
# my_list.append(200)
# my_list.append("hello")
# my_list.append([1,2,3])
# my_list.append("ICELAND")

# # создание заполненного списка

# my_list = [10, 14935, 30, 2.1, "ololol", True]

# s = "Привет, земляне! "
# list_1 = list(s)

# # *** функция range() ****

# numbers  = list( range(10) ) # создается набор чисел от 0 до 10 не включительно 
# numbers  = list( range(2, 10) ) # создается набор чисел от 2 до 10 не включительно 
# numbers  = list( range(2, 10, 2) ) # создается набор чисел от 2 до 10 не включительно с шагом 2
# numbers  = list( range(10, 1, -1) ) # создается набор чисел от 10 до 1 не включительно в обратном направлении


# # ***** МЕТОДЫ СПИСКОВ ******

# a = [10, 15, 20, 25, 50, 20, 3405]

# # объект . метод
# # добавление элемета по индексу
# a.insert(0, "B")


# # удаление элемента из списока по значению
# # remove(20)

# # очистка списка
# # print(a)
# # a.clear()

# # сортировка списка 
# b = [1,4,20,34, 57, 89, 14, 590]
# # b.sort() № по сторону возрастания
# b.sort(reverse=True) # в сторону убывания

# # обращение к элементам

# # c = [1,4,5,7,8]

# # print( c[0]) # извлечение (чтение)значение элемента 

# # del c[1] # удаление элемента по индексу

# # # c[3] = 10 #замена значения
# # c[-1] = 10  # замена значения


# # **** срезы (slice)****

# c = c+ [9,10,11,12,13]

# c_slice = c[0:3] # срез с 0 индекса по 3й индекс не включительно
# c_slice = c[:3] # срез с 0 индекса по 3й индекс не включительно
# c_slice = c[1:4] # срез с 1 индекса по 4 индекс не включительно

# c_slice = c[1:8:2] # срез с 1 индекса по 8 индекс не включительно с шагом 2

# c_slice = c[::2] # срез всего списка с шагом 2

# с_slice = c[::-1] # поворот списка

# c_slice = c[-1: -4: -1] 

 
list = ["Reykjavik", "Kopavougur", "Hvaregardi","Husavik"] # длинаи списка, 4 элемента
# print("Name of sities in Iceland:", len(list))
# print(list[3]) # выявление номера индекса в списке
# print(list[-1]) # отрицательные индексы 

# s = "eyjafjallajökull" #длина строки 16 элементов
# print(len(s))

a = [23, 4, 30, -3, 0, 12, 2, 5, 2, 5, 23, 5, 35]
b = ["Sasha", "Masha", "Kesha", "Valya", "Kris"]
# b. append("Tanya") # append-добавление в список 
# print(b)

x = a.count(23)
print(x) 