# x = int(input())
# if x < 100:
#     print("введенное < 100")
#     y = int(input())
#     if y > -5:
#         print(x * y)
# print("конец прораммы")

# if-else
# x = int(input()) 
# if x < -10:
#     print("введенное число < -10")
# else:
#     print("введенное число => -10")

# # elif -Иначе,если (else-if)
# x = int(input())
# y = int(input())
# a = x == y
# print(a)

# if x < 10:
#     print("введенное число < 10")
# elif y < 10:
#     print("только второе число больше 10")
# else:
#      print("не одно число не меньше 10")

# if x == y:
#     print("число больше либо равно y")
# else:
#     print("число меньше y")


# Логические операторы 

# and   логический оператор "И"
# or    логический оператор "ИЛИ"
# not   логический оператор "НЕ"

x = int(input())
y = int(input())
z = int(input())
if not (x == 32 or y == 32 or z == 32):
    print("условие истинно")
else:
    print("условие ложное") 

