# Задача "Счётчик вызовов":
print('Задача "Счётчик вызовов":')
print

# Функции
# ***********************************
def  count_calls  ():
    global calls
    calls += 1

# ***********************************
def string_info (string):
    count_calls ()
    str_inf = ()
    str_inf  = ((len (string)), ) + (string.upper(),)  + ((string.lower()), )

    return (str_inf)

# ***********************************
def is_contains (string , list_to_search):
    count_calls ()
    True_ = False
    for i in list_to_search:
         if string.lower() == i.lower():
            True_ =True
            break
    return (True_)

# ***********************************

# Основной блок команд

calls = 0

print(string_info('Capybara'))

print(string_info('Armageddon'))

print (is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN

print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches

print(calls)
