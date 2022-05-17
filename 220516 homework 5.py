#1. Создать программный файл в текстовом формате, записать в него 
#построчно данные, вводимые пользователем. Об окончании ввода данных 
#будет свидетельствовать пустая строка.
damp = []
while True:
    a = input('Введите строку данных... ')
    b = a + '\n'
    if b == '\n':
        print('Файл сохранен.')
        break
    else:
        b = a + '\n'
        damp.append(b) 
with open("my_file.txt", 'w+', encoding="utf-8") as f_obj:
    f_obj.writelines(damp)
    
######################################################################
#2. Создать текстовый файл (не программно), сохранить в нём несколько 
#строк, выполнить подсчёт строк и слов в каждой строке.

with open ("my_file.txt", "r") as f_obj:
    content = f_obj.readlines()
    str_v = len(content)
    for i in range(str_v):
        un_str_v = content[i].split()
        print(f"Количество слов в строке № {i+1} составляет: {len(un_str_v)}")
    print("Всего количество строк составляет: ", str_v)
    
#######################################################################    
#3. Создать текстовый файл (не программно). Построчно записать фамилии 
#сотрудников и величину их окладов (не менее 10 строк). Определить, 
#кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих 
#сотрудников. Выполнить подсчёт средней величины дохода сотрудников.
#Пример файла:
#Иванов 23543.12
#Петров 13749.32
my_file = open("my_file.txt", "w+", encoding="utf-8") 
my_file.write("Баран 23543.12\
\nАндрухович 34214.34\
    \nЗданович 23423.54\
        \nГулеватая 12344.23\
            \nГурин 41234.32\
                \nКулеш 41234.78\
                    \nТетерюков 19234.09\
                        \nТотчик 14234.78\
                            \nСеленчик 41234.97\
                                \nХиревич 31234.20")        
my_file.close()

with open ("my_file.txt", "r", encoding="utf-8") as f_obj:
    d = [line.split() for line in f_obj]
    d2 = []
    for i in d:
        if float(i[1]) < 20000:
            print(f"{i[0]} имеет оклад меньше 20000.")
        d2.append(float(i[1]))
    print(f"Cредняя величина дохода сотрудников {round(sum(d2)/len(d2), 2)}.")
    
######################################################################
#4. Создать (не программно) текстовый файл со следующим содержимым:
#One — 1
#Two — 2
#Three — 3
#Four — 4
#Напишите программу, открывающую файл на чтение и считывающую построчно 
#данные. При этом английские числительные должны заменяться на русские. 
#Новый блок строк должен записываться в новый текстовый файл.
my_file = open("my_file.txt", "w+", encoding="utf-8") 
my_file.write("One — 1\
\nTwo — 2\
    \nThree — 3\
        \nFour — 4")        
my_file.close()

my_translator = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре', 'Five': 'Пять'}        

with open ("my_file.txt", "r", encoding="utf-8") as f_obj:
    d = [line.split() for line in f_obj]
    d2 = []
    my_file1 = open("my_file_Translate.txt", "w")
    my_file1.close()
    for i in d:
        print(i[0])
        print(my_translator.get(i[0]))
        my_file = open("my_file_Translate.txt", "a", encoding="utf-8")
        my_file.write((my_translator.get(i[0])+" "+i[1]+" "+i[2]+"\n")) 
        my_file.close()

#######################################################################
#5. Создать (программно) текстовый файл, записать в него программно 
#набор чисел, разделённых пробелами. Программа должна подсчитывать сумму 
#чисел в файле и выводить её на экран.
import random
my_file = open("my_file.txt", "w") 
for i in range(random.randint(1,111)):
    my_file.write(str(random.randint(1,1111))+" ")                  
my_file.close()

my_file = open ("my_file.txt", "r") 
damp1 =  my_file.read()
my_file.close()
b = damp1.split() 
b = [int(x) for x in b]
print("Сумма чисел в файле составляет: ", sum(b))

