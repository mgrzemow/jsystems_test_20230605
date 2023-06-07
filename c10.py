import requests


def konwertuj(waluta, kwota):
    r = requests.get('https://api.nbp.pl/api/exchangerates/tables/a/?format=json')
    kursy = {}
    r.raise_for_status()
    if r.request.method != 'GET':
        raise Exception('Ojej nie ta metoda')
    if r.status_code != 200:
        raise Exception('Ojejku, nie ten status code!')
    for d in r.json()[0]['rates']:
        kursy[d['code'].lower()] = d['mid']
    return kwota / kursy[waluta.lower()]
