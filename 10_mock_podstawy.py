from unittest.mock import Mock

m = Mock()

m.dowolna_funkcja(1, 2, 3, e=99, f=88)
m.atr1 = 22
print(m.atr2)
m(1, 2, 3, e=99, k=88)
print(m.atr1)
m.assert_called()

print(m.called)
print(m.call_args_list)
print(m.call_args)

