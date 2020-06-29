import unittest
from more_fun_with_collections.dict_membership import in_dict

class FunctionTests(unittest.TestCase):

    def test_in_dict_true(self):
        d = {'cat': 4, 'dog': 3, 'horse': 9, 'buggy': 67, 'cart': 34}

        self.assertTrue(in_dict('cat', d))

    def test_in_dict_false(self):
        d = {'A': 4, 'B': 3, 'C': 9, 'D': 67, 'F': 34}
        self.assertFalse(in_dict('cat', d))