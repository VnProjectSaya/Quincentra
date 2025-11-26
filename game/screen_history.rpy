

style fshift_vertical_slider:
    xsize 10
    ysize 200
    base_bar "gui/gui_fshift/bottom.png"
    thumb "gui/gui_fshift/top.png"
    bar_vertical True
    


screen history():

    tag menu
    predict False

    # Fondo
    add "gui/gui_fshift/bg_history.png" fit "cover"

    # Menú lateral
    use fshift_navigation_menu()

    # Título
    text _("History"):
        xoffset 1200
        yoffset 60
        size 60 
        

    # Contenedor general
    viewport:
        xpos 240
        ypos 280
        xsize 1180
        ysize 600

        scrollbars "vertical" 
        
            
        
        
        mousewheel True

        vbox:
            spacing 25  # Espacio entre entradas

            for h in _history_list:

                frame:
                    background None
                    padding (20, 20)
                    xfill True

                    vbox:
                        spacing 10

                        if h.who:
                            text h.who:
                                #color h.who_args.get("color", "#6DF") if "color" in h.who_args else "#6DF"
                                size 30
                                bold True

                        text renpy.filter_text_tags(h.what, allow=gui.history_allow_tags):
                            size 28
                            color "#ffffff9d"
                            substitute False
                            #wrap True

                # Separador decorativo
                text "_______________________________":
                    xalign 0.5
                    size 16
                    color "#888"

            if not _history_list:
                text _("The dialogue history is empty."):
                    size 30
                    color "#ffffff9d"



