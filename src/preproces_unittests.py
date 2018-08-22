import unittest
from src import preprocess


class TestPreprocess(unittest.TestCase):

    def test_parse_first_cabin_letter_is_m(self):
        self.assertEqual(preprocess.parse_first_cabin_letter('M 45'), 'M')


if __name__ == '__main__':
    unittest.main()      