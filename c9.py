import requests


def konwertuj(waluta, kwota):
    r = requests.get('https://api.nbp.pl/api/exchangerates/tables/a/?format=json')
    kursy = {}
    for d in r.json()[0]['rates']:
        kursy[d['code'].lower()] = d['mid']
    return kwota / kursy[waluta.lower()]
