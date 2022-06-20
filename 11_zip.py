"""
Функция zip позволяет легко объединить два списка. После вызова возвращается итератор.
 Чтобы увидеть содержимое, нужно сначала преобразовать его в список. Это полезно в циклах,
  так как позволяет избавиться от лишних вводов. Аналогично можно разбить один список на
  несколько. Для этого нужно перед списком добавить звездочку.
"""

first_list = ['Victor', 'Semen', 'Petr', 'Mickael', 'Serega']
second_list = ['Moscow', 'Piter', 'NewYork', 'London', 'Paris', 'Tokio']
age = [11, 34, 23, 45, 67, 54, 32, 8, 12]
list_iter = list(zip(first_list, second_list, age))

print(list_iter)

for k in list_iter:
    print(k)

split_iter = zip(*first_list)
print(*split_iter)