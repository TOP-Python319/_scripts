def search_key(main_box):
    heap = main_box.check_box()
    while heap is not None:  #  пока куча коробок не пустая
        box = heap.grab_box()  # берём коробку из кучи
        for item in box:  # перебираем элементы в коробке
            if item.is_key():  # если элемент ключ, то задача выполнена, ключ найдет, функция завершает свою работу
                return 'Ключ найден'
            elif item.is_box():  # если элемент ещё одна коробка, то добавляет её в кучу
                heap.append(item)


def search_key_recursive(box):
    for item in box:  # перебираем элементы в коробке
        if item.is_box():  # если элемент является коробкой, то помещаем коробку в функцию search_key_recursive()
            search_key_recursive(item)
        elif item.is_key():  # если элемент ключ, то задача выполнена, ключ найдет, функция завершает свою работу
            return 'Ключ найден'
