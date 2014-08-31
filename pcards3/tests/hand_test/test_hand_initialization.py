#!/usr/bin/python

"""Test module initialization method of Hand class."""

# Disable the following pylint warnings:
#  - long identifier names, these are deliberate for unittests
#  - too many public methods, supposed to be lots of tests here
#  - access to protected attributes, needed for tests
#
# pylint: disable=C0103
# pylint: disable=R0904
# pylint: disable=W0212


import unittest

from ...card import Card
from ...deck import Deck, EmptyDeckError
from ...hand import Hand, NoAssociatedDeckError


class TestSequenceFunctions(unittest.TestCase):

    """Test sequence class for addition and multiplication
    methods of hand module.

    """

    def setUp(self):
        self.deck = Deck()

    def test_deck_nocards(self):

        """
        Test deck initialization with no cards.

        """

        h = Hand(self.deck)
        self.assertEqual(len(h), 0)
        self.assertEqual(len(self.deck), 52)

    def test_deck_cards(self):

        """
        Test deck initialization with cards.

        """

        benchmark = Hand(namelist=["AC", "2C", "3C", "4C", "5C", "6C", "7C"])
        test_card = self.deck._cards[-1]
        h = Hand(self.deck, 7)

        # Check length of hand is consistent with expectations

        self.assertEqual(len(h), 7)

        # Check cards have been popped off the deck in order

        self.assertEqual(h.index_list(), benchmark.index_list())

        # Check first card is the same instance as was at
        # the top of the deck

        self.assertTrue(h._cards[0] is test_card)

        # Check length of deck is consistent with expectations

        self.assertEqual(len(self.deck), 45)

    def test_namelist(self):

        """
        Test deck initialization with namelist.

        """

        pairs = [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0)]
        idx_list = [Card(rank, suit).index() for rank, suit in pairs]
        h = Hand(namelist=["AC", "2C", "3C", "4C", "5C"])

        self.assertEqual(h.index_list(), idx_list)

    def test_cardlist_copy(self):

        """
        Test deck initialization with cardlist and default copying.

        """

        pairs = [(1, 0), (2, 1), (3, 2), (4, 3), (5, 0)]
        card_list = [Card(rank, suit) for rank, suit in pairs]
        idx_list = [card.index() for card in card_list]
        h = Hand(cardlist=card_list)

        # Test cards are correct

        self.assertEqual(h.index_list(), idx_list)

        # Test both lists are not the same

        self.assertFalse(h._cards is card_list)

    def test_cardlist_nocopy(self):

        """
        Test deck initialization with cardlist and no copying.

        """

        pairs = [(1, 0), (2, 1), (3, 2), (4, 3), (5, 0)]
        card_list = [Card(rank, suit) for rank, suit in pairs]
        idx_list = [card.index() for card in card_list]
        h = Hand(cardlist=card_list, nocopy=True)

        # Test cards are correct

        self.assertEqual(h.index_list(), idx_list)

        # Test both lists are the same

        self.assertTrue(h._cards is card_list)

    def test_copy_function(self):

        """
        Test copy function returns a legitimate copy.

        """

        pairs = [(1, 0), (2, 1), (3, 2), (4, 3), (5, 0)]
        card_list = [Card(rank, suit) for rank, suit in pairs]
        idx_list = [card.index() for card in card_list]

        h = Hand(cardlist=card_list)
        h2 = h.copy()

        self.assertFalse(h is h2)
        self.assertFalse(h._cards is h2._cards)

        self.assertEqual(h.index_list(), idx_list)
        self.assertEqual(h2.index_list(), idx_list)

    def test_draw_nodeck(self):

        """
        Test exception is raised when drawing with no deck.

        """

        h = Hand()
        self.assertRaises(NoAssociatedDeckError, h.draw, 5)

    def test_overdraw(self):

        """
        Test exception is raised when overdrawing.

        """

        h = Hand(self.deck, 52)
        self.assertRaises(EmptyDeckError, h.draw, 1)


if __name__ == "__main__":
    unittest.main()
