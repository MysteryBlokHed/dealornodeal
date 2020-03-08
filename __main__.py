# Created by MysteryBlokHed in 2019.
import random
from time import sleep
from math import ceil

from box import Box

BOX_OPEN_DELAY = 3 # Amount of seconds to wait when opening a box
BOX_COUNT = 26 # Amount of boxes in game
CURRENCY_SYMBOL = "$"
VALUES = (0.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, # Price options for each box
        1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000)
BANKER_OFFER_FREQUENCY = 4 # The amount of turns per banker offer
BANKER_PICKUP_DELAY = 3 # Amount of seconds to wait before answering banker call

# Will divide the mean of all remaining values by these numbers (mean of remaining values/7), depending on if it's the first, second, or final third of the game.
# The banker will only call 3 times/game.
FIRST_BANKER_OFFER = 8
SECOND_BANKER_OFFER = 7
THIRD_BANKER_OFFER = 1.75

values = list(VALUES)[:BOX_COUNT]

# Host response variables
POSITIVE = ("Nice!", "Great one!", "Good choice!", "Fantastic!")
NEGATIVE = ("Yikes.", "Oof, that's unfourtunate.", "Too bad.", "Oh, that's not ideal.")

# Keep track of boxes
boxes = {}
box_order = []

turn = 0

random.seed()

# Host response functions
def get_positive():
    return random.choice(POSITIVE)

def get_negative():
    return random.choice(NEGATIVE)

# Other functions
def show_boxes():
    string = ""
    for box in box_order:
        string += "["+str(box)+"]"
    return string

def show_remaining_values():
    string = ""
    for value in values:
        string += CURRENCY_SYMBOL + str(value) + " "
    return string

def get_banker_offer():
    """Use a formula to generate the banker's offer."""
    mean = sum(values)/len(values) # Get mean of all values left
    if turn <= ceil(BOX_COUNT/3): # First third of game
        return round(mean/FIRST_BANKER_OFFER, 2)
    elif turn <= ceil(BOX_COUNT/3)*2: # Second third of game
        return round(mean/SECOND_BANKER_OFFER, 2)
    else: # Final third of game
        return round(mean/THIRD_BANKER_OFFER, 2)

# Create the boxes
random.seed()
for i in range(BOX_COUNT):
    value = random.choice(values)
    boxes[i+1] = Box(i+1, value)
    box_order.append(i+1)
    values.remove(value)

values = list(VALUES)[:BOX_COUNT] # Reset values variable

random.seed()
random.shuffle(box_order) # Randomize the order of the boxes

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Welcome to Deal Or No Deal!")
print("Programmed by MysteryBlokHed")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", end="\n\n")

print("[HOST] Welcome to Deal Or No Deal!")
print("[HOST] Start off by choosing a box from 1-"+str(BOX_COUNT)+" to keep until the end.")
# Select a box to keep
while True:
    try:
        choice = int(input("> "))
        if choice > 0 and choice <= BOX_COUNT:
            saved_box = choice # Save the box
            box_order.remove(choice) # Remove it from the available boxes
            break
        else:
            print("[HOST] Sorry, but that's not an option.")
    except ValueError:
        print("[HOST] Sorry, but that's not an option.")
print("[HOST] "+get_positive())
print("[HOST] Alright, onto the game.")

playing = True

while playing:
    # Banker offer
    if turn % BANKER_OFFER_FREQUENCY == 0 and turn != 0:
        print("\nRemaining values:")
        print(show_remaining_values())
        offer = get_banker_offer()
        print("*Phone ringing*")
        print("[HOST] Looks like the banker has an offer!")
        sleep(BANKER_PICKUP_DELAY)
        print(f"[HOST] The banker offers you {CURRENCY_SYMBOL}{offer}. Deal or no deal?")
        while True:
            choice = input("> ")
            if choice.lower() == "deal":
                print("[HOST] Alright, I guess we're done here!")
                playing = False
                break
            elif choice.lower() == "no" or choice.lower() == "no deal":
                print("[HOST] Okay, let's continue playing.")
                break
            else:
                print("[HOST] That's not a valid answer.")

    if playing:
        if turn+2 != BOX_COUNT:
            print("\nBoxes:" + show_boxes())
            print("Remaining values:")
            print(show_remaining_values())
            print("[HOST] Choose a box to open.")

            while True:
                try:
                    box = int(input("> "))
                    if box in box_order: # Box is available to open
                        print("[HOST] Alright, let's check what's inside...")
                        sleep(BOX_OPEN_DELAY)

                        value = boxes[box].get_value()
                        box_order.remove(box) # Remove the box from the available box list

                        # Host reaction                                       # Make sure that the value chosen wasn't the highest one left
                        if VALUES.index(boxes[box].get_value()) < BOX_COUNT/2 and values.index(value) != len(values)-1:
                            print(f"[HOST] {CURRENCY_SYMBOL}{value}! {get_positive()}") # Say something positive
                        else:
                            print(f"[HOST] {CURRENCY_SYMBOL}{value}. {get_negative()}") # Say something negative

                        values.remove(value) # Remove the value from the remaining values
                        break
                    else: # Box is not available to open
                        print("[HOST] That box isn't available.")
                except ValueError:
                    print("[HOST] That box isn't available.")
            turn += 1
        else:
            print("[HOST] Alright, you're down to two boxes.")
            print(f"[HOST] The remaining values are {' and '.join(show_remaining_values().split())}.")
            print(f"[HOST] Do you want to open up your saved box, #{saved_box}, or do you want to open the remaining box, #{box_order[0]}?")
            while True:
                try:
                    box = int(input("> "))
                    if box == saved_box: # Player opens their saved box
                        print("[HOST] Okay, let's check what's inside...")
                        sleep(BOX_OPEN_DELAY)

                        value = boxes[saved_box].get_value()

                        # Host reaction
                        if VALUES.index(boxes[saved_box].get_value()) > VALUES.index(boxes[box_order[0]].get_value()):
                            print(f"[HOST] Your saved box had {CURRENCY_SYMBOL}{value}! {get_positive()}") # Say something positive
                        else:
                            print(f"[HOST] Your saved box had {CURRENCY_SYMBOL}{value}. {get_negative()}") # Say something negative
                        break
                    elif box == box_order[0]: # Player opens the remaining box
                        print("[HOST] Okay, let's check what's inside...")
                        sleep(BOX_OPEN_DELAY)

                        value = boxes[box_order[0]].get_value()

                        # Host reaction
                        if VALUES.index(boxes[box_order[0]].get_value()) > VALUES.index(boxes[saved_box].get_value()):
                            print(f"[HOST] The remaining box had {CURRENCY_SYMBOL}{value}! {get_positive()}") # Say something positive
                        else:
                            print(f"[HOST] The remaining box had {CURRENCY_SYMBOL}{value}. {get_negative()}") # Say something negative                        
                        break
                except ValueError:
                    pass
            break
    else: # Player accepted banker deal
        print("[HOST] Let's open up the box you saved, and see if you made a good choice.")
        sleep(BOX_OPEN_DELAY)

        # Host reaction
        if boxes[saved_box].get_value() <= offer: # Check if the player made a good decision with the banker deal
            print(f"[HOST] {CURRENCY_SYMBOL}{boxes[saved_box].get_value()}! {get_positive()}") # Say something positive
        else:
            print(f"[HOST] {CURRENCY_SYMBOL}{boxes[saved_box].get_value()}. {get_negative()}") # Say something negative
        
print("[HOST] That's it for Deal Or No Deal!")
input("Press enter to exit.")
