-- Lesson 6
-- 24.04.2024
-- Нормализация данных

-- Создаем таблицу School
CREATE TABLE IF NOT EXISTS School (
    StudentName TEXT,
    CourseName TEXT,
    CourseDescription TEXT,
    TeacherName TEXT,
    TeacherEmail TEXT
);

-- Заполняем таблицу School
INSERT INTO School (StudentName, CourseName, CourseDescription, TeacherName, TeacherEmail)
VALUES
    ('Сергей Иванов', 'Математика', 'Математика для любознательных', 'Андреенко Андрей', 'andreenko@a.ru'),
    ('Cергей Иванов', 'Химия', 'Химия для юных подрывников', 'Андреенко Андрей', 'andreenko@a.ru'),
    ('Александр Петров', 'Python', 'Python для начинающих', 'Петров Петр', 'petr@a.ru')


-- Приводим это к первой нормальной форме
-- Удаление перечней в с столбцах (имя, фамилия разносим по разным столбцам)
Drop table School;

-- Создаем таблицу School
CREATE TABLE IF NOT EXISTS School (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    StudentName TEXT,
    StudentSurname TEXT,
    CourseName TEXT,
    CourseDescription TEXT,
    TeacherName TEXT,
    TeacherSurname TEXT,
    TeacherEmail TEXT
);


-- Заполняем таблицу School
INSERT INTO School (StudentName, StudentSurname, CourseName, CourseDescription, TeacherName, TeacherSurname, TeacherEmail)
VALUES
    ('Сергей', 'Иванов', 'Математика', 'Математика для любознательных', 'Андрей', 'Андреенко', 'andreenko@a.ru'),
    ('Сергей', 'Иванов', 'Химия', 'Химия для юных подрывников', 'Андрей', 'Андреенко', 'andreenko@a.ru'),
    ('Александр', 'Петров', 'Python', 'Python для начинающих', 'Петр', 'Петров', 'petr@a.ru')


-- Приводим это ко второй нормальной форме
-- У нас не будет составных ключей, поэтому просто выделим уникальные столбцы в отдельные таблицы
-- Это закроет и третью нормальную форму
Drop table School;

-- Создадим нормализованные таблицы
-- Студенты
-- Паспортные данные студентов
-- Кафедра
-- Преподаватели

-- Таблица Студенты
-- id - идентификатор студента
-- Name - имя студента
-- Surname - фамилия студента
-- PassportId - паспортные данные студента
-- DepartmentId - идентификатор кафедры
CREATE TABLE IF NOT EXISTS Students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT, -- Стоило озабодится not null хотя бы для имени
    Surname TEXT,
    PassportId INTEGER UNIQUE,
    DepartmentId INTEGER,

    FOREIGN KEY (PassportId) REFERENCES PassportData(id)
);

-- Таблица Паспортные данные студентов
-- id - идентификатор паспортных данных
-- PassNumber - номер паспорта
CREATE TABLE IF NOT EXISTS PassportData (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    PassNumber TEXT UNIQUE
);


-- Таблица Кафедра
-- id - идентификатор кафедры
-- Name - название кафедры
CREATE TABLE IF NOT EXISTS Departments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT UNIQUE
);

-- Таблица Преподаватели
-- id - идентификатор преподавателя
-- Name - имя преподавателя
CREATE TABLE IF NOT EXISTS Teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT,
    Surname TEXT,
    Email TEXT
);

-- Таблица СтудентыПреподаватели
-- id - идентификатор связи
-- StudentId - идентификатор студента
-- TeacherId - идентификатор преподавателя
CREATE TABLE IF NOT EXISTS StudentsTeachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    StudentId INTEGER NOT NULL,
    TeacherId INTEGER NOT NULL,

    FOREIGN KEY (StudentId) REFERENCES Students(id),
    FOREIGN KEY (TeacherId) REFERENCES Teachers(id),

    UNIQUE (StudentId, TeacherId)
);


-- Добавим паспорта студентов в таблицу PassportData
INSERT INTO PassportData (PassNumber)
VALUES
    ('1234567890'),
    ('0987654321'),
    ('1111111111');


-- Добавим кафедры в таблицу Departments
INSERT INTO Departments (Name)
VALUES
    ('Математика'),
    ('Химия'),
    ('Программирование');

