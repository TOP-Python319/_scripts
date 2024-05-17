# класс LengthConverter

# методы:
#   m_to_km
#   km_to_m
#   m_to_mil
#   mil_to_m
#   km_to_mil
#   mil_to_km


def m_to_km(m):
    return m / 1000


def km_to_m(km):
    return km * 1000


def m_to_mil(m):
    return m / 1600


def mil_to_m(mil):
    return mil * 1600


def km_to_mil(km):
    return km / 1.6


def mil_to_km(mil):
    return mil * 1.6


km = m_to_km(3800)
print(km)

mil = km_to_mil(72000)
print(mil)