#!/usr/bin/python

"""Test module for deck module."""

# Disable the following pylint warnings:
#  - long identifier names, these are deliberate for unittests
#  - too many public methods, supposed to be lots of tests here
#
# pylint: disable=C0103
# pylint: disable=R0904


import unittest

from ...deck import Deck


class TestSequenceFunctions(unittest.TestCase):

    """Test sequence class for deck module."""

    def setUp(self):
        pass

    def test_shuffle_shuffles(self):

        """
        Test that the shuffled card list is different to the
        original card list.

        """

        deck = Deck()
        original_list = deck.get_card_list()
        deck.shuffle()
        shuffled_list = deck.get_card_list()
        self.assertNotEqual(original_list, shuffled_list)

    def test_shuffle_no_size_change(self):

        """
        Test that the deck size doesn't change on shuffling (fairly
        unlikely error).

        """

        deck = Deck()
        original_size = len(deck)
        deck.shuffle()
        shuffled_size = len(deck)
        self.assertEqual(original_size, shuffled_size)


if __name__ == "__main__":
    unittest.main()
