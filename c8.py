import os


def f1():
    p = os.getcwd()
    with open(f'{p}/tmp.txt', 'rt', encoding='utf8') as f:
        return f.read()
    