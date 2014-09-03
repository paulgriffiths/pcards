#!/usr/bin/python

"""Test module for deck module."""

# Disable the following pylint warnings:
#  - long identifier names, these are deliberate for unittests
#  - too many public methods, supposed to be lots of tests here
#
# pylint: disable=C0103
# pylint: disable=R0904
# pylint: disable=W0212


import unittest

from ...deck import Deck


class TestSequenceFunctions(unittest.TestCase):

    """Test sequence class for deck module."""

    def setUp(self):
        pass

    def test_get_card_list_equals(self):

        """
        Test that the list returned from get_card_list() is
        equal to the internal card list.

        """

        deck = Deck()
        returned_list = deck.get_card_list()
        self.assertEqual(returned_list, deck._cards)

    def test_get_card_list_not_same(self):

        """
        Test that the list returned from get_card_list() is
        not the same as the internal card list, i.e. that
        the method is returning a copy.

        """

        deck = Deck()
        returned_list = deck.get_card_list()
        self.assertFalse(returned_list is deck._cards)

    def test_get_discard_list_equals(self):

        """
        Test that the list returned from get_discard_list() is
        equal to the internal discard list.

        """

        deck = Deck()
        returned_list = deck.get_discard_list()
        self.assertEqual(returned_list, deck._discards)

    def test_get_discard_list_not_same(self):

        """
        Test that the list returned from get_discard_list() is
        not the same as the internal discard list, i.e. that
        the method is returning a copy.

        """

        deck = Deck()
        returned_list = deck.get_discard_list()
        self.assertFalse(returned_list is deck._discards)


if __name__ == "__main__":
    unittest.main()
