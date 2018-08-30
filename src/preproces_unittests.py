import unittest
import preprocess


class TestPreprocess(unittest.TestCase):

    def test_parse_first_cabin_letter_is_m(self):
        self.assertEqual(preprocess.parse_first_cabin_letter('M 45'), 'M')

    def test_parse_alphabetic_characters_is_a(self):
        self.assertEqual(preprocess.parse_alphabetic_characters('123a567'), 'a')
        
    def test_parse_alphabetic_characters_mutiple_letters(self):
        self.assertEqual(preprocess.parse_alphabetic_characters('1a23b56c7'), 'abc')
        
    def test_parse_alphabetic_characters_no_alphabetic(self):
        self.assertEqual(preprocess.parse_alphabetic_characters('123567'), '')
        
    def test_parse_alphabetic_characters_punct(self):
        self.assertEqual(preprocess.parse_alphabetic_characters(''), '')
        
    def test_parse_alphabetic_characters_from_none(self):
        self.assertEqual(preprocess.parse_alphabetic_characters(None), '')
    
    def test_period_prefix_is_mr(self):
        self.assertEqual(preprocess.parse_period_prefixes_to_list('mr.hemmingway'), ['mr'])
        
    def test_period_prefix_is_mr_and_ms(self):
        self.assertEqual(preprocess.parse_period_prefixes_to_list('mr.hemmingway and ms.hemmingway'), ['mr', 'ms'])
        
    def test_period_prefix_is_empty(self):
        self.assertEqual(preprocess.parse_period_prefixes_to_list('mrhemmingway'), [])

    def test_period_prefix_is_leading_space(self):
        self.assertEqual(preprocess.parse_period_prefixes_to_list(' mr.hemmingway'), ['mr'])

    def test_period_prefix_is_none(self):
        self.assertEqual(preprocess.parse_period_prefixes_to_list(None), [])
    
if __name__ == '__main__':
    unittest.main()      