#######################################################################
#6. Сформировать (не программно) текстовый файл. В нём каждая строка 
#должна описывать учебный предмет и наличие лекционных, практических 
#и лабораторных занятий по предмету. Сюда должно входить и количество 
#занятий. Необязательно, чтобы для каждого предмета были все типы занятий.
#Сформировать словарь, содержащий название предмета и общее количество 
#занятий по нему. Вывести его на экран.
#Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
#Физика: 30(л) — 10(лаб)
#Физкультура: — 30(пр) —
#Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
with open ("my_file.txt", "w", encoding="utf-8") as my_file: 
    my_file.write("Информатика: 100(л) 50(пр) 20(лаб)\
    \nМатематика: 18(л) 40(пр) 12(лаб)\
        \nФизика: 30(л) — 10(лаб)\
            \nБиология: 10(л) - 5(лаб)\
                \nПравоведение: 11(л) - -\
                    \nФизкультура: — 30(пр) —\
                        \nХимия: 20(л) 10(пр) 15(лаб)")                   


with open ("my_file.txt", "r", encoding="utf-8") as f_obj:
    d = [line.split() for line in f_obj]
    key_vol_lst = []
    vol_lst = [];
    for i in d:
        key_vol_lst.append(i[0])
        vol_a = []
        vol1 = i[1].split('(')
        try:
            vol_a.append(int(vol1[0]))
        except ValueError:
            vol_a.append(0)
            pass
        vol2 = i[2].split('(')
        try:
            vol_a.append(int(vol2[0]))
        except ValueError:
            vol_a.append(0)
            pass
        vol3 = i[3].split('(')
        try:
            vol_a.append(int(vol3[0]))
        except ValueError:
            vol_a.append(0)
            pass
        vol_lst.append(vol_a)
    vol2_lst = [sum(x) for x in vol_lst] 
    my_new_dict = {k:v for k, v in zip(key_vol_lst,vol2_lst)}
    print(my_new_dict)

######################################################################
#7. Создать вручную и заполнить несколькими строками текстовый файл, 
#в котором каждая строка будет содержать данные о фирме: название, 
#форма собственности, выручка, издержки.
#Пример строки файла: firm_1 ООО 10000 5000.
#Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчёт средней
# прибыли её не включать.
#Далее реализовать список. Он должен содержать словарь с фирмами 
#и их прибылями, а также словарь со средней прибылью. Если фирма 
#получила убытки, также добавить её в словарь (со значением убытков).
#Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, 
#{“average_profit”: 2000}].
#Итоговый список сохранить в виде json-объекта в соответствующий файл.
#Пример json-объекта:
#[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 
    #2000}]
#Подсказка: использовать менеджер контекста.
with open ("my_file.txt", "w", encoding="utf-8") as my_file: 
    my_file.write("Савушкин_продукт ОАО 2700 122\
    \nСерволюкс ОАО 450 420\
        \nМилавица ЗАО 1000 900\
            \nСерж ООО 1657 1500\
                \nБелвест СООО 102 110\
                    \nБеллакт ООО 180 165")   

with open ("my_file.txt", "r", encoding="utf-8") as my_file: 
    d = [line.split() for line in my_file]
    key_vol_lst = []
    vol_lst = [];
    for i in d:
        key_vol_lst.append(i[0])
        vol_lst.append(int(i[2])-int(i[3]))
    firm_dict = {k:v for k, v in zip(key_vol_lst,vol_lst)}
    profit = [x for x in vol_lst if x > 0]; profit = sum(profit)
    average_profit = {'average_profit':profit/len(d)}
    vol_lst = []; vol_lst.append(firm_dict); vol_lst.append(average_profit)
    print(vol_lst)
    
import json 
       
with open("data_file.json", "w", encoding="utf-8") as write_file:
    json.dump(vol_lst, write_file, ensure_ascii=False)

import json
data = {}
data['people'] = []
data['people'].append({
    'name': 'Scott',
    'website': 'pythonist.ru',
    'from': 'Nebraska'
})
data['people'].append({
    'name': 'Larry',
    'website': 'pythonist.ru',
    'from': 'Michigan'
})
data['people'].append({
    'name': 'Tim',
    'website': 'pythonist.ru',
    'from': 'Alabama'
})
with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)