
def archive_search(name, surname, tel, comment):
    key_value_lst = ['Имя', 'Фамилия', 'Телефон', 'Комментарий']
    user_value_lst = [name, surname, tel, comment]
    result_lst = []
    step = 1
    k = 0
    for i in user_value_lst:
        if i != '1':
            j = 0
            while j < len(archive):
                if i == archive[j][key_value_lst[k]]:
                    if archive[j] not in result_lst:
                        result_lst.append(archive[j])
                j += step
            k += step
        else:
            k += step

    if result_lst != []:
        return result_lst
    else:
        result_lst = 'По вашему запросу совпадений нет'
        return result_lst

archive = [{'Имя': 0, 'Фамилия': 0, 'Телефон': 0, 'Комментарий': 0}, \
           {'Имя': 'Иван', 'Фамилия': 'Иванович', 'Телефон': '89777777777', 'Комментарий': 0}, \
           {'Имя': 'Петр', 'Фамилия': 'Петрович', 'Телефон': '89666666666', 'Комментарий': 0}]
