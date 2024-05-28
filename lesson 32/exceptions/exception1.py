try:
    ...
    # a + b
    # 1 / 0
    # int('hello')
except ValueError:
    print('мы перехватили ошибку ValueError')
except ZeroDivisionError:
    print('мы перехватили ошибку ZeroDivisionError')
except NameError:
    print('мы перехватили ошибку NameError')
else:
    print('else')
finally:
    print('finally')
