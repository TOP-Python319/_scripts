# Домашнее задание 📃

### Резюме Домашнего Задания

**Тема:** Создание и Импорт Данных в Базу данных `marvel`

**Описание:**
Это задание предназначено для студентов, изучающих основы работы с базами данных. Оно включает в себя создание базы данных `marvel`, создание в ней таблицы с определёнными полями, импорт данных в эту таблицу с использованием интерфейса SQLite Studio, а также выполнение серии SQL-запросов для оптимизации и форматирования данных.

### Основной Текст Задания

1. **Создание Базы Данных:**
   - Создайте новую базу данных sqlite с названием `marvel`.

2. **Создание Таблицы:**
   - Создайте в базе данных `marvel` таблицу с указанными полями.

```sql
-- Шаг 1. Создать таблицу MarvelCharacters  
CREATE TABLE MarvelCharacters (  
    page_id          INTEGER,  
    name             TEXT,  
    urlslug          TEXT,  
    identity         TEXT,  
    align            TEXT,  
    eye              TEXT,  
    hair             TEXT,  
    sex              TEXT,  
    GSM              TEXT,  
    alive            TEXT,  
    appearances      INTEGER,  
    first_appearance TEXT,  
    year             INTEGER  
);
```

**Импорт Данных:**
   - Перейдите к созданной таблице, щёлкните по ней правой кнопкой мыши и выберите опцию "Импортировать данные в таблицу".
   - Откроется интерфейс SQLite Studio для импорта данных.
   - Нажмите кнопку "Next".
   - Установите галочку "Имена столбцов в первой строке". Убедитесь, что имена столбцов не импортируются как данные.
   - Установите галочку "Значения null", оставив поле ввода пустым. Это гарантирует автоматическое присвоение null пустым строкам.
   - Активируйте опцию "Обрабатывать кавычки, как символ обрамления значений".
   - Нажмите "Finish" для завершения импорта и получения таблицы в исходном виде.

**Оптимизация и Форматирование Данных:**
   - Выполните серию SQL-запросов, представленных ниже, для улучшения структуры и формата данных в таблице.

### Детальное Описание Задания по Работе с Базой Данных `marvel`

#### Шаг 2: Создание Новой Таблицы `MarvelCharacters_new`

- **Цель:** Создать таблицу `MarvelCharacters_new` с дополнительным столбцом `id`.
- **Описание полей:**
  - `id`: Уникальный идентификатор записи. Используйте тип данных `INTEGER`, ключ `PRIMARY KEY`, и `AUTOINCREMENT` для автоматического увеличения значения.
  - `page_id`: Целочисленный идентификатор страницы, тип `INTEGER`.
  - `name`: Текстовое название, тип `TEXT`.
  - `urlslug`: Текстовый идентификатор URL, тип `TEXT`.
  - `identify`: Текстовая идентификация, тип `TEXT`.
  - `ALIGN`: Текстовое значение выравнивания, тип `TEXT`.
  - `EYE`: Цвет глаз, текстовое поле, тип `TEXT`.
  - `HAIR`: Цвет волос, текстовое поле, тип `TEXT`.
  - `SEX`: Пол, текстовое поле, тип `TEXT`.
  - `GSM`: Не указано, предположительно текстовое поле, тип `TEXT`.
  - `ALIVE`: Статус живой/мертвый, текстовое поле, тип `TEXT`.
  - `APPEARANCES`: Количество появлений, целочисленное значение, тип `INTEGER`.
  - `FIRST_APPEARANCE`: Текстовое описание первого появления, тип `TEXT`.
  - `Year`: Год, целочисленное значение, тип `INTEGER`.

```sql
CREATE TABLE IF NOT EXISTS MarvelCharacters_new ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    page_id          INTEGER,  
    name             TEXT,  
    urlslug          TEXT,  
    identify         TEXT,  
    ALIGN            TEXT,  
    EYE              TEXT,  
    HAIR             TEXT,  
    SEX              TEXT,  
    GSM              TEXT,  
    ALIVE            TEXT,  
    APPEARANCES      INTEGER,  
    FIRST_APPEARANCE TEXT,  
    Year             INTEGER  
);
```

#### Шаг 3: Копирование Данных и Удаление Старой Таблицы

- **Цель:** Скопировать данные из таблицы `MarvelCharacters` в `MarvelCharacters_new`.
- **Операции:**
  - Копирование данных: Используйте команду `INSERT INTO` для вставки данных из `MarvelCharacters`. Используйте `SELECT` для выбора и копирования данных.
  - Удаление старой таблицы: Используйте команду `DROP TABLE` для удаления `MarvelCharacters`.

