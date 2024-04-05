# декоратор который замеряет время выполнения функции

def benchmark(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end-start))
        return return_value
    return wrapper


@benchmark
def fetch_webpage(url):
    import requests
    webpage = requests.get(url)
    return webpage.text


@benchmark
def factoril(n):
    if n == 1:
        return 1
    else:
        return n * factoril(n-1)


# g = fetch_webpage('https://google.com')
# print(g)
# ya = fetch_webpage('https://ya.ru')
# print(ya)

print(factoril(100))