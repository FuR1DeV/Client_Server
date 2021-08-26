"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""
import subprocess
import chardet

dicts = [subprocess.Popen(['ping', 'yandex.ru'], stdout=subprocess.PIPE),
         subprocess.Popen(['ping', 'youtube.com'], stdout=subprocess.PIPE)]
for v in dicts:
    for i in v.stdout:
        res = chardet.detect(i)
        print(res)
        i = i.decode(res['encoding']).encode('utf-8')
        print(i.decode('utf-8'))
