#!/usr/bin/python

"""Test module index methods of Hand class."""

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
from ...hand import Hand


class TestSequenceFunctions(unittest.TestCase):

    """Test sequence class for index methods of
    hand module.

    """

    def setUp(self):
        pass

    def test_getitem_positive_single(self):

        """
        Test __getitem__ with positive indices and no slicing.

        """

        card1 = Card(name="AD")
        card2 = Card(name="JS")
        card3 = Card(name="TD")

        namelist = ["AD", "TC", "JS", "2H", "TD"]
        h = Hand(namelist=namelist)

        self.assertEqual(h[0].index(), card1.index())
        self.assertTrue(h[0] is h._cards[0])

        self.assertEqual(h[2].index(), card2.index())
        self.assertTrue(h[2] is h._cards[2])

        self.assertEqual(h[4].index(), card3.index())
        self.assertTrue(h[4] is h._cards[4])

    def test_getitem_negative_single(self):

        """
        Test __getitem__ with negative indices and no slicing.

        """

        card1 = Card(name="TD")
        card2 = Card(name="2H")
        card3 = Card(name="TC")

        namelist = ["AD", "TC", "JS", "2H", "TD"]
        h = Hand(namelist=namelist)

        self.assertEqual(h[-1].index(), card1.index())
        self.assertTrue(h[-1] is h._cards[-1])

        self.assertEqual(h[-2].index(), card2.index())
        self.assertTrue(h[-2] is h._cards[-2])

        self.assertEqual(h[-4].index(), card3.index())
        self.assertTrue(h[-4] is h._cards[-4])

    def test_getitem_positive_slicing(self):

        """
        Test __getitem__ with positive indices and slicing.

        """

        namelist = ["AD", "TC", "JS", "2H", "TD"]
        h = Hand(namelist=namelist)

        handc1 = Hand(namelist=["AD", "TC", "JS"])
        handc2 = Hand(namelist=["TC", "JS"])
        handc3 = Hand(namelist=["JS", "2H", "TD"])

        handt1 = h[:3]
        handt2 = h[1:3]
        handt3 = h[2:]

        self.assertEqual(handt1.index_list(), handc1.index_list())
        self.assertTrue(handt1._cards[0] is h._cards[0])

        self.assertEqual(handt2.index_list(), handc2.index_list())
        self.assertFalse(handt2._cards[1] is h._cards[1])

        self.assertEqual(handt3.index_list(), handc3.index_list())
        self.assertFalse(handt3._cards[2] is h._cards[2])

    def test_getitem_negative_slicing(self):

        """
        Test __getitem__ with negative indices and slicing.

        """

        namelist = ["AD", "TC", "JS", "2H", "TD"]
        h = Hand(namelist=namelist)

        handc1 = Hand(namelist=["AD", "TC", "JS"])
        handc2 = Hand(namelist=["TC", "JS"])
        handc3 = Hand(namelist=["JS", "2H", "TD"])

        handt1 = h[:-2]
        handt2 = h[-4:-2]
        handt3 = h[-3:]

        self.assertEqual(handt1.index_list(), handc1.index_list())
        self.assertTrue(handt1._cards[0] is h._cards[0])

        self.assertEqual(handt2.index_list(), handc2.index_list())
        self.assertFalse(handt2._cards[1] is h._cards[1])

        self.assertEqual(handt3.index_list(), handc3.index_list())
        self.assertFalse(handt3._cards[2] is h._cards[2])

    def test_setitem_positive_single(self):

        """
        Test __setitem__ with positive indices and no slicing.

        """

        card1 = Card(name="JC")
        card2 = Card(name="8H")
        card3 = Card(name="QS")

        h = Hand(namelist=["AD", "TC", "JS", "2H", "TD"])
        h1 = Hand(namelist=["JC", "TC", "JS", "2H", "TD"])
        h2 = Hand(namelist=["JC", "TC", "8H", "2H", "TD"])
        h3 = Hand(namelist=["JC", "TC", "8H", "2H", "QS"])

        h[0] = card1
        self.assertEqual(h.index_list(), h1.index_list())
        self.assertFalse(card1 is h._cards[0])

        h[2] = card2
        self.assertEqual(h.index_list(), h2.index_list())
        self.assertFalse(card2 is h._cards[2])

        h[4] = card3
        self.assertEqual(h.index_list(), h3.index_list())
        self.assertFalse(card3 is h._cards[4])

    def test_setitem_negative_single(self):

        """
        Test __setitem__ with negative indices and no slicing.

        """

        card1 = Card(name="JC")
        card2 = Card(name="8H")
        card3 = Card(name="QS")

        h = Hand(namelist=["AD", "TC", "JS", "2H", "TD"])
        h1 = Hand(namelist=["JC", "TC", "JS", "2H", "TD"])
        h2 = Hand(namelist=["JC", "TC", "8H", "2H", "TD"])
        h3 = Hand(namelist=["JC", "TC", "8H", "2H", "QS"])

        h[-5] = card1
        self.assertEqual(h.index_list(), h1.index_list())
        self.assertFalse(card1 is h._cards[0])

        h[-3] = card2
        self.assertEqual(h.index_list(), h2.index_list())
        self.assertFalse(card2 is h._cards[2])

        h[-1] = card3
        self.assertEqual(h.index_list(), h3.index_list())
        self.assertFalse(card3 is h._cards[4])

    def test_setitem_positive_slicing(self):

        """
        Test __setitem__ with positive indices and slicing.

        """

        hc1 = Hand(namelist=["3C", "2H"])
        hc2 = Hand(namelist=["AC", "KS", "9D"])
        hc3 = Hand(namelist=["6H"])

        h = Hand(namelist=["JC", "TC", "JS", "2H", "TD"])
        h1 = Hand(namelist=["JC", "TC", "3C", "2H", "2H", "TD"])
        h2 = Hand(namelist=["JC", "AC", "3C", "KS", "2H", "9D"])
        h3 = Hand(namelist=["6H", "AC", "3C", "KS", "2H", "9D"])

        h[2:3] = hc1
        self.assertEqual(h.index_list(), h1.index_list())
        self.assertTrue(h._cards[2] is hc1._cards[0])

        h[1:6:2] = hc2
        self.assertEqual(h.index_list(), h2.index_list())
        self.assertTrue(h._cards[1] is hc2._cards[0])

        h[:1] = hc3
        self.assertEqual(h.index_list(), h3.index_list())
        self.assertTrue(h._cards[0] is hc3._cards[0])

    def test_setitem_negative_slicing(self):

        """
        Test __setitem__ with negative indices and slicing.

        """

        hc1 = Hand(namelist=["3C", "2H"])
        hc2 = Hand(namelist=["AC", "KS", "9D"])
        hc3 = Hand(namelist=["6H"])

        h = Hand(namelist=["JC", "TC", "JS", "2H", "TD"])
        h1 = Hand(namelist=["JC", "TC", "3C", "2H", "2H", "TD"])
        h2 = Hand(namelist=["JC", "9D", "3C", "KS", "2H", "AC"])
        h3 = Hand(namelist=["6H", "9D", "3C", "KS", "2H", "AC"])

        h[-3:-2] = hc1
        self.assertEqual(h.index_list(), h1.index_list())
        self.assertTrue(h._cards[2] is hc1._cards[0])

        h[-1:-6:-2] = hc2
        self.assertEqual(h.index_list(), h2.index_list())
        self.assertFalse(h._cards[1] is hc2._cards[0])

        h[:-5] = hc3
        self.assertEqual(h.index_list(), h3.index_list())
        self.assertTrue(h._cards[0] is hc3._cards[0])

    def test_delitem_positive(self):

        """
        Test __delitem__ with negative indices.

        """

        h = Hand(namelist=["JC", "TC", "JS", "2H", "TD", "7H", "6S"])
        h1 = Hand(namelist=["TC", "JS", "2H", "TD", "7H", "6S"])
        h2 = Hand(namelist=["JS", "TD", "6S"])
        h3 = Hand(namelist=["JS", "TD"])

        del(h[0])
        self.assertEqual(h.index_list(), h1.index_list())

        del(h[:5:2])
        self.assertEqual(h.index_list(), h2.index_list())

        del(h[2])
        self.assertEqual(h.index_list(), h3.index_list())

    def test_delitem_negative(self):

        """
        Test __delitem__ with negative indices.

        """

        h = Hand(namelist=["JC", "TC", "JS", "2H", "TD", "7H", "6S"])
        h1 = Hand(namelist=["TC", "JS", "2H", "TD", "7H", "6S"])
        h2 = Hand(namelist=["JS", "TD", "6S"])
        h3 = Hand(namelist=["JS", "TD"])

        del(h[-7])
        self.assertEqual(h.index_list(), h1.index_list())

        del(h[-2:-7:-2])
        self.assertEqual(h.index_list(), h2.index_list())

        del(h[-1])
        self.assertEqual(h.index_list(), h3.index_list())

    def test_iter(self):

        """
        Test __iter__.

        """

        h = Hand(namelist=["TC", "JS", "2H", "TD", "7H", "6S"])

        idx_list = [card.index() for card in h]
        self.assertEqual(idx_list, h.index_list())

    def test_contains(self):

        """
        Test __contains__.

        """

        namelist_in = ["TC", "JS", "2H", "TD", "7H", "6S"]
        namelist_out = ["TS", "JC", "2S", "TH", "7D", "6D"]

        h = Hand(namelist=namelist_in)

        for card in [Card(name=name) for name in namelist_in]:
            self.assertTrue(card in h)

        for card in [Card(name=name) for name in namelist_out]:
            self.assertFalse(card in h)


if __name__ == "__main__":
    unittest.main()
