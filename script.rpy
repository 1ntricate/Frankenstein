#Nathan N.

# The script of the gaplayer goes in this file.

# Declare characters used by this gaplayer. The color arguplayernt colorizes the
# naplayer of the character.
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

#Vo archery
    def cursor(naplayer = None):
        if naplayer:
            config.mouse = {'default' : [('images/cursor_' + naplayer + '.png', 0, 0)]}
        else:
            config.mouse = None
    Cursor = renpy.curry(cursor)

########### Backgrounds
image bedroom = "images/bedroom.png"
image outsideapart = "images/outsideapartment.png"
image gaplayerover = "images/gamerover.jpg"
image office = "images/office.jpg"
image mikoRoom = "images/mikoRoom.jpg"
image stabbed = "images/stabbed.png"
image bedroomDay = "images/bedroomDay.png"
image outside = "images/outside.jpg"
image scenee = "images/sceneee.png" 
image maindoor = "images/maindoor.png"
image map = "images/CityMap.jpg"

#### VoHongVy Changes 5/2/2024 added by N.
image parkscene:
    "images/parkscene.png"
    size(1920, 1080)
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
image phone:
    "images/phone.png"
    size(1920,1080)

image office2:
    "images/office2.jpg"
    size(1920,1080)

########## Characters
image miko Happy ="images/mikoHappy.png"
image miko Sad = "images/mikoSad.png"
image miko Creepy = "images/mikoCreepy.png"

###Soplayer add by Vo May 7
image miko Laugh = "images/mikolaugh.png"
image miko Normal = "images/mikonormal.png"
### VoHongVy Changes 5/2/2024
image player Move: 
    "images/playerMove.png" 
    xalign 0.8 yalign 0.5 
    size (1000, 1000)

image player Annoy: 
    "images/playerAnnoyed.png" 
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
image player Ok2: 
    "images/playerok2.png" 
    xalign 1.0 yalign 0.5 
    size (1000, 1000)
image player No: 
    "images/playersaidno.png" 
    xalign 1.0 yalign 0.5 
    size (1000, 1000)
#### Vo archery minigaplayer at the park scene
image fon_les: 
    "images/parkdark.jpg"
    size(1920, 1080)

###### VoHongVy Changes 5/2/204 added by N.

### Added Lucy, she is the players boss at work
image lucy Happy = "images/lucy happy.png"

define miko = Character("Miko", color="#FF0000")
define player = Character("player", color="#0000FF")
define e = Character('Virus', color="#c8ffc8")
define lucy = Character("Lucy", color="#00ca28")

label start:
    voice "audio/main-story1.mp3"
    "Our main character, who is moving to the new apartplayernt, is excited to start fresh and make new neighbor friends. 
    A mysterious story ensues when strange occurrences begin happening in the building,leading our characters to uncover 
    dark secrets hidden within the walls of their new hoplayer. Since his hoplayer moving made him so tired, he felt sleepy and 
    woke up to hear a mysterious laugh and soplayerone knocking his door, sparking a sense of unease within him."

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
        "YAYYY, Let's move to new hoplayer. I'm so excited...":
            player "Go ! Go !"
    show player Ok 
    player "Finally Done"
    show player Move
    pause 0.5
    scene scenee
    show player Relax

    player "AHH! Today such an busy day !!!"
    player "Should I take a nap?"
    menu: 
        "So lazy.. Maybe gonna take a nap then":
            show player Nap
            player "Z Z Z Z"
            player "Nap tiplayer is the best"
        "No, Maybe go to make soplayer drink in the kitchen":
            jump kitchen

######Drinking Scene
label kitchen:
    scene kitchen
    "player" "What should I drink tonight?"
    menu: 
        "Making Orange juice sounds healthy":
            "player" "......"
            show player Make
            "player" "Waiting for orange juice"
            "player" "Yay"
            show player OJ
            "player" "Hmmm.. Delicicous"
            "player" "Perfect"
        "Cocktail or Red Wine, etc. Sounds not bad":
            scene wine 
            pause 1.0
            scene kitchen
            "player" "Ahhhhhhh Shit...."
            "player" "I should not drink this"
            show player Shock
            pause 1.0

### Soplayer adjustation by Vo May 3rd

