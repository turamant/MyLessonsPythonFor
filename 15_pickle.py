"""
Модуль pickle постоянно хранит данные в одном файле. Представление объекта всегда байтовое,
 поэтому для хранения данных необходимо открывать файлы в wb,
  для загрузки данных из pickle - в rb. Данные могут быть любого типа.
"""

import pickle

data = {
    'a': 'some_value',
    'b': [9, 5, 8, 0],
    'c': ['some_str', 'another_str', 'spam', 'ham']
}
#save data
with open('pickledumpfile.dat', 'wb') as file:
    pickle.dump(data, file)

# load data
with open('picklefile.dat', 'rb') as file:
    data = pickle.load(file)


print(data['a'], data['b'])