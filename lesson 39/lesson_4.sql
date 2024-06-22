-- Конспект лекции по SQL:

-- Создание таблицы с помощью выборки данных
-- CREATE TABLE создает новую таблицу
-- AS позволяет создать таблицу на основе результата выборки
-- SELECT выбирает столбцы name и year из таблицы MarvelCharacters
-- WHERE ограничивает выборку только теми строками, у которых столбец align равен 'Bad Characters'
CREATE TABLE marvel_villains AS
SELECT name, YEAR
FROM MarvelCharacters
WHERE align = 'Bad Characters';

-- ПРАКТИКА
-- 1. Создайте новую таблицу FemaleMarvelCharacters, содержащую только женских персонажей.
-- SELECT * выбирает все столбцы из таблицы MarvelCharacters
-- WHERE ограничивает выборку только теми строками, у которых столбец sex равен 'Female Characters'
CREATE TABLE FemaleMarvelCharacters AS
SELECT * FROM MarvelCharacters WHERE sex = 'Female Characters';

-- ПРАКТИКА
-- 2. Создайте новую таблицу CharactersByYear, содержащую количество персонажей, появившихся в каждом году.
-- SELECT выбирает столбцы year и COUNT(*) - количество строк для каждого года
-- FROM указывает таблицу, из которой будут выбираться данные
-- GROUP BY группирует результаты выборки по столбцу year, чтобы подсчитать количество персонажей для каждого года
CREATE TABLE CharactersByYear AS
SELECT year, COUNT(*) AS cnt
FROM MarvelCharacters
GROUP BY year;

-- ПРАКТИКА
-- 3. Создайте таблицу MaleFemaleMarvelCharactersByEyeAndHair, которая содержит количество мужских и женских персонажей Marvel для каждой комбинации цвета волос и глаз, отсортированное по убыванию количества персонажей для каждого пола. Исключите из результатов персонажей, у которых не указаны цвет волос или глаз.
-- SELECT выбирает столбцы sex, eye, hair и COUNT(*) - количество строк для каждой комбинации пола, цвета волос и глаз
-- FROM указывает таблицу, из которой будут выбираться данные
-- WHERE исключает из выборки строки, у которых столбцы eye или hair равны NULL
-- GROUP BY группирует результаты выборки по столбцам sex, eye, hair, чтобы подсчитать количество персонажей для каждой комбинации
-- ORDER BY сортирует результаты выборки по столбцам sex и cnt в порядке убывания
CREATE TABLE MaleFemaleMarvelCharactersByEyeAndHair AS
SELECT
	sex,
	eye,
	hair,
	COUNT(*) AS cnt
FROM
	MarvelCharacters
WHERE
	eye IS NOT NULL AND
	hair IS NOT NULL AND
	sex LIKE '%male%'
GROUP BY
	sex,
	eye,
	hair
ORDER BY
	sex,
	cnt DESC

-- Удаление таблиц
-- DROP TABLE удаляет указанную таблицу из базы данных
DROP TABLE CharactersByYear;
DROP TABLE FemaleMarvelCharacters;
DROP TABLE marvel_villains;
DROP TABLE MaleFemaleMarvelCharactersByEyeAndHair;

-- Выборка строк из таблицы MarvelCharacters, где name не содержит '(Earth-616)' и содержит '(%)'
SELECT * FROM MarvelCharacters WHERE name NOT LIKE '%(Earth-616)%' AND name LIKE '%(%)'

-- Выборка уникальных значений столбца identify из таблицы MarvelCharacters
SELECT DISTINCT identify FROM MarvelCharacters;

-- Подсчет количества строк в таблице MarvelCharacters
SELECT COUNT(*) FROM MarvelCharacters;

-- Выборка уникальных значений столбцов align, eye, hair, sex, gsm, alive из таблицы MarvelCharacters
SELECT DISTINCT align FROM MarvelCharacters;
SELECT DISTINCT eye FROM MarvelCharacters;
SELECT DISTINCT hair FROM MarvelCharacters;
SELECT DISTINCT sex FROM MarvelCharacters;
SELECT DISTINCT gsm FROM MarvelCharacters;
SELECT DISTINCT alive FROM MarvelCharacters;

-- Создание таблицы Students
-- id - первичный ключ, автоинкрементное целое число
-- name - обязательное текстовое поле
-- age - обязательное целочисленное поле
-- class - текстовое поле, содержащее название учебной группы
CREATE TABLE Students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    class TEXT
);

-- Вставка данных в таблицу Students
INSERT INTO Students (name, age, class)
VALUES
	('Анна', 20, 'Python 420'),
	('Мария', 30, 'Python420'),
	('Елена', 32, 'PYTHON420'),
	('Роман', 27, 'PYTHON 420'),
	('Андрей', 29, 'QA 313'),
	('Николай', 29, 'QA 313'),
	('Ярослав', 29, 'QA 313');

-- Создание таблицы Classes
-- id - первичный ключ, автоинкрементное целое число
-- name - уникальное текстовое поле, содержащее название учебной группы
CREATE TABLE Classes (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name UNIQUE
);

-- Создание таблицы Students с внешним ключом class\_id, связанным с полем id таблицы Classes
CREATE TABLE Students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    class_id INTEGER,
    FOREIGN KEY (class_id) REFERENCES Classes(id)
);

-- Вставка данных в таблицу Classes
INSERT INTO Classes (name)
VALUES
	('Python 316'),
	('Python 319'),
	('QA 313'),
	('QA 422'),
    ('Python 317'),
	('Python 320'),
	('QA 315'),
	('QA 423');

