# 4'. Задана натуральная степень k. 
# Сформировать случайным образом список 
# коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x*2 + 4*x + 5 = 0 или x2 + 5 = 0 или 10*x*2 = 0
# k=3 => 2*x*3 + 4*x*2 + 4*x + 5 = 0

import random

def generateEql(k):
    power = ""
    for i in range(k+1):
        constant = random.randint(0, 11)
        if constant != 0 and i < k-1:
            power = power + f"{constant}*x**{k-i} + "
        elif constant != 0 and i == (k-1):
            power = power + f"{constant}*x + "
        elif constant != 0:
            power = power + f"{constant}"
    with open('file_1.txt', 'w') as data:
        data.write(power)

generateEql(2)



# ***Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
# В file1.txt :
# 2*x**2 + 4*x + 5
# В file2.txt:
# 4*x**2 + 1*x + 4
# Результирующий файл:
# 6*x**2 + 5*x + 9



# def sumEql():
#     with open('file 44(1).txt', 'r') as data:
#         eql1 = data.readline()

#     with open('file 44(2).txt', 'r') as data:
#         eql2 = data.readline()

#     # print(eql1+eql2)

#     print(sympy.simplify(f'{eql1} + {eql2}'))


# sumEql()