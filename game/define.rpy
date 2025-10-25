transform midleft:
    xalign 0.25
transform left:
    xalign 0.03
transform midright:
    xalign 0.75
transform blink:
    linear 1.0 alpha 0.0
    linear 1.0 alpha 1.0
    repeat
transform shakey:
    ease .06 xoffset 24
    ease .06 xoffset -24
    ease .05 xoffset 20
    ease .05 xoffset -20
    ease .04 xoffset 16
    ease .04 xoffset -16
    ease .03 xoffset 12
    ease .03 xoffset -12
    ease .02 xoffset 8
    ease .02 xoffset -8
    ease .01 xoffset 4
    ease .01 xoffset -4
    ease .01 xoffset 0
    pass

# Second Character step
transform step_1b:
    anchor (0.5, 0.0)
    xpos 0.4 ypos 0.02
    zoom 0.9

transform step_2b:
    anchor (0.5, 0.1)
    zoom 1.2
    ease 0.4 ypos 0.05
    ease 0.4 ypos 0.07

transform step_3b:
    anchor (0.5, 0.15)
    zoom 1.5
    ease 0.4 ypos 0.10
    ease 0.4 ypos 0.12

transform step_4b:
    anchor (0.5, 0.2)
    zoom 2.0
    ease 0.4 ypos 0.17
    ease 0.4 ypos 0.19

image bayi= "baby.png"
image dance = "dance.png"
image sign = "sign.png"
image p_foreground = "Post_credit_foreground.png"
image nx = "Sprite/nexor.png"
image nx_sad = "Sprite/nexor_sad.png"
image nx_smi = "Sprite/nexor_smile.png"
image nxb = "Sprite/nexorbefore.png"
image nxb_ser = "Sprite/nexorbefore_serious.png"
image nxb_smi = "Sprite/nexorbefore_smile.png"
image nxb_play = "Sprite/nexorbefore_playful.png"

image who = "Sprite/who.png"
image who_smi = "Sprite/who_smile.png"
image who_smi_pc = "Sprite/who_ending_smile.png"
image who_th = "Sprite/who_thinking.png"
image who_th_pc = "Sprite/who_ending_thinking.png"

image sy = "Sprite/syntia.png"
image sy_emo = "Sprite/syntia_emotional.png"
image sy_emp = "Sprite/syntia_empty.png"
image sy_sad = "Sprite/syntia_sad.png"
image sy_smi = "Sprite/syntia_smile.png"
image sy_emo_pc = "Sprite/syntia_ending_emotional.png"
image sy_smi_pc = "Sprite/syntia_ending_smile.png"
image sy_bef = "Sprite/syntiabefore.png"
image sy_bef_smi = "Sprite/syntiabefore_smile.png"

# Right character (nxb_serious) - Weird stiff movements, offbeat tilts
transform awkward_dance_right:
    xoffset 0.75
    ypos -0.2
    xpos 0.4
    rotate 0
    parallel:
        ease 0.3 xoffset -5 rotate -3  # Slight left tilt
        ease 0.3 xoffset 5 rotate 3  # Slight right tilt
        ease 0.2 xoffset -7 rotate -5  # Overcorrects
        ease 0.2 xoffset 7 rotate 5
        ease 0.5 xoffset 0 rotate 0  # Awkward pause
        pause renpy.random.uniform(0.5, 1.5)  # Random freeze moment
        repeat

    parallel:
        ease 0.4 xoffset -4  # Small sway left
        ease 0.4 xoffset 4  # Small sway right
        ease 0.3 xoffset -6
        ease 0.3 xoffset 6
        pause renpy.random.uniform(0.4, 1.0)
        repeat

# Left character (sy_bef_smi) - Random movements, like they don't know what they're doing
transform awkward_dance_left:
    xoffset 0.2
    ypos -0.2
    xpos -0.2
    rotate 0
    parallel:
        ease 0.4 rotate 2 xoffset 4  # Small wiggle
        ease 0.4 rotate -2 xoffset -4
        ease 0.3 rotate 5 xoffset 6  # Overcorrects
        ease 0.3 rotate -5 xoffset -6
        ease 0.6 rotate 0 xoffset 0  # Hesitates awkwardly
        pause renpy.random.uniform(0.6, 1.2)  # Random stop moment
        repeat

    parallel:
        ease 0.5 xoffset -3  # Sway left
        ease 0.3 xoffset 3  # Sway right
        ease 0.4 xoffset -2
        ease 0.4 xoffset 2
        pause renpy.random.uniform(0.4, 1.0)
        repeat


