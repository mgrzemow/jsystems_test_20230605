import pytest
import requests
from unittest.mock import Mock
import c10

JSON_RESPONSE = [
    {
        "table": "A",
        "no": "109/A/NBP/2023",
        "effectiveDate": "2023-06-07",
        "rates": [
            {
                "currency": "bat (Tajlandia)",
                "code": "THB",
                "mid": 0.1205
            },
            {
                "currency": "dolar amerykański",
                "code": "USD",
                "mid": 4.0
            },
            {
                "currency": "dolar australijski",
                "code": "AUD",
                "mid": 2.8024
            },
            {
                "currency": "dolar Hongkongu",
                "code": "HKD",
                "mid": 0.5342
            },
            {
                "currency": "dolar kanadyjski",
                "code": "CAD",
                "mid": 3.1286
            },
            {
                "currency": "dolar nowozelandzki",
                "code": "NZD",
                "mid": 2.5464
            },
            {
                "currency": "dolar singapurski",
                "code": "SGD",
                "mid": 3.1079
            },
            {
                "currency": "euro",
                "code": "EUR",
                "mid": 4.4790
            },
            {
                "currency": "forint (Węgry)",
                "code": "HUF",
                "mid": 0.012144
            },
            {
                "currency": "frank szwajcarski",
                "code": "CHF",
                "mid": 4.6211
            },
            {
                "currency": "funt szterling",
                "code": "GBP",
                "mid": 5.2109
            },
            {
                "currency": "hrywna (Ukraina)",
                "code": "UAH",
                "mid": 0.1140
            },
            {
                "currency": "jen (Japonia)",
                "code": "JPY",
                "mid": 0.030055
            },
            {
                "currency": "korona czeska",
                "code": "CZK",
                "mid": 0.1897
            },
            {
                "currency": "korona duńska",
                "code": "DKK",
                "mid": 0.6012
            },
            {
                "currency": "korona islandzka",
                "code": "ISK",
                "mid": 0.029761
            },
            {
                "currency": "korona norweska",
                "code": "NOK",
                "mid": 0.3794
            },
            {
                "currency": "korona szwedzka",
                "code": "SEK",
                "mid": 0.3845
            },
            {
                "currency": "lej rumuński",
                "code": "RON",
                "mid": 0.9034
            },
            {
                "currency": "lew (Bułgaria)",
                "code": "BGN",
                "mid": 2.2901
            },
            {
                "currency": "lira turecka",
                "code": "TRY",
                "mid": 0.1810
            },
            {
                "currency": "nowy izraelski szekel",
                "code": "ILS",
                "mid": 1.1450
            },
            {
                "currency": "peso chilijskie",
                "code": "CLP",
                "mid": 0.00526
            },
            {
                "currency": "peso filipińskie",
                "code": "PHP",
                "mid": 0.0747
            },
            {
                "currency": "peso meksykańskie",
                "code": "MXN",
                "mid": 0.2413
            },
            {
                "currency": "rand (Republika Południowej Afryki)",
                "code": "ZAR",
                "mid": 0.2193
            },
            {
                "currency": "real (Brazylia)",
                "code": "BRL",
                "mid": 0.8525
            },
            {
                "currency": "ringgit (Malezja)",
                "code": "MYR",
                "mid": 0.9098
            },
            {
                "currency": "rupia indonezyjska",
                "code": "IDR",
                "mid": 0.00028155
            },
            {
                "currency": "rupia indyjska",
                "code": "INR",
                "mid": 0.050772
            },
            {
                "currency": "won południowokoreański",
                "code": "KRW",
                "mid": 0.003214
            },
            {
                "currency": "yuan renminbi (Chiny)",
                "code": "CNY",
                "mid": 0.5882
            },
            {
                "currency": "SDR (MFW)",
                "code": "XDR",
                "mid": 5.5724
            }
        ]
    }
]


class UdajeReponse:
    @staticmethod
    def json(*args, **kwargs):
        return JSON_RESPONSE


# użyć monkeypatch do ustalenia na stałe kursów walut - podmieniamy funkcję get w paczkce requests

def nowy_get(*args, **kwargs):
    m = Mock()
    # m.json = Mock()
    m.json.return_value = JSON_RESPONSE
    m.request.method = 'GET'
    m.status_code = 200
    return m


def test_1(monkeypatch):
    monkeypatch.setattr('requests.get', nowy_get)
    assert c10.konwertuj('usd', 1000) == pytest.approx(250)
