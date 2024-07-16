import json

# с помощью менеджера контекста with, функций open() и json.load() можно считывать
with open('movie_certs.json', 'r') as file:
    all_certs = json.load(file)

au_0_cert = all_certs['certifications']['AU'][0]

# с помощью менеджера контекста with, функций open() и json.dump() можно записывать
with open('au_0_cert.json', 'w') as file:
    json.dump(au_0_cert, file, indent=2)
