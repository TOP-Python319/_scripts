import json
import random


str_json = """
{
    "response": {
        "count": 32363,
        "items": [
            {
                "id": 287350527,
                "first_name": "Sonya",
                "last_name": "Kargina",
                "photo_50": "https://pp.vk.me/...2c1/J2EL--qCZa8.jpg"
            },
            {
                "id": 341523166,
                "first_name": "Slava",
                "last_name": "Kholod",
                "photo_50": "https://pp.vk.me/...321/eTxKNQSJMuk.jpg"
            }
        ]
    }
}
"""

data = json.loads(str_json)

# удалим id и добавим счётчик лайков со сслучайным значением
for item in data['response']['items']:
    del item['id']
    item['likes'] = random.randint(0, 100)


# получили изменённый словарь со счётчиком лайков и без id
# import pprint
# pprint.pprint(data)
# {'response': {'count': 32363,
#               'items': [{'first_name': 'Sonya',
#                          'last_name': 'Kargina',
#                          'likes': 75,
#                          'photo_50': 'https://pp.vk.me/...2c1/J2EL--qCZa8.jpg'},
#                         {'first_name': 'Slava',
#                          'last_name': 'Kholod',
#                          'likes': 98,
#                          'photo_50': 'https://pp.vk.me/...321/eTxKNQSJMuk.jpg'}]}}


# сереализуем словарь в JSON
new_str_json = json.dumps(data, indent=2)
print(new_str_json)
# {
#   "response": {
#     "count": 32363,
#     "items": [
#       {
#         "first_name": "Sonya",
#         "last_name": "Kargina",
#         "photo_50": "https://pp.vk.me/...2c1/J2EL--qCZa8.jpg",
#         "likes": 6
#       },
#       {
#         "first_name": "Slava",
#         "last_name": "Kholod",
#         "photo_50": "https://pp.vk.me/...321/eTxKNQSJMuk.jpg",
#         "likes": 17
#       }
#     ]
#   }
# }