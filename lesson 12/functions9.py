# def draw_star_box(height, width): 
#     for _ in range(height * 2):
#         print('*' * width)
#     print()

# draw_star_box(3, 5)

def draw_star_box(height, width): 
    height = 5
    width = 5
    for _ in range(height):
        print('*' * width)
    print()

h = 10
w = 10
draw_star_box(h, w)
print(h, w)