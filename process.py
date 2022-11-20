from User_Interface import user_choice
from work_file import read_file

def data_processor(lst, n):
    a = []
    if n == 6:
        return lst
    elif 0 < n < 6:
        for i in lst:
            a.append(i[n-1])
        return a
    else:
        return 'До встречи!'