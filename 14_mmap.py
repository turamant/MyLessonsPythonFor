"""
Модуль mmap

С помощью модуля mmap ты можешь получать доступ к произвольным местоположениям в файле,
 отображая файл в память. Это альтернатива использованию обычных операций с файлами.
"""

import mmap

with open('english_text.txt', 'r', encoding="utf8") as fd:
    # 0: сопоставить весь файл
    mm = mmap.mmap(fd.fileno(), 0, access=mmap.ACCESS_READ,)

    print(mm[10:20])
    print(mm.readline())

