# def <название функции>():
#     <тело функции>
#     return <выражение>


# def fahreheit_to_celcius(temperature):
#     result = (5 / 9) * (temperature - 32)
#     return result


# def fahreheit_to_celcius(temperature: int) -> float:
#     return (5 / 9) * (temperature - 32)


def fahreheit_to_celcius(temperature):
    return (5 / 9) * (temperature - 32)


t = int(input('Введите температуру в F: '))

print(fahreheit_to_celcius(t))