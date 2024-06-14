-- Повторили:
-- SELECT
-- FROM
-- WHERE
-- SELECT DISTINCT
-- ORDER BY
-- логические операторы:
-- () - первый приоритет
-- NOT - второй приоритет
-- AND - третий приоритет
-- OR - четвертый приоритет

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


-- 1. Найти 10 злодеев с наибольшим количеством появлений, но пропустить первую десятку.
SELECT
	name,
	year,
	appearances
FROM
	MarvelCharacters
WHERE
	appearances NOT NULL AND 
	year NOT NULL AND
	align NOT NULL AND
	align = "Bad Characters"
ORDER BY
	appearances DESC
LIMIT 10
OFFSET 10;


-- 2. Найти персонажей с появлением между 1940 и 1950. Количество появлений больше 50.
SELECT
	name,
	year,
	appearances
FROM
	MarvelCharacters
WHERE
	appearances > 50 AND 
	year IS NOT NULL AND
	year BETWEEN 1940 AND 1950
ORDER BY
	appearances DESC;

-- аналог такой записи, но короче:
SELECT
	name,
	year,
	appearances
FROM
	MarvelCharacters
WHERE
	appearances > 50 AND 
	year IS NOT NULL AND
	year >= 1940 AND 
	year <= 1950
ORDER BY
	appearances DESC;


-- 3. Найти всех капитанов.
SELECT
	name,
	year
FROM
	MarvelCharacters
WHERE
	name LIKE "%captain%";


-- 4. Найти персонажей в названии которых есть "Earth-616".
SELECT
	name,
	year
FROM
	MarvelCharacters
WHERE
	name LIKE '___ (Earth-616)';


-- 5.
SELECT
	name,
	year
FROM
	MarvelCharacters
WHERE
	name LIKE '%(Earth-%)' AND
	name NOT LIKE '%(Earth-616)' AND
	year IS NOT NULL;


-- ПРАКТИКА
-- 6. Сделать выборку персонажей (имя, год, количество появлений), где год между 1960 и 1970 и количество появлений больше 10
SELECT
	name,
	year,
	appearances
FROM
	MarvelCharacters
WHERE
	year BETWEEN 1960 AND 1970 AND 
	appearances > 10


-- ПРАКТИКА
-- 7. Найдите всех персонажей (имя, год, количество появлений), в имени которых есть 'phoenix'
SELECT
	name,
	year,
	appearances
FROM
	MarvelCharacters
WHERE
	name LIKE '%phoenix%'


-- ПРАКТИКА
-- 8. Найти всех персонажей (имя, год, количество появлений), в имени которых есть 'john' или 'jane' и количество появлений больше 10
SELECT
	name,
	year,
	appearances
FROM
	MarvelCharacters
WHERE
	(name LIKE '%john%' OR
	name LIKE '%jane%') AND
	appearances > 10