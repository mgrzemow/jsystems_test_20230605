from pprint import pprint

import c5
import pytest
import pathlib
import os.path
import random

import faker


# napisać kod który doda n plików w tymczasowym katalogu
# do każdego z plikow zapisze losową ilość linii (random.randint)
# generacja tekstu losowego:
# a następnie zwróci strukturę:

# p1 = pathlib.Path('C:/tmp1')
# p2 = p1 / 'tmp2'


@pytest.fixture(scope='module')
def pliki_testowe(tmp_path_factory):
    N_PLIKOW = 5
    MAX_LINII = 100
    fk = faker.Faker('PL_pl')
    dane = []
    tmp_path = tmp_path_factory.mktemp('pliki_tekstowe')
    for nr_pliku in range(N_PLIKOW):
        sciezka_do_pliku = tmp_path / f'plik_{nr_pliku}.txt'
        with open(sciezka_do_pliku, 'wt', encoding='utf8') as f:
            il_linii = random.randint(1, MAX_LINII)
            linia_do_wpisania = random.randint(1, il_linii - 1)
            najdluzsza_linia = 0
            najdluzsza_linia_nr = 0
            for nr_linii in range(il_linii):
                linia = fk.paragraph().strip()
                aktualna_dlugosc = len(linia)
                if aktualna_dlugosc > najdluzsza_linia:
                    najdluzsza_linia = aktualna_dlugosc
                    najdluzsza_linia_nr = nr_linii
                if nr_linii == linia_do_wpisania:
                    linia += 'TRX222333444'
                f.write(linia + '\n')
        dane.append((sciezka_do_pliku, nr_linii + 1, najdluzsza_linia_nr, linia_do_wpisania))
    pprint(dane)
    return dane


def test_policz_linie(pliki_testowe):
    # testowanie
    for sciezka, il_linii, _, _ in pliki_testowe:
        assert c5.policz_linie(sciezka) == il_linii


def test_najdluzsza_linia(pliki_testowe):
    # testowanie
    for sciezka, _, nr_najdluzszej, _ in pliki_testowe:
        assert c5.znajdz_nadluzsza(sciezka) == nr_najdluzszej


def test_szukaj(pliki_testowe):
    for sciezka, _, _, nr_znaleziony in pliki_testowe:
        assert c5.szukaj_w_pliku(sciezka, 'TRX222333444') == nr_znaleziony
