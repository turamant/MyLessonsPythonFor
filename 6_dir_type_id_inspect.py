"""
help() Встроенная функция help() отображает полезную информацию об объекте,
       переданном в качестве аргумента.

type() В Python вы можете получить информацию о типе объекта с помощью встроенной функции type().
       Под информацией о типе я подразумеваю информацию о классе, реализующем объект.

dir()  Чтобы получить список всех атрибутов объекта, используйте встроенную функцию dir().
        Он возвращает длинный список имен атрибутов, то есть имен методов и переменных объекта.

id()   В Python каждый объект имеет идентификатор.
       Идентификатор — это целочисленное значение, которое остается постоянным на протяжении
       всего времени существования объекта.
       Чтобы получить доступ к идентификатору любого объекта Python, вы можете вызвать для него
       встроенную функцию id().

hasattr()  Метод hasattr() можно использовать для проверки наличия у объекта определенного
           атрибута.

getattr()  Чтобы получить значение атрибута из объекта, вы можете использовать функцию getattr().

callable()  Иногда вам может быть интересно узнать заранее, можно ли вызывать объект.
            С точки зрения непрофессионала, это означает проверку, можете ли вы поместить
            круглые скобки (и аргументы) после объекта для запуска некоторого кода.
            Чтобы проверить, является ли объект вызываемым, вызовите для него встроенную
            функцию callable(). Эта функция возвращает True, если объект можно вызывать,
            и False, если нет.
"""


def my_add(x: int, y: int) -> int:
    """
    Функция сложения двух аргументов
    :param x:
    :param y:
    :return: x +y
    """
    return x + y


class Car:
    def __init__(self, car_name):
        self.name = car_name

    def __str__(self):
        return self.name

    def __call__(self, *args, **kwargs):
        return f"This is: {id(self)}"

class Power:
    def __init__(self, power):
        self.power = power
    def __str__(self):
        return f'Class {Power.__name__}'

    def __call__(self, args):
        return args ** self.power


if __name__ == '__main__':
    name = "Victor"
    print(help(sorted))
    age = 33
    print("Функция dir(): ", dir(my_add(1, 2)))
    my_list = [21, 2, 3, 44, 5, 36, 17, 88, 19]
    print(dir(sorted(my_list)))
    print("Функция type(): ", type(name))
    print("id(age): ", id(age))
    print("Документация: ", my_add.__doc__)
    print(callable(name))

    car = Car("Mercedes")
    print("id(car): ", id(car))
    print(type(car))
    print(dir(car))
    print(callable(car))
    print("from class __callable__", car())
    print(car.__dict__)
    car.__setattr__("year", 2010)
    print(car.__dict__)
    car2 = Car("Volvo")
    print(car2())

    power = Power(3)
    print(power(5))
    print(callable(power))
    print(hasattr(power, "power"))
    print(hasattr(car, "name"))