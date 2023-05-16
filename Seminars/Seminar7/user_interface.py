import logger

def get_data():
    
    a = input('введите число: ')
    operator = input('введите действие над числом: ')
    b = input('введите число: ')

    logger.log_all(f'Мы получаем число: {a}, оператор = "{operator}", число {b}')

    if 'j' in a:
        a = complex(a)
    else:
        a = int(a)

    if 'j' in b:
        b = complex(b)
    else:
        b = int(b)

    return a, b, operator
