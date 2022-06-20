"""
 Предел рекурсии
 Ограничение рекурсии по умолчанию в Python равно 1000. Это означает, что Python не позволит
 функции вызывать саму себя более 1000 раз. Этого вполне достаточно, но при необходимости ты
 можешь увеличить этот лимит. Делается это с помощью sys.setrecursionlimit(limit).
 Пользуйся этим только когда действительно нужно, так как большое количество рекурсий замедлит
 твой код.
"""

def recursing(depth):
    try:
        recursing(depth + 1)
    except RuntimeError as RE:
        print('I recursed {} times'.format(depth))


if __name__ == '__main__':
    recursing(0)

    import sys
    sys.setrecursionlimit(2000)
    recursing(0)