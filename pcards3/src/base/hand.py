"""Generic hand module.

Library Release 1.2

Copyright 2013 Paul Griffiths
Email: mail@paulgriffiths.net

Distributed under the terms of the GNU General Public License.
http://www.gnu.org/licenses/

"""


from collections import defaultdict

from .card import Card, get_rank_integer


# Exceptions

class NoAssociatedDeckError(Exception):

    """Exception for when an instance method requiring
    an associated deck is called, but no deck is
    associated.

    """

    pass


# Class

class Hand(object):

    """Implements a generic card hand class.

    Implemented as a full sequence container class.

    Public methods:
    __init__(deck, numcards, namelist, cardlist, nocopy)
    copy()
    discard()
    draw(numcards)
    exchange(chg)
    get_list()
    index_list()

    Comparison operators:
    All are overloaded, comparison evaluation follows normal
    rules for comparing poker hands.

    Indexing and iteration operators:
    All are overloaded (__getitem__, __setitem__, __delitem__,
    __iter__, __contains__, __len__) and slicing is supported.

    Sequence concatenation and multiplication methods:
    All are overloaded (__add__, __radd__, __iadd__, __mul__,
    __rmul__, __imul__)

    Sequence container methods:
    append(value)
    count(value)
    extend(hand)
    index(value)
    insert(idx, value)
    pop(idx)
    remove(value)
    sort(reverse)
    reverse()

    Conversion operators:
    Only __str__ is overloaded, returning a string showing the
    short values (e.g. "4H") of all five cards.
    """

    def __init__(self, deck=None, numcards=0,
                 namelist=None, cardlist=None, nocopy=False):

        """Initializes a Hand instance.

        Arguments:
        deck -- the Deck instance to draw the cards from
        numcards -- an optional number of cards to draw immediately
        from the deck, if a deck is provided
        namelist -- a list of short names (e.g. "AS", "10C", "7H") to
        populate the hand
        cardlist -- a list of Card instances to populate the hand
        nocopy -- set to True to add the provided cardlist list as the
        internal list of cards, rather than a copy of it which is the
        default behavior.

        """

        self._score = []
        self._cards = []
        self._deck = deck
        self._observers = []

        if numcards and deck and not namelist:
            self.draw(numcards)
            self._cards_changed()
        elif namelist:
            for name in namelist:
                self._cards.append(Card(name=name))
                self._cards_changed()
        elif cardlist:
            if nocopy:
                self._cards = cardlist
            else:
                for card in cardlist:
                    self._cards.append(card.copy())
                    self._cards_changed()

    # Public methods

    def copy(self):

        """Returns a new Hand instance which is a copy of the
        original Hand instance. Copies are made of the Card
        instances comprising the original card list (copies
        are made by the initializer method), as well as of
        the list itself.

        """

        return self.__class__(cardlist=self._cards)

    def discard(self):

        """Discards all cards in the hand and returns them
        to the associated deck.

        """

        if self._deck == None:
            raise NoAssociatedDeckError()

        self._deck.discard(self._cards)
        self._cards = []
        self._cards_changed()

    def draw(self, numcards, face_up=False, face_down=True):

        """Draws a specific number of cards from the deck.

        Arguments:
        numcards -- the number of cards to draw.
        face_up -- draw the new cards face up if True
        face_down -- draw the new cards face down if True

        """

        if self._deck is None:
            raise NoAssociatedDeckError
        else:
            self._cards.extend(self._deck.draw(numcards, face_up, face_down))
            self._cards_changed()

    def exchange(self, chg=None, face_up=False, face_down=False):

        """Exchanges selected cards for new cards drawn from the deck.

        Arguments:
        chg -- a string of digits containing the positions of the
        cards to be exchanged, starting at 1, e.g. "125", or "3", or
        "14". If this is missing, all cards which are face down will
        be exchanged.
        face_up -- draw the new cards face up if True
        face_down -- draw the new cards face down if True

        """

        discards = []

        if chg:
            for idx in chg:
                if int(idx) in range(len(self._cards)):
                    discards.append(self._cards[int(idx) - 1])
                    self._cards[int(idx) - 1] = self._deck.draw(1,
                                                                face_up,
                                                                face_down)[0]
        else:
            for idx, card in enumerate(self._cards):
                if card.is_face_down():
                    discards.append(card)
                    self._cards[idx] = self._deck.draw(1, face_up, face_down)[0]

        self._deck.discard(discards)
        self._cards_changed()

    def face_up(self, position=None):

        """Turns one or all the cards in the hand face up."""

        if position:
            self._cards[position - 1].face_up()
        else:
            for card in self._cards:
                card.face_up()

    def face_down(self, position=None):

        """Turns one or all the cards in the hand face down."""

        if position:
            self._cards[position - 1].face_down()
        else:
            for card in self._cards:
                card.face_down()

    def flip(self, position=None):

        """Flips one or all the cards in the hand."""

        if position:
            self._cards[position - 1].flip()
        else:
            for card in self._cards:
                card.flip()

    def get_list(self):

        """Returns the card list."""

        return self._cards

    def index_list(self):

        """Returns a list of card indices for the current hand.

        Primarily intended to be used for comparing lists, since
        the usual card comparison only compares by rank, so a royal
        flush of clubs and a royal flush of spades would compare as
        identical when equating the output of get_list().

        """

        return [card.index() for card in self._cards]

    def observe(self, target, callback):

        """Adds an observer."""

        if target not in self._observers:
            self._observers.append((target, callback))

    def unobserve(self, target):

        """Removes an observer."""

        self._observers = [(obj, func) for obj, func in
                           self._observers if obj is not target]

    # Conversion operators

    def __str__(self):

        """Override string conversion operator to return a
        representation of the hand in short "6D" format.

        """

        return ''.join([" {0:>3}".format(c.name_string(short=True))
                        for c in self._cards])

    # Comparison operators

    # Disable pylint message for access to protected other._score,
    # usage is safe when comparing two types of the same class
    # by an instance method.
    #
    # pylint: disable=W0212

    def __eq__(self, other):

        """Override == operator based on standard poker hand evaluation."""

        if not isinstance(other, Hand):
            raise NotImplementedError("Only other Hands can be compared " +
                                      "to Hands.")
        if self._score == other._score:
            return True
        else:
            return False

    def __ne__(self, other):

        """Override != operator based on standard poker hand evaluation."""

        return not self == other

    def __gt__(self, other):

        """Override > operator based on standard poker hand evaluation."""

        if not isinstance(other, Hand):
            raise NotImplementedError("Only other Hands can be compared " +
                                      "to Hands.")
        if self._score > other._score:
            return True
        else:
            return False

    def __le__(self, other):

        """Override <= operator based on standard poker hand evaluation."""

        return not self > other

    def __lt__(self, other):

        """Override < operator based on standard poker hand evaluation."""

        if not isinstance(other, Hand):
            raise NotImplementedError("Only other Hands can be compared " +
                                      "to Hands.")
        if self._score < other._score:
            return True
        else:
            return False

    def __ge__(self, other):

        """Override >= operator based on standard poker hand evaluation."""

        return not self < other

    # pylint: enable=W0212

    # Concatenation and repetition operators

    def __add__(self, other):

        """Adds the cards in one Hand to another."""

        if not isinstance(other, Hand):
            raise NotImplementedError("You can only add another " +
                                      "Hand to a Hand.")
        else:
            new_hand = self.copy()
            new_hand.extend(other)
            return new_hand

    def __mul__(self, other):

        """Multiples the cards in a Hand by an integer."""

        if not isinstance(other, int) or other < 1:
            raise NotImplementedError("You can only multiply a Hand " +
                                      "by a positive integer")
        else:
            new_cards = []
            for copies in range(other):    # pylint: disable=W0612
                new_cards.extend(self.copy().get_list())
            return self.__class__(cardlist=new_cards, nocopy=True)

    def __radd__(self, other):

        """Adds the cards in one Hand to another."""

        if not isinstance(other, Hand):
            raise NotImplementedError("You can only add another " +
                                      "Hand to a Hand.")
        else:
            new_hand = self.copy()
            new_hand.extend(other)
            return new_hand

    def __rmul__(self, other):

        """Multiples the cards in a Hand by an integer."""

        if not isinstance(other, int) or other < 1:
            raise NotImplementedError("You can only multiply a " +
                                      "Hand by a positive integer")
        else:
            new_cards = []
            for copies in range(other):    # pylint: disable=W0612
                new_cards.extend(self.copy().get_list())
            return self.__class__(cardlist=new_cards, nocopy=True)

    def __iadd__(self, other):

        """Adds the cards in one Hand to another."""

        if not isinstance(other, Hand):
            raise NotImplementedError("You can only add another " +
                                      "Hand to a Hand.")
        else:
            self.extend(other)
            self._cards_changed()
            return self

    def __imul__(self, other):

        """Multiples the cards in a Hand by an integer."""

        if not isinstance(other, int) or other < 1:
            raise NotImplementedError("You can only multiply a Hand by " +
                                      "a positive integer")
        else:
            new_cards = []
            for copies in range(other - 1):    # pylint: disable=W0612
                new_cards.extend(self.copy().get_list())
            self._cards.extend(new_cards)
            self._cards_changed()
            return self

    # Indexing and iteration methods

    def __len__(self):

        """Returns the number of cards in the hand."""

        return len(self._cards)

    def __getitem__(self, key):

        """Returns the card at the specified index.

        """

        if isinstance(key, slice):
            new_list = []
            for original_card in self._cards[key]:
                new_list.append(original_card)
            return Hand(cardlist=new_list, nocopy=True)
        else:
            return self._cards[key]

    def __setitem__(self, key, value):

        """Sets the card at the specified index."""

        if isinstance(key, slice):
            if not isinstance(value, Hand):
                raise TypeError("Only other Hand instances can be " +
                                "assigned via slicing.")
            self._cards[key] = value.get_list()
            self._cards_changed()
        elif not isinstance(value, Card):
            raise TypeError("Only Card instances can be assigned.")
        else:
            self._cards[key] = value.copy()
            self._cards_changed()

    def __delitem__(self, key):

        """Deletes the card at the specified index."""

        del self._cards[key] 
        self._cards_changed()

    def __iter__(self):

        """Returns a copy of the card list as an iterator object."""

        return iter(self.get_list())

    def __contains__(self, item):

        """Returns true if item is in the card list."""

        if not isinstance(item, Card):
            return False
        else:
            for card in self._cards:
                if card.index() == item.index():
                    return True
            return False

    # Container methods

    def append(self, value):

        """Appends a card to the card list."""

        if not isinstance(value, Card):
            raise TypeError("Only Card instances can be appended.")
        else:
            self._cards.append(value.copy())
            self._cards_changed()

    def count(self, value):

        """Returns the count of a card or integer rank in the card list."""

        if isinstance(value, Card):
            cnt, index = 0, value.index()
            for card in self._cards:
                if card.index() == index:
                    cnt += 1
            return cnt
        elif isinstance(value, int) or isinstance(value, str):
            cnt, value = 0, get_rank_integer(value)
            for card in self._cards:
                if card.rank() == value:
                    cnt += 1
            return cnt
        else:
            return 0

    def extend(self, hand):

        """Extends the card list with that of another Hand."""

        if not isinstance(hand, Hand):
            raise TypeError("Hand instances may only be extended with " +
                            "other Hand instances.")
        else:
            self._cards.extend(hand.copy().get_list())
            self._cards_changed()

    def index(self, value):

        """Returns the index in the card list of the first item whose
        value is 'value'.

        """

        if isinstance(value, Card):
            for idx, card in enumerate(self._cards):
                if card.index() == value.index():
                    return idx
            raise ValueError("Card.index(x): x not in Card")
        elif isinstance(value, int) or isinstance(value, str):
            value = get_rank_integer(value)
            for idx, card in enumerate(self._cards):
                if card.rank() == value:
                    return idx
            raise ValueError("Card.index(x): x not in Card")
        else:
            raise ValueError("Card.index(c): x not in Card")

    def insert(self, idx, value):

        """Inserts a card at an index in the card list."""

        if not isinstance(value, Card):
            raise TypeError("Only Card instances may be inserted into " +
                            "Hand instances.")
        else:
            self._cards.insert(idx, value.copy())
            self._cards_changed()

    def pop(self, idx=None):

        """Pops a card at a specified index (or from the end, if no
        index is provided) of the card list, and returns it.

        """

        if idx != None:
            if not isinstance(idx, int):
                raise TypeError("index must be an integer")
            ret_card = self._cards.pop(idx)
        else:
            ret_card = self._cards.pop()
        self._cards_changed()
        return ret_card

    def remove(self, value):

        """Removes the first Card from the card list whose value is
        'value'.

        """

        if not isinstance(value, Card):
            raise TypeError("Only Cards may be removed from a Hand.")
        else:
            self._cards.remove(value)
            self._cards_changed()

    def sort(self, key=None, reverse=False):        # pylint: disable=W0613

        """Sorts the Cards, in place."""

        # pylint: disable=W0212

        self._cards.sort(key=Card._sort_index, reverse=reverse)

        # pylint: enable=W0212

    def reverse(self):

        """Reverses the order of the cards, in place."""

        self._cards.reverse()

    # Non-public methods

    def _cards_changed(self):

        """Called when the card list changes, will normally
        be override by subclasses.

        """

        self._notify_observers()

    def _notify_observers(self):

        """Notifies observers."""

        for _, callback in self._observers:
            callback()

    def _num_observers(self):

        '''Returns the number of active observers.'''

        return len(self._observers)

    def _ranks(self, sort=False, reverse=False):

        """Returns a list of card ranks.

        Arguments:
        sort -- set to True to sort the list in ascending order
        reverse -- set to True to sort the list in descending order.

        """

        rank_list = [card.rank() for card in self._cards]
        if sort or reverse:
            rank_list.sort(reverse=reverse)
        return rank_list

    def _suits(self):

        """Returns a list of card suits."""

        return [card.suit() for card in self._cards]

    def _get_rank_counts(self):

        """Returns a dictionary of rank counts."""

        rank_counts = defaultdict(int)
        for rank in self._ranks():
            rank_counts[rank] += 1
        return rank_counts

    def _get_suit_counts(self):

        """Returns a dictionary of suit counts."""

        suit_counts = defaultdict(int)
        for suit in self._suits():
            suit_counts[suit] += 1
        return suit_counts
