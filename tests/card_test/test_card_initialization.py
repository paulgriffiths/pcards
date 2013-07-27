#!/usr/bin/python

"""Unit test module for Card class initialization."""

# Disable the following pylint warnings:
#  - long identifier names, these are deliberate for unittests
#  - too many public methods, supposed to be lots of tests here
#
# pylint: disable=C0103
# pylint: disable=R0904


import unittest

from ...card import Card, CardArgumentError


class TestSequenceFunctions(unittest.TestCase):

    """Unit test class for Card class initialization."""

    def setUp(self):
        pass

    def test_all_arguments_missing_exception(self):

        """Test that a CardArgumentError exception is raised
        when attempting to create a card with no arguments
        supplied.

        """

        self.assertRaises(CardArgumentError, Card)

    def test_all_arguments_present_non_zero_exception(self):

        """Test that a CardArgumentError exception is raised
        when attempting to create a card with all arguments
        supplied.

        """

        self.assertRaises(CardArgumentError, Card, 1, 2, 14)
        self.assertRaises(CardArgumentError, Card, 1, 2, "AS")
        self.assertRaises(CardArgumentError, Card, 1, 2, 14, "AS")

    def test_all_arguments_present_zero_exception(self):

        """Test that a CardArgumentError exception is raised
        when attempting to create a card with all arguments
        supplied with zero values (i.e. but not 'None')

        """

        self.assertRaises(CardArgumentError, Card, 0, 0, 0)

    # pylint: disable=R0201
    # pylint: disable=W0612

    def test_rank_range_ok(self):

        """Test that no exceptions are raised when attempting
        to create a card with a rank between one and fourteen.

        """

        cards = [Card(rank, "clubs") for rank in range(1, 15)]

    def test_rank_names_ok(self):

        """Test that no exceptions are raised when attempting
        to create a card with any allowable rank string.

        """

        ranks = [
            "a", "ac", "ace", "t", "tw", "two",
            "t", "th", "thr", "thre", "three",
            "f", "fo", "fou", "four",
            "fi", "fiv", "five",
            "s", "si", "six",
            "se", "sev", "seve", "seven",
            "e", "ei", "eig", "eigh", "eight",
            "n", "ni", "nin", "nine",
            "t", "te", "ten",
            "j", "ja", "jac", "jack",
            "q", "qu", "que", "quee", "queen",
            "k", "ki", "kin", "king",
            ]

        cards = [Card(rank.upper(), "hearts") for rank in ranks]
        cards = [Card(rank, "spades") for rank in ranks]

    # pylint: enable=R0201
    # pylint: enable=W0612

    def test_rank_zero_exception(self):

        """Test that a ValueError exception is raised when
        attempting to create a card with a rank of zero.

        """

        self.assertRaises(ValueError, Card, 0, "clubs")

    def test_rank_negative_exception(self):

        """Test that a ValueError exception is raised when
        attempting to create a card with a negative rank.

        """

        self.assertRaises(ValueError, Card, -5, "diamonds")

    def test_rank_too_high_exception(self):

        """Test that a ValueError exception is raised when
        attempting to create a card with a rank above 14.

        """

        self.assertRaises(ValueError, Card, 15, "spades")

    def test_rank_float_exception(self):

        """Test that a ValueError exception is raised when
        attempting to create a card with a floating point
        rank.

        """

        self.assertRaises(ValueError, Card, 4.5, "spades")

    def test_rank_bad_values_exception(self):

        """Test that a ValueError exception is raised when
        attempting to create a card with a rank from a list
        of bad values.

        """

        bad_ranks = [
            "0", "zero", "15", "fifteen", "clubs",
            "hearts", "spades", "diamonds", "spam",
            "eggs", "15.5", "0.5", "-1", ""
            ]

        for rank in bad_ranks:
            self.assertRaises(ValueError, Card, rank, "diamonds")

    def test_rank_missing_exception(self):

        """Test that a CardArgumentError exception is raised
        when attempting to create a card with a suit supplied
        but not a rank.

        """

        self.assertRaises(CardArgumentError, Card, suit="hearts")

    def test_rank_correctly_set(self):

        """Test that the card's rank is correctly set and
        returned by the rank() method.

        """

        for rank in range(2, 15):
            self.assertEqual(Card(rank, "clubs").rank(), rank)

    def test_rank_one_correctly_set(self):

        """Test that the card's rank is correctly set to 14
        and returned by the rank() method when 1 is passed.

        """

        self.assertEqual(Card(1, "hearts").rank(), 14)

    # pylint: disable=R0201
    # pylint: disable=W0612

    def test_suit_range_ok(self):

        """Test that no exceptions are raised when attempting
        to create a card with a suit between zero and three.

        """

        cards = [Card(10, suit) for suit in range(4)]

    def test_suit_names_ok(self):

        """Test that no exceptions are raised when attempting
        to create a card with any allowable suit string.

        """

        suits = [
            "c", "cl", "clu", "club", "clubs",
            "h", "he", "hea", "hear", "heart", "hearts",
            "s", "sp", "spa", "spad", "spade", "spades",
            "d", "di", "dia", "diam", "diamo", "diamon", "diamond", "diamonds",
            ]

        cards = [Card(1, suit.upper()) for suit in suits]
        cards = [Card(14, suit) for suit in suits]

    # pylint: enable=R0201
    # pylint: enable=W0612

    def test_suit_negative_exception(self):

        """Test that a ValueError exception is raised when
        attempting to create a card with a negative suit.

        """

        self.assertRaises(ValueError, Card, 5, -1)

    def test_suit_too_high_exception(self):

        """Test that a ValueError exception is raised when
        attempting to create a card with a suit above 3.

        """

        self.assertRaises(ValueError, Card, 7, 4)

    def test_suit_float_exception(self):

        """Test that a ValueError exception is raised when
        attempting to create a card with a floating point
        suit.

        """

        self.assertRaises(ValueError, Card, 7, 2.5)

    def test_suit_bad_values_exception(self):

        """Test that a ValueError exception is raised when
        attempting to create a card with a suit from a list
        of bad values.

        """

        bad_suits = [
            "-1", "4", "spam", "eggs", "ace", "four", "five",
            "six", "seven", "eight", "nine", "ten", "jack",
            "queen", "king", "4.5", "-0.5", ""
            ]

        for suit in bad_suits:
            self.assertRaises(ValueError, Card, 12, suit)

    def test_suit_missing_exception(self):

        """Test that a CardArgumentError exception is raised
        when attempting to create a card with a rank supplied
        but not a suit.

        """

        self.assertRaises(CardArgumentError, Card, rank=4)

    def test_suit_correctly_set(self):

        """Test that the card's suit is correctly set and
        returned by the suit() method.

        """

        for suit in range(4):
            self.assertEqual(Card(3, suit).suit(), suit)

    def test_index_negative_exception(self):

        """Test that a ValueError exception is raised
        when attempting to create a card with a negative index
        supplied.

        """

        self.assertRaises(ValueError, Card, index=-1)

    def test_index_too_high_exception(self):

        """Test that a ValueError exception is raised
        when attempting to create a card with too high
        of an index (i.e. above 51).

        """

        self.assertRaises(ValueError, Card, index=52)

    def test_index_float_exception(self):

        """Test that a ValueError exception is raised
        when attempting to create a card with a floating
        point index.

        """

        self.assertRaises(ValueError, Card, index=12.5)

    def test_index_string_exception(self):

        """Test that a ValueError exception is raised
        when attempting to create a card with a string
        index.

        """

        self.assertRaises(ValueError, Card, index="4")

    def test_index_correctly_set(self):

        """Test that the card's index is correctly set and
        returned by the index() method.

        """

        for idx in range(52):
            self.assertEqual(Card(index=idx).index(), idx)

    def test_index_from_rank_and_value_ints(self):

        """Test that the card's index is correctly set and
        returned by the index() method.

        """

        samples = [
            (1, 0, 0), (2, 0, 1), (3, 0, 2), (4, 0, 3), (14, 0, 0),
            (1, 1, 13), (2, 1, 14), (3, 1, 15), (13, 1, 25), (14, 1, 13),
            (1, 2, 26), (5, 2, 30), (10, 2, 35), (11, 2, 36), (14, 2, 26),
            (1, 3, 39), (9, 3, 47), (11, 3, 49), (13, 3, 51), (14, 3, 39)
            ]

        for rank, suit, idx in samples:
            self.assertEqual(Card(rank, suit).index(), idx)

    def test_index_from_rank_and_value_strings(self):

        """Test that the card's index is correctly set and
        returned by the index() method.

        """

        samples = [
            (1, 0, 0), (2, 0, 1), (3, 0, 2), (4, 0, 3), (14, 0, 0),
            (1, 1, 13), (2, 1, 14), (3, 1, 15), (13, 1, 25), (14, 1, 13),
            (1, 2, 26), (5, 2, 30), (10, 2, 35), (11, 2, 36), (14, 2, 26),
            (1, 3, 39), (9, 3, 47), (11, 3, 49), (13, 3, 51), (14, 3, 39)
            ]
        rank_strings = {
            1: "ace", 2: "two", 3: "three", 4: "four", 5: "five",
            6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
            11: "jack", 12: "queen", 13: "king", 14: "ace"
            }
        suit_strings = {0: "clubs", 1: "hearts", 2: "spades", 3: "diamonds"}

        for rank, suit, idx in samples:
            card = Card(rank_strings[rank], suit_strings[suit])
            self.assertEqual(card.index(), idx)

    def test_rank_from_index(self):

        """Test that the card's rank and suit and correctly set
        when initializing a card via index.

        """

        samples = [(0, 14), (1, 2), (2, 3), (3, 4), (4, 5),
                   (5, 6), (6, 7), (7, 8), (8, 9), (9, 10),
                   (10, 11), (11, 12), (12, 13), (13, 14)]

        for idx, rank in samples:
            self.assertEqual(Card(index=idx).rank(), rank)

    def test_construct_by_name(self):

        """Test that a card correctly initializes by name.

        """

        samples = [("AC", 0), ("9c", 8), ("2H", 14), ("kh", 25),
                   ("4S", 29), ("Js", 36), ("7d", 45), ("qD", 50)]

        for name, idx in samples:
            self.assertEqual(Card(name=name).index(), idx)

    def test_construct_by_badname_raises(self):

        """Test that a card initialized by an invalid name raises
        a ValueError exception.

        """

        #samples = ["spam", "eggs", "15c", "0s", "7q", "99", "c", "5"]
        samples = [
            "spam", "eggs", "15c", "0s", "7q", "99", "c", "5", ""
        ]
        for badname in samples:
            self.assertRaises(ValueError, Card, name=badname)


if __name__ == "__main__":
    unittest.main()
