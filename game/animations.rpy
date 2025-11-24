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


