define default_outlines = [(2, "#0009", 1, 1)]
init 1:# Styles

    style notify_item_frame:
        background Frame(gui.textbox_location, 90,8,90,8, tile=gui.frame_tile)
        padding (180,8,180,8)
    style notify_item_text:
        properties gui.text_properties("notify")
        outlines default_outlines

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
        outlines default_outlines
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
        yalign 0.0
    style quick_menu_top_center_button is quick_button
    style quick_menu_top_center_button_text is quick_button_text

    style replay_unlocked_button is gui_button:
        align (1.0, 0.5)
    style replay_unlocked_button_text is gui_button_text:
        outlines default_outlines
        size gui.text_size+20
        text_align 1.0
        align (0.5,0.5)
        font "gui/fonts/JosefinSans-SemiBold.ttf"
        #bold True
        #italic True
        #underline True
    style replay_unlocked_vbox:
        xsize 600
        align (0.96,0.98)

    style shortcuts_button_text is gui_button_text:
        outlines default_outlines
        text_align 0.5
        size gui.text_size+15
    style shortcuts_text is shortcuts_button_text

    style splash:
        outlines [(2, "#a2a2a2", 1, 1)]
        text_align 0.5
        align (0.5,0.5)
        font "mod/CabinSketch-Regular.ttf"

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
        hover_left_bar Frame(Solid(adjust_brightness("#000", 50)), gui.bar_borders, tile=gui.bar_tile)
        hover_right_bar Frame(Solid(adjust_brightness("#FB4301", 50)), gui.bar_borders, tile=gui.bar_tile)

    style cheat_management_slider is gui_slider:
        xsize 500
        xalign 0.5
        base_bar Frame(Solid("#FB4301"), gui.slider_borders, tile=gui.slider_tile)
        thumb Transform(Solid("#000"),ysize=gui.slider_size, xsize=30)
        hover_base_bar Frame(Solid(adjust_brightness("#FB4301", 50)), gui.slider_borders, tile=gui.slider_tile)
        hover_thumb Transform(Solid(adjust_brightness("#000", 50)),ysize=gui.slider_size, xsize=30)

    style cheat_management_button is gui_button:
        padding (10,10,10,10)
        hover_sound "audio/sfx/button_h.mp3"
        activate_sound "audio/sfx/button_a.mp3"

    style cheat_management_button_text is gui_button_text:
        font "gui/fonts/CrimsonText-SemiBold.ttf"
        outlines default_outlines

    style cheat_management_label is gui_label:
        padding (10,10,10,10)

    style cheat_management_label_text is gui_label_text:
        font "gui/fonts/CrimsonText-SemiBold.ttf"
        outlines default_outlines
        size gui.label_text_size-5
        color "#FB4301"

    style cheat_management_vscrollbar is gui_vscrollbar:
        unscrollable "hide"
        xalign 1.0
        base_bar Frame(Solid("#FB4301"), gui.vscrollbar_borders, tile=gui.scrollbar_tile)
        thumb Frame(Solid("#000"), gui.vscrollbar_borders, tile=gui.scrollbar_tile)
        hover_base_bar Frame(Solid(adjust_brightness("#FB4301", 50)), gui.vscrollbar_borders, tile=gui.scrollbar_tile)
        hover_thumb Frame(Solid(adjust_brightness("#000", 50)), gui.vscrollbar_borders, tile=gui.scrollbar_tile)
        hover_sound "audio/sfx/button_h.mp3"
        activate_sound "audio/sfx/button_a.mp3"

    style cheat_management_scrollbar is gui_scrollbar:
        unscrollable "hide"
        base_bar Frame(Solid("#FB4301"), gui.vscrollbar_borders, tile=gui.scrollbar_tile)
        thumb Frame(Solid("#000"), gui.vscrollbar_borders, tile=gui.scrollbar_tile)
        hover_base_bar Frame(Solid(adjust_brightness("#FB4301", 50)), gui.vscrollbar_borders, tile=gui.scrollbar_tile)
        hover_thumb Frame(Solid(adjust_brightness("#000", 50)), gui.vscrollbar_borders, tile=gui.scrollbar_tile)

    style cheat_students_vbox:
        xsize 520

    style cheat_students_vpgrid:
        xsize 540
        ysize 270

    style cheat_students_label_text is gui_label_text:
        size gui.label_text_size-5
        font "gui/fonts/CrimsonText-SemiBold.ttf"
        outlines default_outlines
        color "#FB4301"

    style cheat_students_button is gui_button:
        hover_sound "audio/sfx/button_h.mp3"
        activate_sound "audio/sfx/button_a.mp3"

    style cheat_students_button_text is gui_button_text:
        font "gui/fonts/CrimsonText-SemiBold.ttf"
        outlines default_outlines

    style cheat_students_vscrollbar is gui_vscrollbar:
        unscrollable "hide"
        xalign 1.0
        base_bar Frame(Solid("#FB4301"), gui.vscrollbar_borders, tile=gui.scrollbar_tile)
        thumb Frame(Solid("#000"), gui.vscrollbar_borders, tile=gui.scrollbar_tile)
        hover_base_bar Frame(Solid(adjust_brightness("#FB4301", 50)), gui.vscrollbar_borders, tile=gui.scrollbar_tile)
        hover_thumb Frame(Solid(adjust_brightness("#000", 50)), gui.vscrollbar_borders, tile=gui.scrollbar_tile)
        hover_sound "audio/sfx/button_h.mp3"
        activate_sound "audio/sfx/button_a.mp3"

    style cheat_students_scrollbar is gui_scrollbar:
        unscrollable "hide"
        base_bar Frame(Solid("#FB4301"), gui.vscrollbar_borders, tile=gui.scrollbar_tile)
        thumb Frame(Solid("#000"), gui.vscrollbar_borders, tile=gui.scrollbar_tile)
        hover_base_bar Frame(Solid(adjust_brightness("#FB4301", 50)), gui.vscrollbar_borders, tile=gui.scrollbar_tile)
        hover_thumb Frame(Solid(adjust_brightness("#000", 50)), gui.vscrollbar_borders, tile=gui.scrollbar_tile)

    style cheat_students_bar is gui_bar:
        xsize 500
        xalign 0.5
        left_bar Frame(Solid("#000"), gui.bar_borders, tile=gui.bar_tile)
        right_bar Frame(Solid("#FB4301"), gui.bar_borders, tile=gui.bar_tile)
        hover_left_bar Frame(Solid(adjust_brightness("#000", 50)), gui.bar_borders, tile=gui.bar_tile)
        hover_right_bar Frame(Solid(adjust_brightness("#FB4301", 50)), gui.bar_borders, tile=gui.bar_tile)

    style cheat_students_slider is gui_slider:
        xsize 500
        xalign 0.5
        base_bar Frame(Solid("#FB4301"), gui.slider_borders, tile=gui.slider_tile)
        thumb Transform(Solid("#000"),ysize=gui.slider_size, xsize=30)
        hover_base_bar Frame(Solid(adjust_brightness("#FB4301", 50)), gui.slider_borders, tile=gui.slider_tile)
        hover_thumb Transform(Solid(adjust_brightness("#000", 50)),ysize=gui.slider_size, xsize=30)

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
        outlines default_outlines
        font gui.name_text_font
        hover_sound "audio/sfx/button_h.mp3"
        activate_sound "audio/sfx/button_a.mp3"

