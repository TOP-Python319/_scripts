# my_collection = [
#     (1, 2, 3, 4),
#     [5, 6, 7, 8],
#     {7, 8}
# ]


# for value in my_collection:
#     print(len(value))


class Duck:
    def swim_quack(self):
        print('I am a duck. I can swim and quack.')


class RoboticBird:
    def swim_quack(self):
        print('I am a robobird. I can swim and quack.')


def duck_testing(animal):
    animal.swim_quack()


d = Duck()
r = RoboticBird()

duck_testing(d)
duck_testing(r)