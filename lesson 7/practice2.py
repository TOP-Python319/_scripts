n = int(input())

while n > 1000:
    n //= 10

print(n % 10)

# >>> n = 19745
# >>> n > 1000
# True
# >>> n //= 10
# >>> n
# 1974
# >>> n > 1000
# True
# >>> n //= 10
# >>> n
# 197
# >>> n > 1000
# False
# >>> n % 10
# 7
