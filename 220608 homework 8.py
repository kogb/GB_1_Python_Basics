'''
1. Реализовать класс «Дата», функция-конструктор которого должна 
принимать дату в виде строки формата «день-месяц-год». 
В рамках класса реализовать два метода. 
Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год 
и преобразовывать их тип к типу «Число». 
Второй, с декоратором @staticmethod, должен проводить валидацию числа, 
месяца и года (например, месяц — от 1 до 12). 
Проверить работу полученной структуры на реальных данных.
''' 

import sys

class Date():
    def __init__(self, str_date):
        self.str_date = str_date
        
    @classmethod
    def int_transf (cls, str_date):
        sep = str_date.split('-')
        cls.valid_day(sep)
        print (f'Число - {int(sep[0])}, месяц - {int(sep[1])}, год - {int(sep[2])}.\n')
    
    @staticmethod
    def valid_day (sep):
        if int(sep[0]) < 31:
                pass
        else:
            print("Некорректное число!\n")
            sys.exit()
            
        if int(sep[1]) < 12:
                pass
        else:
            print("Некорректный месяц!\n")
            sys.exit()
            
        if int(sep[2]) <= 2022:
            pass
        else:
            print("Некорректный год!\n")
            sys.exit()
    
a = Date("13-06-2019")
a.int_transf("13-06-2019")

b = Date("13-13-2019")
b.int_transf("13-13-2019")

'''
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления 
на ноль. Проверьте его работу на данных, вводимых пользователем. 
При вводе нуля в качестве делителя программа должна корректно обработать 
эту ситуацию и не завершиться с ошибкой.
'''

class Zero ():
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
    
    def div (self):
        try:
            a = self.v1 / self.v2
        except ZeroDivisionError:
            a = 0
        print (f'Результат деления - {a} \n')

a = Zero(4, 2)
a.div()
b = Zero(4, 0)
b.div()

'''
3. Создайте собственный класс-исключение, который должен проверять содержимое
 списка на наличие только чисел. Проверить работу исключения на реальном 
 примере. Запрашивать у пользователя данные и заполнять список необходимо 
 только числами. Класс-исключение должен контролировать типы данных 
 элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно,
 пока пользователь сам не остановит работу скрипта, введя, например, 
 команду «stop». При этом скрипт завершается, сформированный список 
 с числами выводится на экран.
Подсказка: для этого задания примем, что пользователь может вводить только
 числа и строки. Во время ввода пользователем очередного элемента 
 необходимо реализовать проверку типа элемента. Вносить его в список, 
 только если введено число. Класс-исключение должен не позволить 
 пользователю ввести текст (не число) и отобразить соответствующее
 сообщение. При этом работа скрипта не должна завершаться.
'''

class Exeption_my():
    def str_in(self):
        vol1 = None   
        arg_cycle = []
        while vol1 != 'stop': # команда «stop» становит работу скрипта
            vol1 = input('Введите число... ')
            try:
                if vol1 == 'stop':
                    break
                else:
                    vol1 = int(vol1)
                    arg_cycle.append(vol1)
            except ValueError:
                print('Ошибка! Введите число...')    
                pass
        print(f'Список введенных чисел {arg_cycle}')     
        
a = Exeption_my()
a.str_in()

'''
4. Начните работу над проектом «Склад оргтехники». Создайте класс, 
описывающий склад. А также класс «Оргтехника», который будет базовым 
для классов-наследников. Эти классы — конкретные типы оргтехники 
(принтер, сканер, ксерокс). В базовом классе определите параметры, 
общие для приведённых типов. В классах-наследниках реализуйте параметры,
 уникальные для каждого типа оргтехники.
'''
class Warehouse():
    def __init__(self):
        self.s = []
        
class Ofс_eqt():
    def __init__ (self, m_date, width, height, depth):
        self.m_date = m_date
        self.width = width
        self.height = height
        self.depth = depth
    
class Printer(Ofс_eqt):
    def __init__ (self, m_date, width, height, depth, format_l):
        super().__init__(m_date, width, height, depth)
        self.format_l = format_l

class Scanner(Ofс_eqt):
    def __init__ (self, m_date, width, height, depth, resol):
        super().__init__(m_date, width, height, depth)
        self.resol = resol
        
class Copier(Ofс_eqt):
    def __init__ (self, m_date, width, height, depth, speed):
        super().__init__(m_date, width, height, depth)
        self.speed = speed

a = Printer(2022, 10, 8, 12, 'a4')



'''
5. Продолжить работу над первым заданием. Разработайте методы, которые 
отвечают за приём оргтехники на склад и передачу в определённое 
подразделение компании. Для хранения данных о наименовании и количестве 
единиц оргтехники, а также других данных, можно использовать любую 
подходящую структуру (например, словарь).
'''

