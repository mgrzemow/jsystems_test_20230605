import sys

import pytest
import time

VERSION = '1.2.3'


@pytest.mark.szybki
def test_1():
    assert 1 == 1


@pytest.mark.szybki
def test_2():
    assert 1 == 1


@pytest.mark.wolny
def test_3():
    time.sleep(10)
    assert 1 == 1


@pytest.mark.wolny
def test_4():
    time.sleep(10)
    assert 1 == 1


@pytest.mark.wolny
def test_5():
    time.sleep(10)
    assert 1 == 1


@pytest.mark.skip(reason="Nie mogę uruchomić bo mi wywali cały test")
def test_6():
    exit(1)
    assert 1 == 2


@pytest.mark.skipif(sys.platform == 'win32', reason='Nie da się urucuchomić w windowsie')
def test_7():
    assert 2 == 5


@pytest.mark.xfail
def test_8():
    assert 3 == 5


@pytest.mark.xfail
def test_8():
    assert 3 == 5


@pytest.mark.xfail(raises=ValueError)
def test_9():
    float('asdasdasd')


@pytest.mark.xfail(raises=ValueError, strict=True)
def test_10():
    assert 2 == 3


@pytest.mark.xfail
def test_11():
    assert 2 == 2


@pytest.mark.xfail(run=False)
def test_12():
    exit(1)


@pytest.mark.xfail(run=False)
def test_12():
    exit(1)


@pytest.mark.xfail(condition=VERSION == '1.2.3', reason='chwilowo nie działa w 1.2.3')
def test_13():
    exit(1)


@pytest.mark.niematakiego
def test_14():
    assert 1 == 1
