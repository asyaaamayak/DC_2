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

john = Human("John", 2)
john.move()
john.info()




