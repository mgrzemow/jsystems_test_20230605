import pytest
import c11
from unittest.mock import Mock
import sqlite3

DANE = [
    (1, "Jan", 'Kowalski'),
    (2, "Adam", 'Nowak'),
    (3, "Alina", 'Adamek'),
]


def test_1(monkeypatch):
    # mockowanie
    cursor = Mock()
    cursor.fetchall.return_value = DANE
    connection = Mock()
    connection.cursor.return_value = cursor
    connect = Mock()
    connect.return_value = connection
    monkeypatch.setattr('sqlite3.connect', connect)
    assert c11.laduj_dane(2)[1] == 'Nowak'
