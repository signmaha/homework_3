from test.test_email.test_message import first


def get_multipiled_digits(number):
    number = int(number)

    str_number = str(number)

    first = int(str_number[0])

    if len(str_number) > 1:
        return first * get_multipiled_digits(int(str_number[1:]))
    else:
        return first

        num = input('Введите целое число')
        print(f'произвидение цифр числа {num} :', get_multipiled_digits(num))

        # get_multipiled_digits(40203) - 4*
        # get_multipiled_digits(203) - 4* 2
        # get_multipiled_digits(3) - 4* 2* 3
    result = get_multipiled_digits(40203)
    print(result)
    result2 = get_multipiled_digits(402030)
    print(result2)
