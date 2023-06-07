import pytest
import faker
import random
import datetime as dt
from c2 import rob_pesel

f = faker.Faker('PL_pl')

# 1.Jeżeli zostaną podane wartości z których nie da się zrobić daty:
#   to ma wylecieć błąd ValueError 'Błędna data - z danych XX.YY.YYYY nie da się stworzyć daty'
#
przypadki = [((1999, 11, 3, 34, False), '99110303400'), ((2002, 1, 13, 134, True), '02211313418'),
             ((2012, 9, 30, 4, True), '12293000412'), ((1960, 1, 23, 4, False), '60012300406'),
             ((1901, 1, 1, 1, True), '01010100115')]



@pytest.fixture(scope='module')
def przypadki_fixture():
    print('\n----------------------\n przypadki_fixture\n')
    przypadki = [((1999, 11, 3, 34, False), '99110303400'), ((2002, 1, 13, 134, True), '02211313418'),
                 ((2012, 9, 30, 4, True), '12293000412'), ((1960, 1, 23, 4, False), '60012300406'),
                 ((1901, 1, 1, 1, True), '01010100115')]
    return przypadki


def test_kilka_wartosci_ok_recznie():
    przypadki = [((1999, 11, 3, 34, False), '99110303400'), ((2002, 1, 13, 134, True), '02211313418'),
                 ((2012, 9, 30, 4, True), '12293000412'), ((1960, 1, 23, 4, False), '60012300406'),
                 ((1901, 1, 1, 1, True), '01010100115')]
    for params, pesel in przypadki:
        assert rob_pesel(*params) == pesel


@pytest.mark.parametrize(['parametry', 'pesel'], przypadki)
def test_kilka_wartosci_ok_parametrize(parametry, pesel):
    assert rob_pesel(*parametry) == pesel


def test_kilka_wartosci_ok_fixture1(przypadki_fixture):
    for params, pesel in przypadki_fixture:
        assert rob_pesel(*params) == pesel


def test_kilka_wartosci_ok_fixture2(przypadki_fixture):
    for params, pesel in przypadki_fixture:
        assert rob_pesel(*params) == pesel


def test_wyjatki_data():
    wr = r'Błędna data - z danych -?\d+[.]-?\d+[.]-?\d+ nie da się stworzyć daty'
    # ValueError ValueError 'Błędna data - z danych XX.YY.YYYY nie da się stworzyć daty'
    with pytest.raises(ValueError, match=wr):
        rob_pesel(2023, 2, 29, 11, True)
    with pytest.raises(ValueError, match=wr):
        rob_pesel(2023, 1, 32, 11, True)
    with pytest.raises(ValueError, match=wr):
        rob_pesel(-2023, 11, 9, 11, True)
    with pytest.raises(ValueError, match=wr):
        rob_pesel(2023, 11, -9, 11, True)


def test_wyjatki_nr():
    wr = r'Błędny nr - -?\d+ nie jest z zakresu 0-999'
    # ValueError ValueError 'Błędna data - z danych XX.YY.YYYY nie da się stworzyć daty'
    with pytest.raises(ValueError, match=wr):
        rob_pesel(2023, 2, 28, 1111, True)


def test_losowe_dane():
    f = faker.Faker('PL_pl')
    for _ in range(9999):
        nr = random.randint(0, 999)
        plec_facet = random.choice([True, False])
        d1 = dt.date.today()
        d: dt.date = f.date_between(d1 - 60 * 365 * dt.timedelta(days=1), d1)
        pesel = rob_pesel(d.year, d.month, d.day, nr, plec_facet)
        # przykład brute force
        # pesel = rob_pesel(random.randint(1,2023), random.randint(1,99), random.randint(1,99), nr, plec_facet)
        assert len(pesel) == 11
        assert pesel[-2] in '01', 'Cyfra płci musi byc 0 lub 1'
        assert pesel[4] in '0123', 'Pierwsza cyfra dni'
        assert pesel[2] in '0123' 'Pierwsza cyfra miesięcy'
        assert pesel.isdigit()

def test_example():
    assert 'mama' in 'ala ma kota mama'.split()
