#!/usr/bin/env python3

'''Button bar widget class.'''

# Disable pylint message from inherited tkinter classes
# pylint: disable=too-many-public-methods


from tkinter import Frame, Button, LEFT


class ButtonBarWidget(Frame):

    '''Control widget class.'''

    def __init__(self, parent, buttondefs):

        '''Initialization method.'''

        Frame.__init__(self, parent)

        for title, handler in buttondefs:
            new_button = Button(self, text=title)
            cmd = lambda callback=handler, button=new_button: callback(button)
            new_button.configure(command=cmd)
            new_button.pack(side=LEFT, padx=5, pady=5)
