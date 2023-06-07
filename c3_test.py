# prztestować klasę Pracownik
import itertools
import json
import os
import pickle

import pytest
import c3


@pytest.fixture(scope='module')
def prepare_json_data():
    # to się wykonuje przed: fixtures in funkcjami testowymi zależnymi od tego fixture
    # udajemy że plik pickle jkest duży, wolny i chcemy go czytać tylko raz
    with open('dane_testowe.pickle', 'rb') as f:
        dane = pickle.load(f)
    nazwa_pliku = 'dane_testowe.json'
    print('----- TWORZĘ PLIK ----')
    # to jest symulacja plików tymczasowych, które będę chciał wyczyścić na koniec przebiegu testów
    with open(nazwa_pliku, 'wt', encoding='utf8') as f:
        json.dump(dane, f, ensure_ascii=False, indent=2)
    # dotąd
    # teraz jest zwracana wartość
    yield nazwa_pliku
    # a po zakończeniu testów wykonywana jest reszta kodu:
    print('----- KASUJĘ PLIK ----')
    os.remove(nazwa_pliku)


@pytest.fixture
def all_data_json(prepare_json_data):
    with open(prepare_json_data, 'rt', encoding='utf8') as f:
        d = json.load(f)
    return d


@pytest.fixture
def data_json_int(all_data_json):
    intowe_dane = all_data_json['int']
    return intowe_dane


@pytest.fixture
def data_json_float(all_data_json):
    intowe_dane = all_data_json['float']
    return intowe_dane


@pytest.fixture
def data_json_zerowe_czasy(all_data_json):
    intowe_dane = all_data_json['zerowe_czasy']
    return intowe_dane


@pytest.fixture
def data_json_brak_pracy(all_data_json):
    intowe_dane = all_data_json['brak_pracy']
    return intowe_dane


@pytest.fixture
def employees():
    return [
        (70, 100, 'Jan'),
        (20, 50, 'Anna'),
    ]


@pytest.fixture
def employees_value_error():
    return [
        (-70, 100, 'Jan'),
        (20, -50, 'Anna'),
    ]


def test_pracownik_data_int_float(data_json_int, data_json_float):
    for d in itertools.chain(data_json_int, data_json_float):
        p = c3.Pracownik(d['imie'],
                         stawka_normalna=d['s_normalna'],
                         stawka_nadgodzinowa=d['s_nadgodzinowa'])
        for t in d['dni']:
            p.pracuj(t)
        assert p.wyplata() == d['wyplata']


def test_pracownik_data_zero(data_json_zerowe_czasy, data_json_brak_pracy):
    for d in itertools.chain(data_json_zerowe_czasy, data_json_brak_pracy):
        p = c3.Pracownik(d['imie'],
                         stawka_normalna=d['s_normalna'],
                         stawka_nadgodzinowa=d['s_nadgodzinowa'])
        for t in d['dni']:
            p.pracuj(t)
        assert p.wyplata() == 0


# 1. Czy dobrze nalicza zarobki
# 2. Czy wyplata resetuje licznik
# 5. imie jest zmienialne

def test_basic(employees):
    for s_norm, s_nad, imie in employees:
        p = c3.Pracownik(imie, stawka_normalna=s_norm, stawka_nadgodzinowa=s_nad)
        assert p is not None
        assert hasattr(p, 'imie')
        p.imie == imie
        assert p.wyplata() == 0
        p.pracuj(5)
        assert p.wyplata() > 0
        assert p.wyplata() == 0
        with pytest.raises(AttributeError):
            p.asdjlqweioasdhklasdfjhklasdjklasdjkl = 'asdasdasd'
        stare_imie = p.imie
        p.imie = p.imie + '3332121212'
        assert p.imie != stare_imie
        assert str(p)
        assert imie in str(p)
        assert 'zarobki' in str(p)


def test_basic_pracownik(employees):
    for s_norm, s_nad, imie in employees:
        p = c3.Pracownik(imie, stawka_normalna=s_norm, stawka_nadgodzinowa=s_nad)
        p.pracuj(1)
        assert p.wyplata() == s_norm

        p.pracuj(2)
        assert p.wyplata() == 2 * s_norm

        p.pracuj(6)
        assert p.wyplata() == 6 * s_norm

        p.pracuj(7)
        assert p.wyplata() == 7 * s_norm

        p.pracuj(8)
        w = p.wyplata()
        p.pracuj(9)
        assert p.wyplata() - w == s_nad


# 3. Warunki brzegowe - poprawne
def test_wartosci_brzegowe(employees):
    ...


# 4. Wartości błędne:
# - 0 <= ile_h <= 24 - jeżeli nie to ValueError
# - ile_h musi być int lub float - jak nie to TypeError

def test_bledne_wartosci(employees):
    for s_norm, s_nad, imie in employees:
        p = c3.Pracownik(imie, stawka_normalna=s_norm, stawka_nadgodzinowa=s_nad)
        with pytest.raises(ValueError):
            p.pracuj(-1)
        with pytest.raises(ValueError):
            p.pracuj(25)
        with pytest.raises(ValueError):
            p.pracuj(-0.000001)
        with pytest.raises(ValueError):
            p.pracuj(24.000001)


# - błędy zaokrągleń - co z .1 + .1 + .1 - poprosze zaokrąglanie do 3 miejsca po kropce

def test_zaokraglenie_float():
    p1 = c3.Pracownik('Ala', stawka_normalna=0.1, stawka_nadgodzinowa=10)
    p1.pracuj(1)
    p1.pracuj(1)
    p1.pracuj(1)
    assert p1.wyplata() == .3


def test_pracownik_tworzenie_bledy(employees_value_error):
    for s_norm, s_nad, imie in employees_value_error:
        with pytest.raises(ValueError):
            c3.Pracownik(imie, stawka_normalna=s_norm, stawka_nadgodzinowa=s_nad)

# 6. duża ilość operacji przed wypłatą
#
# - jak sobie pomóc - tj jak zautomatyzować takie testy
