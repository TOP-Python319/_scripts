-- -- MarvelCharacters определение

-- CREATE TABLE "MarvelCharacters" (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     page_id INTEGER,
--     name TEXT,
--     urlslug TEXT,
--     identify TEXT,
--     ALIGN TEXT,
--     EYE TEXT,
--     HAIR TEXT,
--     SEX TEXT,
--     GSM TEXT,
--     ALIVE TEXT,
--     APPEARANCES INTEGER,
--     FIRST_APPEARANCE TEXT,
--     Year INTEGER
-- );


-- 1. Выбрать из таблицы MarvelCharacters ВСЁ
SELECT *
FROM MarvelCharacters;


--2. Выбрать из таблицы MarvelCharacters только name, alive, year
SELECT name, alive, year
FROM MarvelCharacters;


--3. Выбрать из таблицы MarvelCharacters только name, alive, year, eye с условием, что они погибшие "Deceased Characters"
SELECT
	name,
	alive,
	year,
	eye
FROM
	MarvelCharacters
WHERE 
	alive = "Deceased Characters";


--4. Выбрать из таблицы MarvelCharacters только name, alive, year, eye с условием, что они живые "Living Characters" и eye не "Blue Eyes" или "Brown Eyes" и год первого появления не позднее 1989
SELECT
	name,
	alive,
	year,
	eye
FROM
	MarvelCharacters
WHERE 
	year <= 1989 AND
	NOT (eye = "Blue Eyes" OR eye = "Brown Eyes") AND 
	alive = "Living Characters";
-- логические операторы:
-- () - первый приоритет
-- NOT - второй приоритет
-- AND - третий приоритет
-- OR - четвертый приоритет


--5. Выбрать из таблицы MarvelCharacters только name, alive, year, eye с условием что у них белые, красные, оранжевые или розовые глаза
SELECT
	name,
	alive,
	year,
	eye
FROM
	MarvelCharacters
WHERE 
	eye = "White Eyes" OR 
	eye = "Red Eyes" OR 
	eye = "Orange Eyes" OR 
	eye = "Pink Eyes";

SELECT
	name,
	alive,
	year,
	eye
FROM
	MarvelCharacters
WHERE 
	eye IN ("White Eyes", "Red Eyes", "Orange Eyes", "Pink Eyes");


--6. Выбрать из таблицы MarvelCharacters только name, alive, year, eye с условием что у них НЕ белые, красные, оранжевые или розовые глаза
SELECT
	name,
	alive,
	year,
	eye
FROM
	MarvelCharacters
WHERE 
	eye NOT IN ("White Eyes", "Red Eyes", "Orange Eyes", "Pink Eyes");


--7. Выбрать все уникальные типы/цвета волос
SELECT DISTINCT hair FROM MarvelCharacters;


--8. Выбрать из таблицы MarvelCharacters только name, year, align с условием, что year не NULL и align не NULL, и сортировать по year по возрастанию, align по убыванию
SELECT
	name,
	year,
	align
FROM
	MarvelCharacters
WHERE
	appearances NOT NULL AND 
	year NOT NULL AND
	align NOT NULL
ORDER BY
	year ASC,
	align DESC;
