# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests

# content of test_code.py

#Comprobar si el api rest de cryptowatch esta disponible para extraer datos
def func():
    r = requests.get("https://api.cryptowat.ch/markets/bitmex/btcusd-perpetual-futures/price?apikey=M1SR7D1BZ1Q688SYH30V")
    if r.status_code == 200:
        return 200
    else:
        return 400


def test_answer():
    assert func() == 200