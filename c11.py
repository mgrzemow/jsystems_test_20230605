import sqlite3


def laduj_dane(id):
    conn = sqlite3.connect('moja_baza.db')
    cursor = conn.cursor()
    cursor.execute('select * from tabela')
    all_data = cursor.fetchall()
    for i, *reszta in all_data:
        if id == i:
            return reszta
