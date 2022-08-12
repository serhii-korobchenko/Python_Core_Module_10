class IDException(Exception):
    pass


def add_id(id_list, employee_id):
    
    if employee_id.startswith('01'):
        id_list.append(employee_id)
        return id_list
    else:         
        raise IDException


print(add_id(['See', 'GHjk', '01hjkj'], '01rhii'))