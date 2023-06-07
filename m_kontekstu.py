class MojMenedzer():
    def __enter__(self):
        print('__enter__')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__', exc_type, exc_val, exc_tb)
        return True

m_kontekstu = MojMenedzer()

with m_kontekstu as mk:
    print(1, mk)
    print(2)
    open('asdasdasdasd')
    print(3)
    9 / 0
print(4)