style custom_caret:
    color gui.accent_color
    xalign 0.0
    yalign 0.5
    text_align 0.5

style custom_caret_2:
    color gui.accent_color
    size gui.text_size-10
    xalign 0.0
    yalign 0.5
    text_align 0.5


image custom_caret_2:
    Text("|", style="custom_caret_2")
    pause .5
    Text("")
    pause .5
    Text("|", style="custom_caret_2")
    pause .5
    repeat

image custom_caret:
    Text("|", style="custom_caret")
    pause .5
    Text("")
    pause .5
    Text("|", style="custom_caret")
    pause .5
    repeat


#Style Overrides
style pref_label_text:
    properties gui.text_properties("pref_label")

style confirm_prompt_text:
    properties gui.text_properties("confirm_prompt")

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")

style history_name_text:
    properties gui.text_properties("history_name")

style history_text:
    properties gui.text_properties("history_text")

style history_label_text:
    properties gui.text_properties("history_label")

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")

style radio_button:
    properties gui.button_properties("radio_button")

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_button:
    properties gui.button_properties("check_button")

style check_button_text:
    properties gui.text_properties("check_button")

style slider_button:
    properties gui.button_properties("slider_button")

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style help_text:
    properties gui.text_properties("help_text")

style skip_text:
    properties gui.text_properties("skip")

style slot_name_text:
    properties gui.text_properties("slot_name")

style page_label:
    properties gui.text_properties("page_label")

style page_label_text:
    properties gui.text_properties("slot_page")

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")

style file_slots_delete_button_text:
    properties gui.text_properties("slot_delete")

style about_text:
    properties gui.text_properties("about_text")

style about_label_text:
    properties gui.text_properties("about_label")

style game_menu_label_text:
    properties gui.text_properties("game_menu_label")

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")

style navigation_button_text:
    properties gui.text_properties("navigation_button")

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")



