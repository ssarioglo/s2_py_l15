#Родительский класс
class Transport(object):
    def __init__ (self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def info(self):
        print(f"Название автомобиля: {self.name} Скорость: {self.max_speed} Пробег: {self.mileage}")

#Дочерний класс с вместимостью по умолчанию 50
class Autobus (Transport):
    capacity = 50

    def __init__(self, name, max_speed, mileage, seating_capacity = 50):        #Переопределение конструктора, вместимость указана по умолчанию
        super().__init__(name, max_speed, mileage)
        self.capacity = seating_capacity

    def get_capacity(self):                                                     #Метод для вывода вместимости автобуса
        print(f"Вместимость одного автобуса {self.name}: {self.capacity}")



ikarus = Autobus("Ikarus", 120, 654000)

ikarus.get_capacity()