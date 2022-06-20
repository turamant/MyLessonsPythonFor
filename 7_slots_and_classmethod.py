"""По умолчанию Python использует dict для хранения атрибутов экземпляра объекта.
   Это действительно полезно, когда у тебя произвольное количество атрибутов.
   В небольших классах это уже проблема – dict тратит много оперативной памяти.
   Для экономии ресурсов используй slots. Память выделится только для фиксированного
   значения атрибутов.
   Это позволяет снизить использование оперативной памяти почти на 40-50 процентов.
   """

class Car:
    id = 0
    __slots__ = ["name", "price"]

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Car.increment_id()

    @classmethod
    def increment_id(cls):
        Car.id += 1
        print("Id this car: ", Car.id)

    def __str__(self):
        return f'This Car: {self.name} price: {self.price}'


class CarWithOut_Slots_:
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    car = Car("Y", 12)
    print(car)
    car2 = Car("N", 122)
    print(car2)
    print("Всего построено экземпляров данного проекта(класса): ", Car.id)
    # car2.color = "blue"  color не допустим , в __slots__ его нет
    print("Допустимые атрибуты(поля) класса Car: ", Car.__slots__)
    #print(Car.__dict__)

    car_with_out_slots = CarWithOut_Slots_("Mercedes")
    car_with_out_slots.color = "blue"
    print(car_with_out_slots.color)
    #print(CarWithOut_Slots_.__dict__)

