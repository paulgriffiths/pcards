#!/usr/bin/python

"""Unit test module for Card class conversion operators."""

# Disable the following pylint warnings:
#  - long identifier names, these are deliberate for unittests
#  - too many public methods, supposed to be lots of tests here
#
# pylint: disable=C0103
# pylint: disable=R0904


import unittest

from ...card import Card


class TestSequenceFunctions(unittest.TestCase):

    """Unit test class for Card class conversion operators."""

    def setUp(self):
        pass

    def test_eq_true_same_card(self):

        """Test that identical cards are considered equal to
        each other.

        """

        self.assertTrue(Card(8, 2) == Card(8, 2))

    def test_eq_true_same_rank(self):

        """Test that cards of the same rank are considered equal to
        each other.

        """

        self.assertTrue(Card(8, 2) == Card(8, 3))

    def test_eq_false_diff_card(self):

        """Test that cards of different rank are not considered equal to
        each other.

        """

        self.assertFalse(Card(8, 2) == Card(5, 1))

    def test_ne_false_same_card(self):

        """Test that identical cards are not considered not equal to
        each other.

        """

        self.assertFalse(Card(8, 2) != Card(8, 2))

    def test_ne_false_same_rank(self):

        """Test that cards of the same rank are not considered not equal to
        each other.

        """

        self.assertFalse(Card(8, 2) != Card(8, 3))

    def test_ne_true_diff_card(self):

        """Test that cards of different rank are considered not equal to
        each other.

        """

        self.assertTrue(Card(8, 2) != Card(5, 1))

    def test_gt_true_diff_card(self):

        """Test greater than operator tests true for different ranks.

        """

        self.assertTrue(Card(8, 2) > Card(5, 1))

    def test_gt_false_diff_card(self):

        """Test greater than operator tests false for different ranks.

        """

        self.assertFalse(Card(5, 1) > Card(8, 2))

    def test_gt_false_same_rank(self):

        """Test greater than operator tests false for same ranks.

        """

        self.assertFalse(Card(8, 2) > Card(8, 1))

    def test_lt_true_diff_card(self):

        """Test less than operator returns true for different ranks.

        """

        self.assertTrue(Card(5, 1) < Card(8, 2))

    def test_lt_false_diff_card(self):

        """Test less than operator returns false for different ranks.

        """

        self.assertFalse(Card(8, 2) < Card(5, 1))

    def test_lt_false_same_rank(self):

        """Test less than operator returns false for same ranks.

        """

        self.assertFalse(Card(8, 1) < Card(8, 2))

    def test_ge_true_same_rank(self):

        """Test greater than or equal to operator returns true for same ranks.

        """

        self.assertTrue(Card(8, 1) >= Card(8, 2))

    def test_ge_true_diff_rank(self):

        """Test greater than or equal to operator returns true for same ranks.

        """

        self.assertTrue(Card(8, 1) >= Card(5, 0))

    def test_ge_false_diff_rank(self):

        """Test greater than or equal to operator returns false for
        different ranks.

        """

        self.assertFalse(Card(5, 1) >= Card(8, 2))

    def test_le_true_same_rank(self):

        """Test less than or equal to operator returns true for same ranks.

        """

        self.assertTrue(Card(8, 1) <= Card(8, 2))

    def test_le_true_diff_rank(self):

        """Test less than or equal to operator returns true for same ranks.

        """

        self.assertTrue(Card(5, 1) <= Card(8, 0))

    def test_le_false_diff_rank(self):

        """Test less than or equal to operator returns false for
        different ranks.

        """

        self.assertFalse(Card(8, 1) <= Card(5, 2))


if __name__ == "__main__":
    unittest.main()
