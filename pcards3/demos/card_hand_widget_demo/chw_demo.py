#!/usr/bin/env python3

'''Simple demonstration of CardHandWidget.

Invoke with 'large' on the command line to get large card
images, which requires PIL and some of its dependencies to
be installed. Small card images (which just require tkinter)
are used by default.

Instructions:
1. Click the 'Deal' button to deal a hand of cards.
2. Left-click on a card to flip it face-down (or face-up again)
3. Click the 'Exchange' button to replace any face-down cards
4. Click the 'Deal' button again at any time to deal a new hand of cards.
5. Click the 'Quit' button to exit.
'''


# Disable pylint message from inherited tkinter classes
# pylint: disable=too-many-public-methods


import sys
from tkinter import Tk, Frame, TOP, BOTTOM, SUNKEN
import pcards
from buttonbarwidget import ButtonBarWidget


class DemoWindow(Frame):

    '''Main demo window class.'''

    def __init__(self, parent, use_large_images=False):

        '''Initialization method.'''

        Frame.__init__(self, parent)

        # Set playing cards variables

        self._deck = pcards.Deck()
        self._hand = pcards.Hand(self._deck)
        self._num_cards = 3

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
            ("Quit", parent.quit)
            ]

        bbw = ButtonBarWidget(self, button_defs)
        bbw.pack(side=BOTTOM)

    def _exchange(self):

        '''Exchanges any face-down cards.'''

        self._hand.exchange(face_up=True)

    def _deal(self):

        '''Deals a new hand of cards.'''

        self._hand.discard()
        self._deck.shuffle()
        self._hand.draw(self._num_cards, face_up=True)
        self._chw.deal(self._hand)


def main():

    '''Main function.'''

    root_window = Tk()
    root_window.title("Card Hand Widget Demo")

    if len(sys.argv) > 1 and sys.argv[1].lower() == 'large':
        use_large_images = True
    else:
        use_large_images = False

    demo_window = DemoWindow(root_window, large=use_large_images)
    demo_window.pack(side=TOP)

    root_window.mainloop()


if __name__ == '__main__':
    main()