label Scene1:
    scene maindoor
    play sound "audio/knock.mp3" volume 0.8
    play music "audio/spooky.mp3" volume 0.5
    "???" "*Knock Knock*"
    
    player "Who's knocking on my door so late?"
    player "What tiplayer is it right now?"
    player "12am!? Who's up so late at this hour?"
    player "Should I pick it up?  It might that manga I ordered earlier this week."
    player "Wait.. No way they would coplayer this late?"
    play sound "audio/knock.mp3" volume 0.8

    menu: 
        "Coplayer and open the door to check.":
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
    miko "It's a bit late right now, and all my stuff is outside, I was wondering if you could help player move soplayer boxes inside?"
    miko "You're the only one that openened the door, I knocked on soplayer other doors earlier, but it seeplayerd like everyone else seeplayerd asleep."

    player "{i}I was asleep too.. {/i} "
    player "Uhhh..."

    show miko Sad
    miko "Pleaseeee!! It will only take like 5 mins!!"
    player "{i} Should I help her?  She is a stranger though..."
    player "{i} Mom always told player not trust strangers.."
    player "{i} Although, She is kind of cute."

menu:

    "I guess I'll help her":
        jump mikoRoom

    "Nah... I am going to bed.":
        jump stabbed

label mikoRoom:
    scene mikoRoom
    show miko Happy

    miko "Welcoplayer to my room"
    jump Scene2

label stabbed:
    scene stabbed
    "You've been stabbed..."
    miko "Maybe you should have caplayer to my room..."
    scene stabbed

    jump death

label death:
        scene gaplayerover
        "Gaplayer Over"
        menu:
            "Return to Tile Screen":
                return 
        
label Scene2:
    scene bedroom
    player "I'm finally back in my room."
    player "I am wondering if Miko is doing feeling at hoplayer"
    player "I am feeling a bit tired now, I guess it's tiplayer to sleep"
    
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
        "Spend tiplayer with Miko":
            jump mikoTiplayer
        "Touch soplayer grass":
            jump outside
        "Sleep the whole day":
            jump Scene4

        "Check out the map":
            call screen MapUI

####work scene
label work:
    scene  office
    player "*** Hours later ***"
    show player OJ at center
    player "Man.. 5 p.m can't coplayer soon enough"
    show miko Happy at right with moveinright 
    show player Shock at center with dissolve
    miko "Heyyyy neighbor!!! I though that was you!!"
    show player Annoy at center with dissolve
    player "Hey Miko, what are you doing here?"
    miko  "{i} Ohhh, I'm here for an interview."
    player "Oh, I see. Good luck with that."
    miko "Thank you, It was nice running into you. Bye"
    hide miko Happy with dissolve
    show player Ok with dissolve
    player "{i} That's strange, I didn't know Lucy was hiring..."

label work2:
    scene office2
    show player Ok at center with moveinleft
    show lucy Happy at right
    player "Hey Lucy, how did Miko do on her interview?"
    lucy "Who?"
    player "Miko...my neighbor?"
    lucy "I have never heard of her. I'm sorry, I don't know what you're talking about."
    player "Oh, thats strange. I ran into her in the office and she said she was here for interview."
    lucy " I don't know what to tell you, we're not even hiring right now"
    lucy " Anyways, it's a good thing you're here. I need you to stay in late tonight"
    show player Annoy at center with dissolve
    player "What?... {i} Ok."

    jump Scene2
####miko scene

label mikoTiplayer:
    scene mikoRoom
    show miko Happy
    miko "Ah hello player~ I've been waiting for you"
    scene mikoRoom

    jump Scene2
####touching soplayer grass

label outside: 
    scene outside
    player "Wow it sure it nice outside today"

    jump Scene2

#### Scene leading to Good or Bad Ending
label Scene4:
    scene bedroom
    show player Relax at center 
    play sound "audio/muffled_arguing.mp3"
    "???" "*ARGUING*"
    show player Ok2 at center
    player "Huh?... What is that noise?"

    player "Is that coming from Mikos room?"
    player "...."
    player "Who is she arguing with?"
    play sound "audio/wall_impact.mp3"

    show player Annoy with vpunch
    player "What was that?!" 
    player "I better go check on her."
    hide player Annoy with moveinright
    
    scene outsideapart
    show player Ok2 with moveinleft
    player "Miko?"
    #play sound "audio/muffled_music.mp3"
    #player "Thats weird... I can hear music coming from her room."
    player "I better hurry."
    hide player Ok2 with dissolve

label scene3:
    scene lock_plate
    show lock_cylinder
    player "I need to find a way to open this door."
    call screen Lockpicking_mini_gaplayer

screen Lockpicking_mini_gaplayer:
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
    # Set varaiables for tiplayerr
    $ tiplayer = 90
    $ tiplayerr_range = 90

    # Set a boolean value to keep track of gaplayer status
    $ gaplayer_over = False

    #Dictionary to keep track if items has been clicked
    default clickable_items = {1: True, 2: True, 3: True, 4: True}

    scene bg_room
    show player Ok at center with easeinleft
    play sound "audio/shower.mp3" 
    player "*Whispers*  Miko?? {i} She's showering..."
    player "Something feels off..."
    call screen items_screen

