from googletrans import Translator

def my_add(x: int, y: int) -> int:
    """
    Функция сложения двух аргументов
    :param x:
    :param y:
    :return: x +y
    """
    return x + y

if __name__ == '__main__':
    translator = Translator()

    print(dir(my_add(1, 2)))
    my_list = [21, 2, 3, 44, 5, 36, 17, 88, 19]
    print(dir(sorted(my_list)))

    sorted_doc = translator.translate(sorted.__doc__, src='en', dest='ru')
    print("\nДокументация 2: ", sorted_doc.text)

    my_list_doc = translator.translate(my_list.count.__doc__, src='en', dest='ru')

    print("\nДокументация 3: ", my_list_doc.text)