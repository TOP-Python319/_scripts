
# декоратор который замеряет время выполнения функции

def benchmark(iterations):

    def actual_decorator(func):
        import time

        def wrapper(*args, **kwargs):
            total = 0
            for i in range(iterations):
                start = time.time()
                return_value = func(*args, **kwargs)
                end = time.time()
                total = total + (end - start)
            print('[*] Среднее время выполнения: {} секунд.'.format(total / iterations))
            return return_value
        
        return wrapper

    return actual_decorator


@benchmark(iterations=10)
def fetch_webpage(url):
    import requests
    webpage = requests.get(url)
    return webpage.text


g = fetch_webpage('https://google.com')
print(g)
