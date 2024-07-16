# что во что преобразуется:
# JSON            Python
# object          dict
# array           list
# string          str
# number (int)    int
# number (real)   float
# true            True
# false           False
# null            None

import json
from pprint import pprint
from random import randint


str_json = """
{
    "id": 287350527,
    "first_name": "Sonya",
    "last_name": "Kargina",
    "photo_50": "https://pp.vk.me/...2c1/J2EL--qCZa8.jpg"
}
"""

data = json.loads(str_json)

del data['photo_50']
data['likes'] = randint(0, 100)
data['is_married'] = False
data['is_adult'] = True
data['mail'] = None

new_json = json.dumps(data, indent=2)
print(new_json)


# Не все типы данных можно преобразовать в JSON
# import datetime
# data['now'] = datetime.datetime.now()
# new_json_with_date = json.dumps(data, indent=2)
# TypeError: Object of type datetime is not JSON serializable


# Например дату можно предварительно преобразовать в текстовый формат
import datetime
data['now'] = datetime.datetime.now().strftime('%d.%m.%Y')
new_json_with_date = json.dumps(data, indent=2)
print(new_json_with_date)
# {
#   "id": 287350527,
#   "first_name": "Sonya",
#   "last_name": "Kargina",
#   "likes": 82,
#   "is_married": false,
#   "is_adult": true,
#   "mail": null,
#   "now": "16.07.2024"
# }


# преоборазование даты в текст
import datetime
now = dateitme.datetime.now()
print(now)
# >>>: datetime.datetime(2024, 7, 16, 21, 21, 25, 245807)
type(now)
# >>>: <class 'datetime.datetime'>
now = datetime.datetime.now().strftime('%d.%m.%Y')
print(now)
# >>>: '16.07.2024'
type(now)
# >>>: <class 'str'>
