def policz_linie(nazwa_pliku):
    with open(nazwa_pliku, 'rt', encoding='utf8') as f:
        # comprehension - bardzo fajne!!!
        return sum(1 for linia in f)


def znajdz_nadluzsza(nazwa_pliku):
    with open(nazwa_pliku, 'rt', encoding='utf8') as f:
        najdluzsza = 0
        najdluzsza_nr = 0
        for i, linia in enumerate(f):
            linia_len = len(linia)
            if linia_len > najdluzsza:
                najdluzsza = linia_len
                najdluzsza_nr = i
        return najdluzsza_nr


def szukaj_w_pliku(nazwa_pliku, napis):
    with open(nazwa_pliku, 'rt', encoding='utf8') as f:
        for i, linia in enumerate(f):
            if napis in linia:
                return i