define gui.main_menu_text_outlines = default_outlines
#define gui.title_text_outlines = default_outlines
#define gui.version_text_outlines = default_outlines
define gui.game_menu_label_text_outlines = default_outlines
define gui.history_name_text_outlines = default_outlines
define gui.history_text_text_outlines = default_outlines
define gui.history_label_text_outlines = default_outlines
define gui.navigation_button_text_outlines = default_outlines
## to your navigation text button text outlines and uncomment the ones below
#define gui.navigation_button_text_idle_outlines = default_outlines
#define gui.navigation_button_text_hover_outlines = default_outlines
#define gui.navigation_button_text_selected_outlines = default_outlines
#define gui.navigation_button_text_insensitive_outlines = default_outlines
define gui.about_label_text_outlines = default_outlines
define gui.about_text_text_outlines = default_outlines
define gui.about_music_button_text_outlines = default_outlines
#define gui.about_music_button_text_idle_outlines = default_outlines
#define gui.about_music_button_text_hover_outlines = default_outlines
#define gui.about_music_button_text_selected_outlines = default_outlines
#define gui.about_music_button_text_insensitive_outlines = default_outlines
define gui.about_music_text_outlines = default_outlines
define gui.input_prompt_text_outlines = default_outlines
define gui.input_text_outlines = default_outlines
define gui.input_hint_text_outlines = default_outlines
define gui.input_button_text_outlines = default_outlines
# to your input buttons text outlines and uncomment the ones below
#define gui.input_button_text_idle_outlines = default_outlines
#define gui.input_button_text_hover_outlines = default_outlines
define gui.choice_button_text_idle_outlines = default_outlines
define gui.choice_button_text_hover_outlines = default_outlines
define gui.choice_button_text_insensitive_outlines = default_outlines
define gui.choice_alt_button_text_idle_outlines = gui.choice_button_text_idle_outlines
define gui.choice_alt_button_text_hover_outlines = gui.choice_button_text_hover_outlines
define gui.choice_alt_button_text_insensitive_outlines = gui.choice_button_text_hover_outlines
define gui.choice_tooltip_text_outlines = default_outlines
define gui.quick_button_text_outlines = default_outlines
# to your quick menu buttons text outlines and uncomment the ones below
#define gui.quick_button_text_idle_outlines = default_outlines
#define gui.quick_button_text_hover_outlines = default_outlines
#define gui.quick_button_text_selected_outlines = default_outlines
#define gui.quick_button_text_insensitive_outlines = default_outlines
define gui.quick_menu_text_outlines = default_outlines
define gui.name_text_outlines = default_outlines
define gui.dialogue_text_outlines = default_outlines
define gui.slot_button_text_outlines = default_outlines
# to your slot text button text outlines and uncomment the ones below
#define gui.slot_button_text_idle_outlines = default_outlines
#define gui.slot_button_text_hover_outlines = default_outlines
define gui.slot_name_text_outlines = default_outlines
# to your slot name text outlines and uncomment the ones below
#define gui.slot_name_text_idle_outlines = default_outlines
#define gui.slot_name_text_hover_outlines = default_outlines
define gui.slot_delete_text_outlines = default_outlines
# to your slot delete button text outlines and uncomment the ones below
#define gui.slot_delete_text_idle_outlines = default_outlines
#define gui.slot_delete_text_hover_outlines = default_outlines
define gui.slot_page_text_outlines = default_outlines
# to your page heading button text outlines and uncomment the ones below
#define gui.slot_page_text_idle_outlines = default_outlines
#define gui.slot_page_text_hover_outlines = default_outlines
#define gui.slot_page_text_selected_outlines = default_outlines
define gui.page_button_text_outlines = default_outlines
# to your page button text outlines and uncomment the ones below
#define gui.page_button_text_idle_outlines = default_outlines
#define gui.page_button_text_hover_outlines = default_outlines
#define gui.page_button_text_selected_outlines = default_outlines
define gui.radio_button_text_outlines = default_outlines
define gui.check_button_text_outlines = default_outlines
define gui.slider_button_text_outlines = default_outlines
define gui.pref_label_text_outlines = default_outlines
define gui.help_button_text_outlines = default_outlines
# to your help text button text outlines and uncomment the ones below
#define gui.help_button_text_idle_outlines = default_outlines
#define gui.help_button_text_hover_outlines = default_outlines
#define gui.help_button_text_selected_outlines = default_outlines
define gui.help_label_text_outlines = default_outlines
define gui.help_text_text_outlines = default_outlines
define gui.confirm_button_text_outlines = default_outlines
# to your confirm buttons text outlines and uncomment the ones below
#define gui.confirm_button_text_idle_outlines = default_outlines
#define gui.confirm_button_text_hover_outlines = default_outlines
define gui.confirm_prompt_text_outlines = default_outlines
define gui.skip_text_outlines = default_outlines
define gui.notify_text_outlines = default_outlines
define gui.tooltip_text_outlines = default_outlines