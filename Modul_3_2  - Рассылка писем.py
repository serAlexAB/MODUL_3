# Задача 3-2 "Счётчик вызовов":
print('Задача "Рассылка писем":')
print('*' * 20)
print ()

# Функции
# ***********************************

def send_email (message ,recipient,  sender = "university.help@gmail.com" ):
    print ('Сообщение в письме:   ', message)
    print ('_' * (len (message)))


    if recipient != sender: # Проверяем п.3

        if sender != 'university.help@gmail.com':  # Проверяем п.4

            # Проверяем п.2

            j, ns ,nr =  0 , 0 , 0

            if sender.find('@') == -1 or recipient.find('@') == -1:
                j = 1
            for i in ('.com', '.ru', '.net'):
                if  sender.find(i) == -1:
                    ns += 1
                if recipient.find(i) == -1:
                    nr += 1
            if j == 1 or ns == 3 or nr == 3:
                print('Невозможно отправить письмо с ', sender,
                  'на адрес', recipient)
            else:
                print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ!'
                  ' Письмо отправлено с адреса ', sender,
                  'на адрес ', recipient)
        else:
            print('Письмо успешно отправлено с адреса', sender ,
              'на адрес ', recipient)
    else:
        print('Нельзя отправить письмо самому себе!')
    print()

# ***********************************

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')