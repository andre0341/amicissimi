# -*- coding: utf-8 -*-
# !/usr/bin/env
# !/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
# " Elenco di tutte le carte in mtg prese da scryfall.
# Si connette, richiede l'elenco di tutte le carte,
# le stampa una prima volta in
# response, che ha 4 elementi. Poi prende solo "data" che è il payload vero e
# lo ristampa mandando a capo ogni volta "
# Buone regole per l'uso delle Scryfall API:
# API Docs at https://scryfall.com/docs/api
# 50 – 100 milliseconds delay between requests
# Otherwise HTTP 429 Too Many Requests

import requests
import json
import sys
from requests.exceptions import HTTPError
sys.path.append('/Users/andre/Google Drive/Projects/Python/Scryfall/')
from modules.stringsOperations import escape_string

url_to_get = []
url_to_get.append('https://api.scryfall.com/catalog/card-names')
# response = requests.get(url_to_get[0])

'''
if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found.')
'''

for url in url_to_get:
    try:
        response = requests.get(url,
                                params={'format': 'json'}
                                )
        # If the response was successful, no Exception will be raised
        response.raise_for_status()
        print(response.__class__)

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        # Python 3.6

    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')
        # print(response.text)

        # Se vuoi vedere tutte le carte
        # print(response.json())
        temp = response.json()
        # sets = json.load(temp)

        print("lunghezza = ", len(response.json()))

        # lunghezza 4 perchè nel json ci sono 4 attributi:
        # object, uri, total_values, data.
        # In 'data' ci sono tutte le 23K carte
        # Così stampi solo le carte
        # print(temp['data'])

        # !!!! Se vuoi solo il nome delle carte !!!!
        # print('\n'.join(temp['data']))

        # Se vuoi solo il nome delle carte nel formato "selectize"
        # { email: 'Game Night 2019',
        #   first_name: 'Game Night 2019',
        #   last_name: 'Game Night 2019'},

        json = ""

        for i in temp['data']:
            escaped = escape_string(i)
            """escaped = i.translate(str.maketrans({"-": r"\-",
                                                 "]": r"\]",
                                                "\\": r"\\",
                                                 "^": r"\^",
                                                 "$": r"\$",
                                                 "*": r"\*",
                                                 ".": r"\.",
                                                 "'": r"\'",
                                                 }))"""

            json += '{\"Name\":\"' + i + '\", "Qty": 0},'
            # print 'JSON', json.dumps(data)
            # print(escaped)
            print(json)
            # print('{\"Name\":\"', escaped,'\", "Qty": 0},')


# print(sys.version_info)