```sql
BEGIN;

INSERT INTO MarvelCharacters_new (
    page_id,
    name,
    urlslug,
    identity,
    align,
    eye,
    hair,
    sex,
    GSM,
    alive,
    appearances,
    first_appearance,
    year)
    
SELECT
    page_id,
    name,
    urlslug,
    identity,
    align,
    eye,
    hair,
    sex,
    GSM,
    alive,
    appearances,
    first_appearance,
    year
FROM
    MarvelCharacters;

DROP TABLE MarvelCharacters;

COMMIT;
/*ROLLBACK;*/
```

#### Шаг 4: Переименование Таблицы

- **Цель:** Переименовать `MarvelCharacters_new` обратно в `MarvelCharacters`.
- **Операции:**
  - Используйте команду `ALTER TABLE ... RENAME TO` для переименования таблицы.

  ```sql
  ALTER TABLE MarvelCharacters_new RENAME TO MarvelCharacters
  ```

#### Шаг 5: Создание Таблиц для Уникальных Значений

- **Цель:** Создать отдельные таблицы для уникальных значений полей `SEX`, `EYE`, `HAIR`, `ALIGN`, `ALIVE`, `GSM`, и `IDENTIFY`.
- **Описание Таблиц:**
  - Каждая таблица будет иметь два поля: идентификатор (`*_id`) и значение (`name` или `color`).
  - Используйте `INTEGER PRIMARY KEY AUTOINCREMENT` для идентификаторов.
  - Используйте `TEXT UNIQUE` для полей значений, чтобы гарантировать уникальность.

```sql
BEGIN;

CREATE TABLE IF NOT EXISTS identity (  
    id INTEGER PRIMARY KEY AUTOINCREMENT,  
    identity TEXT UNIQUE  
);

CREATE TABLE IF NOT EXISTS alignment (  
    id INTEGER PRIMARY KEY AUTOINCREMENT,  
    alignment TEXT UNIQUE  
);

CREATE TABLE IF NOT EXISTS eye_color (  
    id INTEGER PRIMARY KEY AUTOINCREMENT,  
    eye_color TEXT UNIQUE  
);

CREATE TABLE IF NOT EXISTS hair_color (  
    id INTEGER PRIMARY KEY AUTOINCREMENT,  
    hair_color TEXT UNIQUE  
);

CREATE TABLE IF NOT EXISTS sex (  
    id INTEGER PRIMARY KEY AUTOINCREMENT,  
    sex TEXT UNIQUE  
);

CREATE TABLE IF NOT EXISTS GSM (  
    id INTEGER PRIMARY KEY AUTOINCREMENT,  
    gsm TEXT UNIQUE  
);

CREATE TABLE IF NOT EXISTS living_status (  
    id INTEGER PRIMARY KEY AUTOINCREMENT,  
    living_status TEXT UNIQUE  
);

COMMIT;
```

#### Шаг 6: Наполнение Уникальных Таблиц Данными

- **Цель:** Заполнить созданные таблицы уникальными значениями из `MarvelCharacters`.
- **Операции:**
  - Используйте команду `INSERT INTO ... SELECT DISTINCT` для извлечения уникальных значений из `MarvelCharacters` и их вставки в соответствующие таблицы.

```sql
BEGIN;

INSERT INTO identity (identity)
SELECT DISTINCT identity
FROM marvel_characters
WHERE identity IS NOT NULL AND identity != '';

INSERT INTO alignment (alignment)
SELECT DISTINCT align
FROM marvel_characters
WHERE align IS NOT NULL AND align != '';

INSERT INTO eye_color (eye_color)
SELECT DISTINCT eye
FROM marvel_characters
WHERE eye IS NOT NULL AND eye != '';

INSERT INTO hair_color (hair_color)
SELECT DISTINCT hair
FROM marvel_characters
WHERE hair IS NOT NULL AND hair != '';

INSERT INTO sex (sex)
SELECT DISTINCT sex
FROM marvel_characters
WHERE sex IS NOT NULL AND sex != '';

INSERT INTO GSM (gsm)
SELECT DISTINCT gsm
FROM marvel_characters
WHERE gsm IS NOT NULL AND gsm != '';

INSERT INTO living_status (living_status)
SELECT DISTINCT alive
FROM marvel_characters
WHERE alive IS NOT NULL AND alive != '';

COMMIT;
/*ROLLBACK;*/
```

