import json
import unittest.mock

json = unittest.mock.Mock()
print(json)
ret = json.load(1, 2, 3, a=11, b=22)
ret = json.load(4, 5, 6, a=999, b=222)
ret = json.loads(4, 5, 6, a=999, b=222)
print(ret)
json.load.assert_called()
print(json.load.call_args_list)
print(json.method_calls)