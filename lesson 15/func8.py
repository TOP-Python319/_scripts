# a * x**2 + b*x + c
# квадратный трехчлен

def generate_poly(a, b, c):
    def poly(x):
        return a * x**2 + b * x + c
    return poly

f = generate_poly(a=1, b=2, c=3)
# def generate_poly(1, 2, 3):
#     def poly(x):
#         return 1 * x**2 + 2 * x + 3
#     return poly

g = generate_poly(a=2, b=0, c=1)
h = generate_poly(a=-3, b=-10, c=50)

print(f(1))
print(g(2))
print(h(-1))