-- Вставка данных в таблицу Students с указанием id учебной группы
INSERT INTO Students (name, age, class_id)
VALUES
    ('Мария', 23, 1),
    ('Анна', 32, 1),
    ('Елена', 32, 1),
    ('Макс', 32, 1),
    ('Роман', 22, 2),
    ('Андрей', 35, 2),
    ('Василий', 35, 3),
    ('Ольга', 17, 4),
    ('Виталий', 19, 4),
    ('Олег', 35, 5),
    ('Мартин', 35, 6),
    ('Эдуард', 32, 6),
    ('Георгий', 35, 6),
    ('Андрей', 24, 7),
    ('Василий', 22, 8);

-- Выборка данных из таблиц Students и Classes с использованием JOIN
-- SELECT выбирает столбцы name и age из таблицы Students и столбец name из таблицы Classes
-- FROM указывает таблицу Students с псевдонимом s и таблицу Classes с псевдонимом c
-- JOIN объединяет таблицы Students и Classes по столбцу class_id таблицы Students и столбцу id таблицы Classes
SELECT
	s.name AS student_name,
	s.age AS age,
	c.name AS class
FROM
	Students AS s
		JOIN Classes AS c ON s.class_id = c.id

-- Выборка данных из таблиц Students и Classes с использованием INNER JOIN
-- INNER JOIN возвращает только те строки, которые имеют совпадения в обеих таблицах
SELECT
	s.name AS student_name,
	s.age AS age,
	c.name AS class
FROM
	Students AS s
		INNER JOIN Classes AS c ON s.class_id = c.id

-- Вставка данных в таблицу Students без указания id учебной группы
INSERT INTO Students (name, age)
VALUES
	('Виталий', 73),
	('Виктор', 34),
	('Виктория', 34);

-- Вставка NULL в таблицу Classes
INSERT INTO Classes (name)
VALUES (NULL)

-- Выборка данных из таблиц Students и Classes с использованием LEFT JOIN
-- LEFT JOIN возвращает все строки из таблицы Students и соответствующие строки из таблицы Classes
SELECT
	s.name AS student_name,
	s.age AS age,
	c.name AS class
FROM
	Students AS s
		LEFT JOIN Classes AS c ON s.class_id = c.id

-- Выборка данных из таблиц Students и Classes с использованием RIGHT JOIN
-- RIGHT JOIN возвращает все строки из таблицы Classes и соответствующие строки из таблицы Students
SELECT
	s.name AS student_name,
	s.age AS age,
	c.name AS class
FROM
	Students AS s
		RIGHT JOIN Classes AS c ON s.class_id = c.id

-- Выборка данных из таблиц Students и Classes с использованием FULL OUTER JOIN
-- FULL OUTER JOIN возвращает все строки из обеих таблиц
SELECT
	s.name AS student_name,
	s.age AS age,
	c.name AS class,
	c.id
FROM
	Classes AS c
		FULL JOIN Students AS s ON c.id = s.class_id

-- Создание таблиц months и years
CREATE TABLE months (
	MONTH TEXT NOT NULL UNIQUE
);
CREATE TABLE years (
	year INTEGER NOT NULL UNIQUE
);

-- Вставка данных в таблицу months
INSERT INTO months (month)
VALUES
	('jan'),
    ('feb'),
    ('mar'),
    ('apr'),
    ('may'),
    ('jun'),
    ('jul'),
    ('aug'),
    ('sep'),
    ('oct'),
    ('nov'),
    ('dec');

-- Вставка данных в таблицу years
INSERT INTO years (year)
VALUES
	(2020),
    (2021),
    (2022),
    (2023),
    (2024),
    (2025),
    (2026),
    (2027),
    (2028),
    (2029);

-- Выборка данных из таблиц months и years с использованием CROSS JOIN
-- CROSS JOIN возвращает все возможные комбинации строк из обеих таблиц
SELECT
	m.month,
	y.year
FROM months m
	CROSS JOIN years y
ORDER BY
	y.year

-- Виды JOIN
-- INNER JOIN - возвращает строки, которые есть в обеих таблицах
-- Он же - JOIN
-- LEFT JOIN - возвращает все строки из левой таблицы и соответствующие строки из правой
-- RIGHT JOIN - возвращает все строки из правой таблицы и соответствующие строки из левой
-- FULL JOIN - возвращает все строки из обеих таблиц

-- Комментарии:

-- В примерах выше используются разные типы JOIN для выбора данных из таблиц Students и Classes.
-- INNER JOIN используется для выбора только тех строк, которые имеют совпадающие значения в обеих таблицах.
-- LEFT JOIN используется для выбора всех строк из левой таблицы (Students) и соответствующих им строк из правой таблицы (Classes). Если в правой таблице нет соответствующей строки, то в результате будут выведены NULL.
-- RIGHT JOIN используется для выбора всех строк из правой таблицы (Classes) и соответствующих им строк из левой таблицы (Students). Если в левой таблице нет соответствующей строки, то в результате будут выведены NULL.
-- FULL OUTER JOIN используется для выбора всех строк из обеих таблиц. Если в одной из таблиц нет соответствующей строки, то в результате будут выведены NULL.
-- Для каждого типа JOIN используется соответствующее ключевое слово (INNER, LEFT, RIGHT, FULL OUTER) перед ключевым словом JOIN.
-- В примерах выше также используются псевдонимы для таблиц (s для Students и c для Classes), чтобы сократить код и сделать его более читабельным.
-- В примерах выше также используется ключевое слово AS для присвоения псевдонимов столбцам в результате выборки.
-- В примерах выше используется оператор ON для указания условия соединения таблиц. Это условие должно быть verdad, чтобы строки из обеих таблиц были объединены в результате.
-- В примерах выше используется оператор SELECT для выбора столбцов из таблиц, которые будут отображаться в результате выборки.
-- В примерах выше также используется оператор FROM для указания таблиц, из которых будут выбираться данные.