
#1. Создать класс TrafficLight (светофор).
#определить у него один атрибут color (цвет) и метод running (запуск);
#атрибут реализовать как приватный;
#в рамках метода реализовать переключение светофора в режимы: красный,
#  жёлтый, зелёный;
#продолжительность первого состояния (красный) составляет 7 секунд, 
# второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
#переключение между режимами должно осуществляться только в указанном 
# порядке (красный, жёлтый, зелёный);
#проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов. 
# При его нарушении выводить соответствующее сообщение и завершать 
# скрипт.
import time
from colorama import init, Fore, Style
init()
class TrafficLight:
    __color = ["\033[31m", "\033[33m", "\033[32m"]      
    def running(self):
        print("\033[H\033[J")
        for i in range(3):
            def console_TrafficLight():
                print(Style.BRIGHT + TrafficLight.__color[i])
                print("        *******          ")
                print("      ***********        ")
                print("     *************       ")
                print("     *************       ")
                print("      ***********        ")
                print("        *******          ")
            console_TrafficLight()
            if i == 0:
                time.sleep(7)
                print("\033[H\033[J")
            if i == 1:
                time.sleep(2)
                print("\033[H\033[J")
            if i == 2:
                time.sleep(4)
                print("\033[H\033[J")               
a = TrafficLight()
a.running() # !!! После запуска консоль очистится для демонстрации!!! 
# Необходимо немного промотать консоль в начало 

#######################################################################
# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия 
# всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия 
# одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины 
# полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.
class Road:
    _mass = 2.5
    def mass_asp(self, _length, _width, _thickness = None):
        if _thickness is not None:
            pass
        else:
            _thickness = 1/100
        a = _length*_width*_thickness*Road._mass
        print(f'Масса асфальта размером \
{_length}x{_width}x{_thickness} метров составила \
{int(a)} тонн.')    
a = Road()
a.mass_asp(5000, 20, 0.05) # Необходимо ввести длину и ширину, 
# также можно указать толщину в метрах (необязательный параметр)

######################################################################
# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income 
# (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": 
    # bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени 
# сотрудника 
# (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры 
# класса Position, передать данные, проверить значения атрибутов, 
# вызвать методы экземпляров.
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        print(f"{self.position}: {self.name} {self.surname}")
    def get_total_income(self):
        print(f'Зарплата {self.income.get("wage")+self.income.get("bonus")} рублей.')
b = Position("Nikolay", "Ivanov", "Data_Scientist", 150000, 9000)
b.get_full_name()
b.get_total_income()

c = Position("Rita", "Dakota", "Frontend-разработчик", 170000, 10000)
c.get_full_name()
c.get_total_income()

#####################################################################
# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, 
# is_police (булево). А также методы: go, stop, turn(direction),
#  которые должны сообщать, что машина поехала, остановилась, повернула 
# (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, 
# PoliceCar;
# добавьте в базовый класс метод show_speed, который должен 
# показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. 
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно 
# выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. 
# Выполните доступ к атрибутам, выведите результат. 
# Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print(f"Машина {self.color} {self.name} поехала.")
    def stop(self):
        print(f"Машина {self.color} {self.name} остановилась.\n")
    def turn(self, direction):
        print(f"Машина {self.color} {self.name} повернула {direction}.")
    def show_speed(self):
        print(f"Скорость машины {self.color} {self.name} составляет {self.speed} км\ч.")
class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"{self.color} {self.name} превышение скорости на {self.speed - 60} км/ч.")              
        else:
            print(f"Машина {self.color} {self.name} движется со скоростью {self.speed} км/ч.") 
class SportCar(Car):
    def show_speed(self):
        super(SportCar, self).show_speed()
            
class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"{self.color} {self.name} превышение скорости на {self.speed - 40} км/ч.")             
        else:
            print(f"Машина {self.color} {self.name} движется со скоростью {self.speed} км/ч.")           
            
class PoliceCar(Car):
    def show_speed(self):
        super(PoliceCar, self).show_speed()
    def only_police(self):
        if self.is_police == True:
            print("Это полицейская машина.")
        else:
            print("Данная машина гражданская!")
                
a = TownCar(40, "White", "Opel", False)
a.go()
a.show_speed()
a.turn('налево')
a.stop()

b = SportCar(270, "Red", "Mazda", False)
b.go()
b.show_speed()
b.turn('направо')
b.stop()

с = WorkCar(59, "Yellow", "Volkswagen", False)
с.go()
с.show_speed()
с.turn('налево')
с.stop()

d = PoliceCar(50, "Black", "Ford", True)
d.only_police()
d.go()
d.show_speed()
d.turn('налево')
d.stop()


            
# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). 
# Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), 
# Handle (маркер);
# в каждом классе реализовать переопределение метода draw. 
# Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный 
# метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title
        
    def draw(self):
        print("Запуск отрисовки.")

class Pen(Stationery):
    def __init__(self, title, line=None):
        super().__init__(title)
        self.line = line  
        
    def draw(self):
        print(f"Запуск отрисовки. Режим - {self.title}.")
        if self.line is not None:
            print(f"Толщина линнии - {self.line}.")
            
class Pencil(Stationery):
    def __init__(self, title, line=None):
        super().__init__(title)
        self.line = line    
        
    def draw(self):
        print(f"Запуск отрисовки. Режим - {self.title}.")
        if self.line is not None:
            print(f"Толщина линнии - {self.line}.")
            
class Handle(Stationery):
    def __init__(self, title, line=None):
        super().__init__(title)
        self.line = line    
        
    def draw(self):
        print(f"Запуск отрисовки. Режим - {self.title}.")
        if self.line is not None:
            print(f"Толщина линнии - {self.line}.")
        
a = Pen('ручка', 2)
a.draw()

a = Pencil('карандаш')
a.draw()

a = Handle('маркер', 10)
a.draw()

