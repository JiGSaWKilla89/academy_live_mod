init 1:# Styles

    style notify_item_frame:
        background Frame("gui/textbox.png", 180,8,180,8, tile=gui.frame_tile)
        padding (180,8,180,8)
    style notify_item_text:
        properties gui.text_properties("notify")
        outlines [(2, "#0009", 1, 1)]
    
    style radio_button:
        hover_sound "audio/sfx/button_h.mp3"
        activate_sound "audio/sfx/button_a.mp3"
    style check_button:
        hover_sound "audio/sfx/button_h.mp3"
        activate_sound "audio/sfx/button_a.mp3"
    style slider_button:
        hover_sound "audio/sfx/button_h.mp3"
        activate_sound "audio/sfx/button_a.mp3"

    style slider:
        hover_sound "audio/sfx/button_h.mp3"
        activate_sound "audio/sfx/button_a.mp3"

    style file_slots_delete_button:
        hover_background None
        hover_sound None
        align (1.0,0.0)
    style file_slots_delete_button_text:
        properties gui.text_properties("slot_delete")
        bold True
        text_align 0.5

    style input_prompt:
        xalign gui.dialogue_text_xalign
        properties gui.text_properties("input_prompt")
    style input_button_text:
        properties gui.text_properties("input_button")
        text_align 0.5
    style input_button:
        properties gui.button_properties("input_button")

    style input_hint_vbox:
        xalign 0.98
        yalign 0.5
    style input_hint_button is input_button
    style input_hint_button_text is input_button_text

    style tooltip_frame:
        padding (50,10,50,10)
        xfill False
        yfill False
        align (0.5,0.5)
    style tooltip_hbox:
        align (0.5,0.5)
    style tooltip_text:
        size gui.text_size -10
        text_align 0.5
    style tooltip_button_text is gui_button_text:
        color "#FB4301"
        hover_color "#FFF"
        outlines [(2, "#0009", 1, 1)]
    style tooltip_button is gui_button:
        hover_sound "audio/sfx/button_h.mp3"
        activate_sound "audio/sfx/button_a.mp3"
    style tooltip_vscrollbar is gui_vscrollbar:
        unscrollable "hide"
        base_bar Frame(Solid("#FB4301"), gui.vscrollbar_borders, tile=gui.scrollbar_tile)
        thumb Frame(Solid("#000"), gui.vscrollbar_borders, tile=gui.scrollbar_tile)


    style quick_button is default
    style quick_button_text is button_text
    style quick_button:
        properties gui.button_properties("quick_button")
    style quick_button_text:
        properties gui.text_properties("quick_button")

    style quick_menu_bottom_center_text is quick_menu_text
    style quick_menu_bottom_center_hbox:
        xalign 0.5
        yalign 1.0
    style quick_menu_bottom_center_button is quick_button
    style quick_menu_bottom_center_button_text is quick_button_text

    style quick_menu_top_center_text is quick_menu_text
    style quick_menu_top_center_hbox:
        xalign 0.5
        yalign 0.05
    style quick_menu_top_center_button is quick_button
    style quick_menu_top_center_button_text is quick_button_text

    style replay_unlocked_button is gui_button:
        align (1.0, 0.5)
    style replay_unlocked_button_text is gui_button_text:
        outlines [(2, "#0009", 1, 1)]
        size gui.text_size+20
        text_align 1.0
        align (0.5,0.5)
        font "gui/fonts/JosefinSans-SemiBold.ttf"
        #bold True
        #italic True
        #underline True
    style replay_unlocked_vbox:
        xsize 600
        align (0.98,0.98)
    
    style shortcuts_button_text is gui_button_text:
        outlines [(2, "#0009", 1, 1)]
        text_align 0.5
        size gui.text_size+15
    style shortcuts_text is shortcuts_button_text

    style splash:
        outlines [(2, "#a2a2a2", 1, 1)]
        text_align 0.5
        align (0.5,0.5)


