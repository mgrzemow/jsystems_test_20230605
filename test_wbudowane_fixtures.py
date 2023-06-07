import os
from builtins import staticmethod

import pytest
import logging

import requests as requests

import funkcje


def test_capture(capfd):
    print('akuku')
    t1 = capfd.readouterr().out
    assert 'akuku' in t1
    print('kukuryku')
    with capfd.disabled():
        print('a to się wydrukuje!')
        t2 = capfd.readouterr().out
        print([t1, t2])

    os.system('dir c:\\asdasdasdad')
    with capfd.disabled():
        print(capfd.readouterr().err)


@pytest.fixture
def temp_file(tmp_path):
    return tmp_path / 'tmp.txt'


def test_logging1(caplog, temp_file, capfd):
    logging.basicConfig(filename=temp_file, filemode='wt', encoding='utf8', level=logging.DEBUG)
    lgr = logging.getLogger(__name__)

    for lvl in [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL]:
        lgr.log(lvl, f'{lvl} message')
    with capfd.disabled():
        for r in caplog.records:
            print(r.msg)
    with caplog.at_level(logging.DEBUG):
        for lvl in [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL]:
            lgr.log(lvl, f'{lvl} message')


def test_logging2(caplog, temp_file, capfd):
    logging.basicConfig(filename=temp_file, filemode='wt', encoding='utf8', level=logging.DEBUG)
    lgr = logging.getLogger(__name__)
    with caplog.at_level(logging.DEBUG):
        for lvl in [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL]:
            lgr.log(lvl, f'{lvl} message')
    with capfd.disabled():
        for r in caplog.records:
            print(r.msg)


def test_monkeypatch_simple(monkeypatch):
    def f1_new():
        return 'tata'

    monkeypatch.setattr(funkcje, 'f1', f1_new)
    assert funkcje.f1() == 'tata'


def test_monkeypatch_built_in(monkeypatch):
    def newcwd():
        return 'karramba!'

    monkeypatch.setattr(os, 'getcwd', newcwd)
    assert os.getcwd() == 'karramba!'


def test_monkeypatch_class(monkeypatch):
    class FakeResponse:
        @staticmethod
        def json():
            return {'k1': 122}

    def fake_get(*args, **kwargs):
        return FakeResponse()

    with monkeypatch.context() as mp:
        mp.setattr(requests, 'get', fake_get)
        r = requests.get('http://fake.url')
        assert 'k1' in r.json()

