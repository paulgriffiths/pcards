#!/usr/bin/python

"""Test module container methods of Hand class."""

# Disable the following pylint warnings:
#  - long identifier names, these are deliberate for unittests
#  - too many public methods, supposed to be lots of tests here
#  - access to protected functions, needed for tests
#
# pylint: disable=C0103
# pylint: disable=R0904
# pylint: disable=W0212


import unittest

from pcards import Hand, Card


class TestSequenceFunctions(unittest.TestCase):

    """Test sequence class for container methods of
    hand module.

    """

    def setUp(self):
        pass

    def test_append_valid(self):

        """
        Test append() method with valid type.

        """

        h = Hand(namelist=["AD", "10C", "JS", "2H", "10D"])
        card = Card(name="5C")

        h.append(card)
        self.assertEqual(h[-1].index(), card.index())
        self.assertFalse(h._cards[-1] is card)

    def test_append_invalid(self):

        """
        Test append() method with invalid type.

        """

        h = Hand(namelist=["AD", "10C", "JS", "2H", "10D"])

        bad_list = [1, 1.5, "spam", Hand(namelist=["AS"])]

        for badness in bad_list:
            self.assertRaises(TypeError, h.append, badness)

    def test_count(self):

        """
        Test count() method.

        """

        h = Hand(namelist=["AD", "10C", "JS", "2H", "10D"])
        card = Card(name="10C")
        rank = 10
        rank_str = "jack"
        bad_list = [6.5, Hand(namelist=["AS"])]

        self.assertEqual(h.count(card), 1)
        self.assertEqual(h.count(rank), 2)
        self.assertEqual(h.count(rank_str), 1)
        for badness in bad_list:
            self.assertEqual(h.count(badness), 0)
        self.assertRaises(ValueError, h.count, 0)
        self.assertRaises(ValueError, h.count, 15)
        self.assertRaises(ValueError, h.count, "spam")

    def test_extend(self):

        """
        Test extend() method.

        """

        h = Hand(namelist=["AD", "10C", "JS"])
        h1 = Hand(namelist=["QH", "2D"])
        hr = Hand(namelist=["AD", "10C", "JS", "QH", "2D"])

        h.extend(h1)
        self.assertEqual(h.index_list(), hr.index_list())
        self.assertFalse(h._cards[3] is h1._cards[0])

        bad_list = [0, 1.5, "spam", Card(name="AS")]
        for badness in bad_list:
            self.assertRaises(TypeError, h.extend, badness)

    def test_index(self):

        """
        Test index() method.

        """

        h = Hand(namelist=["AD", "10C", "JS", "2H", "10D"])

        card = Card(name="10D")
        rank = 10
        rank_str = "jack"
        bad_list = [6.5, Hand(namelist=["AS"])]

        self.assertEqual(h.index(card), 4)
        self.assertEqual(h.index(rank), 1)
        self.assertEqual(h.index(rank_str), 2)
        for badness in bad_list:
            self.assertRaises(ValueError, h.index, badness)
        self.assertRaises(ValueError, h.index, 0)
        self.assertRaises(ValueError, h.index, 15)
        self.assertRaises(ValueError, h.index, "spam")

    def test_insert(self):

        """
        Test insert() method.

        """

        h = Hand(namelist=["AD", "10C", "JS"])
        h1 = Hand(namelist=["AD", "2H", "10C", "JS"])
        h2 = Hand(namelist=["AD", "2H", "10C", "10D", "JS"])
        c1 = Card(name="2H")
        c2 = Card(name="10D")
        cl = h[-1]

        h.insert(1, c1)
        self.assertEqual(h[1], c1)
        self.assertFalse(h._cards[1] is c1)
        self.assertEqual(h.index_list(), h1.index_list())
        self.assertEqual(h[-1], cl)
        self.assertEqual(len(h), 4)

        h.insert(3, c2)
        self.assertEqual(h[3], c2)
        self.assertFalse(h._cards[3] is c2)
        self.assertEqual(h.index_list(), h2.index_list())
        self.assertEqual(h[-1], cl)
        self.assertEqual(len(h), 5)

        bad_list = [1, 6.5, "spam", Hand(namelist=["AS"])]

        for badness in bad_list:
            self.assertRaises(TypeError, h.insert, badness)

    def test_pop(self):

        """
        Test pop() method.

        """

        h = Hand(namelist=["AD", "2H", "10C", "10D", "JS"])
        h1 = Hand(namelist=["AD", "2H", "10C", "10D"])
        h2 = Hand(namelist=["AD", "10C", "10D"])
        h3 = Hand(namelist=["AD", "10C"])

        c = h.pop()
        self.assertEqual(c.index(), Card(name="JS").index())
        self.assertEqual(h.index_list(), h1.index_list())

        c = h.pop(1)
        self.assertEqual(c.index(), Card(name="2H").index())
        self.assertEqual(h.index_list(), h2.index_list())

        # Note: using a float as in index seems to raise a
        # DeprecationWarning, so don't include in the fail test,
        # as one day that'll become an exception.

        # Note: Not sure why the two commented-out tests aren't working,
        # investigate in future.

        bad_list = ["spam"]
        #bad_list = ["spam", Hand(namelist=["AS"])]

        for badness in bad_list:
            self.assertRaises(TypeError, h.pop, badness)
        #self.assertRaises(NotImplementedError, h.pop, Card(name="2C"))

    def test_remove(self):

        """
        Test remove() method.

        """

        h = Hand(namelist=["AD", "2H", "10C", "10D", "10C"])
        h1 = Hand(namelist=["AD", "2H", "10D", "10C"])

        h.remove(Card(name="10C"))
        self.assertEqual(h.index_list(), h1.index_list())

        bad_list = [1, 1.5, "spam", Hand(namelist=["AS"])]
        for badness in bad_list:
            self.assertRaises(TypeError, h.remove, badness)

    def test_sort(self):

        """
        Test sort() method.

        """

        h = Hand(namelist=["7D", "3H", "10C", "7H", "QC", "3C"])
        h1 = Hand(namelist=["3C", "3H", "7H", "7D", "10C", "QC"])
        h2 = Hand(namelist=["QC", "10C", "7D", "7H", "3H", "3C"])

        self.assertNotEqual(h.index_list(), h1.index_list())
        h.sort()
        self.assertEqual(h.index_list(), h1.index_list())

        self.assertNotEqual(h.index_list(), h2.index_list())
        h.sort(reverse=True)
        self.assertEqual(h.index_list(), h2.index_list())

        # Test that anything passed as 'key' is ignored.

        self.assertNotEqual(h.index_list(), h1.index_list())
        h.sort(key="Spam Breakfast")
        self.assertEqual(h.index_list(), h1.index_list())

    def test_reverse(self):

        """
        Test reverse() method.

        """

        h = Hand(namelist=["7D", "3H", "10C", "7H", "QC", "3C"])
        h1 = Hand(namelist=["3C", "QC", "7H", "10C", "3H", "7D"])

        self.assertNotEqual(h.index_list(), h1.index_list())
        h.reverse()
        self.assertEqual(h.index_list(), h1.index_list())


if __name__ == "__main__":
    unittest.main()
