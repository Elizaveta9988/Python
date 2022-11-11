#Добавьте возможность использования скобок, меняющих приоритет операций.
#Пример:
#1+2*3 => 7;
#(1+2)*3 => 9;

from random import randint

def create_list(size, m, n):
    return [randint(m, n) for i in range(size)]

def get_unic_value(list):
    return [i for i in set(list)]

size = 10
m = 1
n = 10

origin = create_list(size, m, n)
print(origin)
print(get_unic_value(origin))