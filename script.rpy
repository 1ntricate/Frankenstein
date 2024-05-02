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
image stabbed = "images/stabbed.png"
image bedroomDay = "images/bedroomDay.png"
image outside = "images/outside.jpg"
image scenee = "images/sceneee.png" 

####Vo Changes 5/2/2024 added by N.

image morning: 
    "images/morningapartment.png" 
    size(1920, 1080)
image kitchen: 
    "images/kitchen.png" 
    size(1920, 1080)
image outsideapart = "images/outsideapartment.png"
image raining = Movie(play="images/rain.ogv")
image wine: 
    "images/wine.png" 
    size(1920, 1080)

########## Characters
image miko Happy ="images/mikoHappy.png"
image miko Sad = "images/mikoSad.png"

###Vo Changes 5/2/2024
image player Move: 
    "images/playerMove.png" 
    xalign 0.5 yalign 0.5 
    size (700, 700)

image player Annoy: 
    "images/playerAnnoy.png" 
    xalign 0.5 yalign 0.5 
    size (700, 700)
image player Ok: 
    "images/playerOk.png" 
    xalign 0.5 yalign 0.5 
    size (650, 700)
image player Nap: 
    "images/playerNap.png" 
    xalign 0.5 yalign 0.5 
    size (1000, 1000)
image player Tired: 
    "images/playerTired.png" 
    xalign 0.5 yalign 0.5 
    size (1000, 1000)
image player bike: 
    "images/playerBike.png"
    xalign 1.0 yalign 0.5 
    size (1000, 1000)
image player Suprised: 
    "images/playerSurprised.png" 
    xalign 1.0 yalign 0.5 
    size (1000, 1000)
image player OJ: 
    "images/playerOJ.png" 
    xalign 1.0 yalign 0.5 
    size (1000, 1000)
image player Make:
    "images/playerMake.png" 
    xalign 0.5 yalign 0.5 
    size (1000, 1000)
image player Shock: 
    "images/playerShock.png" 
    xalign 1.0 yalign 0.5 
    size (1000, 1000)
image player Relax: 
    "images/playerRelax.png" 
    xalign 1.0 yalign 0.5 
    size (1000, 1000)
######Vo Changes 5/2/204 added by N.

define miko = Character("Miko", color="#FF0000")
define player = Character("Me", color="#0000FF")


label start:
    "Hello World"
    voice "audio/main-story1.mp3"
    "Our main character, who is moving to the new apartment, is excited to start fresh and make new neighbor friends. 
    A mysterious story ensues when strange occurrences begin happening in the building,leading our characters to uncover 
    dark secrets hidden within the walls of their new home. Since his home moving made him so tired, he felt sleepy and 
    woke up to hear a mysterious laugh and someone knocking his door, sparking a sense of unease within him."
####Prologue Scene
label Scene0:
#####Moving Scene
    scene morning
    menu:
        "Waaahhh, It such a beautiful day outside":
            play sound "audio/rain.wav" volume 0.8
            pause 0.5
            scene raining
            show player Suprised
            player "Wait Whatttt the hell "
            player "Maybe let moving tommorrow"
            scene morning
        "YAYYY, Let's move to new home. I'm so excited...":
            player "Go ! Go !"
    show player Ok 
    player "Finally Done"
    pause 0.5
    scene scenee
    show player Relax

    player "AHH! Today such an busy day !!!"
    player "Should I take a nap?"
    menu: 
        "So lazy.. Maybe gonna take a nap then":
            show player Nap
            player "Z Z Z Z"
            player "Nap time is the best"
            player "No, Maybe go to make some drink in the kitchen"
#######OJ Scene
    scene kitchen
    "Me" "What should I drink tonight?"
    menu: 
        "Making Orange juice sounds healthy":
            "Me" "......"
            show player Make
            "Me" "Waiting for orange juice"
            "Me" "Yay"
            show player OJ
            "Me" "Hmmm.. Delicicous"
            "Me" "Perfect"
        "Cocktail or Red Wine, etc. Sounds not bad":
            scene wine 
            pause 1.0
            scene kitchen
            "Me" "Ahhhhhhh Shit...."
            "Me" "I should not drink this"
            show player Shock
            pause 1.0
            



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

    menu: 
        "Come and open the door to check.":
            show player Ok
            "Me" "...."
            "Me" "Alright, let check it, just in case"
        "Nevermind, skip it and continue sleep.":
            play sound "audio/knock.mp3" volume 0.8
            "???" "* Knock Knock *"
            show player Annoy
            "Me" "Ahh!!! They're knocking again!!!! "
            "Me" "Maybe I should check"



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
        jump stabbed

label mikoRoom:
    scene mikoRoom
    show miko Happy

    miko "Welcome to my room"


    jump Scene2

label stabbed:
    scene stabbed
    "You've been stabbed..."
    miko "Maybe you should have came to my room..."
    scene stabbed

    jump death

label death:
        scene gameover
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

###primary scene for player, add more places

label playerRoom: 
    scene bedroomDay
    player "I guess I should start my day."
    scene bedroomDay
    player "What should I do today?"

    menu: 
        "Work": 
            jump work
        "Spend time with Miko":
            jump mikoTime
        "Touch some grass":
            jump outside
        "Sleep the whole day":
            jump Scene4


    
####work scene
label work:
    scene  office
    player "I sure am working hard today~"
    scene office 

    jump Scene2
####miko scene

label mikoTime:
    scene mikoRoom
    show miko Happy
    miko "Ah hello player~ I've been waiting for you"
    scene mikoRoom

    jump Scene2
####touching some grass

label outside: 
    scene outside
    player "Wow it sure it nice outside today"

    jump Scene2

####Map Scene (Insert map here and do logic )
label Scene4:



