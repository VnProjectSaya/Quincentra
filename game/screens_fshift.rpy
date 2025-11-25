"""
init -2 python:
    style.fshift_slider = Style(style.slider)
    
    style.fshift_slider.left_bar   = "gui/fshift/bar_fill.png"   # la parte que se llena (purple)
    style.fshift_slider.right_bar  = "gui/fshift/bar_empty.png"  # la parte vacía
    style.fshift_slider.xmaximum   = 600                         # ancho real de tus imágenes
    style.fshift_slider.ymaximum   = 54                          # alto real de tus imágenes
    style.fshift_slider.thumb      = None                        # sin thumb
    style.fshift_slider.thumb_offset = 0

""" 


screen preferences():
    
    tag menu

    add "gui/gui_fshift/bg_options.png" fit "cover"

    use fshift_navigation_menu()

    text _("Options"):
        xoffset 1200 yoffset 60 size 60 bold True

    text _("Display"):
        xoffset 280 yoffset 200 size 50 bold True
    
    text _("Audio"):
        xoffset 280 yoffset 770 size 50 bold True

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
                        xoffset 150
                        yoffset 10
                        spacing 80

                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")
            
            hbox:
                style_prefix "check"
                label _("Skip Text")
                
                hbox:
                    xoffset 200
                    yoffset 20
                    spacing 55

                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

            hbox:

                xoffset 350
                yoffset 0

                #box_wrap True
                label _("Rollback Side")

                hbox:
                    xoffset 100
                    #yoffset 20
                    spacing 60


                    style_prefix "radio"
                    
                    textbutton _("Disable") action Preference("rollback side", "disable")
                    textbutton _("Left") action Preference("rollback side", "left")
                    textbutton _("Right") action Preference("rollback side", "right"):
                        xoffset 40

            vbox:
                yoffset -32
                style_prefix "slider"

                label _("Text Speed")

                bar value Preference("text speed")

                label _("Auto-Forward Time")

                bar value Preference("auto-forward time")
            

        
            ## Additional vboxes of type "radio_pref" or "check_pref" can be
            ## added here, to add additional creator-defined preferences.

        #null height (4 * gui.pref_spacing)

        hbox:
            style_prefix "slider"
            box_wrap True

            xoffset 400
            yoffset -25

            vbox:
                spacing 17
                label _("Music")
                label _("Sound")
                label _("Voice")

            

            vbox:
                spacing 40
                yoffset 18
                xoffset -500


                if config.has_music:
                    

                    hbox:
                        bar value Preference("music volume")

                if config.has_sound:

                    

                    hbox:
                        bar value Preference("sound volume")

                        if config.sample_sound:
                            textbutton _("Test") action Play("sound", config.sample_sound)


                if config.has_voice:
                    

                    hbox:
                        bar value Preference("voice volume")

                        if config.sample_voice:
                            textbutton _("Test") action Play("voice", config.sample_voice)

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
        
        

    add "gui/gui_fshift/bg_slots.png" fit "cover"

    text (title):
        xoffset 1170 yoffset 70 size 60 bold True
    
    #text ("Preview"):
    #    xoffset 1110 yoffset 280 size 60 bold True

    use fshift_navigation_menu()

    #use game_menu(title):

    fixed:

        ## This ensures the input will get the enter event before any of the
        ## buttons do.
        order_reverse True

        ## The page name, which can be edited by clicking on a button.
        button:
            #style "page_label"

            key_events True

            yalign 0.16
            xalign 0.13
            
            action page_name_value.Toggle()

            input:
                style "page_label_text"
                value page_name_value

        ## The grid of file slots.
        vbox:
            #style_prefix "slot"

            xalign 0.22
            yalign 0.75

            spacing -80

            for i in range(3):
                vbox:
                    spacing 8   # espacio interno entre la imagen y el texto dentro de un slot
                    
                    $ slot = i + 1

                    imagebutton:
                        idle "gui/gui_fshift/save-load/slot_idle.png"
                        hover "gui/gui_fshift/save-load/slot_hover.png"
                        #selected_idle "gui/gui_fshift/save-load/slot_selected.png"
                        at side
                        action FileAction(slot)

                        
                        

                        #key "save_delete" action FileDelete(slot)
                    vbox:
                            yoffset -114
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
                    idle "gui/gui_fshift/button/prev_page.png"
                    action FilePagePrevious(auto = False, quick = False)
                ## range(1, 10) gives the numbers from 1 to 9.
                textbutton ("[page]/5") action FilePage(page) 

                
                imagebutton:
                    idle "gui/gui_fshift/button/next_page.png"
                    action FilePageNext(5)
    
################################################

screen fshift_navigation_menu():

    # This tag ensures only one instance of this screen is shown at a time.
    #style_prefix "game_menu"
    #tag menu

    # A frame to contain the buttons, centered on the screen.

    imagebutton:
        idle "gui/gui_fshift/button/back_idle.png"
        hover "gui/gui_fshift/button/back_hover.png"
        xalign 0.86
        yalign 0.97
        action Return()
        
    
    # A vbox organizes elements vertically with spacing.
    vbox:

        xalign 1.010
        yalign 0.35
        spacing 20
        at side_enter
        # Each textbutton defines a menu option.
        # 'action' specifies what happens when the button is clicked.
        

        if main_menu:
            imagebutton:
                idle "gui/gui_fshift/button/side_menu/start_idle.png"
                hover "gui/gui_fshift/button/side_menu/start_idle.png"
                at side
                action Start()
        else:
            imagebutton:
                idle "gui/gui_fshift/button/side_menu/mainmenu_idle.png"
                hover "gui/gui_fshift/button/side_menu/mainmenu_idle.png"
                at side
                action MainMenu(confirm=True)

        imagebutton:
            idle "gui/gui_fshift/button/side_menu/history_idle.png"
            hover "gui/gui_fshift/button/side_menu/history_idle.png"
            at side
            action ShowMenu("history")

        

        imagebutton:
            idle "gui/gui_fshift/button/side_menu/save_idle.png"
            hover "gui/gui_fshift/button/side_menu/save_idle.png"
            at side
            action ShowMenu("save")

        imagebutton:
            idle "gui/gui_fshift/button/side_menu/load_idle.png"
            hover "gui/gui_fshift/button/side_menu/load_idle.png"
            at side
            action ShowMenu("load")

        imagebutton:
            idle "gui/gui_fshift/button/side_menu/options_idle.png"
            hover "gui/gui_fshift/button/side_menu/options_idle.png"
            at side
            action ShowMenu("preferences")

        imagebutton:
            idle "gui/gui_fshift/button/side_menu/quit_idle.png"
            hover "gui/gui_fshift/button/side_menu/quit_idle.png"
            at side
            action Quit()
