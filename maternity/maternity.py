#-*- coding: utf-8 -*-

import requests


def get_response(BASE_URL, params):
    response = requests.get(
        BASE_URL,
        params = params,
    )

    return response
