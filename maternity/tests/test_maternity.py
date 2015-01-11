import unittest

import maternity


class TestMaternity(unittest.TestCase):
    def test_crawl_should_return_true(self):
        self.assertTrue(maternity.crawl())

    def test_parse_should_return_true(self):
        self.assertTrue(maternity.parse())
