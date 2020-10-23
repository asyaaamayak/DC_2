# *** Обработка исключений (исключительные события, искл. ситуации) ***


# генерация исключения
a = 100
b = 0

# "деление на ноль" - пример ошибки (не рабочий код)
# c = a / b


# решение - обработка исключений (отлов исключения)
# конструкция "try-except"

# try:
# 	# потенциальной аварийный код
# 	c = a / b
# 	print("Все отлично")
# except:
# 	# тут должен быть код, который срабатывает при исключительных ситуациях
# 	# т.е. "запасной" код
# 	print("Что-то пошло не так")
# 	c = a / 0.1

# # тут может быть код который выполняется после предыдущего блока
# print("Result: ", c)

# Обработка множества исключений

try:
    var = int(input("Введите число отличное от нуля   "))
    result = 50 / var
#  обработка конкретного типа (класса)
except ZeroDivisionError: # в данном примере тип исключения - ZeroDivisionError:
    print("Вы попытались поделить на 0! ")
    result =  50 / 1
except ValueError as val_error: # в данном примере тип исключения - ValError, его инфор-я передается в  val_error
    print(f"По моему,  вы ввели не число. Инфо {val_error}")
    result = 0


print("Result: ", result)


# конструкция "try-except-finally"

# try:
# 	var = int(input("Введите число: "))
# 	c = 100 / var
# 	print("Полет нормальный!")
# except ZeroDivisionError:
# 	c = 0
# 	print("Попытка деления на ноль")
# finally:
# 	# finally срабатывает в любом случае, даже если программа завершится аварийно
# 	# т.е. тут должна быть критически важная логика
# 	print("Критически важное действие")

# print("Result", c)


# конструкция "try-except-else-finally"

try:
	var = int(input("Введите число: "))
	c = 100 / var
	print("Полет нормальный!")
except ZeroDivisionError:
	c = 0
	print("Попытка деления на ноль")
else:
	# else срабатывает только тогда, когда нет исключений
	print("Логика, которая выполняется только если нет исключений")
finally:
	# finally срабатывает в любом случае, даже если программа завершится аварийно
	# т.е. тут должна быть критически важная логика
	print("Критически важное действие")

print("Result", c)