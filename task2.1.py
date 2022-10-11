#Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

n = int(input('input quarter number: '))
if n < 1 or n > 4:
    print('Please, repeat the input')
elif n == 1:
     print('x > 0 and y > 0')
elif n == 2:
     print('x < 0 and y > 0')
elif n == 3:
     print('x < 0 and y < 0')
elif n == 4:
     print('x > 0 and y < 0')
