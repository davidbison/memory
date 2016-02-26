# implementation of card game - Memory

import simplegui
import random

# global state
FRAME_WIDTH = 800
FRAME_HEIGHT = 100
CARD_FONT_SIZE = 56
CARD_COLOR = "orange"

# helper function to initialize globals
def new_game():
    global deck
    set1 = range(9)
    set2 = range(9)
    deck = set1 + set2
    random.shuffle(deck)


# define event handlers
def mouseclick(pos):
    # add game state logic here
    pass


# cards are logically 50x100 pixels in size
def draw(canvas):
    card_posX = 12
    card_posY = FRAME_HEIGHT - (CARD_FONT_SIZE / 2 + 4)
    for card in deck:
        canvas.draw_text(str(card),
                         [card_posX, card_posY],
                         CARD_FONT_SIZE,
                         CARD_COLOR)
        card_posX += 100 - 56


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", FRAME_WIDTH, FRAME_HEIGHT)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()