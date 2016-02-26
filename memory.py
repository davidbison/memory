# implementation of card game - Memory

import simplegui
import random


# global state
FRAME_WIDTH = 800
FRAME_HEIGHT = 100


# helper function to initialize globals
def new_game():
    global deck, exposed
    set1, set2 = range(9), range(9)
    deck = set1 + set2
    random.shuffle(deck)
    exposed = [card == None for card in deck]


# helper function to convert pt to px
def pt_to_px(font_size):
    # 12pt font is 16px
    return font_size * 16 / 12


# define event handlers
def mouseclick(pos):
    global deck, exposed, selected_card

    # Convert mouse click position to card index
    click_position = list(pos)
    if click_position[0] > 0 and click_position[0] <= 50:
        selected_card = 0
    elif click_position[0] > 50 and click_position[0] < 100:
        selected_card = 1
    elif click_position[0] > 100 and click_position[0] < 150:
        selected_card = 2
    elif click_position[0] > 150 and click_position[0] < 200:
        selected_card = 3
    elif click_position[0] > 200 and click_position[0] < 250:
        selected_card = 4
    elif click_position[0] > 250 and click_position[0] < 300:
        selected_card = 5
    elif click_position[0] > 300 and click_position[0] < 350:
        selected_card = 6
    elif click_position[0] > 350 and click_position[0] < 400:
        selected_card = 7
    elif click_position[0] > 400 and click_position[0] < 450:
        selected_card = 8
    elif click_position[0] > 450 and click_position[0] < 500:
        selected_card = 9
    elif click_position[0] > 500 and click_position[0] < 550:
        selected_card = 10
    elif click_position[0] > 550 and click_position[0] < 600:
        selected_card = 11
    elif click_position[0] > 600 and click_position[0] < 650:
        selected_card = 12
    elif click_position[0] > 650 and click_position[0] < 700:
        selected_card = 13
    elif click_position[0] > 700 and click_position[0] < 750:
        selected_card = 14
    elif click_position[0] > 750 and click_position[0] < 800:
        selected_card = 15
    print "Card face value:", deck[selected_card]
    print "Card index:", selected_card

    # Flip cards over and back
    if not exposed[selected_card]:
      exposed[selected_card] = True
    elif exposed[selected_card]:
      exposed[selected_card] = False

# cards are logically 50x100 pixels in size
def draw(canvas):
    global exposed
    card_posX = 0
    card_posY = 0
    i = 0
    point1 = [0, 0]
    """
    Check whether the card is exposed or not.
    If exposed, draw the number.
    If not, draw a rectangle
    """
    for card in deck:
        if exposed[i]:
            canvas.draw_text(str(card),
                            [card_posX + 12, card_posY + (FRAME_HEIGHT - 26)],
                            56,
                            "orange")
        else:
            canvas.draw_polygon([point1,
                                  [point1[0]+50, point1[1]],
                                  [point1[0]+50, point1[1]+100],
                                  [point1[0],point1[1]+100]],
                                2,
                                "black",
                                "green")
        i += 1
        card_posX += 50
        point1[0] += 50


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