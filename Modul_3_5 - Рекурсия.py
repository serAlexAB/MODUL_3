#  Задача 3-5 "Рекурсивное умножение цифр":
print ( 'Задача "Рекурсивное умножение цифр"')
print (' * ' * 20)
print ()

# Функция для рекурсии
# *********************************

def get_multiplied_digits (number):
    if number % 10 == 0:
       number = number // 10
    str_number = str(number)
    first = int(str_number[0])
    if (len(str_number)) > 1 :
        first = int(str_number[:1])
        return (get_multiplied_digits (int((str_number[1:])))) * first
    else:

        return  first
# *********************************
result = get_multiplied_digits (40203 )
print(' Результат рекурсии 1: ' , result)

result2 = get_multiplied_digits(402030)
print(' Результат рекурсии 2: ' , result2)

