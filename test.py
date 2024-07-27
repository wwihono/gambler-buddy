import unittest
from unittest import mock

# Assuming the functions are defined in a module named card_parser
from func import parse_cards, check_royal, add_royal, get_flop, get_player, convert_to_original


class TestCardFunctions(unittest.TestCase):

    def test_parse_cards(self):
        taken = []
        result = parse_cards("Ad10cKc", 3, taken)
        expected = {'13': ['d'], '9': ['c'], '12': ['c']}
        self.assertEqual(result, expected)
        self.assertEqual(taken, ['13d', '9c', '12c'])

        taken = []
        result = parse_cards("10d9s6c", 3, taken)
        expected = {'9': ['d'], '8': ['s'], '5': ['c']}
        self.assertEqual(result, expected)
        self.assertEqual(taken, ['9d', '8s', '5c'])


    def test_check_royal(self):
        self.assertTrue(check_royal('J'))
        self.assertTrue(check_royal('Q'))
        self.assertTrue(check_royal('K'))
        self.assertTrue(check_royal('A'))
        self.assertFalse(check_royal('2'))
        self.assertFalse(check_royal('9'))

    def test_add_royal(self):
        self.assertEqual(add_royal('J'), '11')
        self.assertEqual(add_royal('Q'), '12')
        self.assertEqual(add_royal('K'), '13')
        self.assertEqual(add_royal('A'), '14')

    def test_get_flop(self):
        taken = []
        # Mock input
        with mock.patch('builtins.input', return_value='Ad10cKc'):
            result = get_flop(taken)
            expected = {'13': ['d'], '9': ['c'], '12': ['c']}
            self.assertEqual(result, expected)
            self.assertEqual(taken, ['13d', '9c', '12c'])

    def test_get_player(self):
        taken = []
        # Mock input
        with unittest.mock.patch('builtins.input', return_value='AdKc'):
            result = get_player(taken)
            expected = {'13': ['d'], '12': ['c']}
            self.assertEqual(result, expected)
            self.assertEqual(taken, ['13d', '12c'])

    def test_convert_to_original(self):
        dictionary = {'13': ['d', 'c'], '10': ['h']}
        result = convert_to_original(dictionary)
        expected = {'A': ['d', 'c'], 'J': ['h']}
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
