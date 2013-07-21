#!/usr/bin/python

"""Test module other methods of Hand class."""

# Disable the following pylint warnings:
#  - long identifier names, these are deliberate for unittests
#  - too many public methods, supposed to be lots of tests here
#  - access to protected attributes, needed for tests
#
# pylint: disable=C0103
# pylint: disable=R0904
# pylint: disable=W0212


import unittest

from pcards import Deck, Hand, Card, NoAssociatedDeckError


class TestSequenceFunctions(unittest.TestCase):

    """Test sequence class for other methods of
    hand module.

    """

    def setUp(self):
        pass

    def test_exchange(self):

        """
        Test exchange() method

        """

        deck = Deck()
        h = Hand(deck, 5)
        self.assertEqual(len(h), 5)

        hil = h.index_list()
        h.exchange("24")
        self.assertEqual(hil[0], h[0].index())
        self.assertEqual(hil[2], h[2].index())
        self.assertEqual(hil[4], h[4].index())
        self.assertNotEqual(hil[1], h[1].index())
        self.assertNotEqual(hil[3], h[3].index())
        self.assertEqual(len(h), 5)

    def test_discard(self):

        """Test discard() method."""

        deck = Deck()
        h = Hand(deck, 5)
        self.assertEqual(len(h), 5)
        h.discard()
        self.assertEqual(len(h), 0)

    def test_discard_no_deck(self):

        """Test discard() method raises an exception with no
        associated deck.
        
        """

        h = Hand()
        self.assertRaises(NoAssociatedDeckError, h.discard)

    def test_getlist(self):

        """Test get_list() method."""

        namelist = ["AC", "5H", "7C", "QD"]
        h = Hand(namelist=namelist)
        idx_list = [Card(name=name).index() for name in namelist]

        h2 = h.get_list()
        hidx_list = [card.index() for card in h2]
        self.assertEqual(idx_list, hidx_list)
        self.assertFalse(h2 is h._cards)


if __name__ == "__main__":
    unittest.main()
