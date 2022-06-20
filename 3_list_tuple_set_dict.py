my_string = 'Hello world, this is miracle world'

# list (изменяемый список)
my_list = list(my_string)
print(my_list)

my_list.append("give me") # добавить
my_list.pop(2) # удалить порядковый элемент

#перебрат список
for i in my_list:
    print(i)

# tuple (неизменяемый кортеж)
my_tuple = tuple(my_string)
print(my_tuple)

# set (множество уникальных элементов, неупорядоченные)
my_set = set(my_string)
print(my_set)

my_set.add("addy")
print(my_set)

# найти дубликаты последовательности
duplicates = set([x for x in my_string if my_string.count(x) > 1])
print("Дубликаты: ", duplicates)


# dict (словарь)
my_dict = dict(zip(range(0, len(my_string)), my_string))
for k, v in my_dict.items():
    print(k, ":", v)

# update dict
my_dict.update({111: "qwe"})

# update/add dict
if my_dict.get(2):
    my_dict[2] = "hello amigos"

for k, v in my_dict.items():
    print(k, ":", v)

