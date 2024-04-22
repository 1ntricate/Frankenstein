#Nathan N.

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

########### Backgrounds
image bedroom = "images/bedroom.png"
image outsideapart = "images/outsideapartment.png"


########## Characters
image miko Happy ="images/mikoHappy.png"
image miko Sad = "images/mikoSad.png"



define miko = Character("miko", colors = "#FFFF00")

label start:
    "Hello World"


label Scene1:
    scene bedroom
    play sound "audio/knock.mp3" volume 0.8
    play music "audio/spooky.mp3" volume 0.5
    "???" "*Knock Knock*"

    "Me" "Who's knocking on my door so late?"
    "Me" "What time is it right now?"
    "Me" "12am!? Who's up so late at this hour?"
    "Me" "Should I pick it up?  It might that manga I ordered earlier this week."
    "Me" "Wait.. No way they would come this late?"
    play sound "audio/knock.mp3" volume 0.8

    "Me" "Ahhh!! They're knocking again.  "

    "???" "Anyone there?"

    scene outsideapart
    "Me" "There seems to be no one?"
    "Me" "It might have been a ghost..."
    show miko Happy
    "Miko" "Hello Neighbor!"

    "Me" "Ahhh!! Who are you?"

    "Miko" "Hello, I am Miko.  I just recently moved in today."
    "Miko" "It's a bit late right now, and all my stuff is outside, I was wondering if you could help me move some boxes inside?"
    "Miko" "You're the only one that openened the door, I knocked on some other doors earlier, but it seemed like everyone else seemed asleep."

    "Me" "{i}I was asleep too.. {/i} "
    "Me" "Uhhh..."

    show miko Sad
    "Miko" "Pleaseeee!! It will only take like 5 mins!!"
    "Me" "{i} Should I help her?  She is a stranger though..."
    "Me" "{i} Mom always told me not trust strangers.."
    "Me" "{i} Although, She is kind of cute."

label Scene2:

    