-- Добавим студентов
-- Мы не сможем этого сделать, потому, что PassportId должен быть уникальным
INSERT INTO Students (Name, Surname, PassportId, DepartmentId)
VALUES
    ('Сергей', 'Иванов', 1, 1),
    ('Сергей', 'Иванов', 2, 2),
    ('Александр', 'Петров', 3, 3),
    ('Александр', 'Петров', 1, 1);

-- Пробуем сделать запрос, где мы даем номер паспорта и название кафедры
-- и добываем их id для создания записи в таблице студентов
INSERT INTO Students (Name, Surname, PassportId, DepartmentId)
VALUES
    ('Сергей', 
    'Иванов', 
    (SELECT id FROM PassportData WHERE PassNumber = '1234567890'), 
    (SELECT id FROM Departments WHERE Name = 'Математика')),

    ('Сергей',
    'Иванов',
    (SELECT id FROM PassportData WHERE PassNumber = '0987654321'),   '),
    (SELECT id FROM Departments WHERE Name = 'Химия')),

    ('Александр',
    'Петров',
    (SELECT id FROM PassportData WHERE PassNumber = '1111111111'),
    (SELECT id FROM Departments WHERE Name = 'Программирование'));


-- Добавим преподавателей
INSERT INTO Teachers (Name, Surname, Email)
VALUES
    ('Андрей', 'Федоров', 'af@mail.ru'),
    ('Александр', 'Cидоров', 'as@mail.ru'),
    ('Анна', 'Степанова', 'sa@mail.ru');

-- Добавим связи студентов и преподавателей
INSERT INTO StudentsTeachers (StudentId, TeacherId)
VALUES
    (1, 1);

-- Добавим связь студента и преподавателя, через и Имя и Фамилию
-- Александр Петров и Анна Степанова
INSERT INTO StudentsTeachers (StudentId, TeacherId)
VALUES
    ((SELECT id 
    FROM Students 
    WHERE Name = 'Сергей' 
    AND Surname = 'Иванов' 
    AND DepartmentId = (SELECT id FROM Departments WHERE Name = 'Математика')),
    
    (SELECT id 
    FROM Teachers 
    WHERE Name = 'Анна' 
    AND Surname = 'Степанова'));


-- Данные студента ID 1
SELECT * FROM Students WHERE id = 1;

-- А теперь с номером паспорта и кафедрой
SELECT Students.id, Students.Name, Students.Surname, PassportData.PassNumber, Departments.Name
FROM Students
JOIN PassportData ON Students.PassportId = PassportData.id
JOIN Departments ON Students.DepartmentId = Departments.id
WHERE Students.id = 1;


-- А теперь с номером паспорта и кафедрой
SELECT
    Students.id,
    Students.Name AS имя_студента,
    Students.Surname AS фамилия_студента,
    PassportData.PassNumber AS номер_паспорта,
    Departments.Name AS кафедра
FROM Students
    INNER JOIN PassportData ON Students.PassportId = PassportData.id
    INNER JOIN Departments ON Students.DepartmentId = Departments.id
WHERE
    Students.id = 1;

-- Практика
-- Получите номер паспорта студента с именем Сергей, фамилией Иванов
-- Попробуйте добавить в выборку кафедра not in ('Программирование', 'Химия')
SELECT Students.id, Students.Name AS Имя, Students.Surname AS Фамилия, PassportData.PassNumber AS "Номер паспорта", Departments.Name AS Кафедра
FROM Students
JOIN PassportData ON Students.PassportId = PassportData.id
JOIN Departments ON Students.DepartmentId = Departments.id
WHERE Students.Name = 'Сергей' AND Students.Surname = 'Иванов' AND Departments.Name NOT IN ('Программирование', 'Химия');

-- Вывести всех преподавателей с их связанными студентами
SELECT
    Teachers.Name имя_преподавателя,
    Teachers.Surname фамилия_преподавателя,
    Students.Name имя_студента,
    Students.Surname фамилия_студента,
    Students.PassportId
FROM Teachers
    INNER JOIN StudentsTeachers ON Teachers.id = StudentsTeachers.TeacherId
        INNER JOIN Students ON StudentsTeachers.StudentId = Students.id
