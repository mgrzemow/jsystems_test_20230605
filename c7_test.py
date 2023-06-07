import logging

import pytest
import c7

# def test_1(caplog, capfd):
#     c7.f1(logging.DEBUG, 'message DEBUG')
#     c7.f1(logging.INFO, 'message INFO')
#     c7.f1(logging.WARNING, 'message WARNING')
#     c7.f1(logging.ERROR, 'message ERROR')
#     c7.f1(logging.CRITICAL, 'message CRITICAL')
#
#     with capfd.disabled():
#         for m in caplog.messages:
#             print(m)
#     assert 1 == 2

def test_2(caplog, capfd):
    with caplog.at_level(logging.DEBUG):
        c7.f1(logging.DEBUG, 'message DEBUG')
        c7.f1(logging.INFO, 'message INFO')
        c7.f1(logging.WARNING, 'message WARNING')
        c7.f1(logging.ERROR, 'message ERROR')
        c7.f1(logging.CRITICAL, 'message CRITICAL')

    with capfd.disabled():
        print('a teraz:')
        for m in caplog.messages:
            print(m)
        for r in caplog.records:
            print(r)
    assert 1 == 2
