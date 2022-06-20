from functools import reduce

my_digits = [1, 5, 3, 7, 9, 3, 5]


# map (применение функции к каждому элементу последовательности),
# например усножение всех элементов на -3-
print("-= map =-")
my_map = map(lambda x: x * 3, my_digits)
for item in my_map:
    print(item)

# filter(возращает список элементов , удовлетворяющих условию),
# выбрать все элементы которые больше числа -3-
print("-= filter =-")
my_filter = filter(lambda x: x if x > 3 else None, my_digits)
for item in my_filter:
    print(item)

# reduce(действие на списке элементов с единственным результатом,
# например, вычисление суммы всех элементов последовательности)
print("-= reduce =-")
my_reduce = reduce(lambda x, y: x+y, my_digits)
print(my_reduce)