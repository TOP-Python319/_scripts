# функция timer, которая засекает сколько прошло времени с момента первого вызова

import datetime
import time


def timer() -> callable:
    start = datetime.datetime.now()
    def inner() -> datetime.timedelta:
        return round((datetime.datetime.now() - start).total_seconds(), 4)

    return inner


f1 = timer()
print(f1())
time.sleep(2)
print(f1())
time.sleep(2)
print(f1())
print(f1())
print(f1())


print('######################')
f2 = timer()
print(f2())
time.sleep(2)
print(f2())