label Fail:
    show lucy mad
    show miko normal at left with moveinleft
    miko "You're not supposed to be in here..."
    miko "I'm sorry, but I can't let you leave."
    play sound "audio/sharp.mp3"
    scene black with hpunch
    call screen Death


screen Death:
    vbox align (.5,.5):
        text "YOU DIED" color "#ff0000"

    textbutton "QUIT" action Return() 