class Warehouse():
    def __init__(self):
        self.stor = {"Printer":2, "Scanner":7, "Copier":3}
        
    def accept (self, name, quantity):
        self.name = name
        self.quantity = int(quantity)
        if self.name == "Printer":
            self.stor["Printer"] = int(self.stor.get("Printer")) + self.quantity
        if self.name == "Scanner":
            self.stor["Scanner"] = int(self.stor.get("Scanner")) + self.quantity
        if self.name == "Copier":
            self.stor["Copier"] = int(self.stor.get("Copier")) + self.quantity
        print(f'Был добавлен {self.name} в количестве {self.quantity} шт. Актуальное состояние склада {self.stor}\n')
     
    def debit (self, name, quantity):
        self.name = name
        self.quantity = int(quantity)
        if self.name == "Printer":
            self.stor["Printer"] = int(self.stor.get("Printer")) - self.quantity
        if self.name == "Scanner":
            self.stor["Scanner"] = int(self.stor.get("Scanner")) - self.quantity
        if self.name == "Copier":
            self.stor["Copier"] = int(self.stor.get("Copier")) - self.quantity
        print(f'Был списан {self.name} в количестве {self.quantity} шт. Актуальное состояние склада {self.stor}\n')
            
class Ofс_eqt():
    def __init__ (self, m_date, width, height, depth):
        self.m_date = m_date
        self.width = width
        self.height = height
        self.depth = depth
    
class Printer(Ofс_eqt):
    def __init__ (self, m_date, width, height, depth, format_l):
        super().__init__(m_date, width, height, depth)
        self.format_l = format_l

class Scanner(Ofс_eqt):
    def __init__ (self, m_date, width, height, depth, resol):
        super().__init__(m_date, width, height, depth)
        self.resol = resol
        
class Copier(Ofс_eqt):
    def __init__ (self, m_date, width, height, depth, speed):
        super().__init__(m_date, width, height, depth)
        self.speed = speed

company1 = Printer(2022, 10, 8, 12, 'a4')
a = Warehouse()
a.accept("Printer", 1)
a.debit("Scanner", 3)



'''
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации 
вводимых пользователем данных. Например, для указания количества 
принтеров, отправленных на склад, нельзя использовать строковый тип 
данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» 
аксимум возможностей, изученных на уроках по ООП.
'''
class Warehouse():
    def __init__(self):
        self.stor = {"Printer":2, "Scanner":7, "Copier":3}
        
    def accept (self, name, quantity):
        self.name = name
        self.quantity = quantity
        try:
            if self.name == "Printer":
                self.stor["Printer"] = int(self.stor.get("Printer")) + self.quantity
            if self.name == "Scanner":
                self.stor["Scanner"] = int(self.stor.get("Scanner")) + self.quantity
            if self.name == "Copier":
                self.stor["Copier"] = int(self.stor.get("Copier")) + self.quantity
            print(f'Был добавлен {self.name} в количестве {self.quantity} шт. Актуальное состояние склада {self.stor}\n')
        except ValueError:
            print("Введены некорректные данные")
        except TypeError:
            print("Введены некорректные данные")
            
    def debit (self, name, quantity):
        self.name = name
        self.quantity = quantity
        try:
            if self.name == "Printer":
                self.stor["Printer"] = int(self.stor.get("Printer")) - self.quantity
            if self.name == "Scanner":
                self.stor["Scanner"] = int(self.stor.get("Scanner")) - self.quantity
            if self.name == "Copier":
                self.stor["Copier"] = int(self.stor.get("Copier")) - self.quantity
            print(f'Был списан {self.name} в количестве {self.quantity} шт. Актуальное состояние склада {self.stor}\n')
        except ValueError:
            print("Введены некорректные данные")
        except TypeError:
            print("Введены некорректные данные")
           
class Ofс_eqt():
    def __init__ (self, m_date, width, height, depth):
        self.m_date = m_date
        self.width = width
        self.height = height
        self.depth = depth
    
class Printer(Ofс_eqt):
    def __init__ (self, m_date, width, height, depth, format_l):
        super().__init__(m_date, width, height, depth)
        self.format_l = format_l

class Scanner(Ofс_eqt):
    def __init__ (self, m_date, width, height, depth, resol):
        super().__init__(m_date, width, height, depth)
        self.resol = resol
        
class Copier(Ofс_eqt):
    def __init__ (self, m_date, width, height, depth, speed):
        super().__init__(m_date, width, height, depth)
        self.speed = speed

company1 = Printer(2022, 10, 8, 12, 'a4')
a = Warehouse()
a.accept("Printer", 1)
a.debit("Scanner", 3)
a.debit("Copier", 'efw')
'''
7. Реализовать проект «Операции с комплексными числами». Создайте класс 
«Комплексное число». Реализуйте перегрузку методов сложения и умножения 
комплексных чисел. Проверьте работу проекта. Для этого создаёте 
экземпляры класса (комплексные числа), выполните сложение и умножение 
созданных экземпляров. Проверьте корректность полученного результата.
'''
class Compl_numb:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        a1 = self.a + self.b
        a2 = other.a + other.b
        return f'z = {a1 + a2}\n'

    def __mul__(self, other):
        a1 = self.a + self.b
        a2 = other.a + other.b
        return f'z = {a1 * a2}\n'
        
    def __str__(self):
        a1 = self.a + self.b
        return f'z = {a1}\n'
    
a = Compl_numb(1, -1j)
b = Compl_numb(1, 4j)
print(a)
print(a + b)
print(a * b)
