import pytest
import os

import c8


# Dokończyć test:
# Wygenerować katalog tymczasowy
# zapisać do niego plik
# podmienić getcwd
# wywolac c8.f1, sprawdzając, czy poprawnie wczyta plik

def test_c8(monkeypatch, tmp_path):
    def nowe_getcwd():
        return tmp_path

    with open(tmp_path / 'tmp.txt', 'wt', encoding='utf8') as f:
        f.write('treść pliku')

    monkeypatch.setattr('os.getcwd', nowe_getcwd)
    assert c8.f1() == 'treść pliku'

def test_c8_context(monkeypatch, tmp_path):
    def nowe_getcwd():
        return tmp_path

    with open(tmp_path / 'tmp.txt', 'wt', encoding='utf8') as f:
        f.write('treść pliku')
    with monkeypatch.context() as mpc:
        mpc.setattr('os.getcwd', nowe_getcwd)
        assert c8.f1() == 'treść pliku'
