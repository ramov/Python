import controller

def start():
    temp = input('Введите 1, если хотите найти или 2, если хотите добавить: ')
    if temp == '1':
        print(controller.data_export())
    elif temp == '2':
        print(controller.data_import())
    else:
        print('Не верный ввод, попробуйте еще раз!\n')
        start()

def get_data():    
    name = input('Введите Имя или 1, что бы пропустить: ')
    surname = input('Введите Фамилию или 1, что бы пропустить: ')
    tel = input('Введите Телефон или 1, что бы пропустить: ')
    comment = input('Введите Комментарий или 1, что бы пропустить: ')
    
    return name, surname, tel, comment



    


