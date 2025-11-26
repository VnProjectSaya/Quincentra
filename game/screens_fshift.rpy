style sound_bar:
    xsize 455
    ysize 32
    left_bar "gui/gui_fshift/toggles/audio_fill.png"
    right_bar "gui/gui_fshift/toggles/audio_empty.png"
    #thumb "gui/custom_bar_thumb.png"
    bar_invert False

style text_bar:
    xsize 1142
    ysize 44
    left_bar "gui/gui_fshift/toggles/bar_fill.png"
    right_bar "gui/gui_fshift/toggles/bar_empty.png"
    #thumb "gui/custom_bar_thumb.png"
    bar_invert False




screen preferences():
    
    tag menu

    add "gui/gui_fshift/bg_options.png" fit "cover"

    use fshift_navigation_menu()

    text _("Options"):
        xoffset 1200 yoffset 60 size 60 

    text _("Display"):
        xoffset 280 yoffset 200 size 50 
    
    text _("Audio"):
        xoffset 280 yoffset 780 size 50 

    vbox:
        
        xoffset 330
        yoffset 300
        vbox:
            spacing 30
            box_wrap True
            hbox:
                if renpy.variant("pc") or renpy.variant("web"):

                
                    style_prefix "radio"
                    label _("Window Mode")
                    
                    hbox:
                        xoffset 85
                        yoffset 20
                        spacing 80

                        textbutton _("Window") action Preference("display", "window"):
                            text_size 30
                            xoffset 20
                            
                        textbutton _("Fullscreen") action Preference("display", "fullscreen"):
                            text_size 30
                            xoffset 20
            
            hbox:
                style_prefix "radio"
                label _("Skip Text")
                
                hbox:
                    xoffset 170
                    yoffset 25
                    spacing 55

                    textbutton _("Unseen Text") action Preference("skip", "toggle"):
                        text_size 30
                        xoffset 20
                    textbutton _("After Choices") action Preference("after choices", "toggle"):
                        text_size 30
                        xoffset 35
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle")):
                        text_size 30
                        xoffset 65
            hbox:

                xoffset 350
                yoffset -10

                #box_wrap True
                label _("Rollback Side")

                hbox:
                    xoffset 70
                    yoffset 5
                    spacing 40


                    style_prefix "radio"
                    
                    textbutton _("Disable") action Preference("rollback side", "disable")
                    textbutton _("Left") action Preference("rollback side", "left")
                    textbutton _("Right") action Preference("rollback side", "right")
                        #xoffset 40

            vbox:
                yoffset -75
                style_prefix "slider"

                label _("Text Speed")

                bar:
                    style "text_bar"
                    value Preference("text speed")

                label _("Auto-Forward Time")

                bar:
                    style "text_bar"
                    value Preference("auto-forward time")
            

        
            ## Additional vboxes of type "radio_pref" or "check_pref" can be
            ## added here, to add additional creator-defined preferences.

        #null height (4 * gui.pref_spacing)

    hbox:
        style_prefix "slider"
        box_wrap True

        xalign 0.6
        yalign 0.9

        xoffset 400
        yoffset -55

        vbox:
            spacing 10
            label _("Music")
            label _("Sound")
            label _("Voice")

        

        vbox:
            spacing 40
            yoffset 22
            xoffset -500


            if config.has_music:
                
                
                bar:
                    style "sound_bar"
                    value Preference("music volume")


            if config.has_sound:

                

                bar:
                    style "sound_bar"
                    value Preference("sound volume")

                    #if config.sample_sound:
                    #    textbutton _("Test") action Play("sound", config.sample_sound)


            if config.has_voice:
                

                bar:
                    style "sound_bar"
                    value Preference("voice volume")

                    #if config.sample_voice:
                    #    textbutton _("Test") action Play("voice", config.sample_voice)

"""
            if config.has_music or config.has_sound or config.has_voice:
                null height gui.pref_spacing

                textbutton _("Mute All"):
                    action Preference("all mute", "toggle")
                    style "mute_all_button"

"""
    
################################################

