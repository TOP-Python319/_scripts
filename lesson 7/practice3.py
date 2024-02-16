n = int(input())

last_digit = n % 10

counter_3 = 0
counter_last_digit = 0
counter_even = 0
sum_above_5 = 0
mult_above_7 = 1
counter_0_5 = 0

while n > 0:
    digit = n % 10

    if digit == 3:
        counter_3 += 1

    if digit == last_digit:
        counter_last_digit += 1

    if digit % 2 == 0:
        counter_even += 1

    if digit > 5:
        sum_above_5 += digit

    if digit > 7:
        mult_above_7 *= digit
    
    if digit == 0 or digit == 5:
        counter_0_5 += 1
    
    n //= 10

print(f'{counter_3 = }')
print(f'{counter_last_digit = }')
print(f'{counter_even = }')
print(f'{sum_above_5 = }')
print(f'{mult_above_7 = }')
print(f'{counter_0_5 = }')