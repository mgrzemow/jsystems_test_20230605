"""
Ćwiczenie:

Napisać funkcję, która:

1. Na podstawie:
 - roku urodenia,
 - miesiąca urodzenia
 - dnia urodzenia
 - nr kolejnego
 - określenia płci True == mężczyzna

wygeneruje pesel w następującego schematu:
 - 2 ostatnie cyfry roku
 - 2 cyfrowy miesiąc uzupełniony od lewej zerem (jeżeli rok >= 2000 to do miesiąca dodajemy 20)
 - 2 cyfrowy dzień uzupełniony od lewej zerem
 - 3 cyfrowy nr kolejny uzupełniony od lewej zerem
 - cyfra płci - 1 mężczyzna, 0 kobieta
 - suma kontrolna będąca ostatnią cyfrą sumy powyższych cyfr

Np dla kobiety urodzonej 3.12.2005r jako 13ta osoba powinno wyjść:
05320301307

Podpowiedzi:
 - pętla for dla napisów iteruje po literach
 - str(12)
 - int('12')
 - '2'.zfill(3)

Rozszerzenia ćwiczenia:
 - czy da się uniknąć użycia zfill (formatowanie fstringów)
"""
import datetime as dt

def rob_pesel(rok: int, miesiac: int, dzien: int, nr: int, plec_facet: bool) -> str:
    if nr > 999 or nr < 0:
        raise ValueError(f'Błędny nr - {nr} nie jest z zakresu 0-999')
    try:
        dt.date(year=rok, month=miesiac, day=dzien)
    except ValueError:
        raise ValueError(f'Błędna data - z danych {rok}.{miesiac}.{dzien} nie da się stworzyć daty')
    pesel = f'{str(rok)[-2:]}{miesiac + 20 if rok >= 2000 else miesiac:02}{dzien:02}{nr:03}{int(plec_facet)}'
    # suma = 0
    # for znak in pesel:
    #     suma += int(znak)
    # pesel += str(suma)[-1]
    pesel += str(sum(int(znak) for znak in pesel))[-1]
    return pesel

if __name__ == '__main__':
    przypadki = []
    k = (1999, 11, 3, 34,False)
    przypadki.append((k, rob_pesel(*k)))
    k = (2002, 1, 13, 134, True)
    przypadki.append((k, rob_pesel(*k)))
    k = (2012, 9, 30, 4, True)
    przypadki.append((k, rob_pesel(*k)))
    k = (1960, 1, 23, 4, False)
    przypadki.append((k, rob_pesel(*k)))
    k = (1901, 1, 1, 1, True)
    przypadki.append((k, rob_pesel(*k)))
    print(przypadki)

