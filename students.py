import os
import pickle
 
class Students(object):
    
    def __init__(self,name):
        
        self.filename = name
        self.key = ('name','surname','age')
        
        if self.filename in os.listdir():
            with open(self.filename, 'rb') as f:
                self.group_students = self.fileinfo()
        else:
            self.group_students = []
         
    def add_students(self):
        dct = {}
        for key in ('name','surname','age'):
            dct[key] = input(f'введите {key} ->>: ')
        self.group_students.append(dct)
        
        with open(self.filename,'wb') as datafile:
            pickle.dump(self.group_students, datafile)
        
    def info(self,number):
        number -= 1
        if len(self.group_students) < number:
            print('нет такого номера в списке')
        else:
            print(*self.group_students[number].values())
 
    def selec(self,age):
        for data in self.group_students:
            if data['age'] == age:
                print(*data.values()) 
 
    def fileinfo(self):
        with open(self.filename,'rb') as f:
            return pickle.load(f)
            
stud = Students(input('введите имя файла для записи ->  '))
print('''выберите действие.
            1- добавить студента, 2-вывод по номеру
            3- вывод по возрасту, 4 - вывод из файла
            5 - вывод списка
            для выхода - 0\n''')
 
while True: 
    f = input('ввод действия:  ')
    if f == '1':
        stud.add_students()
    elif f == '2':
        stud.info(int(input('номер ->  ')))
    elif f == '3':
        stud.selec(input('возраст-> '))
    elif f == '4':
        for data in stud.group_students:
            print(*data.values())
    elif f == '5':
        print(stud.group_students)
    else:
        break