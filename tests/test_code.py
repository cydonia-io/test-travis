# -*- coding: utf-8 -*-
"""
@author: angeljuarez

"""
import requests

#run test
# !python -m pytest

#Import variables from src/api
from src.api.api_rest import * 


# content of test_code.py

#Check if cryptowatch api rest is available to extract data
def func():
    r = requests.get(api_price_bitmex_btcusd)
    if r.status_code == 200:
        return 200
    else:
        return 400


def test_answer():
    assert func() == 200