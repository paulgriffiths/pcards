"""Card images classes."""

import os
from tkinter import PhotoImage


class CardImagesSmall:

    '''Small card images class. Does not require PIL.'''

    cardimgs = None
    backimg = None
    emptyimg = None
    dirname, _ = os.path.split(os.path.realpath(__file__))
    imgdir = dirname + "/card_images_small/"

    def __init__(self):

        '''This class is not intended to be instantiated.'''

        pass

    @classmethod
    def empty(cls):

        '''Returns an image for an empty card place.'''

        if not cls.emptyimg:
            cls.emptyimg = PhotoImage(file="{0}empty.gif".format(cls.imgdir))
        return cls.emptyimg

    @classmethod
    def back(cls):

        '''Returns an image for the card back.'''

        if not cls.backimg:
            cls.backimg = PhotoImage(file="{0}b.gif".format(cls.imgdir))
        return cls.backimg

    @classmethod
    def card(cls, cardindex=None):

        '''Returns a card image.'''

        if not cls.cardimgs:
            cls.cardimgs = []
            for idx in range(1, 53):
                newcard = PhotoImage(file="{0}{1}.gif".format(cls.imgdir, idx))
                cls.cardimgs.append(newcard)

        return cls.cardimgs[cardindex - 1]


class CardImagesLarge:

    '''Large card images class. Requires PIL.'''

    cardimgs = None
    backimg = None
    emptyimg = None
    dirname, _ = os.path.split(os.path.realpath(__file__))
    imgdir = dirname + "/card_images_large/"

    def __init__(self):

        '''This class is not intended to be instantiated.'''

        pass

    @classmethod
    def empty(cls):

        '''Returns an image for an empty card place.'''

        from PIL.ImageTk import PhotoImage

        if not cls.emptyimg:
            cls.emptyimg = PhotoImage(file="{0}card_empty@2x.png".
                                      format(cls.imgdir))
        return cls.emptyimg

    @classmethod
    def back(cls):

        '''Returns an image for the card back.'''

        from PIL.ImageTk import PhotoImage

        if not cls.backimg:
            cls.backimg = PhotoImage(file="{0}card_back_blue@2x.png".
                                     format(cls.imgdir))
        return cls.backimg

    @classmethod
    def card(cls, cardindex=None):

        '''Returns a card image.'''

        from PIL.ImageTk import PhotoImage

        if not cls.cardimgs:
            cls.cardimgs = []
            for idx in range(0, 52):
                newcard = PhotoImage(file="{0}card{1}@2x.png".
                                     format(cls.imgdir, idx))
                cls.cardimgs.append(newcard)

        return cls.cardimgs[cardindex - 1]
