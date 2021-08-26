"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""
from sys import getdefaultencoding

getdefaultencoding()

dicts = ['разработка', 'администрирование', 'protocol', 'standard']

dicts_encode = [i.encode('utf-8') for i in dicts]
print(dicts_encode)

dicts_decode = [i.decode('utf-8') for i in dicts_encode]
print(dicts_decode)
