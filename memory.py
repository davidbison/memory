# implementation of card game - Memory

import simplegui
import random

# global state
FRAME_WIDTH = 800
FRAME_HEIGHT = 100


# helper function to initialize globals
def new_game():
    global deck, exposed
    set1 = range(9)
    set2 = range(9)
    deck = set1 + set2
    random.shuffle(deck)
    exposed = [card == None for card in deck]


# helper function to convert pt to px
def pt_to_px(font_size):
    # 12pt font is 16px
    return font_size * 16 / 12


# define event handlers
def mouseclick(pos):
    # add game state logic here
    pass


# cards are logically 50x100 pixels in size
def draw(canvas):
    global exposed, upper_left, upper_right, lower_left, lower_right
    card_posX = 12
    card_posY = FRAME_HEIGHT - 26
    i = 0
    for card in deck:
        if exposed[i]:
            canvas.draw_text(str(card),
                            [card_posX, card_posY],
                            56,
                            "orange")
            card_posX += 100 - 56
        else:
            point1 = [0, 0]
            for card in exposed:
                canvas.draw_polygon([point1, [point1[0]+50, point1[1]], [point1[0]+50, point1[1]+100],[point1[0],point1[1]+100]],
                    2,
                    "black",
                    "green")
                point1[0] += 50
        i += 1


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