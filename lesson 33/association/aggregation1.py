class Teacher:
    def __init__(self, name):
        self.name = name

    def teach(self):
        print(f"{self.name} is teaching.")


class University:
    def __init__(self, name):
        self.name = name
        self.teachers = []

    def add_teacher(self, teacher: Teacher):
        self.teachers.append(teacher)

    def conduct_classes(self):
        for teacher in self.teachers:
            teacher.teach()


# Создание объектов
teacher1 = Teacher("Alice")
teacher2 = Teacher("Bob")
university = University("MIT")

# Агрегация
university.add_teacher(teacher1)
university.add_teacher(teacher2)

# Университет проводит занятия
university.conduct_classes()
