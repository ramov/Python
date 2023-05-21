import archive
import user_interface

def data_export():    
    name, surname, tel, comment = user_interface.get_data()
    result = archive.archive_search(name, surname, tel, comment)
    return result

'''  
    # name, surname, tel, comment = get_data()
    # if name != 1:
    #     archive_search(name, surname, tel, com)
    # if surname != 1:

    # if tel != 1:

    # if comment != 1:
'''    

def data_import():
    pass