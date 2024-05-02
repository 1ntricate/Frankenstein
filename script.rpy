#Nathan N.

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

########### Backgrounds
image bedroom = "images/bedroom.png"
image outsideapart = "images/outsideapartment.png"
image gameover = "images/gameover.jpg"
image office = "images/office.jpg"
image mikoRoom = "images/mikoRoom.jpg"

########## Characters
image miko Happy ="images/mikoHappy.png"
image miko Sad = "images/mikoSad.png"



define miko = Character("Miko", color="#FF0000")
define player = Character("Me", color="#0000FF")


label start:
    "Hello World"


label Scene1:
    scene bedroom
    play sound "audio/knock.mp3" volume 0.8
    play music "audio/spooky.mp3" volume 0.5
    "???" "*Knock Knock*"

    player "Who's knocking on my door so late?"
    player "What time is it right now?"
    player "12am!? Who's up so late at this hour?"
    player "Should I pick it up?  It might that manga I ordered earlier this week."
    player "Wait.. No way they would come this late?"
    play sound "audio/knock.mp3" volume 0.8

    player "Ahhh!! They're knocking again.  "

    "???" "Anyone there?"

    scene outsideapart
    player "There seems to be no one?"
    player "It might have been a ghost..."
    show miko Happy
    miko "Hello Neighbor!"

    player "Ahhh!! Who are you?"

    miko "Hello, I am Miko.  I just recently moved in today."
    miko "It's a bit late right now, and all my stuff is outside, I was wondering if you could help me move some boxes inside?"
    miko "You're the only one that openened the door, I knocked on some other doors earlier, but it seemed like everyone else seemed asleep."

    player "{i}I was asleep too.. {/i} "
    player "Uhhh..."

    show miko Sad
    miko "Pleaseeee!! It will only take like 5 mins!!"
    player "{i} Should I help her?  She is a stranger though..."
    player "{i} Mom always told me not trust strangers.."
    player "{i} Although, She is kind of cute."

menu:

    "I guess I'll help her":
        jump mikoRoom

    "Nah... I am going to bed.":
        jump death

label mikoRoom:
    scene bedroom
    show miko Happy

    miko "Welcome to my room"


    jump Scene2


label death:
        "Game Over"
        menu:
            "Return to Tile Screen":
                return 
        

label Scene2:
    scene bedroom
    player "I'm finally back in my room."
    player "I am wondering if Miko is doing feeling at home"
    player "I am feeling a bit tired now, I guess it's time to sleep"
    
    jump playerRoom


label playerRoom: 
    scene bedroom
    player "I guess I should start my day."
    player "What should I do today?"

    menu: 
        "Work": 
            jump work
        "Spend time with Miko":
            jump mikoTime
        "Touch some grass":
            jump outside


    

label work:
    scene bg office
    player "I sure am working hard today~"

    jump Scene2

label mikoTime:
    scene bg mikoRoom
    show miko Happy
    miko "Ah hello player~ I've been waiting for you"

    jump Scene2


label outside: 
    player "Wow it sure it nice outside today"
