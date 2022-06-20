""" Ключевое слово lambda позволяет сделать небольшие безымянные функции.
    Результат выражения всегда автоматически возвращается.
    Лучше всего использовать lambda для одноразовых функций."""

my_list = [[3, 2], [4, 2], [6, 2], [2, 6], [5, 9], [0, 2]]

print(my_list)
my_list.sort(key=lambda x: x[0])
print(my_list)
my_list.sort(key=lambda x: x[1])
print(my_list)


def func_add(x, y):
    return x + y


if __name__ == '__main__':
    res = func_add(1, 2)
    print(res)
    res2 = lambda x, y: x + y
    print(res2(1, 2))

    res3 = lambda x, y: x * y
    print(res3(3, 4))