#### Шаг 7: Создание Таблицы `MarvelCharacters_New` с Внешними Ключами

- **Цель:** Создать новую таблицу `MarvelCharacters_New`, заменяя текстовые описания на внешние ключи.
- **Описание Полей:**
  - Аналогично `MarvelCharacters_new`, но поля `identity`, `align`, `eye`, `hair`, `sex`, `status`

` заменяются на `*_id`, ссылающиеся на соответствующие таблицы.
- **Операции:**
  - Используйте `FOREIGN KEY (...) REFERENCES ...` для указания внешних ключей.

```sql
CREATE TABLE IF NOT EXISTS marvel_characters_temp (
    id               INTEGER PRIMARY KEY AUTOINCREMENT,
    page_id          INTEGER,
    name             TEXT,
    urlslug          TEXT,
    identity_id      INTEGER,
    align_id         INTEGER,
    eye_id           INTEGER,
    hair_id          INTEGER,
    sex_id           INTEGER,
    gsm_id           INTEGER,
    alive_id         INTEGER,
    appearances      INTEGER,
    first_appearance TEXT,
    year             INTEGER,
    
    FOREIGN KEY (identity_id) REFERENCES identity(id),
    FOREIGN KEY (align_id) REFERENCES alignment(id),
    FOREIGN KEY (eye_id) REFERENCES eye_color(id),
    FOREIGN KEY (hair_id) REFERENCES hair_color(id),
    FOREIGN KEY (sex_id) REFERENCES sex(id),
    FOREIGN KEY (gsm_id) REFERENCES GSM(id),
    FOREIGN KEY (alive_id) REFERENCES living_status(id)
);
```
#### Шаг 8: Наполнение Новой Таблицы Данными

- **Цель:** Заполнить `MarvelCharacters_New` данными, сопоставляя текстовые поля с соответствующими идентификаторами.
- **Операции:**
  - Используйте комбинацию `INSERT INTO` и `SELECT` с соединениями (`JOIN`) для сопоставления текстовых значений с идентификаторами из соответствующих таблиц.

```sql
BEGIN;
INSERT INTO marvel_characters_temp (
    page_id,
    name,
    urlslug, 
    identity_id,
    align_id,
    eye_id,
    hair_id,
    sex_id,
    gsm_id,
    alive_id,
    appearances,
    first_appearance,
    year
)  
SELECT
    mc.page_id,
    mc.name,
    mc.urlslug,
    i.id,
    a.id,
    ec.id,
    hc.id,
    s.id,
    g.id,
    ls.id,
    mc.appearances,
    mc.first_appearance,
    mc.year 
FROM
    marvel_characters mc  
        LEFT JOIN identity i ON mc.identity = i.identity
        LEFT JOIN alignment a ON mc.align = a.alignment
        LEFT JOIN eye_color ec ON mc.eye = ec.eye_color
        LEFT JOIN hair_color hc ON mc.hair = hc.hair_color
        LEFT JOIN sex s ON mc.sex = s.sex
        LEFT JOIN GSM g ON mc.GSM = g.gsm
        LEFT JOIN living_status ls ON mc.alive = ls.living_status;
