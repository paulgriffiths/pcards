#!/usr/bin/python

"""Unit test module for Card class conversion operators."""

# Disable the following pylint warnings:
#  - long identifier names, these are deliberate for unittests
#  - too many public methods, supposed to be lots of tests here
#
# pylint: disable=C0103
# pylint: disable=R0904


import unittest

from ...card import Card


class TestSequenceFunctions(unittest.TestCase):

    """Unit test class for Card class conversion operators."""

    def setUp(self):
        pass

    def test_string_conversion(self):

        """Test that a correct long name string is returned
        with the capitalization option set when a card is
        converted to a string.

        """

        samples = [
            (1, 0, "Ace of Clubs"), (5, 1, "Five of Hearts"),
            (9, 2, "Nine of Spades"), (12, 3, "Queen of Diamonds")
            ]

        for rank, suit, name_string in samples:
            test_string = str(Card(rank, suit))
            self.assertEqual(test_string, name_string)

    def test_int_conversion(self):

        """Test that the card's rank is correctly returned
        when converting to an integer

        """

        for rank in range(1, 14):
            self.assertEqual(int(Card(rank, "clubs")), rank)

    def test_int_conversion_ace_as_one(self):

        """Test that the card's rank is correctly returned
        when converting to an integer and the card is created
        with a rank of 14

        """

        self.assertEqual(int(Card(14, "diamonds")), 1)


if __name__ == "__main__":
    unittest.main()
