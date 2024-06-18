/*18. Название: Персонажи с максимальным количеством появлений в десятилетие
     - Описание: Найти персонажа с максимальным количеством появлений в каждом десятилетии начиная с 1940-х.
     			Вывести десятилетие, имя персонажа и количество появлений.
     - Выборка: Группировка по десятилетиям (используя год),
     	определение персонажа с максимальным количеством 
     	появлений в каждом десятилетии.
     - Количество строк: 9*/
SELECT
	name,
	MAX(appearances) AS appearances,
	decade
FROM (SELECT name, appearances, (year / 10) * 10 AS decade
	  FROM MarvelCharacters
      WHERE year IS NOT NULL)
GROUP BY
	decade
ORDER BY
	decade;

-- другой метод
WITH mc_decades AS
	(SELECT name, appearances, (year / 10) * 10 AS decade
	 FROM MarvelCharacters
     WHERE year IS NOT NULL)
     
SELECT
	name,
	MAX(appearances) AS appearances,
	decade
FROM mc_decades
GROUP BY
	decade
ORDER BY
	decade


-- 1. Вывести всех персонажей, у которых количество появлений больше, 
-- чем у персонажа с именем 'Wanda Maximoff'.
SELECT name, appearances
FROM MarvelCharacters
WHERE appearances > (SELECT appearances
					 FROM MarvelCharacters
					 WHERE name = 'Wanda Maximoff (Earth-616)')


-- 2. Вывести всех персонажей, которые появились в том же году, что и 'Iron Man'.
SELECT name
FROM MarvelCharacters
WHERE year = (SELECT year
			  FROM MarvelCharacters
			  WHERE name = 'Iron Man (Anthony \"Tony\" Stark)')


-- 3. Вывести всех персонажей с цветами глаз,
-- которые встречаются менее чем у 10 персонажей.
SELECT name, eye, year
FROM MarvelCharacters
WHERE eye IN (SELECT eye
			  FROM MarvelCharacters
              GROUP BY eye
              HAVING COUNT(*) < 10)


-- ПРАКТИКА
-- 4. Задача: Вывести имена и количество появлений всех персонажей,
-- количество появлений которых превышает среднее количество появлений
-- среди всех персонажей. [2034 строк]
SELECT name, appearances
FROM MarvelCharacters
WHERE appearances > (SELECT AVG(appearances) FROM MarvelCharacters)


-- ПРАКТИКА
-- 5. Задача: Вывести имена и год первого появления всех персонажей,
-- которые появились раньше, чем Капитан Америка. [290 строк]
SELECT name, appearances, year
FROM MarvelCharacters mc
WHERE year < (SELECT year
			  FROM MarvelCharacters mc
			  WHERE name = 'Captain America (Steven Rogers)')


-- ПРАКТИКА
-- 6. Задача: Вывести имена и цвет волос всех персонажей, 
-- которые имеют уникальный цвет волос
-- (т.е. есть нет других персонажей с таким же цветом волос). [2 строки]
SELECT name, hair, year
FROM MarvelCharacters
WHERE hair IN (SELECT hair
			   FROM MarvelCharacters
               GROUP BY hair
               HAVING COUNT(*) = 1)


-- ПРАКТИКА
-- 7. Задача: Вывести имена и пол всех персонажей,
-- у которых пол совпадает со вторым по популярности полом в базе данных. [3837 строк]
SELECT
    name,
    sex
FROM 
    MarvelCharacters
WHERE
    sex = (SELECT sex FROM (
	    	   SELECT sex, COUNT(*) as cnt
		       FROM MarvelCharacters
	           WHERE sex IS NOT NULL
	           GROUP BY sex
	           ORDER BY cnt DESC
	           LIMIT 1
	           OFFSET 1)
	      )


-- Создаем новую таблицу с именем Students
CREATE TABLE Students (
    -- Определяем столбец ID как целое число
    -- Это будет первичный ключ таблицы, что означает, что каждое значение в этом столбце уникально
    -- AUTOINCREMENT указывает, что значение в этом столбце будет автоматически увеличиваться
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    -- Столбец для хранения имени студента
    -- Тип данных TEXT используется для хранения текстовой строки
    name TEXT NOT NULL,

    -- Столбец для хранения возраста студента
    -- Тип данных INTEGER используется для хранения целых чисел
    age INTEGER NOT NULL,

    -- Столбец для хранения специальности студента
    -- Также используется тип TEXT для текстовых данных
    major TEXT,

    -- Столбец для хранения среднего балла студента
    -- REAL используется для хранения чисел с плавающей точкой
    GPA REAL
);
    

-- Добавим данные одного студента
INSERT INTO Students (Name, Age, Major, GPA) 
VALUES ('Сергей', 35, "Студент", 12);

-- Добавим нескольких студентов одним запросом
INSERT INTO Students (Name, Age)
VALUES ('Алексей', 22),
       ('Мария', 23),
       ('Иван', 24);

-- Нельзя оставлять обязательные поля пустыми
-- INSERT INTO Students (Major, GPA)
-- VALUES ('Программирование', 11.2),
--        ('3D графика', 2.5),
--        ('Софистика', 3.2);


-- Обновим всем студентам средний бал
UPDATE Students
SET GPA = 12;

-- Обновим профессию студентам, где профессия пустая
UPDATE Students
SET Major = "Аналитик"
WHERE Major IS NULL;

-- Обновим данные студента с ID = 1
UPDATE Students
SET Name = "Владимир Петрович",
    Age = 26,
    Major = "Программист",
    GPA = 4.5
WHERE ID = 1;

-- Меняем ему отчество на Александрович через подзапрос
UPDATE Students
SET name = "Владимир Александрович"
WHERE name = (
    SELECT name
    FROM Students
    WHERE ID = 1
);


-- Удалим студента с ID = 21
DELETE FROM Students
WHERE ID = 21;

-- Удалить всех студентов с именем "Сергей"
DELETE FROM Students
WHERE name = 'Сергей';


-- Создадим столбец для хранения даты рождения студента
ALTER TABLE Students
ADD COLUMN BirthDate TEXT;

-- Удалим столбец для хранения даты рождения студента
ALTER TABLE Students
DROP COLUMN BirthDate


-- Создадим новую таблицу StudentsAnalytics и заполним ее данными из таблицы Students,
-- с условием Major = "Аналитик"
CREATE TABLE StudentsAnalytics (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Age INTEGER NOT NULL,
    Major TEXT,
    GPA REAL
);
INSERT INTO StudentsAnalytics (Name, Age, Major, GPA)
SELECT Name, Age, Major, GPA
FROM Students
WHERE Major = 'Аналитик';