COMMIT;
/*ROLLBACK;*/
```
#### Шаг 9 и 10: Удаление Старой и Переименование Новой Таблицы

- **Цели:**
  - Удалить старую таблицу `MarvelCharacters`.
  - Переименовать `MarvelCharacters_New` в `MarvelCharacters`.
- **Операции:**
  - Удаление: Используйте `DROP TABLE`.
  - Переименование: Используйте `ALTER TABLE ... RENAME TO`.
```sql
DROP TABLE MarvelCharacters;
ALTER TABLE marvel_characters_temp RENAME TO marvel_characters;
```

# Структура ДО и структура ПОСЛЕ

Ваше задание по работе с базой данных включает несколько шагов, начиная с создания исходной таблицы и заканчивая реорганизацией данных с использованием нормализации. Ниже приведен полный список таблиц на каждом этапе с описанием их структуры.

### Исходная Таблица

#### Шаг 1: Создание таблицы `MarvelCharacters`

- `page_id`: INTEGER - целочисленный идентификатор страницы.
- `name`: TEXT - текстовое название персонажа.
- `urlslug`: TEXT - текстовый идентификатор URL.
- `identify`: TEXT - текстовая идентификация персонажа.
- `ALIGN`: TEXT - текстовое значение выравнивания персонажа.
- `EYE`: TEXT - текстовое значение цвета глаз.
- `HAIR`: TEXT - текстовое значение цвета волос.
- `SEX`: TEXT - текстовое значение пола персонажа.
- `GSM`: TEXT - не уточнено, предположительно текстовое поле.
- `ALIVE`: TEXT - текстовое значение статуса живой/мертвый.
- `APPEARANCES`: INTEGER - целочисленное значение количества появлений.
- `FIRST_APPEARANCE`: TEXT - текстовое значение первого появления.
- `Year`: INTEGER - целочисленное значение года.

### Промежуточная Таблица

#### Шаг 2: Создание таблицы `MarvelCharacters_new`

- `id`: INTEGER PRIMARY KEY AUTOINCREMENT - уникальный идентификатор.
- Остальные поля аналогичны исходной таблице `MarvelCharacters`.

### Нормализованные Таблицы

#### Шаг 5: Создание таблиц для уникальных значений

1. `Sex`
   - `sex_id`: INTEGER PRIMARY KEY AUTOINCREMENT - уникальный идентификатор пола.
   - `name`: TEXT UNIQUE - название пола.

2. `EyeColor`
   - `eye_id`: INTEGER PRIMARY KEY AUTOINCREMENT - уникальный идентификатор цвета глаз.
   - `color`: TEXT UNIQUE - название цвета.

3. `HairColor`
   - `hair_id`: INTEGER PRIMARY KEY AUTOINCREMENT - уникальный идентификатор цвета волос.
   - `color`: TEXT UNIQUE - название цвета.

4. `Alignment`
   - `align_id`: INTEGER PRIMARY KEY AUTOINCREMENT - уникальный идентификатор выравнивания.
   - `name`: TEXT UNIQUE - название выравнивания.

5. `LivingStatus`
   - `status_id`: INTEGER PRIMARY KEY AUTOINCREMENT - уникальный идентификатор статуса живой/мертвый.
   - `status`: TEXT UNIQUE - статус.

6. `Identity`
   - `identity_id`: INTEGER PRIMARY KEY AUTOINCREMENT - уникальный идентификатор идентификации.
   - `identity`: TEXT UNIQUE - идентификация.

#### Шаг 7: Создание таблицы `MarvelCharacters_New` с внешними ключами

- `id`: INTEGER PRIMARY KEY AUTOINCREMENT - уникальный идентификатор.
- `page_id`: INTEGER - идентификатор страницы.
- `name`: TEXT - название персонажа.
- `urlslug`: TEXT - идентификатор URL.
- `identity_id`: INTEGER - внешний ключ к `Identity`.
- `align_id`: INTEGER - внешний ключ к `Alignment`.
- `eye_id`: INTEGER - внешний ключ к `EyeColor`.
- `hair_id`: INTEGER - внешний ключ к `HairColor`.
- `sex_id`: INTEGER - внешний ключ к `Sex`.
- `status_id`: INTEGER - внешний ключ к `LivingStatus`.
- `APPEARANCES`: INTEGER - количество появлений.
- `FIRST_APPEARANCE`: TEXT - первое появление.
- `Year`: INTEGER - год.

### Финальная Таблица

#### Шаг 10: Переименование `MarvelCharacters_New` в `MarvelCharacters`

- Структура таблицы `MarvelCharacters_New` становится финальной структурой для `MarvelCharacters`.

Этот процесс демонстрирует создание исходной таблицы, преобразование её структуры и нормализацию данных через создание связанных таблиц с внешними ключами.

### Тестовые запросы

Вот пять тестовых запросов с использованием `JOIN` для вашей базы данных SQLite, ориентированные на таблицу `MarvelCharacters` и связанные с ней таблицы:

1. **Запрос на соединение информации о персонажах с их полом:**
2. **Запрос на соединение информации о персонажах с цветом их глаз:**
3. **Запрос на соединение информации о персонажах с цветом волос и статусом жив/мертв:**
4. **Запрос на соединение информации о персонажах с их идентификацией и характером:**
5. **Запрос на получение полной информации о персонажах, соединяя все связанные таблицы:**

Эти запросы позволяют извлекать и соединять данные из разных таблиц, что демонстрирует мощь реляционных баз данных и их способность обеспечивать гибкое управление информацией.
# Критерии проверки 👌

- Получение структуры "ПОСЛЕ" указанной в тексте задания
- Будьте внимательны с названиями полей - это важно (возможно сделаем авто-тесты)
- Возможность проверить БД тестовыми запросами
- **ВСЯ РАБОТА СДАЕТСЯ В 1 SQL файле**
- **ЗАПРОСЫ ЗАКАНЧИВАЮТСЯ НА ;**