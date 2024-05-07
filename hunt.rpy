image target:
    "hunt/archery1.png"
    zoom 0.5
 
transform moving_target: #target
    ypos 500 #position at
    linear 3.0 xpos 1000 #distance and speed at which the target will move
    xpos -200 #begin behind the frame
    size(300,300)
    repeat
 
label begin_hunt:
    
    $ shots_fired = 0
    $ targets_hit = 0
    call hunting from _call_hunting
    return
    
label hunting:
    $ cursor("metl") #call broom
    scene fon_les #game background
    show target at moving_target
    $ position = At(ImageReference("target"), moving_target)
    show expression position
 
    $ ui.imagebutton("hunt/target.png", "hunt/target.png", clicked = ui.returns("fired"), xpos= 200, ypos = 500) #position of aim
    $ fired_gun = ui.interact()
    
    show expression position #where the hit will be counted.
    if position.xpos > 500: #Acts from
        if position.xpos < 700: #At this coordinate
            play sound ("click.wav") #hitting sound
            with vpunch
            "You're missed. "
            $ shots_fired = shots_fired + 1
            $ targets_hit = targets_hit + 1
            if shots_fired >= 3:
                return
            call hunting from _call_hunting_1
   
    play sound ("click.wav")
    with vpunch
    "You Got IT. "
    $ shots_fired = shots_fired + 1
    if shots_fired >= 3:
        return
    
    call hunting from _call_hunting_2
    
    return