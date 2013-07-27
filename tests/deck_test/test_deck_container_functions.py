#!/usr/bin/python

"""Test module for container functions of deck module."""

# Disable the following pylint warnings:
#  - long identifier names, these are deliberate for unittests
#  - too many public methods, supposed to be lots of tests here
#
# pylint: disable=C0103
# pylint: disable=R0904


import unittest

from ...deck import Deck


class TestSequenceFunctions(unittest.TestCase):

    """Test sequence class for container functions of deck module."""

    def setUp(self):
        pass

    def test_contains(self):

        """
        Test operation of the __contains__ method.

        """

        deck = Deck()
        get_list = deck.get_card_list()
        contains_list = [card for card in deck]
        self.assertEqual(get_list, contains_list)

    def test_getitem(self):

        """
        Test operation of the __getitem__ method.

        """

        deck = Deck()
        get_list = deck.get_card_list()
        getitem_list = [deck[idx] for idx in range(52)]
        self.assertEqual(get_list, getitem_list)

    def test_setitem(self):

        """
        Test operation of the __setitem__ method.

        """

        deck1 = Deck()
        deck2 = Deck()
        d1_clist = deck1.get_card_list()
        d2_clist = deck1.get_card_list()
        self.assertEqual(d1_clist, d2_clist)

        deck1.shuffle()
        d1_clist = deck1.get_card_list()
        self.assertNotEqual(d1_clist, d2_clist)

        for idx, card in enumerate(d1_clist):
            deck2[idx] = card
        d2_clist = deck2.get_card_list()
        self.assertEqual(d1_clist, d2_clist)

    def test_delitem(self):

        """
        Test operation of the __delitem__ method.

        """

        deck = Deck()
        del(deck[33])
        self.assertEqual(len(deck), 51)


if __name__ == "__main__":
    unittest.main()
