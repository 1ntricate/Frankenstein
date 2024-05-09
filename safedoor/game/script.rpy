init python:
    import math
    def dial_events(event,x,y,st): 
        global dial_rotate
        global old_mousepos
        global old_degrees
        global degrees
        global dial_start_rotate
        global dial_text
        global previous_dial_text
        if event.type == renpy.pygame_sdl2.MOUSEBUTTONDOWN:
            if event.button == 1:
                if dial_start_rotate:
                    if dial_sprite.x <= x <= dial_sprite.x + dial_size[0] + dial_offset and dial_sprite.y <= y <= dial_sprite.y + dial_size[1] + dial_offset:
                        dial_rotate = True
                        old_mousepos = (x, y)
                        angle_radians = math.atan2((dial_sprite.y + dial_size[1] - dial_offset /2) - y, (dial_sprite.x + dial_size[0] - dial_offset/2)-x)
                        old_degrees = math.degrees(angle_radians) % 360
                else:
                    if dial_sprite.x <= x <= dial_sprite.x + dial_size[0] and dial_sprite.y <= y <= dial_sprite.y + dial_size[1] :
                        dial_rotate = True
                        old_mousepos = (x, y)
                        angle_radians = math.atan2((dial_sprite.y + dial_size[1] /2) - y, (dial_sprite.x + dial_size[0]/2)-x)
                        old_degrees = math.degrees(angle_radians) % 360
                        
        elif event.type == renpy.pygame_sdl2.MOUSEBUTTONUP:
            if event.button == 1:
                dial_rotate = False
        elif event.type == renpy.pygame_sdl2.MOUSEMOTION:
            if dial_rotate:
                angle_radians = math.atan2((dial_sprite.y +dial_size[1]/2) -y, (dial_sprite.x +dial_size[0]/2)-x)
                degrees = math.degrees(angle_radians)%360
                rotate_amount = math.hypot(x - old_mousepos[0], y - old_mousepos[1])/5
                if degrees > old_degrees:
                    dial_sprite.rotate_amount += rotate_amount
                elif degrees < old_degrees:
                    dial_sprite.rotate_amount -= rotate_amount
                
                t = Transform(child = dial_image, zoom = 0.5)
                t.rotate = 3.6 * round(dial_sprite.rotate_amount/3.6)
                if int(t.rotate / 3.6) % 100 == 0 and int(t.rotate / 3.6) != 0:
                    dial_number = 0
                    dial_sprite.rotate_amount = 0.0
                else: 
                    dial_number = int(t.rotate / 3.6)

                if dial_number > 0:
                    dial_text = 100 - dial_number
                elif dial_number < 0:
                    dial_text = abs(dial_number)
                else:
                    dial_text = dial_number

                if dial_text != previous_dial_text:
                    renpy.music.play("audio/dial.ogg", "sound", relative_volume = 0.3)
                previoud_dial_text = dial_text

                t.subpixel = True
                dial_start_rotate = True
                dial_sprite.set_child(t)
                dial_sprite.x = config.screen_width / 2 - dial_size[0] / 2 - dial_offset
                dial_sprite.y = config.screen_height / 2 - dial_size[1] / 2 - dial_offset
                old_degrees = math.degrees(angle_radians) % 360
                old_mousepos = (x,y)
                dial_sprite_manager.redraw(0)
                renpy.restart_interaction()

screen scene_1:
    image "images/scene-1-background.png" at size
    imagebutton auto "images/scene-1-safe-door-%s.png" focus_mask True action [Show("safe_puzzle", Fade(1,1,1)), Hide("scene_1")] at size2

screen safe_puzzle:
    image "images/safe-closeup-background.png" at size
    image "images/dial-shadow.png" align(0.48, 0.5) alpha 0.3 at half_size
    image "images/dial-backing.png" align(0.5,0.5) at half_size
    add dial_sprite_manager
    imagebutton auto "images/dial-reset-button-%s.png" align(0.5, 0.18) at half_size
    image "images/dial-text-background.png" align(0.5, 0.05) at text_size
    imagebutton auto "images/back-button-%s.png" align(0.95, 0.95) action [Show("scene_1", Fade(1,1,1)), Hide("safe_puzzle")] at half_size
    text "[dial_text]" color "#d71399" align(0.5, 0.23) text_align 0.3

transform size:
    size(1920,1080)

transform size2:
    size(410, 810)
    xalign 0.5
    yalign 0.5

transform half_size: 
    zoom 0.5
transform text_size:
    size(400,400)
label start:
    $dial_image = "images/dial.png"
    $dial_size = (660/2, 660/2)
    $t = Transform(child = dial_image, zoom = 0.5)
    $dial_sprite_manager = SpriteManager(event = dial_events)
    $dial_sprite = dial_sprite_manager.create(t)
    $dial_sprite.x = config.screen_width / 2 - dial_size[0] / 2
    $dial_sprite.y = config.screen_height / 2 - dial_size[1] / 2
    $dial_rotate = False
    $dial_sprite.rotate_amount = 0
    $dial_offset = 68.2
    $dial_start_rotate = False
    $dial_number = 0
    $dial_text = 0
    $previous_dial_text = 0

    #old
    $old_mousepos = (0.0, 0.0)
    $degrees = 0
    $old_degrees = 0

    call screen scene_1
    return

