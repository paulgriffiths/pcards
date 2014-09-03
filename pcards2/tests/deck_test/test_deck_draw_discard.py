#!/usr/bin/python

"""Test module for deck module."""

# Disable the following pylint warnings:
#  - long identifier names, these are deliberate for unittests
#  - too many public methods, supposed to be lots of tests here
#
# pylint: disable=C0103
# pylint: disable=R0904


import unittest

from ...deck import Deck, EmptyDeckError


class TestSequenceFunctions(unittest.TestCase):

    """Test sequence class for deck module."""

    def setUp(self):
        pass

    def test_overdraw_exception(self):

        """
        Test that an EmptyDeckError is raised when too many cards
        are drawn from the deck.

        """

        deck = Deck()
        deck.draw(52)
        self.assertRaises(EmptyDeckError, deck.draw, 1)

    def test_draw_deck_count(self):

        """
        Test that the list counts are consistent and expected after
        a draw() operation.

        """

        deck = Deck()
        d_list = deck.draw(8)
        self.assertEqual(len(deck), 44)
        self.assertEqual(len(d_list), 8)

    def test_draw_discard_count(self):

        """
        Test that the list counts are consistent and expected after
        a draw() and discard() operation.

        """

        deck = Deck()
        deck.discard(deck.draw(12))
        self.assertEqual(len(deck), 40)
        self.assertEqual(deck.discard_size(), 12)

    def test_draw_discard_replace_count(self):

        """
        Test that the list counts are consistent and expected after
        a draw() and discard() operation, and a replace_discards()
        operation.

        """

        deck = Deck()
        deck.discard(deck.draw(17))
        self.assertEqual(len(deck), 35)
        self.assertEqual(deck.discard_size(), 17)
        deck.replace_discards()
        self.assertEqual(deck.discard_size(), 0)
        self.assertEqual(len(deck), 52)

    def test_discard_replace_top_card(self):

        """
        Test that the top card doesn't change after a replace_discards()
        operation, i.e. that the discards are being replaced at the
        back of the deck.

        """

        deck = Deck()
        deck.draw(4)
        card = deck[-1]
        deck.replace_discards()
        self.assertTrue(deck[-1] is card)


if __name__ == "__main__":
    unittest.main()
