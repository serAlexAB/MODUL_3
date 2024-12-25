# Задача 3-3 "Распаковка":
print ( 'Задача "Распаковка" : ')
print (' * ' * 20)
print ()

# Функции
# ***********************************
def print_params (a = 1, b = 'строка', c = True) :
    print ('a = ' , a , '   b =  ',  b , '    c = ',  c)

#  ******************************************
# проверка по п.1.2
print_params(b=25)
print_params(c=[1, 2, 3])

# задание по  п.2
values_list  =  [77, False , ' Values']  # п.2.1
values_dict = {'a': 22, 'b': 'Next', 'c': False}  # п.2.2
print_params (* values_list )
print_params (**values_dict)

# задание по  п.3

values_list_2 = [False , ' Stroka']    # п.3.1
print_params(*values_list_2, 42)  # п.3.2

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)