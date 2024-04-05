# write tail recursion for factorial
    
def factorial_tail(n, accumulator=1):
    if n == 1:
        return accumulator
    else:
        return factorial_tail(n - 1, accumulator * n)
    

print(factorial_tail(1000))