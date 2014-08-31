#!/usr/bin/python

"""Test module comparison methods of Hand class."""

# Disable the following pylint warnings:
#  - long identifier names, these are deliberate for unittests
#  - too many public methods, supposed to be lots of tests here
#  - access to protected class members, needed for tests
#
# pylint: disable=C0103
# pylint: disable=R0904
# pylint: disable=W0212


import unittest

from ...card import Card
from ...hand import Hand


class TestSequenceFunctions(unittest.TestCase):

    """Test sequence class for comparison methods of
    hand module.

    """

    def setUp(self):
        self.h1 = Hand(namelist=["AD", "TC", "JS", "2H", "TD"])
        self.h2 = Hand(namelist=["3D", "6S", "QD", "4D", "9H"])

    def test_eq(self):

        """
        Test equality operator.

        """

        self.assertTrue(self.h1 == self.h2)

        bad_comps = [1, 2.5, "spam", Card(name="AS")]
        for comp in bad_comps:
            self.assertRaises(NotImplementedError, self.h1.__eq__, comp)

    def test_ne(self):

        """
        Test non-equality operator.

        """

        self.assertFalse(self.h1 != self.h2)

        bad_comps = [1, 2.5, "spam", Card(name="AS")]
        for comp in bad_comps:
            self.assertRaises(NotImplementedError, self.h1.__ne__, comp)

    def test_lt(self):

        """
        Test less-than operator.

        """

        self.assertFalse(self.h1 < self.h2)

        bad_comps = [1, 2.5, "spam", Card(name="AS")]
        for comp in bad_comps:
            self.assertRaises(NotImplementedError, self.h1.__lt__, comp)

    def test_gt(self):

        """
        Test greater-than operator.

        """

        self.assertFalse(self.h1 > self.h2)

        bad_comps = [1, 2.5, "spam", Card(name="AS")]
        for comp in bad_comps:
            self.assertRaises(NotImplementedError, self.h1.__gt__, comp)

    def test_ge(self):

        """
        Test greater-than-or-equal-to operator.

        """

        self.assertTrue(self.h1 >= self.h2)

        bad_comps = [1, 2.5, "spam", Card(name="AS")]
        for comp in bad_comps:
            self.assertRaises(NotImplementedError, self.h1.__ge__, comp)

    def test_le(self):

        """
        Test less-than-or-equal-to operator.

        """

        self.assertTrue(self.h1 <= self.h2)

        bad_comps = [1, 2.5, "spam", Card(name="AS")]
        for comp in bad_comps:
            self.assertRaises(NotImplementedError, self.h1.__le__, comp)


if __name__ == "__main__":
    unittest.main()
