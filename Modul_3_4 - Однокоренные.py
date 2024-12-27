# Задача 3-4 "Однокоренные":
print ( 'Задача "Однокоренные" : ')
print (' * ' * 20)
print ()

# Функции
# *********************************
def single_root_words (root_word , * other_words):
    same_words = []
    r_word = root_word. lower ( )
    # print ( r_word )
   #  print ( other_words)
    for  i in  other_words :
        j =  i. lower ( )
        if  r_word in j  or j in  r_word:
            same_words. append ( i )
    return  same_words


# *********************************

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
print ( result1 )
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print ( result2 )