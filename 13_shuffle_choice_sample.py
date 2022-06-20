"""
Ты можешь использовать random.shuffle() для рандомизации элементов в изменяемой и индексируемой последовательности.
 Метод choice() произвольно выбирает элемент в последовательности. Если тебе нужно выбрать несколько элементов,
 используй sample().

"""

import random

laughs = ["hi", "Ho", "He"]

random.shuffle(laughs)
print(laughs)

print(random.choice(laughs))

print(random.sample(laughs, 2))