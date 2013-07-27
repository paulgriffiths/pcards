#!/usr/bin/python

"""Test module string conversion method of Hand class."""

# Disable the following pylint warnings:
#  - long identifier names, these are deliberate for unittests
#  - too many public methods, supposed to be lots of tests here
#  - access to protected attributes, needed for tests.
#
# pylint: disable=C0103
# pylint: disable=R0904
# pylint: disable=W0212


import unittest

from ...hand import Hand


class TestSequenceFunctions(unittest.TestCase):

    """Test sequence class for string conversion method of
    hand module.

    """

    def setUp(self):
        pass

    def test_string_converstion(self):

        """
        Test string conversion.

        """

        h = Hand(namelist=["AD", "10C", "JS", "2H", "10D"])
        outstr = "  AD 10C  JS  2H 10D"
        self.assertEqual(str(h), outstr)


if __name__ == "__main__":
    unittest.main()
