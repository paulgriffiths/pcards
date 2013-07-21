#!/usr/bin/python

"""
Test module for PokerHand object of cards module.
"""

# Disable the following pylint warnings:
#  - long identifier names, these are deliberate for unittests
#  - too many public methods, supposed to be lots of tests here
#  - too many instance attributes, this class will have lots
#
# pylint: disable=C0103
# pylint: disable=R0904
# pylint: disable=R0902


import unittest

from pcards import PokerHand


class TestSequenceFunctions(unittest.TestCase):

    """
    Test sequence class for poker hands.
    """

    def setUp(self):
        self.rf_1 = PokerHand(namelist=["AS", "KS", "QS", "JS", "10S"])
        self.rf_2 = PokerHand(namelist=["AC", "KC", "QC", "JC", "10C"])
        self.rf_false = PokerHand(namelist=["AC", "KC", "JC", "JC", "10C"])

        self.sf_ace_low = PokerHand(namelist=["AD", "2D", "3D", "4D", "5D"])
        self.sf_king_high = PokerHand(namelist=["9H", "KH", "QH", "JH", "10H"])
        self.sf_ten_high = PokerHand(namelist=["6D", "7D", "8D", "9D", "10D"])
        self.sf_false = PokerHand(namelist=["6D", "7D", "8D", "8D", "10D"])

        self.fk_king_ten = PokerHand(namelist=["KC", "KH", "KS", "KD", "10C"])
        self.fk_king_ace = PokerHand(namelist=["KC", "KH", "KS", "KD", "AC"])
        self.fk_nine_ten = PokerHand(namelist=["9C", "9H", "9S", "9D", "10C"])
        self.fk_nine_ace = PokerHand(namelist=["9C", "9H", "9S", "9D", "AC"])
        self.fk_nine_four = PokerHand(namelist=["9C", "9H", "9S", "9D", "4C"])
        self.fk_ace_ten = PokerHand(namelist=["AC", "AH", "AS", "AD", "10C"])

    def test_rf_evaluates(self):

        """
        Test a royal flush correctly evaluates
        """

        self.assertEqual(self.rf_1.show_value(short=True), "RF")

    def test_rf_false_not_evaluates(self):

        """
        Test a false royal flush does not evaluate to one, e.g.
        AC, KC, JC, JC, 10C.
        """

        self.assertNotEqual(self.rf_false.show_value(short=True), "RF")

    def test_rf_false_evaluates_flush(self):

        """
        Test a false royal flush evaluates to a flush, e.g.
        AC, KC, JC, JC, 10C.
        """

        self.assertEqual(self.rf_false.show_value(short=True), "FL")

    def test_sf_evaluates(self):

        """
        Test a straight flush correctly evaluates
        """

        self.assertEqual(self.sf_ace_low.show_value(short=True), "SF")

    def test_sf_false_not_evaluates(self):

        """
        Test a false straight flush does not evaluate to one, e.g.
        AC, 2C, 3C, 3C, 4C.
        """

        self.assertNotEqual(self.sf_false.show_value(short=True), "SF")

    def test_sf_false_evaluates_flush(self):

        """
        Test a false straight flush evaluates to a flush, e.g.
        AC, 2C, 3C, 3C, 4C.
        """

        self.assertEqual(self.sf_false.show_value(short=True), "FL")

    def test_rf_beats_sf(self):

        """
        Test a royal flush beats a self flush, tests > operator
        """

        self.assertTrue(self.rf_2 > self.sf_king_high)

    def test_sf_loses_to_rf(self):

        """
        Test a self flush loses to a royal flush, tests < operator
        """

        self.assertTrue(self.sf_ten_high < self.rf_1)

    def test_rf_le_rf(self):

        """
        Test a royal flush is <= another royal flush, i.e. that
        similar hands are <= each other.
        """

        self.assertTrue(self.rf_1 <= self.rf_2)

    def test_rf_ge_rf(self):

        """
        Test a royal flush is >= another royal flush, i.e. that
        similar hands are >= each other.
        """

        self.assertTrue(self.rf_1 >= self.rf_2)

    def test_sf_le_rf(self):

        """
        Test a straight flush is <= a royal flush, i.e. that dissimilar
        hands are <= each other with the lower hand on the left.
        """

        self.assertTrue(self.sf_king_high <= self.rf_2)

    def test_rf_ge_sf(self):

        """
        Test a royal flush is >= a straight flush, i.e. that dissimilar
        hands are >= each other with the lower hand on the right.
        """

        self.assertTrue(self.rf_1 >= self.sf_ace_low)

    def test_rf_eq_rf(self):

        """
        Test a royal flush is equal to another royal flush, i.e.
        tests the == operator.
        """

        self.assertTrue(self.rf_1 == self.rf_2)

    def test_rf_ne_sf(self):

        """
        Test a royal flush is not equal to a straight flush, i.e.
        tests the != operator.
        """

        self.assertTrue(self.rf_1 != self.sf_ten_high)

    def test_sfk_beats_sfa(self):

        """
        Test a straight flush with king high beats a straight
        flush ace low, i.e. ensure that the presence of the ace
        does not cause a bad comparison due to it being called
        a "high card".
        """

        self.assertTrue(self.sf_king_high > self.sf_ace_low)

    def test_sfk_beats_sft(self):

        """
        Test a straight flush with king high beats a straight
        flush ten high.
        """

        self.assertTrue(self.sf_king_high > self.sf_ten_high)

    def test_sf_beats_fk(self):

        """
        Test a straight flush beats a four of a kind
        """

        self.assertTrue(self.sf_king_high > self.fk_ace_ten)

    def test_fk_king_beats_fk_nine(self):

        """
        Test four kings beat four nines
        """

        self.assertTrue(self.fk_king_ten > self.fk_nine_ace)

    def test_fk_ace_beats_fk_king(self):

        """
        Test four aces beat four kings
        """

        self.assertTrue(self.fk_ace_ten > self.fk_king_ace)

    def test_fk_king_ace_beats_fk_king_ten(self):

        """
        Test four kings with an ace beats four kings with a ten
        """

        self.assertTrue(self.fk_king_ace > self.fk_king_ten)

    def test_fk_nine_ten_beats_fk_nine_four(self):

        """
        Test four nines with a ten beat four nines with a four
        """

        self.assertTrue(self.fk_nine_ten > self.fk_nine_four)

if __name__ == "__main__":
    unittest.main()
