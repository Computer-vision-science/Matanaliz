import math

n1t = input ("Введите количество опытов первой серии: ")
n1t = int (n1t)

n11 = input ("Введите количество успехов первой серии: ")
n11 = int (n11)

n12 = n1t - n11

n2t = input ("Введите количество опытов второй серии: ")
n2t = int (n2t)

n21 = input ("Введите количество успехов второй серии: ")
n21 = int (n21)

n22 = n2t - n21

nt1 = n11 + n21

nt2 = n12 + n22

n = n1t + n2t

Ha = input ('''
            Введите версию альтернативной гипотезы:
            1. Вариант А не равен варианту B
            2. Вариант А значимый (p1>p2)
            3. Вариант А не значимый (p1<p2)\n
            ''')

Ha = int (Ha)

T = (n11/n1t-n21/n2t)/math.sqrt((nt1/n)*(1-nt1/n)*(1/n1t+1/n2t))
print ('Значение статистики критерия: ',T)

if Ha == 1:
    if -1.96<T<1.96:
        print ('Вариант А равен варианту В')
    else:
        print ('Вариант А не равен варианту B')

if Ha == 2:
    if T<1.6449:
        print ('Вариант А равен варианту В')
    else:
        print ('Вариант А значимый')

if Ha == 3:
    if T<-1.6449:
        print ('Вариант А равен варианту В')
    else:
        print ('Вариант А не значимый')

print('Введите из таблицы значение функции нормального распределения для статистики критерия', T, ': ' )

F = input ()
F = float(F)

if T>0:
    F=1-F

if Ha == 1:
    
    P = min [2*F,2-2*F]

if Ha == 2:
    P=1-F

if Ha == 3:
    P=F
    
print ('Значение статистики критерия: ',P)

