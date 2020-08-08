﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image sam happy = "Characters/Sam/sam happy.png"
image sam angry = "Characters/Sam/sam angry.png"
image sam neutral = "Characters/Sam/sam neutral.png"
image sam shocked = "Characters/Sam/sam shocked.png"

image mimi happy = "Characters/Mimi/mimi happy.png"
image mimi angry = "Characters/Mimi/mimi angry.png"
image mimi neutral = "Characters/Mimi/mimi neutral.png"
image mimi shocked = "Characters/Mimi/mimi shocked.png"

image bg bakery = "Backgrounds/bg bakery.jpg"
#image mimihead composite = LiveComposite(
#      (100,200), #assuming your dolls have a 360x720 format)
#      (0,0), "head right.png", # Assuming you have a "base head"
#      (0,0), "neutral right.png", # and you just impose a face on it
#      (0,0), "hair curls right.png" # and you just impose a face on it
#    )


define e = Character("Eileen")
define s = Character("Sam", color="#ff0000")
define m = Character("Mimi", color="#0000ff")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg bakery
    play music "audio/Purple Planet Music - African Adventure (1 27) 120bpm (L).mp3"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

#    show sam happy:# at left
#        xalign 0.5 yalign 0.5
    show sam happy:# at left
        xalign 0.1 yalign 0.5

    # These display lines of dialogue.

    s "Hi Mimi!"

    hide sam happy

    "Whom may I help?"

    show mimi neutral:# at left
        xalign 0.9 yalign 0.5

    m "One casino brown please"

    hide mimi neutral
    show sam angry:# at left
        xalign 0.1 yalign 0.5

    s "Hey, it is my turn you bitch!"

    hide sam angry
    # This ends the game.
    show mimi shocked:
        xalign 0.9 yalign 0.5

    "Let's not get upset about this, people"

    return
