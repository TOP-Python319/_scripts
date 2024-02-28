mammals = {
    'тигр',
    'верблюд',
    'овца',
    'кит',
    'морж'
}

aquatic = {
    'осьминог',
    'кальмар',
    'краб',
    'кит',
    'морж'
}

mammals | aquatic  # объединение множеств
aquatic.union(mammals)
# {'овца', 'тигр', 'верблюд', 'морж', 'кальмар', 'осьминог', 'кит', 'краб'}

mammals & aquatic  # пересечение множеств
aquatic.intersection(mammals)  # то же самое, но с помощью метода
# {'морж', 'кит'}

mammals - aquatic  # вычитание множеств
mammals.difference(aquatic)  # то же самое, но с помощью метода
# {'овца', 'тигр', 'верблюд'}
aquatic - mammals  # вычитание множеств
aquatic.difference(mammals)  # то же самое, но с помощью метода
# {'кальмар', 'осьминог', 'краб'}


aquatic ^ mammals  # симметричная разность
aquatic.symmetric_difference(mammals)  # то же самое, но с помощью метода
(mammals | aquatic) - (mammals & aquatic)  # симметричная разность, но длинная запись
# {'овца', 'кальмар', 'осьминог', 'краб', 'тигр', 'верблюд'}


mammals2 = {*mammals}
mammals2
# {'овца', 'кит', 'тигр', 'верблюд', 'морж'}
mammals2 |= aquatic
mammals2
# {'овца', 'тигр', 'верблюд', 'морж', 'кальмар', 'осьминог', 'кит', 'краб'}
mammals2 = {*mammals}
mammals2
# {'овца', 'кит', 'тигр', 'верблюд', 'морж'}
mammals2.intersection_update(aquatic)
mammals2
# {'морж', 'кит'}


{1, 2, 3} == {3, 1, 2}
# True
{1, 2} < {1, 2, 3}
# True
{3, 1} < {1, 2, 3}
# True
{1, 2, 3} < {3, 2, 1}
# False
{1, 2, 3} <= {3, 2, 1}
# True
