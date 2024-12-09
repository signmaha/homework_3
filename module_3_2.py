def send_email(message, recipient, sender="university.help@gmail.com"):
    if "@" not in recipient and "@" not in sender \
            and not recipient.endswith((".com", ".ru", ".net")) \
            and not sender.endswith((".com", ".ru", ".net")):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return
    if recipient == sender:
        print("Нельзя отправить письмо самому себе!")
        return

    if sender == "university.help@gmail.com":
        print(f'Письмо успешно отправлено с адреса {sender}   на адрес   {recipient}')
        return
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса   {sender}   на адрес {recipient}')


print(send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com'))
print(send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com'))
print(send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk'))
print(send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru'))
