# Выполняем определённую функцию в зависимости от команды
# start(), stop(), pause()

def start():
    print('Started.')

def stop():
    print('Stopped.')

def pause():
    print('Paused.')


commands = {
    'start': start, 
    'stop': stop, 
    'pause': pause
}

command = input('Введите команду: ')


# if command == 'start':
#     start()
# elif command == 'stop':
#     stop()
# elif command == 'pause':
#     pause()


commands[command]()
# когда пользователь ввёл 'start'
# по ключу 'start' из словаря commands
# извлеклось значение start
# а start это ссылка на функцию start
# 1. commands['start']()
# 2. start()