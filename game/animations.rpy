#GUI Animations!

# This file contains definitions for animations used in the GUI.

################################################

#SIDE MENU

transform side_enter:
    xoffset 80
    alpha 0
    easein 0.37 xoffset 0 alpha 1

transform side:
    on hover:
        easein 0.25 xoffset -17
    on idle:
        easein 0.30 xoffset 0

#QUICK MENU

transform enter_bottom:
    alpha 0.0
    easein 0.50 alpha 1.0

transform hover_qm:
    on hover:
        easein 0.25 yoffset -17
    on idle:
        easein 0.50 yoffset 0

#Dialogue Box

transform saybox:
    yoffset 20
    alpha 0
    easein 0.41 yoffset 0 alpha 1

#Confirm Box
transform confirm:
    yoffset -50
    alpha 0
    easein 0.37 yoffset 0 alpha 1

transform l_enter:
    xoffset -80
    alpha 0
    easein 0.37 xoffset 0 alpha 1
    on hover:
        easein 0.25 yoffset -17
    on idle:
        easein 0.50 yoffset 0

transform r_enter:
    xoffset 80
    alpha 0
    easein 0.37 xoffset 0 alpha 1
    on hover:
        easein 0.25 yoffset -17
    on idle:
        easein 0.50 yoffset 0

transform zoom:
    on hover:
        easein 0.15 zoom 1.01
    on idle:
        easein 0.30 zoom 1.0

#Main Menu Buttons

transform mm_enter:
    yoffset 80
    alpha 0
    easein 0.37 yoffset 0 alpha 1

transform hover_mm:
    on hover:
        easein 0.15 yoffset -10
    on idle:
        easein 0.50 yoffset 0

#Choice Buttons
transform choice_hover:
    on hover:
        easein 0.15 yoffset -10
    on idle:
        easein 0.50 yoffset 0
transform choice_enter:
    yoffset 50
    alpha 0
    zoom 0.95
    easein 0.37 yoffset 0 alpha 1 zoom 1.0

