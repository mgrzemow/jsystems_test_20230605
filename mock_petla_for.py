from unittest.mock import Mock, MagicMock

m = Mock()
m.__iter__ = Mock()
m.__iter__ = lambda i: [1, 2, 3, 4].__iter__()

for i in m:
    print(i)

for i in m:
    print(i)

m = MagicMock()
m.__iter__.return_value = [1, 2, 3, 4]

for i in m:
    print(i)

for i in m:
    print(i)
