# -*- coding: utf-8 -*-
import unittest

import requests

from maternity import get_response
from maternity import get_total_pages
from maternity import get_locations
from maternity import get_all_detail_page_url_in_location


class TestAssociation(unittest.TestCase):
    def setUp(self):
        self.response = get_response()
        self.total_pages = get_total_pages(self.response)

    def test_get_response_should_requests_valid_url(self):
        self.assertEqual(
            self.response.url,
            "http://shjw.or.kr/bbs/board.php?bo_table=postnataldb&sca=%EC%84%9C%EC%9A%B8%EC%8B%9C"
        )

    def test_get_response_should_have_status_code_ok(self):
        self.assertEqual(
            self.response.status_code,
            requests.codes.ok,
        )

    def test_get_total_pages_should_return_int(self):
        self.assertTrue(isinstance(self.total_pages, int))

    def test_get_locations_should_return_list(self):
        self.assertTrue(isinstance(get_locations(), list))

    def test_get_locations_should_return_list_not_empty(self):
        self.assertGreaterEqual(
            get_locations(), 1
        )

    def test_get_all_detail_page_url_in_Seoul_should_return_list(self):
        self.assertTrue(
            isinstance(
                get_all_detail_page_url_in_location(get_locations()[0]),
                list
            )
        )
