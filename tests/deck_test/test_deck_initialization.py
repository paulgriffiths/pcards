#!/usr/bin/python

"""Test module for deck module."""

# Disable the following pylint warnings:
#  - long identifier names, these are deliberate for unittests
#  - too many public methods, supposed to be lots of tests here
#
# pylint: disable=C0103
# pylint: disable=R0904


import unittest

from pcards import Card, Deck


class TestSequenceFunctions(unittest.TestCase):

    """Test sequence class for deck module."""

    def setUp(self):
        pass

    def test_packs_zero(self):

        """Test that a ValueError exception is raised when
        creating a deck with zero packs.

        """

        self.assertRaises(ValueError, Deck, 0)

    def test_packs_negative(self):

        """Test that a ValueError exception is raised when
        creating a deck with negative packs.

        """

        self.assertRaises(ValueError, Deck, -1)

    def test_packs_float(self):

        """Test that a ValueError exception is raised when
        creating a deck with floating point packs.

        """

        self.assertRaises(ValueError, Deck, 2.5)

    def test_packs_string(self):

        """Test that a ValueError exception is raised when
        creating a deck with a string passed for packs.

        """

        self.assertRaises(ValueError, Deck, "3")

    def test_decks_size_one_pack_unspecified(self):

        """Test that the correct size is returned for a deck
        with one pack implicitly specified.

        """

        deck = Deck()
        self.assertEqual(len(deck), 52)

    def test_decks_size_one_pack_specified(self):

        """Test that the correct size is returned for a deck
        with one pack explicitly specified.

        """

        deck = Deck(1)
        self.assertEqual(len(deck), 52)

    def test_decks_size_two_packs(self):

        """Test that the correct size is returned for a deck
        with two packs.

        """

        deck = Deck(2)
        self.assertEqual(len(deck), 104)

    def test_decks_size_three_packs(self):

        """Test that the correct size is returned for a deck
        with three packs.

        """

        deck = Deck(3)
        self.assertEqual(len(deck), 156)

    def test_all_cards_present(self):

        """
        Test that all expected cards are in a newly created deck.

        """

        deck = Deck()

        for card in [Card(rank, suit) for rank in range(1, 14)
                                      for suit in range(4)]:
            self.assertTrue(card in deck)

    def test_deck_top_card(self):

        """
        Test that the top card of a newly created deck is the
        ace of clubs.

        """

        deck = Deck()
        self.assertTrue(deck[-1].index() == 0)


if __name__ == "__main__":
    unittest.main()
