import pytest
import c6


def test_1(capfd):
    print('ala ma kota')
    # wczytuje krotkę (out, err) i kasuje to co się do tej pory zapisało
    txt1 = capfd.readouterr().out
    assert 'ma kota' in txt1
    txt2 = capfd.readouterr().out
    assert not txt2
    # standardowo:
    # _  = capfd.readouterr()
    # kod_ktory_ma_cos_wypisac
    # txt = capfd.readouterr()
    # assert ...
    with capfd.disabled():
        print('akuku, to się wypisze normalnie!!!')


def test_c6(capfd):
    # przetestować:
    # 1. że dir bez parametrów coś wypisze -
    # przykładowo - że zawiera: 'File(s)'
    c6.wypisz_dir('C:\\')
    txt = capfd.readouterr().out
    assert 'File(s)' in txt
    # 2. że dir C:\asdhilasdjasdjhklasdjhklasdjhkl2123412312
    # będzie mieć niepusty strumien err
    c6.wypisz_dir('asdfadasdadasdasdasdasdasdasd')
    txt = capfd.readouterr().err
    with capfd.disabled():
        print('wypisało się', txt)
    assert txt