init 1:# Styles Cheats

    style menu_text_button_custom_cheats is menu_text_button_custom:
        selected_color "#FB4301"

    style cheat_management_vbox:
        xsize 520

    style cheat_management_vpgrid:
        xsize 560
        ysize config.screen_height-200

    style cheat_management_bar is gui_bar:
        xsize 500
        xalign 0.5
        left_bar Frame(Solid("#000"), gui.bar_borders, tile=gui.bar_tile)
        right_bar Frame(Solid("#FB4301"), gui.bar_borders, tile=gui.bar_tile)
        hover_left_bar Frame(Solid(adj_bri("#000", 50)), gui.bar_borders, tile=gui.bar_tile)
        hover_right_bar Frame(Solid(adj_bri("#FB4301", 50)), gui.bar_borders, tile=gui.bar_tile)

    style cheat_management_slider is gui_slider:
        xsize 500
        xalign 0.5
        base_bar Frame(Solid("#FB4301"), gui.slider_borders, tile=gui.slider_tile)
        thumb Transform(Solid("#000"),ysize=gui.slider_size, xsize=30)
        hover_base_bar Frame(Solid(adj_bri("#FB4301", 50)), gui.slider_borders, tile=gui.slider_tile)
        hover_thumb Transform(Solid(adj_bri("#000", 50)),ysize=gui.slider_size, xsize=30)

    style cheat_management_button is gui_button:
        padding (10,10,10,10)
        hover_sound "audio/sfx/button_h.mp3"
        activate_sound "audio/sfx/button_a.mp3"

    style cheat_management_button_text is gui_button_text:
        font "gui/fonts/CrimsonText-SemiBold.ttf"
        outlines [(2, "#0009", 1, 1)]

    style cheat_management_label is gui_label:
        padding (10,10,10,10)

    style cheat_management_label_text is gui_label_text:
        font "gui/fonts/CrimsonText-SemiBold.ttf"
        outlines [(2, "#0009", 1, 1)]
        size gui.label_text_size-5
        color "#FB4301"

    style cheat_management_vscrollbar is gui_vscrollbar:
        unscrollable "hide"
        xalign 1.0
        base_bar Frame(Solid("#FB4301"), gui.vscrollbar_borders, tile=gui.scrollbar_tile)
        thumb Frame(Solid("#000"), gui.vscrollbar_borders, tile=gui.scrollbar_tile)
        hover_base_bar Frame(Solid(adj_bri("#FB4301", 50)), gui.vscrollbar_borders, tile=gui.scrollbar_tile)
        hover_thumb Frame(Solid(adj_bri("#000", 50)), gui.vscrollbar_borders, tile=gui.scrollbar_tile)
        hover_sound "audio/sfx/button_h.mp3"
        activate_sound "audio/sfx/button_a.mp3"
    style cheat_management_scrollbar is gui_scrollbar:
        unscrollable "hide"
        base_bar Frame(Solid("#FB4301"), gui.vscrollbar_borders, tile=gui.scrollbar_tile)
        thumb Frame(Solid("#000"), gui.vscrollbar_borders, tile=gui.scrollbar_tile)
        hover_base_bar Frame(Solid(adj_bri("#FB4301", 50)), gui.vscrollbar_borders, tile=gui.scrollbar_tile)
        hover_thumb Frame(Solid(adj_bri("#000", 50)), gui.vscrollbar_borders, tile=gui.scrollbar_tile)



    style cheat_students_vbox:
        xsize 520
        
    style cheat_students_vpgrid:
        xsize 540
        ysize 270

    style cheat_students_label_text is gui_label_text:
        size gui.label_text_size-5
        font "gui/fonts/CrimsonText-SemiBold.ttf"
        outlines [(2, "#0009", 1, 1)]
        color "#FB4301"

    style cheat_students_button is gui_button:
        hover_sound "audio/sfx/button_h.mp3"
        activate_sound "audio/sfx/button_a.mp3"

    style cheat_students_button_text is gui_button_text:
        font "gui/fonts/CrimsonText-SemiBold.ttf"
        outlines [(2, "#0009", 1, 1)]

    style cheat_students_vscrollbar is gui_vscrollbar:
        unscrollable "hide"
        xalign 1.0
        base_bar Frame(Solid("#FB4301"), gui.vscrollbar_borders, tile=gui.scrollbar_tile)
        thumb Frame(Solid("#000"), gui.vscrollbar_borders, tile=gui.scrollbar_tile)
        hover_base_bar Frame(Solid(adj_bri("#FB4301", 50)), gui.vscrollbar_borders, tile=gui.scrollbar_tile)
        hover_thumb Frame(Solid(adj_bri("#000", 50)), gui.vscrollbar_borders, tile=gui.scrollbar_tile)
        hover_sound "audio/sfx/button_h.mp3"
        activate_sound "audio/sfx/button_a.mp3"
    style cheat_students_scrollbar is gui_scrollbar:
        unscrollable "hide"
        base_bar Frame(Solid("#FB4301"), gui.vscrollbar_borders, tile=gui.scrollbar_tile)
        thumb Frame(Solid("#000"), gui.vscrollbar_borders, tile=gui.scrollbar_tile)
        hover_base_bar Frame(Solid(adj_bri("#FB4301", 50)), gui.vscrollbar_borders, tile=gui.scrollbar_tile)
        hover_thumb Frame(Solid(adj_bri("#000", 50)), gui.vscrollbar_borders, tile=gui.scrollbar_tile)

    style cheat_students_bar is gui_bar:
        xsize 500
        xalign 0.5
        left_bar Frame(Solid("#000"), gui.bar_borders, tile=gui.bar_tile)
        right_bar Frame(Solid("#FB4301"), gui.bar_borders, tile=gui.bar_tile)
        hover_left_bar Frame(Solid(adj_bri("#000", 50)), gui.bar_borders, tile=gui.bar_tile)
        hover_right_bar Frame(Solid(adj_bri("#FB4301", 50)), gui.bar_borders, tile=gui.bar_tile)

    style cheat_students_slider is gui_slider:
        xsize 500
        xalign 0.5
        base_bar Frame(Solid("#FB4301"), gui.slider_borders, tile=gui.slider_tile)
        thumb Transform(Solid("#000"),ysize=gui.slider_size, xsize=30)
        hover_base_bar Frame(Solid(adj_bri("#FB4301", 50)), gui.slider_borders, tile=gui.slider_tile)
        hover_thumb Transform(Solid(adj_bri("#000", 50)),ysize=gui.slider_size, xsize=30)

    style cheats_inline:
        size 30
        color "#000000"
        font "gui/fonts/CrimsonText-SemiBold.ttf"

    style cheats_inline_replay:
        size 30
        color "#000000"
        font "gui/fonts/CrimsonText-SemiBold.ttf"


    style cheats_inline_itallic:
        italic True
        size 20
        color "#000"

    style cheats_inline_20:
        size 20
        color "#000000"
        font "gui/fonts/CrimsonText-SemiBold.ttf"

    style cheats_inline_25:
        size 25 
        color "#000000"
        font "gui/fonts/CrimsonText-SemiBold.ttf"
        
    style cheats_inline_40:
        size 40
        color "#000000"
        font "gui/fonts/CrimsonText-SemiBold.ttf"

    style cheats_inline_50:
        size 50
        color "#000000"
        font "gui/fonts/CrimsonText-SemiBold.ttf"

    style cheats_inline_15:
        size 15
        color "#000000"

    style cheats_inline_random:
        size 22
        font "gui/fonts/CrimsonText-SemiBold.ttf"


    style cheats_student_vscrollbar is cheat_students_vscrollbar

    style cheats_student_button is cheat_students_button

    style cheats_student_button_text is cheat_students_button_text

    style replay_cheat is cheat_students_button_text:
        color "#FB4301"
        hover_color "#FFF"
        selected_color "#000"
        size 22
        outlines [(2, "#0009", 1, 1)]
        font gui.name_text_font
        hover_sound "audio/sfx/button_h.mp3"
        activate_sound "audio/sfx/button_a.mp3"

