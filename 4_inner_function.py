# две внутренние функции (защищены от внешнего кода)
def func_outer(name="Victor"):
    print("inside outer func")

    def greet():
        return f"Inside greet({name}) func"

    def welcome():
        return f"Inside welcome({name}) func"

    print(greet())
    print(welcome())
    print("Inside func_outer() func")


# closure (замыкания)
def outer(x):
    def inner(y):
        result = x * y
        return result

    return inner


# декоратор html_result
def html_result(func):
    def wrapper(*args):
        result = func(*args)
        print(f'<h2>Результат: {result} чего то там..</h2>')

    return wrapper


@html_result
def add(*args):
    return sum(args)


if __name__ == '__main__':
    outer("Semen")
    res = outer(4)
    print(res(3))
    add(2, 4, 6, 8)
