#Nathan N.

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


######Alberto python script lockpick init

init python:
    def check_drop(drags, drop):
        # Access the dragged and dropped objects directly
        dragged_piece = drags[0]
        dropped_on = drop

        if dragged_piece.drag_name == dropped_on.drag_name:
            renpy.jump("scene4")
        else:
            renpy.notify("Try again!")
        

########### Backgrounds

image outsideapart = "images/outsideapartment.png"
image gameover = "images/gameover.jpg"
image office = "images/office.jpg"
image stabbed = "images/stabbed.png"
image outside = "images/outside.jpg"
image scenee = "images/sceneee.png" 
image maindoor = "images/maindoor.png"

image bedroom day = "images/roomDay.jpg"
image bedroom night = "images/roomNight.jpg"
image miko room = "images/mikosRoom.jpg"
image theater lobby = "images/MovieTheaterLobby.jpg"
image cinema = "images/cinema.jpg"
image cinema movie = "images/cinemaMovie.jpg"
image cinema explosion = "images/theaterExplosion.jpg"
image fire exit = "images/fireExit.jpg"
image fire exit on fire = "images/fireExitOnFire.jpg"
image fire = "images/fireExitInFlames.jpg"
image cinema fire = "images/theaterInFlames.jpg"

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
image miko = "images/mikoDefault.png"

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
        "No, Maybe go to make some drink in the kitchen":
            jump kitchen

######Drinking Scene
label kitchen:
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

    scene maindoor
    player "Ahhh!! They're knocking again.  "
    scene maindoor

    menu: 
        "Come and open the door to check.":
            show player Ok
            player "...."
            player "Alright, let check it, just in case"
        "Nevermind, skip it and continue sleep.":
            play sound "audio/knock.mp3" volume 0.8
            "???" "* Knock Knock *"
            show player Annoy
            player "Ahh!!! They're knocking again!!!! "
            player "Maybe I should check"



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
    play sound "audio/screamWoman.mp3" 0.8
    "You've been stabbed..."
    miko "Maybe you should have came to my room..."
    scene stabbed

    jump death

label death:
        scene gameover
        play sound "audio/glitch.mps" 0.8
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
        "lockpicking test":
            jump scene3
        "Check out the map":
            jump scene7


    
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

label scene3:
    scene lock_plate
    show lock_cylinder
    player "I need to find a way to open this door."
    call screen Lockpicking_mini_game


screen Lockpicking_mini_game:
    draggroup:
        drag:
            drag_name "lock_pick"
            focus_mask True
            drag_raise False
            image "lock_pick.png" xysize (700, 700)
            dragged check_drop
        drag:
            drag_name "lock_pick"
            draggable False
            droppable True
            focus_mask True
            image "lock_hole.png"  
    

label scene4:
    play sound "audio/creak.mp3"
    # Set varaiables for timer
    $ time = 90
    $ timer_range = 90

    # Set a boolean value to keep track of game status
    $ game_over = False

    #Dictionary to keep track if items has been clicked
    default clickable_items = {1: True, 2: True, 3: True, 4: True}

    scene bg_room
    show lucy Normal with easeinleft
    play sound "audio/shower.mp3" 
    me "*Whispers*  Miko?? {i} She's showering..."
    me "Something feels off..."
    call screen items_screen

