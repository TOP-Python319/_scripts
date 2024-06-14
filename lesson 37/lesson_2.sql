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
	appearances > 10;


-- ПРАКТИКА
-- 7. Найдите всех персонажей (имя, год, количество появлений), в имени которых есть 'phoenix'
SELECT
	name,
	year,
	appearances
FROM
	MarvelCharacters
WHERE
	name LIKE '%phoenix%';


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
	appearances > 10;


-- 10. Выведите пол и количество персонажей
SELECT 
	sex,
	COUNT(*) AS cnt
FROM
	MarvelCharacters
GROUP BY
	sex;


-- 11. Выведите год и количество персонажей
SELECT 
	sex,
	year,
	COUNT(*) AS cnt
FROM
	MarvelCharacters
WHERE
	sex IS NOT NULL AND 
	year IS NOT NULL
GROUP BY
	sex,
	year
ORDER BY
	year,
	sex,
	cnt;


-- 12. Выведите года в которых количество персонажей больше 350
SELECT 
	year,
	COUNT(*) AS cnt
FROM
	MarvelCharacters
WHERE
	year IS NOT NULL
GROUP BY
	year
HAVING
	cnt > 350
ORDER BY
	year;


-- 13. Выведите цвет глаз и количество персонажей с цветными глазными яблоками
SELECT
	eye AS цвет_глаз,
	COUNT(*) AS количество_персонажей
FROM
	MarvelCharacters
WHERE
	цвет_глаз LIKE '%eyeballs%'
GROUP BY
	цвет_глаз;


-- 14. Выведите цвет глаз и количество появлений персонажей
SELECT
	eye AS цвет_глаз,
	SUM(appearances) AS количество_появлений
FROM
	MarvelCharacters
WHERE
	цвет_глаз LIKE '%eyeballs%'
GROUP BY
	цвет_глаз


-- 15. Выведите год и количество появлений персонажей, количество персонажей и среднее количество появлений (с округлением до 2 знака после запятой) по годам
SELECT
	year,
	SUM(appearances),
	COUNT(appearances),
	ROUND(AVG(appearances), 2)
FROM
	MarvelCharacters
WHERE
	year IS NOT NULL
GROUP BY
	year
ORDER BY
	year;


-- 16. Выведите пол, цвет глаз, цвет волос и количество персонажей с такими параметрами
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
	cnt DESC;
	

-- 17. Выведите год и количество появлений персонажей, где количество появлений максимальное
SELECT
	year,
	name,
	MAX(appearances) AS максимальное_количество_появлений
FROM
	MarvelCharacters
WHERE
	year IS NOT NULL
GROUP BY
	year
ORDER BY
	year;


-- ПРАКТИКА
-- 18. Сгруппировать персонажей по годам, получить минимальное количество и имя персонажа.
-- Выбрать имя, год, минимальное количество появлений
SELECT
	year,
	name,
	MIN(appearances) AS минимальное_количество_появлений
FROM
	MarvelCharacters
WHERE
	year IS NOT NULL 
GROUP BY
	year
ORDER BY
	year;


-- ПРАКТИКА
-- 19. Сгруппировать пероснажей по годам, получить максимальное колчество и имя персонажа.
-- Выбрать имя, год, максимальное количество появлений. Количество появлений 50 и больше
SELECT
	year,
	name,
	MAX(appearances) AS максимальное_количество_появлений
FROM
	MarvelCharacters
WHERE
	year IS NOT NULL AND
	appearances > 50
GROUP BY
	year
ORDER BY
	year;
