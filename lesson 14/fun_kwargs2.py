def print_user_info(
        name, 
        surname, 
        age, 
        city, 
        *children,  # для наглядности "переименовал" *args в *children
        **additinal_info  # для наглядности "переименовал" **kwargs в **additinal_info
):
    print(f'Имя: {name}')
    print(f'Фамилия: {surname}')
    print(f'Возраст: {age}')
    print(f'Город проживания: {city}')
    if len(children) > 0:
        print(f'Дети: {" ".join(children)}')
    if len(additinal_info) > 0:
        print(f'Дополнительная информация:')
        for key, value in additinal_info.items():
            print(f'{key}: {value}')


ch = ['John', 'Karen', 'Lilly']
add_inf = {'salary': 2000, 'job': 'hr-manager'}

print_user_info('Jack', 'Smith', 48, 'New York', *ch, **add_inf)