screen items_screen:
    modal True # Prevents user from leaving screen until minigame is done
    zorder 1 # Ensures screen is on top of everything else

   
    # IF time is less than 0 and game_over is True, jump to Fail label
    timer 0.01 repeat True action If(time > 0 and not game_over, true = SetVariable('time', time - 0.1),
    false = [Hide('countdown'), Jump("Fail")])
   
    bar value time range timer_range xalign 0.5 yalign 0.1 xmaximum 300 at alpha_disolve

    # Shows the items unitl they are clicked
    showif clickable_items[1]:
        imagebutton:
            focus_mask True
            xanchor 0.2
            yanchor 0.8
            xpos 0.2
            ypos 0.76
            idle "bg_darkteddy_idle"
            action [SetDict(clickable_items, 1, False), Notify("A cute teddy bear")]          
    showif clickable_items[2]:
        imagebutton:
            xanchor 0.2
            yanchor 0.1
            xpos 0.75
            ypos 0.8
            idle "bg_sushi"
            action [SetDict(clickable_items, 2, False), Notify("This nori roll is harmless!")]
    showif clickable_items[3]:
        imagebutton:
            xanchor 0.6
            yanchor 0.3
            xpos 0.32
            ypos 0.72
            idle "bg_letter"
            action [SetDict(clickable_items, 3, False), Notify("A simple letter!")]
    showif clickable_items[4]:
        imagebutton:
            xanchor 0.2
            yanchor 0.7
            xpos 0.4
            ypos 0.8
            idle "bg_knife"
            action [SetDict(clickable_items, 4, False), Notify("A bloody kitchen knife..."),
                SetVariable('game_over', True), Jump("Success")]

# Adds a fade effect to the timer bar
transform alpha_disolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0.0

label scene5:
    scene bedroom
    show lucy Normal with moveinleft
    me "Omg...What do I do..."
    me "{i} Do I call the police or..."
    play audio "audio/knocking.mp3"
    "* Knocking on the door *"
    show lucy Shocked
    me " ...... "
    play audio "audio/creak.mp3"


label scene6:
    scene outsideApartment
    show lucy Normal at left with moveinleft
    show miko Happy at center
    me "Heyyyy Miko... What's going on?"
    miko "Hey Lucy, I just wanted to apoligize about the noise earlier."
    miko " I was trying smash a spider and I ended up knocking over some stuff."
    miko "I'm sorry if I woke you up."
    me "Oh, no worries, I didn't even hear anything."
    miko "Oh, okay. Well, I'm gonna head out then, goodnight!"
    me "Goodnight Miko."
    hide miko Happy with dissolve
    
screen MapUI:
    add  "CityMap.jpg"

    imagebutton:
        focus_mask True
        idle "Movie.png"
        hover "Movie_hover.png"
        action Jump("scene8")
    imagebutton:
        focus_mask True
        idle "Home.png"
        hover "Home_hover.png"
        action Jump("scene11")
    imagebutton:
        focus_mask True
        idle "Work.png"
        hover "Work_hover.png"
        action Jump("scene9")
    imagebutton:
        focus_mask True
        idle "Park.png"
        hover "Park_hover.png"
        action Jump("scene10")

label scene7:
    #scene CityMap 

    call screen MapUI

label scene8:
    "Movie picked"
    jump movies

label scene9:
    "Work picked"

label scene10:
    "Park picked"

label scene11:
    "Home Picked"


label movies:
    scene bg theater lobby
    player "{i} I can't wait to see this movie. I've been hearing about it nonstop for days"
    player "{i} Hopefully it's as good as my landlord made it out to be"
    player "{i} Hmm I wonder if I should get a popcorn. Or maybe I could get some--"
    player "..."
    player "Miko?"
    show miko
    miko "Oh hi there. What a coincidence that we are both here at the same time"
    player "Yea that's pretty crazy haha. What movie are you here to see?"
    miko "Movie?"
    player "Aren't you here to see a movie?"
    miko "...Oh yea! Yea um, what movie are you here to see?"
    player "'Agents in Australia'..."
    show miko happy
    miko "Oh my gosh! Me too!"
    player "Wow really? What a coincidence"
    miko "That is so weird"
    miko "Well since we are going to see the same movie, maybe we can see it together?"
    player "Um yea sure. Would you like any popcorn?"
    show miko
    miko "Are you getting popcorn?"
    player "..."

    scene bg cinema
    player "Are you ok with a spot in the back?"
    miko "Yea these seats are fine"
    player "So Miko, how are you liking it here so far?"
    show miko happy
    miko "Oh it's been great. I really like the sunny weather and everyone I met has been really great"
    player "Have you met more people recently?"
    miko "No but I've met you"
    player "Oh haha"

    
