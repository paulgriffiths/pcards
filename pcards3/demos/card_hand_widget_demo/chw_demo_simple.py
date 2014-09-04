#!/usr/bin/env python3

'''Simple demonstration of CardHandWidget.

Invoke with 'large' on the command line to get large card
images, which requires PIL and some of its dependencies to
be installed. Small card images (which just require tkinter)
are used by default.

Invoke with an integer argument on the command line to specify
the number of cards in the hand. For this demo, the default is 3,
the minimum is 1, and the maximum is 7.

Instructions:
1. Click the 'Deal' button to deal a hand of cards.
2. Left-click on a card to flip it face-down (or face-up again)
3. Click the 'Exchange' button to replace any face-down cards
4. Click the 'Deal' button again at any time to deal a new hand of cards.
5. Click the 'Clear' button to discard all the cards in the hand.
6. Click the 'Quit' button to exit.
'''


# Disable pylint message from inherited tkinter classes
# pylint: disable=too-many-public-methods


import sys
from tkinter import Tk, Frame, TOP, BOTTOM, SUNKEN
import pcards
from buttonbarwidget import ButtonBarWidget


class DemoWindow(Frame):

    '''Main demo window class.'''

    def __init__(self, parent, use_large_images=False, num_cards=3):

        '''Initialization method.'''

        Frame.__init__(self, parent)

        # Set playing cards and miscellaneous variables

        self._deck = pcards.Deck()
        self._hand = pcards.Hand(self._deck)
        self._num_cards = num_cards
        self._parent = parent

        # Create and pack card hand widget

        card_images = (pcards.CardImagesLarge if use_large_images
                       else pcards.CardImagesSmall)

        self._chw = pcards.CardHandWidget(self, card_images,
                                          numcards=self._num_cards,
                                          relief=SUNKEN, borderwidth=2)
        self._chw.pack(side=TOP, padx=5, pady=5)

        # Create and pack control buttons widget

        button_defs = [
            ("Deal", self._deal),
            ("Exchange", self._exchange),
            ("Clear", self._clear),
            ("Quit", self._quit)
            ]

        bbw = ButtonBarWidget(self, button_defs)
        bbw.pack(side=BOTTOM)

    def _clear(self, _):

        '''Clears the hands from the deck.'''

        self._hand.discard()

    def _deal(self, _):

        '''Deals a new hand of cards.'''

        self._hand.discard()
        self._deck.shuffle()
        self._hand.draw(self._num_cards, face_up=True)
        self._chw.deal(self._hand)

    def _exchange(self, _):

        '''Exchanges any face-down cards for new face-up cards.'''

        self._hand.exchange(face_up=True)

    def _quit(self, _):

        '''Quits the program.'''

        self._parent.quit()


def main():

    '''Main function.'''

    root_window = Tk()
    root_window.title("Card Hand Widget Demo")

    # Set default options

    use_large_images = False
    num_cards = 3

    # Override with specified options from command line, if any

    for arg in sys.argv:
        if arg.lower() == 'large':
            use_large_images = True
        else:
            try:
                num_arg = int(arg)
                if num_arg > 0 and num_arg < 8:
                    num_cards = num_arg
            except ValueError:
                pass

    # Create and pack widget, then run main Tk loop.

    demo_window = DemoWindow(root_window,
                             use_large_images=use_large_images,
                             num_cards=num_cards)
    demo_window.pack(side=TOP)

    root_window.mainloop()


if __name__ == '__main__':
    main()