screen items_screen:
    modal True # Prevents user from leaving screen until minigaplayer is done
    zorder 1 # Ensures screen is on top of everything else

   
    # IF tiplayer is less than 0 and gaplayer_over is True, jump to Fail label
    timer 0.01 repeat True action If(tiplayer > 0 and not gaplayer_over, true = SetVariable('tiplayer', tiplayer - 0.1),
    false = [Hide('countdown'), Jump("Fail")])
   
    bar value tiplayer range tiplayerr_range xalign 0.5 yalign 0.1 xmaximum 300 at alpha_disolve

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
            xpos 0.3
            ypos 0.8
            idle "bg_knife"
            action [SetDict(clickable_items, 4, False), Notify("A bloody kitchen knife..."),
                SetVariable('gaplayer_over', True), Jump("Success")]

# Adds a fade effect to the tiplayerr bar
transform alpha_disolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0.0

label scene5:
    scene bedroom
    show player Suprised at center with moveinleft
    player "Omg...What do I do..."
    player "{i} Do I call the police or..."
    play audio "audio/knocking.mp3"
    "* Knocking on the door *"
    show player Annoy at center 
    player " ...... "
    play audio "audio/creak.mp3"


label scene6:
    scene outsideapart
    show player Ok at left with moveinleft
    show miko Creepy at center
    player "Heyyyy Miko... What's going on?"
    miko "Hey, I just wanted to apoligize about the noise earlier."
    miko " I was trying smash a spider and I ended up knocking over soplayer stuff."
    miko "I'm sorry if I woke you up."

    menu: 
        "Oh, no worries, I didn't even hear anything.":
            miko "Oh, okay. Well, I'm gonna head out then, goodnight!"
            player "Goodnight Miko."
            play sound "audio/sharp.mp3"
            scene black with hpunch
            call screen Death
        "Actually, I heard everything and I found a bloody knife in your room.":
            player "I'm calling the police."
            miko "Wait, what? No, please don't call the police."
            miko "I can explain everything."
            player "Explain what? Why is there a bloody knife in your room?"
            miko "You don't understand, I'm not a bad person."
            miko "Please, let me explain."
            player "Fine, explain."
            jump scene7

# Ok this is trash I know but you get it
label scene7:
    scene bedroom
    show miko Creepy at center
    miko "I'm not a bad person, I swear."
    menu: 
        "I don't believe you, I'm calling the police.":
            miko "You leave me no choice then."
            play sound "audio/sharp.mp3"
            scene black with hpunch
            call screen Death
        "I believe you":
            miko "Thank you, I knew you would understand."
            jump ending

screen goodEnding:  
        
    vbox align (.5,.5):
        text "The player and Miko both lived out their lives in the city, murdering as they pleased." color "#ff0000"
        text "THE END" color "#ff0000"
    
    textbutton "QUIT" action Return()


# MAP Screen
screen MapUI:
    add  "CityMap2.jpg"

    imagebutton:
        focus_mask True
        idle "Movie.png"
        hover "Movie_hover.png"
        action Jump("scene8")
    imagebutton:
        focus_mask True
        idle "Hoplayer.png"
        hover "Hoplayer_hover.png"
        action Jump("Scene2")
    imagebutton:
        focus_mask True
        idle "Work.png"
        hover "Work_hover.png"
        action Jump("work")
    imagebutton:
        focus_mask True
        idle "Park.png"
        hover "Park_hover.png"
        action Jump("scene10")


label scene10:
    scene phone
    show miko Happy 
    miko "Do you wanna hang out to theplayer park with player?"
    show player Suprised
    menu: 
        "Yes, It'll be fun":
            show miko Laugh 
            miko "okay, let's go"
        "No, I'm kinda lazy":
            show player No
            player "No, thank you"
            show miko Sad
            scene outsideapart
            "Then, you were still dragged to the park by the miko"
    jump ParkTheplayerScene

label ParkTheplayerScene:
    scene parkscene
    show miko Normal
    miko "Let's play a mini gaplayer"
    show miko Happy
    miko "I want to play archery gaplayer over there"
    show player Ok2
    player "Okay"
    jump Archery

label Archery:
    play music ("main-playernu-theplayer.mp3")
    scene fon_les
    show miko Happy
    miko "Help player playyy"
    call begin_hunt from _call_begin_hunt

    if targets_hit == 0: # on 0 hits
        $ cursor() #reset broom
        scene fon_les with dissolve
        show miko Happy
        miko "Let's try again together"
        scene fon_les with dissolve
        show miko Happy
        
    if targets_hit > 0: # on more than 0 hits
        $ cursor() #resets the broom
        e "[targets_hit] tiplayers hit. "
        scene fon_les with dissolve
        show miko Laugh
        miko "Wonderful, Thank you!"   
 
    jump Scene2

label ending: 
    scene black
    call screen goodEnding
 