# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора
# класса (метод __init__()), который должен принимать данные 
# ( список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, 
# расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# 
# 31    32         3    5    32        3    5    8    3
# 37    43         2    4    6         8    3    7    1
# 51    86        -1   64   -8
# Следующий шаг — реализовать перегрузку метода __str__() для вывода 
# матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции 
# сложения двух объектов класса Matrix (двух матриц). 
# Результатом сложения должна быть новая матрица.
# одсказка: сложение элементов матриц выполнять поэлементно — 
# первый элемент первой строки первой матрицы складываем 
# с первым элементом первой строки второй матрицы и т.д.

from itertools import zip_longest

class Matrix:
    def __init__(self, list_vol):
        self.list_vol = list_vol
        
    def __add__(self, oser):
        '''
        Можно работать с листами любой длины и любой вложенности
        '''
        new_list_vol = [[] for _ in range(max(len(self.list_vol), len(oser.list_vol)))] 
        for y, y2 in zip_longest(range(len(self.list_vol)), range(len(oser.list_vol))):
            if y == None:
                for x2 in range(len(oser.list_vol[y2])): 
                    new_list_vol[y2].append(oser.list_vol[y2][x2])
            elif y2 == None:
                for x in range(len(self.list_vol[y])): 
                    new_list_vol[y].append(self.list_vol[y][x])        
            else:                
                for x, x2 in zip_longest(range(len(self.list_vol[y])), range(len(oser.list_vol[y2]))):
                    if x == None:
                        new_list_vol[y2].append(oser.list_vol[y2][x2])
                    elif x2 == None:   
                        new_list_vol[y].append(self.list_vol[y][x])
                    else:    
                        new_list_vol[y].append(self.list_vol[y][x]+oser.list_vol[y2][x2])  
        return Matrix(new_list_vol)
        
         
    def __str__(self):
        vol_print = ""
        for y in self.list_vol:
            y = [str(i) for i in y]
            y_str = " ".join(y)
            vol_print += y_str + '\n'
        return vol_print                               

list_vol_a = [[51,86,9,8],[37,43,48],[51,86,9],[37,43,48],[37,43,48]]
a = Matrix(list_vol_a)

list_vol_b = [[1,2,4],[3,4,7,3,4,3],[0,8,4],[0,8,8,4]]
b = Matrix(list_vol_b)
print(a+b)

#######################################################################
# 2. Реализовать проект расчёта суммарного расхода ткани на 
# производство одежды. 
# Основная сущность (класс) этого проекта — одежда, которая 
# может иметь определённое название. К типам одежды в этом проекте 
# относятся пальто и костюм. У этих типов одежды существуют параметры: 
# размер (для пальто) и рост (для костюма). 
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать 
# формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). 
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике 
# полученные на этом уроке знания: реализовать абстрактные классы для 
# основных классов проекта, проверить на практике работу декоратора 
# @property.
class Clothes:
    amount_vol = [[],[]] 

    @staticmethod
    def sum_cloth():        
        amount_vol_r = []
        for x in Clothes.amount_vol:
            amount_vol_r.extend(x)
        print(sum(amount_vol_r))
    
class Coat(Clothes):
    def __init__(self, size):
        self.size = size  
    
    @property    
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, size):
        self.__size = size/6.5 + 0.5
        Clothes.amount_vol[0].append(self.__size)
        
    
class Suit(Clothes):
    def __init__(self, height):
        self.height = height 
    
    @property    
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, height):
        self.__height = 2*height + 0.3
        Clothes.amount_vol[1].append(self.__height)
    

Elema = Coat(5)
Comintern = Suit(5)
Bigstar = Coat(4)
Keyman = Suit(3)
Pizhon = Coat(6)
Clothes.sum_cloth() #сведения о затраченной ткани



# 3. Реализовать программу работы с органическими клетками, 
# состоящими из ячеек. Необходимо создать класс Клетка. 
# В его конструкторе инициализировать параметр, соответствующий 
# количеству ячеек клетки (целое число). В классе должны быть 
# реализованы методы перегрузки арифметических операторов: сложение 
# (__add__()), вычитание (__sub__()), умножение (__mul__()), 
# деление (__truediv__()). Данные методы должны применяться только 
# к клеткам и выполнять увеличение, уменьшение, умножение 
# и целочисленное (с округлением до целого) деление клеток, 
# соответственно.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки 
# должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять 
# только если разность количества ячеек двух клеток больше нуля, 
# иначе выводить соответствующее сообщение.
# Умножение. Создаётся общая клетка из двух. Число ячеек общей 
# клетки определяется как произведение количества ячеек этих двух клеток.
# Деление. Создаётся общая клетка из двух. Число ячеек общей клетки 
# определяется как целочисленное деление количества ячеек этих двух 
# клеток.

# В классе необходимо реализовать метод make_order(), принимающий 
# экземпляр класса и количество ячеек в ряду. Данный метод позволяет 
# организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., 
# где количество ячеек между \n равно переданному аргументу. 
# Если ячеек на формирование ряда не хватает, то в последний ряд 
# записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек 
# в ряду — 5. Тогда метод make_order() вернёт строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. 
# Тогда метод make_order() вернёт строку: *****\n*****\n*****.
# Подсказка: подробный список операторов для перегрузки доступен по 
# ссылке.

class Org_cell:
    def __init__(self, sells):
        self.sells = int(sells)

    def __str__(self):
        return f'Количество ячеек новой клетки {self.sells}.\nВид клетки: {self.sells * "*"}\n'

    def __add__(self, other):
        return Org_cell(self.sells + other.sells)

    def __sub__(self, other):
        if self.sells > other.sells:
            return Org_cell(self.sells - other.sells) 
        elif self.sells < other.sells:
            return Org_cell(other.sells - self.sells) 
        else:
            print ("Клетка уничтожена!")
       
    def __mul__(self, other):
        return Org_cell(int(self.sells * other.sells))

    def __truediv__(self, other):
        if self.sells > other.sells:
            return Org_cell(self.sells // other.sells) 
        elif self.sells < other.sells:
            return Org_cell(other.sells // self.sells) 
        else:
            print ("Клетка уничтожена!")

    def make_order(self, row_of_cells):
        row = ''
        for x in range(int(self.sells / row_of_cells)):
            row += f'{row_of_cells * "*"}\n'
        row += f'{(self.sells % row_of_cells)* "*"}\n'
        return row

a = Org_cell(3)
b = Org_cell(12)
print(a)
print(b)
print(a + b)
print(a - b)
print(a * b) 
print(a / b)  
print(a.make_order(5))
print(b.make_order(3))
       
