# napisać klasę Pracownik, która będzie:
# - pamiętać imie, stawkę normalną i nadgodzinową
# - naliczać zarobki za dzień .pracuj(ile_h). Do 8h - stawka normalna, powyżej - nadgodzinowa
# - zwracać nzarobioną kwotę i resetować licznik - .wyplata()

class Pracownik:
    __slots__ = ['imie',
                 '_stawka_normalna',
                 '_stawka_nadgodzinowa',
                 '_zarobki']

    # konstruktor:
    def __init__(self, imie, stawka_normalna, stawka_nadgodzinowa):
        # walidowanie:
        if stawka_normalna < 0 or stawka_nadgodzinowa < 0:
            raise ValueError(f'Błędne dane pracownika {imie}, {stawka_normalna}, {stawka_nadgodzinowa}')
        # dodawanie atrybutów do instancji:
        self.imie = imie
        self._stawka_normalna = stawka_normalna
        self._stawka_nadgodzinowa = stawka_nadgodzinowa
        self._zarobki = 0

    def pracuj(self, ile_h):
        if ile_h < 0 or ile_h > 24:
            raise ValueError('Jakiś sensowny komunikat')
        if ile_h < 8:
            self._zarobki = round(self._zarobki + ile_h * self._stawka_normalna, 2)
        else:
            self._zarobki = round(self._zarobki + 8 * self._stawka_normalna + (ile_h - 8) * self._stawka_nadgodzinowa, 2)

    # można pomagać sobie w testach - niezbyt ładny design ale bywa i tak
    # def _wyplata(self):
    #     return self._wyplata()

    def wyplata(self):
        tmp = self._zarobki
        self._zarobki = 0
        return tmp

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.imie}", zarobki={self._zarobki})'

    # def __str__(self):
    #     return 'S: reprezentacja stringowa obiektu'


# if __name__ == '__main__':
#     ...
    # p1 = Pracownik('Jan', stawka_normalna=20, stawka_nadgodzinowa=40)
    # p2 = Pracownik('Ala', stawka_normalna=20, stawka_nadgodzinowa=40)
    # print(p1)  # Pracownik("Jan", zarobki=340)
    # p1.imie = 'Tomek'
    # print(p1)  # Pracownik("Jan", zarobki=340)
    # print(p1.imie)
    # p1.pracuj(5)
    # p1.pracuj(10)
    # print(p1)  # Pracownik("Jan", zarobki=340)
    # print(p1.wyplata())  # 340
    # print(p1)  # Pracownik("Jan", zarobki=0)
    # print(p1.wyplata())  # 0
    #
