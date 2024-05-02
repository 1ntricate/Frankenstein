# The script of the game goes in this file.

######### Backgrounds 
image bedroom = "bedroom.png"
image outsideApartment = "outsideapartment.png"
image mikoRoom = "bg_room.png"
image CityMap = "CityMap.jpg"


#### Item imgage for lockpicking mini game
image lockPick = "lock_pick.png"


######### Characters
image miko Happy = "mikoHappy.png"
image miko Sad = "mikoSad.png"
#image miko Angry = "miko angry.png"
image miko Shocked = "miko shocked.png"
image miko Normal = "miko normal.png"
image miko Laugh = "miko laugh.png"

image lucy Normal = "lucy happy.png"
image lucy Shocked = "lucy mad.png"

define me = Character("lucy", color = "#2025b6")
define miko = Character("miko", colors = "#ff0000")

label start:
    scene bedroom
    play sound "audio/muffled_arguing.mp3"
    "???" "*ARGUING*"
    me "Huh?... What is that noise?"
    show lucy Normal with moveinbottom

    me "Is that coming from Mikos room?"
    me "...."
    me "Who is she arguing with?"
    play sound "audio/wall_impact.mp3"

    show lucy Shocked with vpunch
    me "What was that?!" 
    me "I better go check on her."
    hide lucy with moveinright
    
    scene outsideApartment
    show lucy Normal with moveinleft
    me "Miko?"
    #play sound "audio/muffled_music.mp3"
    #me "Thats weird... I can hear music coming from her room."
    me "I better hurry."
    hide lucy with dissolve

label scene2:
    # Decaare variable for timer
    $ time = 120
    $ timer_range = 120
    scene black_door
    play sound "audio/knocking.mp3"
    me "* Knocks on door *"
    me "Miko? Are you in there?"
    "* No response *"
    me "{i} I need to get in there." 
    me "{i} But how?"

####### Python for LockPick mini-game logic ####
init python:
    def check_drop(drags, drop):
        # Access the dragged and dropped objects directly
        dragged_piece = drags[0]
        dropped_on = drop

        if dragged_piece.drag_name == dropped_on.drag_name:
            renpy.jump("scene4")
        else:
            renpy.notify("Try again!")
        
##########################################

label scene3:
    scene lock_plate
    show lock_cylinder
    me "I need to find a way to open this door."
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

label scene9:
    "Work picked"

label scene10:
    "Park picked"

label scene11:
    "Home Picked"





    









    



    
