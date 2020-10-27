# **** Основы объектно-ориентированного программирования (ООП) ****

# Объекты обладает свойствами и методами (умение объекта)
# Каждый объект принадлежит к определенному типу (классу)
# Класс - это "чертеж" объекта
# "Реализация " класса - объект (экземпляр, инстанс)

# Создание класса. Название класса принято писать с заглавной буквы
class Cat: 
    # метод (метод экземпляра) - функция внутри класса
    def mur(self, name):
        # атрибут (свойства, поля)
        self._name = name
        print("Meow! Меня зовут: ", self._name)

    # Метод информации
    def info(self):
        print(f"Name: {self._name}")

# создание объекта (экземляара) класса Cat
cat_1 = Cat()
cat_2 = Cat()

# вызов метода первого объекта
# cat_1.mur("Котя")
# cat_2.mur("Гав")
# # вызов второго метода, который использует атрибут, созданный в первом методе
# cat_1.info()


# Метод-конструктор
class Dog:
    # конструктор (installator)
    # нужен для каких-либо настроек или других 
    # приготовлений в момент создания объектов
    def __init__(self, name, age, weight):
       self.name = name
       self.age = age
       self.weight = weight

    def gaf(self):
        print(f"Гав! Меня зовут {self.name}")

dog_1 = Dog("Барсик", 10, 30)
dog_2 = Dog("Собакен", 5, 15.3)

# чтение значения атрибута
name_dog_1 = dog_1.name
# print(name_dog_1)
# изменение значения атрибута
dog_2.name = "Барбос"
# print(dog_2.name )
# print(name_dog_1)

# вызов метода
# dog_1.gaf()
# dog_2.gaf()

# *** Принципы Наследования - 1-й принцип ООП ***

# Родительские (предковый) класс
class Animal:
    def __init__(self, legs):
       self.num_legs = legs

    def move(self):
        print(f"i'm moving, i have {self.num_legs} legs")

# дочерние классы
class Insect(Animal):
    pass

class Wolf(Animal):
    pass

bug = Insect(8)
wolf = Wolf(4)

# bug.move()
# wolf.move()

class Human(Animal):
    def __init__(self, name, num_legs):
        self.num_legs = num_legs
        self.name  = name

    def info(self):
        print(f"I'm human, my name is {self.name} ")

# john = Human("John", 2)
# john.move()
# john.info()

# **** Принцип Полиморфизма ****

# поли + морф = разные формы чего-то одного (информаицонные объекты )

# 1 вид. Разные классы могут обладать методами с одним именем, но с разной функциональностью 

# родительский класс
class A:
    def method_1(self, arg):
        print(f"Data: {arg}")

# дочерний класс у которого родительский метод переопределен 
class A_1(A):
    def method_1(self, a, b):
        print(f"Data: {a + b}")


# создание экземпляров классов
a = A()
a_1 = A_1()

# вызов методов у экзмемпляров 
# a.method_1(100)
# a_1.method_1(20, 50)

# * 2 вид. применение "Магических методов" (методы перегрузки операторов)

#  метод, который позволяет из экземпляра (объекта) класса "делать" функцию 

class CustomSum:
    def __init__(self, param):
        self.coeff = param

    def ___call___(self, a, b):
        res = (a + b) * self.coeff
        print(f"Result: {res}")

    #  маг-метод 
    def __str__(self):
        return f"Custom Summator. Coeff: {self.coeff}"

sum_1 = CustomSum(1.5)
sum_2 = CustomSum(2.44)

# Эффект магического метода 
# sum_1 = (3, 5)
# sum_2 = (3, 5) 

# print(sum_1)

# **** Инкапсуляция ****
# инкапсуляция - сркытие атрибутов и/или методов

class B:
    def __init__(self, arg):
        # не строгая инкапсулированный атрибут
        self._attr = arg
        # строго инкапсулированный атрибут
        self.__attr2 = 200


    # не строгая инкапсулированный атрибут
    def _method(self):
        print("hello!")
    
    # строго инкапсулированный атрибут
    def __method_2(self):
        print("World!")

    # не инкапсулированный метод
    def method_3(self):
        self.__method_2()


b = B(100) 
# print(b._attr)
# b._method()

# command+shift+P - вызов линтера 
# print(b._B__attr2)
# b._B__method_2() 
# b.method_3()

# *** Композиция (Агрегация) ****

# использовние экземпляров одних классов внутри других классов

class C:
    def __call__(self, a):
        return a ** 2

class D:
    def method(self, x):
        c = C() # создается объект класса D
        res = c(x) + x # здесь D используется в качестве функции
        print(res)

d = D()
# d.method(5)