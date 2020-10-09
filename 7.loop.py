# **** генератор списка ****
# my_list = [num for num in range(10)]
# my_list = [num ** 2 for num in range(10)]
my_list = [num ** 2 for num in range(10) if num > 3]

# print(my_list)

# **** класс enumerate() ****

data = ['a', 'hello', 'r', 'w']

# print( list(enumerate(data)) )

# for index, item in enumerate(data):
#     print(index, item)

# **** Генератор словаря ****

# my_dict = { i : i for i in ['a', 'b', 'c', 'd']}

# my_dict = { item : index for index, item in enumerate(data)}

my_dict = { item : index for index, item in enumerate(data) if index > 0 }

# print(my_dict)

# **** калькулятор с циклами ****

while True: 
    cmd = None
    # ввод чисел
    num_list = []
    for n in range(2):
        num = int(input(f"введите {n} число: "))    
        num_list.append(num)   

    # ввод команды 
    while True:
        cmd = input("Введите команду: ")
        if cmd not in {"stop", "+", "-", "*", "/"}:
            print("вы ввели неправвльную команду!!! :((")
            continue 
        else:
            break
    # обработка выключения
    if cmd == "stop":
        print(" До свидание!")
        break 

    # вычисления 
    if cmd == "+":
        res = num_list[0] + num_list[1]
    elif cmd == "-":
        res = num_list[0] - num_list[1]
    elif cmd == "*":
        res = num_list[0] * num_list[1]
    elif cmd == "/":
        res = num_list[0] / num_list[1]
     # вывод результат
    if float is type(res):
        print(f"Результат: {res:.4f}")
    else: 
        print(f"Результат: {res}")
    
    res = float(res)

    # # вывод результат
    # print(f"Результат: {res:.4f}")