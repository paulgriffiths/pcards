"""Poker hand widget."""

# Disable pylint message from inherited tkinter classes
# pylint: disable=too-many-public-methods

from tkinter import Label, Frame, TOP, LEFT, SUNKEN
import pcards

class CardPlace(Label):

    '''Card place class.'''

    def __init__(self, parent, hand, cardImages, card=None):

        '''Initializes a card place.'''

        Label.__init__(self, parent)
        self.bind('<Button-1>', self.flip)
        self.hand = hand
        self.cardImages = cardImages
        self.flippable = True

        self.place(card)

    def set_image(self):
        if self.card:
            if self.card.is_face_down():
                newImage = self.cardImages.back()
            else:
                newImage = self.cardImages.card(self.card.index() + 1)
        else:
            newImage = self.cardImages.empty()
        self.configure(image=newImage)

    def is_empty(self):
        return not self.card

    def clear(self):
        oldCard = self.card
        self.place(None)
        return oldCard

    def enable_flip(self, enabled=True):
        self.flippable = enabled

    def flip(self, dummy):

        '''Flips a card if there is currently a card in this place.'''

        if self.flippable and self.card:
            self.card.flip()
            self.set_image()

    def place(self, card=None):
        self.card = card
        self.set_image()

class CardHandWidget(Frame):

    '''Hand place class.'''

    def __init__(self, parent, cardImages, numcards=5, *args, **kwargs):

        '''Initializes a hand place.'''

        Frame.__init__(self, parent, *args, **kwargs)
        self.cards = []
        self.hand = None

        for cardnum in range(numcards):
            newcard = CardPlace(self, self, cardImages)
            newcard.pack(side=LEFT, padx=10, pady=10)
            self.cards.append(newcard)

    def clear(self):

        '''Clears the cards from their places.'''

        for card in self.cards:
            card.clear()
        self.hand.unobserve(self)
        self.hand = None

    def deal(self, hand, animated=False):

        '''Deals a hand of cards into the widget.'''

        self.hand = hand
        self.hand.observe(self, self.refresh)

        for index, card in enumerate(self.hand):
            self.cards[index].place(card)

    def enable_flip(self, enabled=True):

        '''Enables or disables flipping of cards.'''

        for place in self.cards:
            place.enable_flip(enabled)

    def refresh(self):

        '''Refreshes the widget (e.g. after the cards in the hand
        might have changed).
        
        '''

        for index, card in enumerate(self.hand):
            self.cards[index].place(card)

        if len(self.cards) > len(self.hand):
            for place in self.cards[len(self.hand):]:
                place.place(None)

    def show_hand(self):
        
        '''Returns a string representation of the hand.'''

        if self.hand:
            hand_text = ""
            for card in self.hand:
                if card.is_face_down():
                    hand_text += "[{0}] ".format(card.name_string(short=True))
                else:
                    hand_text += "{0} ".format(card.name_string(short=True))

            return hand_text
        else:
            return "<Empty>"
