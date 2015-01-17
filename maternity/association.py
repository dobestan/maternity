# -*- coding: utf-8 -*-

import requests


def get_response():
    BASE_URL = "http://shjw.or.kr/bbs/board.php"
    params = {
        'bo_table': 'postnataldb',
        'sca': '서울시',
    }

    response = requests.get(BASE_URL, params=params)
    return response
