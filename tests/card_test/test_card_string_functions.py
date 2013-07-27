#!/usr/bin/python

"""Unit test module for Card class string output methods."""

# Disable the following pylint warnings:
#  - long identifier names, these are deliberate for unittests
#  - too many public methods, supposed to be lots of tests here
#
# pylint: disable=C0103
# pylint: disable=R0904


import unittest

from ...card import Card


class TestSequenceFunctions(unittest.TestCase):

    """Unit test class for Card class string output methods."""

    def setUp(self):
        pass

    def test_get_suit_string_short(self):

        """Test that a correct short suit string is returned.

        """

        samples = [(0, "C"), (1, "H"), (2, "S"), (3, "D")]

        for suit, suit_string in samples:
            test_string = Card(2, suit).suit_string(short=True)
            self.assertEqual(test_string, suit_string)

    def test_get_suit_string_long_nocaps(self):

        """Test that a correct long suit string is returned.

        """

        samples = [(0, "clubs"), (1, "hearts"), (2, "spades"), (3, "diamonds")]

        for suit, suit_string in samples:
            test_string = Card(7, suit).suit_string()
            self.assertEqual(test_string, suit_string)

    def test_get_suit_string_long_caps(self):

        """Test that a correct long suit string is returned.
        with the capitalize option set.

        """

        samples = [(0, "Clubs"), (1, "Hearts"), (2, "Spades"), (3, "Diamonds")]

        for suit, suit_string in samples:
            test_string = Card(12, suit).suit_string(capitalize=True)
            self.assertEqual(test_string, suit_string)

    def test_get_rank_string_short(self):

        """Test that a correct short rank string is returned.

        """

        samples = [
            (1, "A"), (2, "2"), (3, "3"), (4, "4"),
            (5, "5"), (6, "6"), (7, "7"), (8, "8"),
            (9, "9"), (10, "10"), (11, "J"), (12, "Q"),
            (13, "K"), (14, "A")
            ]

        for rank, rank_string in samples:
            test_string = Card(rank, "spades").rank_string(short=True)
            self.assertEqual(test_string, rank_string)

    def test_get_rank_string_long_nocaps(self):

        """Test that a correct long rank string is returned.

        """

        samples = [
            (1, "ace"), (2, "two"), (3, "three"), (4, "four"),
            (5, "five"), (6, "six"), (7, "seven"), (8, "eight"),
            (9, "nine"), (10, "ten"), (11, "jack"), (12, "queen"),
            (13, "king"), (14, "ace")
            ]

        for rank, rank_string in samples:
            test_string = Card(rank, "hearts").rank_string()
            self.assertEqual(test_string, rank_string)

    def test_get_rank_string_long_caps(self):

        """Test that a correct long rank string is returned.
        with the capitalize option set.

        """

        samples = [
            (1, "Ace"), (2, "Two"), (3, "Three"), (4, "Four"),
            (5, "Five"), (6, "Six"), (7, "Seven"), (8, "Eight"),
            (9, "Nine"), (10, "Ten"), (11, "Jack"), (12, "Queen"),
            (13, "King"), (14, "Ace")
            ]

        for rank, rank_string in samples:
            test_string = Card(rank, "clubs").rank_string(capitalize=True)
            self.assertEqual(test_string, rank_string)

    def test_get_name_string_short(self):

        """Test that a correct short name string is returned.

        """

        samples = [
            (1, 0, "AC"), (5, 1, "5H"), (9, 2, "9S"), (12, 3, "QD")
            ]

        for rank, suit, name_string in samples:
            test_string = Card(rank, suit).name_string(short=True)
            self.assertEqual(test_string, name_string)

    def test_get_name_string_short_caps(self):

        """Test that a correct short name string is returned.

        """

        samples = [
            (1, 0, "AC"), (5, 1, "5H"), (9, 2, "9S"), (12, 3, "QD")
            ]

        for rank, suit, name_string in samples:
            test_string = Card(rank, suit).name_string(short=True,
                                                       capitalize=True)
            self.assertEqual(test_string, name_string)

    def test_get_name_string_long_nocaps(self):

        """Test that a correct long name string is returned.

        """

        samples = [
            (1, 0, "ace of clubs"), (5, 1, "five of hearts"),
            (9, 2, "nine of spades"), (12, 3, "queen of diamonds")
            ]

        for rank, suit, name_string in samples:
            test_string = Card(rank, suit).name_string()
            self.assertEqual(test_string, name_string)

    def test_get_name_string_long_caps(self):

        """Test that a correct long name string is returned
        with the capitalization option set.

        """

        samples = [
            (1, 0, "Ace of Clubs"), (5, 1, "Five of Hearts"),
            (9, 2, "Nine of Spades"), (12, 3, "Queen of Diamonds")
            ]

        for rank, suit, name_string in samples:
            test_string = Card(rank, suit).name_string(capitalize=True)
            self.assertEqual(test_string, name_string)


if __name__ == "__main__":
    unittest.main()
