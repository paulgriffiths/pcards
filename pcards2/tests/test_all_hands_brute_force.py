#!/usr/bin/python

"""Test to calculate every possible 5-card poker hand using a single
standard deck with no wildcards, and to ensure that the PokerHand
functionality from the cards2 module calculates the correct number
of different hands when run over the entire population.

"""


import timeit

from ..deck import Deck
from ..pokerhand import PokerHand


def main():

    """
    main() function.
    """

    hand_types = ["RF", "SF", "FK", "FH", "FL",
                  "ST", "TK", "TP", "PR", "HI"]
    types_found = {"RF": 0, "SF": 0, "FK": 0, "FH": 0,
                   "FL": 0, "ST": 0, "TK": 0, "TP": 0,
                   "PR": 0, "HI": 0}
    expected = {"RF": 4, "SF": 36, "FK": 624, "FH": 3744,
                "FL": 5108, "ST": 10200, "TK": 54912, "TP": 123552,
                "PR": 1098240, "HI": 1302540}
    total_expected = 2598960
    total_hands = 0
    percent = 0

    deck = Deck()
    cards = deck.draw(52)

    deck = Deck()
    hand = PokerHand(deck)

    # Loop through all hands and store number of hand types

    for a in range(48):
        for b in range(a + 1, 52):
            for c in range(b + 1, 52):
                for d in range(c + 1, 52):
                    for e in range(d + 1, 52):
                        cds = [cards[a], cards[b], cards[c],
                               cards[d], cards[e]]
                        hand._cards = cds
                        hand.evaluate()
                        types_found[hand.show_value(short=True)] += 1
                        total_hands += 1

                        # Print status indicator

                        if total_hands % 25990 == 0:
                            percent += 1
                            print "{0}%.....".format(percent)

    # Output results

    sumscores = 0
    failed = False
    for hand_type in hand_types:
        if expected[hand_type] == types_found[hand_type]:
            result = "passed"
        else:
            result = "failed"
            failed = True
        print "{0}: {1} expected, {2} found...{3}.".format(
            hand_type, expected[hand_type], types_found[hand_type], result)
        sumscores += types_found[hand_type]

    if total_expected == sumscores:
        result = "passed"
    else:
        result = "failed"
        failed = True
    print "Total hands: {0} expected, {1} found...{2}".format(
        total_expected, sumscores, result)

    if not failed:
        print("All tests passed.")
    else:
        print("SOME TESTS FAILED!")


if __name__ == "__main__":
    print "Time taken: {0:.2} seconds.".format(timeit.timeit("main()",
                            setup="from __main__ import main", number=1))
