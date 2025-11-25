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

#NAMEBOX
