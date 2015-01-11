import unittest

import maternity


class TestMaternity(unittest.TestCase):
    def test_target_url_is_valid(self):
        self.assertEqual(
            maternity.get_response().url,
            "http://shjw.or.kr/bbs/board.php" + \
            "?bo_table=postnataldb" + \
            "&sca=%EC%84%9C%EC%9A%B8%EC%8B%9C"
        )

    def test_get_response_should_get_response(self):
        self.assertEqual(
            maternity.get_response().status_code,
            200
        )
