#!/usr/bin/env python3

"""Test module addition and multiplication methods of Hand class."""

# Disable the following pylint warnings:
#  - long identifier names, these are deliberate for unittests
#  - too many public methods, supposed to be lots of tests here
#  - access to protected class members, necessary for tests
#
# pylint: disable=C0103
# pylint: disable=R0904
# pylint: disable=W0212


import unittest

from pcards import Card, Hand


class TestSequenceFunctions(unittest.TestCase):

    """Test sequence class for addition and multiplication
    methods of hand module.

    """

    def setUp(self):
        self.hand1 = Hand(namelist=["AC", "2C", "3C"])
        self.hand2 = Hand(namelist=["4S", "5S", "6S"])
        self.hand3 = Hand(namelist=["AH", "2H"])
        self.hand4 = Hand(namelist=["3D", "4D"])

    def test_add_basic(self):

        """
        Test basic hand addition.

        """

        benchmark = Hand(namelist=["AC", "2C", "3C", "4S", "5S", "6S"])
        hand3 = self.hand1 + self.hand2
        self.assertEqual(benchmark.index_list(), hand3.index_list())

    def test_add_copy_made_left_hand_index(self):

        """Test copies are appropriately made during addition, so
        that the new hand does not change when the original left
        side hand changes. Use the hand index to make the change.

        """

        benchmark3 = Hand(namelist=["AC", "2C", "3C", "4S", "5S", "6S"])
        benchmark1 = Hand(namelist=["AH", "2C", "3C"])

        # Form hand3 by adding hand2 to hand1...

        hand3 = self.hand1 + self.hand2

        # ...change first element of hand1...

        self.hand1[0] = Card(name="AH")

        # ...check first element of hand1 really changed...

        self.assertEqual(benchmark1.index_list(), self.hand1.index_list())

        # ...and check hand3 did *not* change when hand1 did.

        self.assertEqual(benchmark3.index_list(), hand3.index_list())

    def test_add_copy_made_right_hand_index(self):

        """Test copies are appropriately made during addition, so
        that the new hand does not change when the original right
        side hand changes. The hand index makes the change.

        """

        benchmark3 = Hand(namelist=["AC", "2C", "3C", "4S", "5S", "6S"])
        benchmark2 = Hand(namelist=["AD", "5S", "6S"])

        # Form hand3 by adding hand2 to hand1...

        hand3 = self.hand1 + self.hand2

        # ...change first element of hand2...

        self.hand2[0] = Card(name="AD")

        # ...check first element of hand2 really changed...

        self.assertEqual(benchmark2.index_list(), self.hand2.index_list())

        # ...and check hand3 did *not* change when hand2 did.

        self.assertEqual(benchmark3.index_list(), hand3.index_list())

    def test_add_copy_made_left_list_change(self):

        """Test copies are appropriately made during addition, so
        that the new hand does not change when the original left
        side hand changes. Manually access the card list to make
        the change.

        The difference between this and the related 'match_index'
        tests is that the latter replaces a list member, and this
        changes it. If the *list* is copied, but the individual
        cards are not, the 'match_index' tests will pass, but the
        'list_change' tests will fail.

        """

        benchmark3 = Hand(namelist=["AC", "2C", "3C", "4S", "5S", "6S"])
        benchmark1 = Hand(namelist=["AH", "2C", "3C"])

        # Form hand3 by adding hand2 to hand1...

        hand3 = self.hand1 + self.hand2

        # ...change first element of hand1...

        self.hand1._cards[0]._rank = 14
        self.hand1._cards[0]._suit = 1
        self.hand1._cards[0]._index = 13

        # ...check first element of hand1 really changed...

        self.assertEqual(benchmark1.index_list(), self.hand1.index_list())

        # ...and check hand3 did *not* change when hand1 did.

        self.assertEqual(benchmark3.index_list(), hand3.index_list())

    def test_add_copy_made_right_list_change(self):

        """Test copies are appropriately made during addition, so
        that the new hand does not change when the original right
        side hand changes. Manually access the card list to make
        the change.

        The difference between this and the related 'match_index'
        tests is that the latter replaces a list member, and this
        changes it. If the *list* is copied, but the individual
        cards are not, the 'match_index' tests will pass, but the
        'list_change' tests will fail.

        """

        benchmark3 = Hand(namelist=["AC", "2C", "3C", "4S", "5S", "6S"])
        benchmark2 = Hand(namelist=["AD", "5S", "6S"])

        # Form hand3 by adding hand2 to hand1...

        hand3 = self.hand1 + self.hand2

        # ...change first element of hand2...

        self.hand2._cards[0]._rank = 1
        self.hand2._cards[0]._suit = 4
        self.hand2._cards[0]._index = 39

        # ...check first element of hand2 really changed...

        self.assertEqual(benchmark2.index_list(), self.hand2.index_list())

        # ...and check hand3 did *not* change when hand2 did.

        self.assertEqual(benchmark3.index_list(), hand3.index_list())

    def test_inplace_add_basic(self):

        """Test basic inplace addition."""

        benchmark1 = Hand(namelist=["AC", "2C", "3C", "4S", "5S", "6S"])
        card = self.hand1._cards[0]

        # Add hand2 to hand1 in place, and test hand1 ends up with
        # the right list members.

        self.hand1 += self.hand2
        self.assertEqual(self.hand1.index_list(), benchmark1.index_list())

        # Test the operation left hand1's original members intact.

        self.assertTrue(card is self.hand1._cards[0])

    def test_inplace_add_basic_copied_hand_index(self):

        """Test that changing the new list members following
        in-place addition does not alter the original hand's
        list. Use the hand index to make the change.

        """

        benchmark1 = Hand(namelist=["AC", "2C", "3C", "AD", "5S", "6S"])
        benchmark2 = Hand(namelist=["4S", "5S", "6S"])

        self.hand1 += self.hand2
        self.hand1[3] = Card(name="AD")

        # Check the change was made

        self.assertEqual(self.hand1.index_list(), benchmark1.index_list())

        # Check hand2 remains unchanged

        self.assertEqual(self.hand2.index_list(), benchmark2.index_list())

    def test_inplace_add_basic_copied_manual_change(self):

        """Test that changing the new list members following
        in-place addition does not alter the original hand's
        list. Use the hand index to make the change.

        """

        benchmark1 = Hand(namelist=["AC", "2C", "3C", "AD", "5S", "6S"])
        benchmark2 = Hand(namelist=["4S", "5S", "6S"])

        self.hand1 += self.hand2
        self.hand1._cards[3]._rank = 14
        self.hand1._cards[3]._suit = 3
        self.hand1._cards[3]._index = 39

        # Check the change was made

        self.assertEqual(self.hand1.index_list(), benchmark1.index_list())

        # Check hand2 remains unchanged.

        self.assertEqual(self.hand2.index_list(), benchmark2.index_list())

    def test_bad_add_assertion(self):

        """Test than a NotImplementedError is raised for invalid
        addition operands.

        """

        bad_opers = [3, 9.5, "spam", Card(name="AS")]

        for oper in bad_opers:
            self.assertRaises(NotImplementedError, self.hand1.__add__, oper)
            self.assertRaises(NotImplementedError, self.hand1.__radd__, oper)
            self.assertRaises(NotImplementedError, self.hand1.__iadd__, oper)

    def test_mult_basic(self):

        """Tests basic Hand repetition."""

        benchmark = Hand(namelist=["AH", "2H", "AH", "2H", "AH", "2H"])

        hl = self.hand3 * 3
        hr = 3 * self.hand3

        self.assertEqual(benchmark.index_list(), hl.index_list())
        self.assertEqual(benchmark.index_list(), hr.index_list())

    def test_mult_copies_made_hand_index(self):

        """Tests copies are properly made. Use hand_index change to
        make change.

        """

        benchmark3 = Hand(namelist=["AH", "2H"])
        benchmark2 = Hand(namelist=["6D", "2H", "AH", "2H", "AH", "2H"])

        hl = self.hand3 * 3
        hr = 3 * self.hand3

        hl[0] = Card(name="6D")
        hr[0] = Card(name="6D")

        # Ensure changed results match benchmark. This also ensures
        # that copies were made during the repetition (i.e. that
        # changing hl._cards[0], for instance, does not also change
        # hl._cards[2] and hl._cards[4]

        self.assertEqual(benchmark2.index_list(), hl.index_list())
        self.assertEqual(benchmark2.index_list(), hr.index_list())

        # Test hand3 was not altered.

        self.assertEqual(benchmark3.index_list(), self.hand3.index_list())

    def test_mult_copies_made_manual_change(self):

        """Tests copies are properly made. Use manual change to
        make change.

        """

        benchmark3 = Hand(namelist=["AH", "2H"])
        benchmark2 = Hand(namelist=["6D", "2H", "AH", "2H", "AH", "2H"])

        hl = self.hand3 * 3
        hr = 3 * self.hand3

        hl._cards[0]._rank = 6
        hl._cards[0]._suit = 3
        hl._cards[0]._index = 44
        hr._cards[0]._rank = 6
        hr._cards[0]._suit = 3
        hr._cards[0]._index = 44

        # Ensure changed results match benchmark. This also ensures
        # that copies were made during the repetition (i.e. that
        # changing hl._cards[0], for instance, does not also change
        # hl._cards[2] and hl._cards[4]

        self.assertEqual(benchmark2.index_list(), hl.index_list())
        self.assertEqual(benchmark2.index_list(), hr.index_list())

        # Test hand3 was not altered.

        self.assertEqual(benchmark3.index_list(), self.hand3.index_list())

    def test_inplace_mult_basic(self):

        """Test basic inplace multiplication."""

        benchmark4 = Hand(namelist=["3D", "4D", "3D", "4D", "3D", "4D"])
        card = self.hand4._cards[0]

        # Multiply hand4 by 3 in-place.

        self.hand4 *= 3
        self.assertEqual(self.hand4.index_list(), benchmark4.index_list())

        # Test the operation left hand4's original members intact.

        self.assertTrue(card is self.hand4._cards[0])

    def test_inplace_mult_copies_made_hand_index(self):

        """Test copies are made correctly during in-place
        multiplication. Make change using hand_index change.

        """

        benchmark = Hand(namelist=["AS", "4D", "3D", "4D", "3D", "4D"])

        # Multiply hand4 by 3 in-place.

        self.hand4 *= 3
        self.hand4[0] = Card(name="AS")

        self.assertEqual(self.hand4.index_list(), benchmark.index_list())

    def test_inplace_mult_copies_made_manual_change(self):

        """Test copies are made correctly during in-place
        multiplication. Make change using manual change.

        """

        benchmark = Hand(namelist=["AS", "4D", "3D", "4D", "3D", "4D"])

        # Multiply hand4 by 3 in-place.

        self.hand4 *= 3
        self.hand4._cards[0]._rank = 1
        self.hand4._cards[0]._suit = 2
        self.hand4._cards[0]._index = 26

        self.assertEqual(self.hand4.index_list(), benchmark.index_list())

    def test_bad_mult_assertion(self):

        """Test than a NotImplementedError is raised for invalid
        multiplication operands.

        """

        bad_opers = [9.5, "spam", Card(name="AS"),
                     self.hand3]

        for oper in bad_opers:
            self.assertRaises(NotImplementedError, self.hand4.__mul__, oper)
            self.assertRaises(NotImplementedError, self.hand4.__rmul__, oper)
            self.assertRaises(NotImplementedError, self.hand4.__imul__, oper)


if __name__ == "__main__":
    unittest.main()