image rain:
    "rain/rain1.png"
    0.2
    "rain/rain3.png"
    0.2
    "rain/rain2.png"
    0.2
    repeat

image mainmenu_flicker:
    "MAINMENUDIM.PNG"
    0.3  # Quick dim
    "MAINMENUBRIGHT.PNG"
    1.5  # Bright stays the longest
    "MAINMENUNORMAL.PNG"
    0.2
    "MAINMENUBRIGHT.PNG"
    1.2  # Bright again
    "MAINMENUDIM.PNG"
    0.1
    "MAINMENUBRIGHT.PNG"
    0.8  # Stays bright longer
    "MAINMENUNORMAL.PNG"
    0.3
    "MAINMENUBRIGHT.PNG"
    1.7  # Bright holds for dramatic effect
    "MAINMENUDIM.PNG"
    0.15
    "MAINMENUBRIGHT.PNG"
    1.4  # Final bright hold before restarting
    repeat

# Define transform for **parallax background shake** (more dramatic)
transform background_shake:
    xoffset 0
    yoffset 0
    ease 1.0 yoffset -8
    ease 1.0 yoffset 8
    ease 0.8 yoffset -6
    ease 0.8 yoffset 6
    ease 1.2 yoffset -10
    ease 1.2 yoffset 10
    repeat  # Background moves in **longer, deeper motions** for a parallax feel

# Define transform for **foreground crying shake** (subtle, soft trembling)
transform foreground_shake:
    xoffset 0
    yoffset 0
    ease 0.1 yoffset -4 xoffset -2  # Sharper movement, like a hiccup in breath
    ease 0.08 yoffset 3 xoffset 2
    ease 0.12 yoffset -6 xoffset -3  # More erratic shaking, gasping for air
    ease 0.1 yoffset 5 xoffset 3
    ease 0.07 yoffset -3 xoffset -1
    ease 0.09 yoffset 2 xoffset 1
    ease 0.15 yoffset -8 xoffset -4  # Heaviest sob moment
    ease 0.13 yoffset 6 xoffset 3
    ease 0.12 yoffset 0 xoffset 0
    repeat  # Keeps looping the intense sobbing effect

transform step_1:
    anchor (0.5, 0.0)  # Locks the sprite's TOP
    xpos 0.5 ypos 0.0  # Ensures the top of the sprite starts at the top
    zoom 1.0  # Default size

transform step_2:
    anchor (0.5, 0.1)
    zoom 1.3  # Zooms in closer
    ease 0.3 ypos 0.06  # Bobbing motion up
    ease 0.3 ypos 0.08  # Bobbing motion down

transform step_3:
    anchor (0.5, 0.15)
    zoom 1.6  # Closer view
    ease 0.3 ypos 0.13
    ease 0.3 ypos 0.15

transform step_4:
    anchor (0.5, 0.2)
    zoom 2.3
    ease 0.3 ypos 0.2
    ease 0.3 ypos 0.22


image BG = "BG.PNG"
image park = "park.jpg"

image CG1_norain = "CG1_norain.png"
image CG1 = "CG1.png"

image CG2 = "CG2.png"
image CG2_background = "CG2_background.png"
image CG2_background_blur = "CG2_background_blur.png"
image CG2_foreground = "CG2_foreground.png"
image CG2_foreground_2 = "CG2_foreground_2.png"
image CG2_foreground_blur = "CG2_foreground_blur.png"

image CG3 = "CG3.png"
image CG3_2 = "CG3_2.png"
image CG3_3 = "CG3_3.png"

image garage = "Garage.jpg"
image neon_sky = "neon_sky.jpg"
image flower = "flower.jpg"

image Post1 = "Post1.png"
image Post3 = "Post3.png"

image Choice_1 = "Choice_1.png"
image CG4 = "CG4.png"
