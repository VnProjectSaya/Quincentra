"""
screen preferences():
    

    tag menu

    add "gui/gui_fshift/bg_options.png" fit "cover"
    text _("Display"):
        xoffset 280 yoffset 180 size 50 bold True
    vbox:
        
        xoffset 330
        yoffset 290
        vbox:
            spacing 30
            box_wrap True
            hbox:
                if renpy.variant("pc") or renpy.variant("web"):

                
                    style_prefix "radio"
                    label _("Window Mode")
                    
                    hbox:
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")
            
            hbox:
                style_prefix "check"
                label _("Skip Text")
                
                hbox:
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

            hbox:

                xoffset 330

                box_wrap True
                

            
                style_prefix "radio"
                #label _("Rollback Side")
                textbutton _("Disable") action Preference("rollback side", "disable")
                textbutton _("Left") action Preference("rollback side", "left")
                textbutton _("Right") action Preference("rollback side", "right")

            vbox:
                spacing 20
                style_prefix "slider"

                #label _("Text Speed")

                bar value Preference("text speed")

                #label _("Auto-Forward Time")

                bar value Preference("auto-forward time")
            

            
            ## Additional vboxes of type "radio_pref" or "check_pref" can be
            ## added here, to add additional creator-defined preferences.

        #null height (4 * gui.pref_spacing)

        hbox:
            style_prefix "slider"
            box_wrap True

            

            vbox:

                if config.has_music:
                    label _("Music Volume")

                    hbox:
                        bar value Preference("music volume")

                if config.has_sound:

                    label _("Sound Volume")

                    hbox:
                        bar value Preference("sound volume")

                        if config.sample_sound:
                            textbutton _("Test") action Play("sound", config.sample_sound)


                if config.has_voice:
                    label _("Voice Volume")

                    hbox:
                        bar value Preference("voice volume")

                        if config.sample_voice:
                            textbutton _("Test") action Play("voice", config.sample_voice)

                if config.has_music or config.has_sound or config.has_voice:
                    null height gui.pref_spacing

                    textbutton _("Mute All"):
                        action Preference("all mute", "toggle")
                        style "mute_all_button"
"""