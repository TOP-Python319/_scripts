# можно открыть несколько файлов

with open('venv.txt') as f1, open('test.txt') as f2:
    print(f1.read())
    print(f2.read())