#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
#Пример:
#- x=34; y=-30 -> 4
#- x=2; y=4-> 1
#- x=-34; y=-30 -> 3

x = int(input('input x: '))
y = int(input('input y: '))
if x > 0 and y > 0:
     print('1')
if x < 0 and y > 0:
     print('2')
if x < 0 and y < 0:
     print('3')
if x > 0 and y < 0:
     print('4')