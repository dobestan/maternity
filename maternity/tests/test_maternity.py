import unittest

import maternity


class TestMaternity(unittest.TestCase):
    def test_get_response_should_get_response(self):
        self.assertEqual(
            maternity.get_response().status_code,
            200
        )