screen file_slots(title):

    
    
    default page_name_value = FilePageNameInputValue(pattern=_("Page {} of 5"))
        
        
    use save_preview()
    add "gui/gui_fshift/bg_slots.png" fit "cover"

    text (title):
        xoffset 1170 yoffset 70 size 60 
    
    #text ("Preview"):
    #    xoffset 1110 yoffset 280 size 60 

    use fshift_navigation_menu()
    use details_preview()

    #use game_menu(title):

    fixed:

        ## This ensures the input will get the enter event before any of the
        ## buttons do.
        #order_reverse True

        ## The page name, which can be edited by clicking on a button.
        text "[page_name_value.get_text()]":
            xalign 0.2
            yalign 0.19
            style "page_label_text"


        ## The grid of file slots.
        vbox:
            #style_prefix "slot"

            xalign 0.22
            yalign 0.75

            spacing -80

            for i in range(3):
                vbox at confirm:
                    spacing 8
                    
                    $ slot = i + 1

                    imagebutton:
                        idle "gui/gui_fshift/save-load/slot_idle.png"
                        hover "gui/gui_fshift/save-load/slot_hover.png"
                        hover_sound "gui/gui_fshift/sfx/data_click.mp3"
                        activate_sound "gui/gui_fshift/sfx/click.mp3"
                        #selected_idle "gui/gui_fshift/save-load/slot_selected.png"


                        hovered [
                            SetVariable("persistent._preview_slot", slot),
                            Show("save_preview", transition= None)
                        ]
                        unhovered SetVariable("persistent._preview_slot", None)
                        at side
                        action FileAction(slot)

                        
                        

                        #key "save_delete" action FileDelete(slot)
                    vbox:
                            yoffset -170
                            xoffset 250
                            text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                                style "slot_time_text"
                                ypos 30

                            text FileSaveName(slot):
                                style "slot_name_text"
        ## Buttons to access other pages.
        
        hbox:
            style_prefix "page"

            

            xalign 0.5
            yalign 1.0

            spacing gui.page_spacing

            $page = FileCurrentPage()
            

            #textbutton _("<") action FilePagePrevious()

            #if config.has_autosave:
            #    textbutton _("{#auto_page}A") action FilePage("auto")

            #if config.has_quicksave:
            #    textbutton _("{#quick_page}Q") action FilePage("quick")
            hbox:
                xoffset -300
                yoffset -100
                imagebutton:
                    at zoom
                    idle "gui/gui_fshift/button/prev_page.png"
                    action FilePagePrevious(quick = False)
                ## range(1, 10) gives the numbers from 1 to 9.
                textbutton ("[page]/5") action FilePage(page) 

                
                imagebutton:
                    at zoom
                    idle "gui/gui_fshift/button/next_page.png"
                    action FilePageNext(5, quick = False)
    
################################################
##SCREEN OF PREVIEW
screen save_preview():
    zorder -1
    
    #tag menu

    

    #use fshift_navigation_menu()

    frame:
        xpos 1050
        ypos 400

        background None
        if persistent._preview_slot == None:
            add "gui/gui_fshift/save-load/preview_empty.png" 
        else:
            add FileScreenshot(persistent._preview_slot):
                zoom 1.5
                    
screen details_preview():                
    vbox:
        at side_enter
        xpos 1100
        ypos 400

        yoffset 300
        xoffset 50
        
        

        text _("Slot: [persistent._preview_slot]"):
            size 40

        text FileTime(persistent._preview_slot, format=_("%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
            xmaximum 400
            size 30

        text FileSaveName(persistent._preview_slot):
            size 30

                


###########
screen fshift_navigation_menu():

    # This tag ensures only one instance of this screen is shown at a time.
    #style_prefix "game_menu"
    #tag menu

    # A frame to contain the buttons, centered on the screen.

    imagebutton at zoom:
        idle "gui/gui_fshift/button/back_idle.png"
        hover "gui/gui_fshift/button/back_hover.png"
        hover_sound "gui/gui_fshift/sfx/hover.mp3"
        activate_sound "gui/gui_fshift/sfx/click.mp3"
        xalign 0.86
        yalign 0.97
        action Return()
        
    
    # A vbox organizes elements vertically with spacing.
    vbox:

        xalign 1.010
        yalign 0.35
        spacing 15
        at side_enter
        # Each textbutton defines a menu option.
        # 'action' specifies what happens when the button is clicked.
        

        if main_menu:
            imagebutton:
                idle "gui/gui_fshift/button/side_menu/start_idle.png"
                hover "gui/gui_fshift/button/side_menu/start_idle.png"
                at side
                action Start()
                hover_sound "gui/gui_fshift/sfx/hover.mp3"
                activate_sound "gui/gui_fshift/sfx/click.mp3"
        else:
            imagebutton:
                idle "gui/gui_fshift/button/side_menu/mainmenu_idle.png"
                hover "gui/gui_fshift/button/side_menu/mainmenu_idle.png"
                at side
                action MainMenu(confirm=True)
                hover_sound "gui/gui_fshift/sfx/hover.mp3"
                activate_sound "gui/gui_fshift/sfx/click.mp3"

            imagebutton:
                idle "gui/gui_fshift/button/side_menu/save_idle.png"
                hover "gui/gui_fshift/button/side_menu/save_idle.png"
                at side
                action ShowMenu("save")
                hover_sound "gui/gui_fshift/sfx/hover.mp3"
                activate_sound "gui/gui_fshift/sfx/click.mp3"

        imagebutton:
            idle "gui/gui_fshift/button/side_menu/history_idle.png"
            hover "gui/gui_fshift/button/side_menu/history_idle.png"
            at side
            action ShowMenu("history")
            hover_sound "gui/gui_fshift/sfx/hover.mp3"
            activate_sound "gui/gui_fshift/sfx/click.mp3"

        

        imagebutton:
            idle "gui/gui_fshift/button/side_menu/load_idle.png"
            hover "gui/gui_fshift/button/side_menu/load_idle.png"
            at side
            action ShowMenu("load")
            hover_sound "gui/gui_fshift/sfx/hover.mp3"
            activate_sound "gui/gui_fshift/sfx/click.mp3"

        imagebutton:
            idle "gui/gui_fshift/button/side_menu/options_idle.png"
            hover "gui/gui_fshift/button/side_menu/options_idle.png"
            at side
            action ShowMenu("preferences")
            hover_sound "gui/gui_fshift/sfx/hover.mp3"
            activate_sound "gui/gui_fshift/sfx/click.mp3"


