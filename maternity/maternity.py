#-*- coding: utf-8 -*-

import requests


def get_response():
    BASE_URL = "http://shjw.or.kr/bbs/board.php"
    response = requests.get(
        BASE_URL,
        params = {
            'bo_table': 'postnataldb',
            'sca': '서울시',
            # 'wr_id': '123'
        }
    )

    return response
