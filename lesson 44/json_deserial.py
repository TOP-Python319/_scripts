# JSON — это текстовый формат обмена данными.
# Значит информация, хранящаяся в формате JSON, представлена в виде текста или,
# другими словами, в виде строки. 


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
print(type(str_json))
# >>>: <class 'str'>


import json
data = json.loads(str_json)
print(data)
# >>>: {'response': {'count': 32363, 'items': [{'id': 287350527, 'first_name': 'Sonya', 'last_name': 'Kargina', 'photo_50': 'https://pp.vk.me/...2c1/J2EL--qCZa8.jpg'}, {'id': 341523166, 'first_name': 'Slava', 'last_name': 'Kholod', 'photo_50': 'https://pp.vk.me/...321/eTxKNQSJMuk.jpg'}]}}
type(data)
# >>>: <class 'dict'>

print(data['response'])
# >>>: {'count': 32363, 'items': [{'id': 287350527, 'first_name': 'Sonya', 'last_name': 'Kargina', 'photo_50': 'https://pp.vk.me/...2c1/J2EL--qCZa8.jpg'}, {'id': 341523166, 'first_name': 'Slava', 'last_name': 'Kholod', 'photo_50': 'https://pp.vk.me/...321/eTxKNQSJMuk.jpg'}]}
print(data['response']['count'])
# >>>: 32363
print(data['response']['items'])
# >>>: [{'id': 287350527, 'first_name': 'Sonya', 'last_name': 'Kargina', 'photo_50': 'https://pp.vk.me/...2c1/J2EL--qCZa8.jpg'}, {'id': 341523166, 'first_name': 'Slava', 'last_name': 'Kholod', 'photo_50': 'https://pp.vk.me/...321/eTxKNQSJMuk.jpg'}]
print(type(data['response']['items']))
# >>>: <class 'list'>

for i in data['response']['items']:
    print(type(i))
# >>>: <class 'dict'>
# >>>: <class 'dict'>

for i in data['response']['items']:
    print(i['first_name'])
# >>>: Sonya
# >>>: Slava