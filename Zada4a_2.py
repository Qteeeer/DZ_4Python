# 2'. Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
# * 6 -> [1,2,3]
# * 144 -> [2,3]

def SimpMult(num):
    result = [1]
    i = 2
    mutable = num
    while i <= num:
        if num % i == 0:
            if i not in result:
                result.append(i)

            num //= i
        else:
            i += 1
    print(f'Простые множители числа {mutable} : {result}')


Nnum = int(input("Введите число для разложения на простые множители: "))
SimpMult(Nnum)