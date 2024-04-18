# The script of the game goes in this file.

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
            #hover "bg_darkteddy_hover"
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
            action [SetDict(clickable_items, 4, False), Notify("A kitchen knife? I have never seen Abby cook before..."),
            SetVariable('game_over', True), Jump("Success")]

# Adds a fade effect to the timer bar
transform alpha_disolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0.0


label start:

    # This is the first label that is called when the game starts.
    scene bg_darkhall
    show lucy happy


    "Investigate the room to find the source of the curse!"

    # Jumps to label where minigame is called
    call Scavenger_hunt

    return

label Scavenger_hunt:

    # Set varaiables for timer
    $ time = 120
    $ timer_range = 120

    # Set a boolean value to keep track of game status
    $ game_over = False

    #Dictionary to keep track if items has been clicked
    default clickable_items = {1: True, 2: True, 3: True, 4: True}

    scene bg_room
    show lucy happy

    "Invesitage the room!"

    # Shows minigame screen
    call screen items_screen

# Yet to be decided what happens if the player succeeds
label Success:


    scene bg_room
    show lucy mad
    show model at left

# Yet to be decided what happens if the player fails
label Fail:

    show lucy mad
    #show bg_ghost_hover at left
    "Time is up"
    return