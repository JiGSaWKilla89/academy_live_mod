init 5:# Screens persistent._default_replays

    screen game_menu(title, scroll=None, yinitial=0.0):

        style_prefix "game_menu"

        if main_menu:
            add gui.main_menu_background
        else:
            add gui.game_menu_background

        frame:
            style "game_menu_outer_frame"

            hbox:

                ## Reserve space for the navigation section.
                frame:
                    style "game_menu_navigation_frame"

                frame:
                    style "game_menu_content_frame"

                    if scroll == "viewport":

                        viewport:
                            yinitial yinitial
                            scrollbars "vertical"
                            mousewheel True
                            draggable True
                            pagekeys True

                            side_yfill True

                            vbox:
                                transclude

                    elif scroll == "vpgrid":

                        vpgrid:
                            cols 1
                            yinitial yinitial

                            scrollbars "vertical"
                            mousewheel True
                            draggable True
                            pagekeys True

                            side_yfill True

                            transclude

                    else:

                        transclude

        use navigation

        textbutton _("Return"):
            style "return_button"
            #style "menu_text_button_custom" 
            hover_sound "audio/sfx/button_h.mp3"
            activate_sound "audio/sfx/button_a.mp3"
            text_style "menu_text_button_custom"

            if title == "Walkthrough Colors":
                action Hide("color_picker_wt", transition=dissolve)
            else:
                action Return()

        label title

        if main_menu:
            key "game_menu":
                if title == "Walkthrough Colors":
                    action Hide("color_picker_wt", transition=dissolve)
                else:
                    action ShowMenu("main_menu")
        else:
            key "game_menu":
                if title == "Walkthrough Colors":
                    action Hide("color_picker_wt", transition=dissolve)
                else:
                    action Return()

    screen navigation():

        if renpy.get_screen('main_menu'):

            vbox:
                xalign 0.96
                yalign 0.85
                #style_prefix "navigation"
                spacing gui.navigation_spacing
                textbutton _("{size=96}Start{/size}"):
                    style "menu_text_button_custom"
                    text_style "menu_text_button_custom"
                    text_outlines [ (2, "#00000080", 0, 1) ]
                    xalign 0.5
                    action Start()

                textbutton _("{size=96}Load{/size}"):
                    style "menu_text_button_custom"
                    text_style "menu_text_button_custom"
                    text_outlines [ (2, "#00000080", 0, 1) ]
                    xalign 0.5               
                    action ShowMenu("load")
                
                textbutton _("{size=64}Replays{/size}"):
                    style "menu_text_button_custom"
                    text_style "menu_text_button_custom"
                    text_outlines [ (2, "#00000080", 0, 1) ]
                    xalign 0.5
                    #action NullAction()
                    action ShowMenu("replays" if not persistent._default_replays else "replays_custom")

                textbutton _("{size=40}Preferences{/size}"):
                    style "menu_text_button_custom"
                    text_style "menu_text_button_custom"
                    text_outlines [ (2, "#00000080", 0, 1) ]
                    xalign 0.5
                    action ShowMenu("preferences")

                textbutton _("{size=40}Music{/size}"):
                    style "menu_text_button_custom"
                    text_style "menu_text_button_custom"
                    text_outlines [ (2, "#00000080", 0, 1) ]
                    xalign 0.5
                    #action NullAction()
                    action ShowMenu("musicroom")

                textbutton _("{size=40}About{/size}"):
                    style "menu_text_button_custom"
                    text_style "menu_text_button_custom"
                    text_outlines [ (2, "#00000080", 0, 1) ]
                    xalign 0.5
                    action ShowMenu("about")

                if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

                    ## Help isn't necessary or relevant to mobile devices.
                    textbutton _("{size=40}Help{/size}"):
                        style "menu_text_button_custom"
                        text_style "menu_text_button_custom"
                        text_outlines [ (2, "#00000080", 0, 1) ]
                        xalign 0.5
                        action ShowMenu("help")

                if renpy.variant("pc"):

                    ## The quit button is banned on iOS and unnecessary on Android and
                    ## Web.
                    textbutton _("{size=40}Quit{/size}"):
                        style "menu_text_button_custom"
                        text_style "menu_text_button_custom"
                        text_outlines [ (2, "#00000080", 0, 1) ]
                        xalign 0.5
                        action Quit(confirm=not main_menu)

        else:
            vbox:
                style_prefix "navigation"

                xpos gui.navigation_xpos
                yalign 0.5

                spacing gui.navigation_spacing

                if main_menu:

                    textbutton _("Start") action Start() style "menu_text_button_custom" text_style "menu_text_button_custom"

                else:

                    textbutton _("History") action ShowMenu("history") style "menu_text_button_custom" text_style "menu_text_button_custom"

                    textbutton _("Save") action ShowMenu("save") style "menu_text_button_custom" text_style "menu_text_button_custom"

                textbutton _("Load") action ShowMenu("load") style "menu_text_button_custom" text_style "menu_text_button_custom"

                if main_menu:
                    
                    textbutton _("Replays") action ShowMenu("replays" if not persistent._default_replays else "replays_custom") style "menu_text_button_custom" text_style "menu_text_button_custom"

                textbutton _("Preferences") action ShowMenu("preferences") style "menu_text_button_custom" text_style "menu_text_button_custom"

                textbutton _("Music") action ShowMenu("musicroom") style "menu_text_button_custom" text_style "menu_text_button_custom"
                if _in_replay:

                    textbutton _("End Replay") action EndReplay(confirm=True) style "menu_text_button_custom" text_style "menu_text_button_custom"

                elif not main_menu:

                    textbutton _("Main Menu") action MainMenu() style "menu_text_button_custom" text_style "menu_text_button_custom"

                textbutton _("About") action ShowMenu("about") style "menu_text_button_custom" text_style "menu_text_button_custom"

                if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

                    ## Help isn't necessary or relevant to mobile devices.
                    textbutton _("Help") action ShowMenu("help") style "menu_text_button_custom" text_style "menu_text_button_custom"

                if renpy.variant("pc"):

                    ## The quit button is banned on iOS and unnecessary on Android and
                    ## Web.
                    textbutton _("Quit") action Quit(confirm=not main_menu) style "menu_text_button_custom" text_style "menu_text_button_custom"
    
    screen shortcuts():
        style_prefix "shortcuts"
        zorder 300
        default shown = False
        default show_button = False

        mousearea:
            align (1.0, 0.05)
            xysize (50,50)
            hovered SetLocalVariable("show_button", True),With(dissolve)
            unhovered SetLocalVariable("show_button", False),With(dissolve)

        if shown:
            button:
                padding (0,0,0,0)
                add "#000" alpha .9
                add "splashText"
                xysize (config.screen_width, config.screen_height)
                action SetLocalVariable("shown", False),With(dissolve)
            key "game_menu" action SetLocalVariable("shown", False),With(dissolve)

            text "Click anywhere to close or the ? button" align (0.98, 0.98)

        if show_button:
            textbutton "?" action ToggleLocalVariable("shown"),With(dissolve) align (1.0, 0.05)

    screen main_menu():
        use mod_check()
        $ tooltip = GetTooltip()

        ## This ensures that any other menu screen is replaced.
        tag menu

        if persistent.alphaending == True:
            add gui.main_menu_background_alternate
        else:
            add gui.main_menu_background

        ## This empty frame darkens the main menu.
        frame:
            style "main_menu_frame"

        ## The use statement includes another screen inside this one. The actual
        ## contents of the main menu are in the navigation screen.
        use navigation

        if gui.show_name:

            vbox:
                style "main_menu_vbox"

                text "{size=20}{color=#000000}[config.version]":
                    style "main_menu_version"

        hbox:
            spacing 30
            xalign 0.97
            yalign 0.02
            imagebutton:
                xalign 0.5
                yalign 0.5
                focus_mask True
                idle "patreon_idle"
                hover "patreon_hover"
                style "menu_text_button_custom"
                action OpenURL("https://www.patreon.com/passhonQ")
            imagebutton:
                xalign 0.5
                yalign 0.5
                focus_mask True
                idle "substar_idle"
                hover "substar_hover"
                style "menu_text_button_custom"
                action OpenURL("https://subscribestar.adult/passhonq")
            imagebutton:
                focus_mask True
                idle "discord_idle"
                hover "discord_hover"
                style "menu_text_button_custom"
                action OpenURL("https://discord.gg/rPwzE9nBdh")
            imagebutton:
                focus_mask True
                idle "itch_idle"
                hover "itch_hover"
                style "menu_text_button_custom"
                action OpenURL("https://passhonq.itch.io/academy-live")
        $ mod_version = "Mod Compatible" if gui.jg_mod_version == config.version else "Mod Incompatible"
        vbox:
            text "{b}{u}[jg_1]JiG[jg_3][jg_2]SaW[jg_3]{/u}{/b}\nMOD Installed":
                size gui.title_text_size-20
                outlines [(2, "#0009", 1, 1)]
                text_align 0.5

            textbutton "[mod_version!i]":
                text_size 25
                text_outlines [(2, "#0009", 1, 1)]
                text_align 0.5
                action ShowMenu("mod_features")
                tooltip "Click me to view mod features"
    
            if mod_updated[0] not in ["Mod up-to-date", "JSON Error", "Could Not Connect to Host", "HTTP Error", "Timeout", "Request Error", "None"]:
                textbutton ("%s"%mod_updated[1] if mod_updated[0] != "Game Version Newer Than Mod" else "Check for updated mod"):
                    text_size 25
                    text_outlines [(2, "#0009", 1, 1)]
                    text_align 0.5
                    action OpenURL(gui.mod_update_url)
                    tooltip "Click me to get updated mod"
                if mod_changelog:
                    textbutton "Mod Changelog":
                        text_size 25
                        text_outlines [(2, "#0009", 1, 1)]
                        text_align 0.5
                        action ShowMenu("mod_changelog")
                        tooltip "View Mod Changelog"

        if tooltip:
            ## Use With Renpy Version Below 7.5 and 8.0
            #frame:
            #    style_prefix "tooltip"
            #    hbox:
            #        text tooltip
            ## Use With Renpy Version Above 7.5 and 8.0
            nearrect:
                focus "tooltip"
                prefer_top True
                frame:
                    at choice_appear(.5)
                    style_prefix "tooltip"
                    hbox:
                        text tooltip

    screen mod_changelog():
        $ tooltip = GetTooltip()
        tag menu

        use game_menu("Mod Changelog", scroll="viewport"):
            vbox:
                spacing 10
                for i in mod_changelog:
                    for j in i:
                        text j

    screen mod_check():
        timer 600 action SetVariable("mod_updated", get_latest_mod()) repeat True
        
    screen mod_features():
        $ tooltip = GetTooltip()
        tag menu

        use game_menu("Mod Features", scroll="viewport"):
            vbox:
                spacing 10
                if gui.jg_mod_version == config.version:
                    use mod_options_text
                else:
                    text "Mod is outdated {a=gui.mod_update_url}Click Here{/a} to Check for New Version"
                    text "Most mod options will work. Walkthrough will not be synced"
                    text ""
                    use mod_options_text
                    
        if tooltip:
            ## Use With Renpy Version Below 7.5 and 8.0
            #frame:
            #    style_prefix "tooltip"
            #    hbox:
            #        text tooltip
            ## Use With Renpy Version Above 7.5 and 8.0
            nearrect:
                focus "tooltip"
                prefer_top True
                frame:
                    at choice_appear(.5)
                    style_prefix "tooltip"
                    hbox:
                        text tooltip

    screen mod_options_text():
        text "Custom Cheat Menu Toggled Using {a=#:None}{color=#f00}(END){/color}{/a} or button in Quick Menu" tooltip "Keyboard END"
        text "1. Manage Academy Options using {a=#:None}{color=#f00}(1){/color}{/a} on the number row or keypad" xoffset 50 tooltip "Only works on the cheats screen"
        text "2. Manage Lawsuit Options using {a=#:None}{color=#f00}(2){/color}{/a} on the number row or keypad" xoffset 50 tooltip "Only works on the cheats screen"
        text "3. Modify Student Traits using {a=#:None}{color=#f00}(3){/color}{/a} on the number row or keypad" xoffset 50 tooltip "Only works on the cheats screen"
        text "4. Modify Teacher Traits using {a=#:None}{color=#f00}(4){/color}{/a} on the number row or keypad" xoffset 50 tooltip "Only works on the cheats screen"
        text "5. Modify Teacher Traits using {a=#:None}{color=#f00}(5){/color}{/a} on the number row or keypad" xoffset 50 tooltip "Only works on the cheats screen"
        text "Walkthrough"
        text "1. Walkthrough Suggestions Toggled using {a=#:None}{color=#f00}(W){/color}{/a} or in preferences menu" xoffset 50 tooltip "This can be toggled in the main menu or in the game"
        text "2. Walkthrough Tooltips Toggled using {a=#:None}{color=#f00}(Shift+T){/color}{/a} or in preferences menu" xoffset 50 tooltip "This can be toggled in the main menu or in the game"
        text "Music Player"
        text "1. Music Player can be Toggled ingame using {a=#:None}{color=#f00}(M){/color}{/a}" xoffset 50 tooltip "This can be toggled in the main menu or in the game"
        text "2. Hovering over Volume Slider allows mousewheel up/down control" xoffset 50 
        text "Override Replays"
        text "1. View Empty Replays {a=#:None}{color=#f00}(E){/color}{/a} or button in Replays" xoffset 50 tooltip "This works only on the standard replays screen"
        text "2. View Locked Replays {a=#:None}{color=#f00}(L){/color}{/a} or button in Replays" xoffset 50 tooltip "This works only on the standard replays screen"
        text "Quick Menu Options"
        text "1. Quick Menu Visibility Options Toggled using {a=#:None}{color=#f00}(Q){/color}{/a} or in preferences menu" xoffset 50 tooltip "This can be toggled in the main menu or in the game"
        text "2. Quick Menu Position Options Toggled Using {a=#:None}{color=#f00}(Shift+Q){/color}{/a} or in preferences menu" xoffset 50 tooltip "This can be toggled in the main menu or in the game"
        text "Say Dialogue"
        text "1. Textbox Visibility Toggled using {a=#:None}{color=#f00}(T){/color}{/a} or in preferences menu" xoffset 50 tooltip "This can be toggled in the main menu or in the game"
        text "2. Slider in Preferences or NUM {a=#:None}{color=#f00}(+/-){/color}{/a}" xoffset 50 tooltip "This can be toggled in the main menu or in the game"
        text "3. Fancy Text Toggled using {a=#:None}{color=#f00}(F){/color}{/a} or in preferences menu" xoffset 50 tooltip "This can be toggled in the main menu or in the game"
        text "4. Text Effect Toggled using {a=#:None}{color=#f00}(E){/color}{/a} or in preferences menu" xoffset 50 tooltip "This can be toggled in the main menu or in the game"
        text "5. Text Always Effect Toggled using {a=#:None}{color=#f00}(R){/color}{/a} or in preferences menu" xoffset 50 tooltip "This can be toggled in the main menu or in the game"
        text "Credit to {a=https://github.com/yukinogatari/Ren-Py-FancyText}yukinogatari{/a} for the original Fancytext Module Modified by\n[gui.mod_dev] for newer Ren'Py Compatibility" xoffset 50 tooltip "yukinogatari Github"
        text "Custom Save Names"
        text "1. Toggle Custom Savenames using {a=#:None}{color=#f00}(Shift+S){/color}{/a} or in preferences menu" xoffset 50 tooltip "This can be toggled in the main menu or in the game"
        text "Hotkeys"
        text "1. Toggle Choice Hotkeys using {a=#:None}{color=#f00}(C){/color}{/a} or in preferences menu" xoffset 50 tooltip "This can be toggled in the main menu or in the game"
        text "Notifications"
        text "1. Toggle Notification Stack/Standard using {a=#:None}{color=#f00}(N){/color}{/a} or in preferences menu" xoffset 50 tooltip "This can be toggled in the main menu or in the game"
        text "Credit to {a=https://github.com/RenpyRemix/multi-notify}RenpyRemix{/a} for stackable notifications" xoffset 50 tooltip "RenpyRemix Github"
        text "Credit to {a=https://github.com/valery-iwanofu/renpy-shader-collection}valery-iwanofu{/a} for color picker" xoffset 50 tooltip "valery-iwanofu Github"
        text ""
        if mod_updated[0] not in ["Mod up-to-date", "JSON Error", "Could Not Connect to Host", "HTTP Error", "Timeout", "Request Error", "None"]:
            text "Latest MOD update available at {a=gui.mod_update_url}JiGSaW Games Studios{/a}" tooltip "Mod Developer"
        text "If you like what I do {a=https://buymeacoffee.com/jigsawgames}Buy me a beer{/a}" tooltip "Mod Developer BuyMeACoffee Page"
        text "And lastly {a=https://www.patreon.com/passhonQ}passhonQ{/a} for developing [config.name!t]" tooltip "Developer Patreon"

    screen confirm_ok(message, ok_action=None):
        modal True
        zorder 200
        style_prefix "confirm"

        add "gui/overlay/confirm.png"
        frame:

            vbox:
                xalign .5
                yalign .5
                spacing 45

                label _(message):
                    style "confirm_prompt"
                    xalign 0.5

                textbutton _("Ok (Enter)"):
                    xalign 0.5
                    text_align 0.5
                    #if ok_action != None:
                        #action ok_action
                    #else:
                        #action Hide("confirm_ok", transition=d)
                    action ok_action, Hide("confirm_ok", transition=d)

        key "game_menu" action [ok_action, Hide("confirm_ok", transition=d)]
        key "input_enter" action [ok_action, Hide("confirm_ok", transition=d)]

    screen confirm(message, yes_action, no_action):

        ## Ensure other screens do not get input while this screen is displayed.
        modal True

        zorder 200

        style_prefix "confirm"

        add "gui/overlay/confirm.png"

        frame:

            vbox:
                xalign .5
                yalign .5
                spacing 45

                label _(message):
                    style "confirm_prompt"
                    xalign 0.5

                hbox:
                    xalign 0.5
                    spacing 150

                    textbutton (_("Yes") if not persistent._choice_hotkeys else _("(Y)es")) action yes_action
                    textbutton (_("No") if not persistent._choice_hotkeys else _("(N)o")) action no_action

        ## Right-click and escape answer "no".
        key "game_menu" action no_action
        if persistent._choice_hotkeys:
            key "K_y" action yes_action
            key "K_n" action no_action

    screen say(who, what, slow_effect=persistent._slow_effect, slow_effect_delay=persistent._effect_delay, always_effect=persistent._always_effect):
        style_prefix "say"

        window:
            id "window"
            if persistent._textbox_visible and who:
                background Transform(Frame("gui/textbox.png"),
                    alpha=persistent._textbox_alpha,
                    xysize=(config.screen_width, gui.textbox_height))
            else:
                background None
            
            if who is not None:

                window:
                    id "namebox"
                    style "namebox"
                    
                    text who:
                        id "who"
                        if persistent._fancy_text:
                            slow_effect slow_effect
                            slow_effect_delay slow_effect_delay
                            always_effect always_effect

            text what:
                id "what"
                if persistent._fancy_text:
                    slow_effect slow_effect
                    slow_effect_delay slow_effect_delay
                    always_effect always_effect

        ## If there's a side image, display it above the text. Do not display on the
        ## phone variant - there's no room.
        if not renpy.variant("small"):
            add SideImage() xalign 0.0 yalign 1.0

    screen preferences():

        tag menu

        use game_menu(_("Preferences"), scroll="viewport"):

            vbox:

                hbox:
                    box_wrap True

                    if renpy.variant("pc") or renpy.variant("web"):

                        vbox:
                            style_prefix "radio"
                            label _("Display\n[jg_s]")
                            textbutton _("Window"):
                                action Preference("display", "window")
                            textbutton _("Fullscreen"):
                                action Preference("display", "fullscreen")

                    vbox:
                        style_prefix "check"
                        label _("Skip\n[jg_s]")
                        textbutton _("Unseen Text"):
                            action Preference("skip", "toggle")
                        textbutton _("After Choices"):
                            action Preference("after choices", "toggle")
                        textbutton _("Transitions"):
                            action InvertSelected(Preference("transitions", "toggle"))

                    vbox:
                        style_prefix "check"
                        label _("Fancy Text\n[jg_s](Shift+F)")
                        textbutton _("Enabled"):
                            action SetField(persistent, "_fancy_text", True),SetField(preferences, "text_cps", 120)
                        textbutton _("Disabled"):
                            action SetField(persistent, "_fancy_text", False),SetField(preferences, "text_cps", 0)

                    vbox:
                        style_prefix "check"
                        label _("Savename\n[jg_s](Shift+S)")
                        textbutton _("Enabled"):
                            action SetField(persistent, "_custom_savename", True)
                        textbutton _("Disabled"):
                            action SetField(persistent, "_custom_savename", False)
                    ## Additional vboxes of type "radio_pref" or "check_pref" can be
                    ## added here, to add additional creator-defined preferences.

                null height (4 * gui.pref_spacing)

                hbox:
                    box_wrap True
                    if persistent._fancy_text:
                        vbox:
                            style_prefix "check"
                            label _("Effect\n[jg_s](E)")
                            textbutton _("[persistent._slow_effect_title]"):
                                action SlowEffectChange(True)

                        vbox:
                            style_prefix "check"
                            label _("Always Effect\n[jg_s](R)")
                            textbutton _("[persistent._always_effect_title]"):
                                action AlwaysEffectChange(True)

                        vbox:
                            style_prefix "slider"
                            label _("Effect Delay:\n[jg_s]%s Seconds"%EffectDelayDisplay())

                            bar:
                                value FieldValue(persistent, "_effect_delay",
                                    range=1.0,
                                    style="slider",
                                    max_is_zero=False,
                                    step=.1,
                                    force_step=True)

                            textbutton _("Default"):
                                action SetField(persistent, "_effect_delay", 0.2)

                null height (4 * gui.pref_spacing)

                hbox:
                    box_wrap True

                    vbox:
                        style_prefix "check"
                        label _("Choice Hotkeys\n[jg_s](C)")
                        textbutton _("Enabled"):
                            action SetField(persistent, "_choice_hotkeys", True)
                        textbutton _("Disabled"):
                            action SetField(persistent, "_choice_hotkeys", False)
                    vbox:
                        style_prefix "check"
                        label _("Walkthrough\n[jg_s](W)")
                        textbutton _("Enabled"):
                            action SetField(persistent, "_walkthrough", True)
                        textbutton _("Disabled"):
                            action SetField(persistent, "_walkthrough", False)
                    if persistent._walkthrough:
                        vbox:
                            style_prefix "check"
                            label _("Choice Hints\n[jg_s](Shift+T)")
                            textbutton _("Enabled"):
                                action SetField(persistent, "_choice_tooltips", True)
                            textbutton _("Disabled"):
                                action SetField(persistent, "_choice_tooltips", False)

                    vbox:
                        style_prefix "check"
                        label _("Custom Replays\n[jg_s]")
                        textbutton _("Enabled"):
                            action SetField(persistent, "_default_replays", True)
                        textbutton _("Disabled"):
                            action SetField(persistent, "_default_replays", False)

                null height (4 * gui.pref_spacing)

                hbox:
                    box_wrap True
                    if persistent._walkthrough:
                        vbox:
                            style_prefix "check"
                            label _("Adjust WT Colors\n[jg_s]")
                            textbutton _("Change") action Show("color_picker_wt", transition=dissolve)
                    vbox:
                        style_prefix "check"
                        label _("Textbox\n[jg_s](T)")
                        textbutton _("Enabled"):
                            action SetField(persistent, "_textbox_visible", True)
                        textbutton _("Disabled"):
                            action SetField(persistent, "_textbox_visible", False)
                    vbox:
                        style_prefix "check"
                        label _("Quick Menu\n[jg_s](Shift+Q)")
                        textbutton _("{size=-10}%s{/size}"%QuickPositions()):
                            action CycleQuickMenu(True)

                    vbox:
                        style_prefix "check"
                        label _("Quick Menu State\n[jg_s](Q)")
                        textbutton _("{size=-10}[persistent._quick_menu_state!c]{/size}"):
                            action CycleQuickStates(True)

                null height (4 * gui.pref_spacing)

                hbox:
                    box_wrap True
                    vbox:
                        style_prefix "check"
                        label _("Notifictions\n[jg_s](N)")
                        textbutton _("{size=-10}%s{/size}"%("Notification Stack" if persistent._notify_custom else "Notification Standard")):
                            action ToggleField(persistent, "_notify_custom")
                    vbox:
                        style_prefix "check"
                        label _("Music Buttons\n[jg_s]{}".format("Solid" if persistent._use_outline_music_buttons else "Outline"))
                        textbutton _("Solid"):
                            action SetField(persistent, "_use_outline_music_buttons", True)
                        textbutton _("Outline"):
                            action SetField(persistent, "_use_outline_music_buttons", False)
                    vbox:
                        style_prefix "check"
                        label _("Music Volume\n[jg_s]{}".format("Fast" if persistent._fast_vol_music else "Slow"))
                        textbutton _("Fast"):
                            action SetField(persistent, "_fast_vol_music", True)
                        textbutton _("Slow"):
                            action SetField(persistent, "_fast_vol_music", False)

                null height (4 * gui.pref_spacing)

                hbox:
                    style_prefix "slider"
                    box_wrap True

                    vbox:
                        if persistent._textbox_visible:
                            label _("Textbox Opacity:\n[jg_s]%s"%TextBoxAlpha())

                            bar:
                                value FieldValue(persistent, "_textbox_alpha",
                                    range=1.0,
                                    style="slider",
                                    max_is_zero=False,
                                    step=.01,
                                    force_step=True)

                        label _("Text Speed:\n[jg_s]%s"%TextSpeed())

                        bar:
                            value Preference("text speed")

                        label _("Auto-Forward Time:\n[jg_s]%s"%AutoForwardTime())

                        bar:
                            value Preference("auto-forward time")

                    vbox:

                        if config.has_music:
                            label _("Music Volume:\n[jg_s]%s"%VolumeDisplay('music'))

                            hbox:
                                bar:
                                    value Preference("music volume")

                        if config.has_sound:

                            label _("Sound Volume:\n[jg_s]%s"%VolumeDisplay('sfx'))

                            hbox:
                                bar:
                                    value Preference("sound volume")

                                if config.sample_sound:
                                    textbutton _("Test"):
                                        action Play("sound", config.sample_sound)

                        if config.has_voice:
                            label _("Voice Volume:\n[jg_s]%s"%VolumeDisplay('voice'))

                            hbox:
                                bar:
                                    value Preference("voice volume")

                                if config.sample_voice:
                                    textbutton _("Test"):
                                        action Play("voice", config.sample_voice)

                        if config.has_music or config.has_sound or config.has_voice:
                            null height gui.pref_spacing

                            textbutton _("Mute All"):
                                action Preference("all mute", "toggle")
                                style "mute_all_button"

    screen color_picker_wt():
        default activate = False
        default option = ""
        default field = ""
        use game_menu("Walkthrough Colors"):
            vbox:
                hbox:#Good Choice
                    spacing 15
                    vbox:
                        textbutton "Good Choice Color":
                            
                            action If(option == "_good_choice_color", 
                                true=[SetScreenVariable("activate", False), SetScreenVariable("option", ""), SetScreenVariable("field", "")], 
                                false=[SetScreenVariable("activate", True), SetScreenVariable("option", "_good_choice_color"), SetScreenVariable("field", "_good_choice_color")])
                            text_color persistent._good_choice_color
                            text_hover_color adjust_brightness(persistent._good_choice_color, -50)
                    vbox:
                        textbutton "Reset":
                            action SetField(persistent, "_good_choice_color", persistent._default_good_choice_color) 
                            sensitive persistent._good_choice_color != persistent._default_good_choice_color
                hbox:#Bad Choice
                    spacing 15
                    vbox:
                        textbutton "Bad Choice Color":
                            action If(option == "_bad_choice_color", 
                                true=[SetScreenVariable("activate", False), SetScreenVariable("option", ""), SetScreenVariable("field", "")], 
                                false=[SetScreenVariable("activate", True), SetScreenVariable("option", "_bad_choice_color"), SetScreenVariable("field", "_bad_choice_color")])
                            text_color persistent._bad_choice_color
                            text_hover_color adjust_brightness(persistent._bad_choice_color, -50)
                    vbox:
                        textbutton "Reset":
                            action SetField(persistent, "_bad_choice_color", persistent._default_bad_choice_color) 
                            sensitive persistent._bad_choice_color != persistent._default_bad_choice_color
                hbox:#Recommended Choice
                    spacing 15
                    vbox:
                        textbutton "Recommended Choice Color":
                            action If(option == "_recommended_choice_color", 
                                true=[SetScreenVariable("activate", False), SetScreenVariable("option", ""), SetScreenVariable("field", "")],  
                                false=[SetScreenVariable("activate", True), SetScreenVariable("option", "_recommended_choice_color"), SetScreenVariable("field", "_recommended_choice_color")])
                            text_color persistent._recommended_choice_color
                            text_hover_color adjust_brightness(persistent._recommended_choice_color, -50)
                    vbox:
                        textbutton "Reset":
                            action SetField(persistent, "_recommended_choice_color", persistent._default_recommended_choice_color) 
                            sensitive persistent._recommended_choice_color != persistent._default_recommended_choice_color
                hbox:#Best Choice
                    spacing 15
                    vbox:
                        textbutton "Best Choice Color":
                            action If(option == "_best_choice_color", 
                                true=[SetScreenVariable("activate", False), SetScreenVariable("option", ""), SetScreenVariable("field", "")], 
                                false=[SetScreenVariable("activate", True), SetScreenVariable("option", "_best_choice_color"), SetScreenVariable("field", "_best_choice_color")])
                            text_color persistent._best_choice_color
                            text_hover_color adjust_brightness(persistent._best_choice_color, -50)
                    vbox:
                        textbutton "Reset":
                            action SetField(persistent, "_best_choice_color", persistent._default_best_choice_color) 
                            sensitive persistent._best_choice_color != persistent._default_best_choice_color
                hbox:#Dealers Choice
                    spacing 15
                    vbox:
                        textbutton "Good Choice Color":
                            action If(option == "_dealers_choice_color", 
                                true=[SetScreenVariable("activate", False), SetScreenVariable("option", ""), SetScreenVariable("field", "")], 
                                false=[SetScreenVariable("activate", True), SetScreenVariable("option", "_dealers_choice_color"), SetScreenVariable("field", "_dealers_choice_color")])
                            text_color persistent._dealers_choice_color
                            text_hover_color adjust_brightness(persistent._dealers_choice_color, -50)
                    vbox:
                        textbutton "Reset":
                            action SetField(persistent, "_dealers_choice_color", persistent._default_dealers_choice_color) 
                            sensitive persistent._dealers_choice_color != persistent._default_dealers_choice_color

            if activate:
                use color_picker(FieldSimpleValue(persistent,option), field)

    screen quick_menu():

        ## Ensure this appears on top of other screens.
        zorder 100
        default quick_hover = False
        style_prefix "quick"
        if quick_menu:
            if persistent._quick_menu_state == "visible":
                use quick_layout
            elif persistent._quick_menu_state == "hover":
                use quick_mouse
                if quick_hover:
                    use quick_layout
                else:
                    use quick_hover

    screen quick_hover():
        $ qp = persistent._quick_menu_layout
        if persistent._quick_menu_layout in ["bottom_center", "top_center"]:
            hbox:
                xalign 0.5
                style_prefix "quick_menu_%s"%persistent._quick_menu_layout
                text "···"

    screen quick_layout:
        if persistent._quick_menu_layout in ["bottom_center", "top_center"]:
            hbox:
                style_prefix "quick_menu_%s"%persistent._quick_menu_layout
                use quick_menu_buttons

    screen quick_mouse():
        if persistent._quick_menu_layout == "bottom_center":
            mousearea:
                align (0.5,1.0)
                xysize (config.screen_width, gui.text_size)
                hovered ToggleScreenVariable("quick_hover", True),With(dissolve)
                unhovered ToggleScreenVariable("quick_hover", False),With(dissolve)

        if persistent._quick_menu_layout == "top_center":
            mousearea:
                align (0.5,0.05)
                xysize (config.screen_width, gui.text_size)
                hovered ToggleScreenVariable("quick_hover", True),With(dissolve)
                unhovered ToggleScreenVariable("quick_hover", False),With(dissolve)

    screen quick_menu_buttons():
        textbutton _("Back"):
            action Rollback()
        textbutton _("History"):
            action ShowMenu('history')
        textbutton _("Skip"):
            action Skip() alternate Skip(fast=True, confirm=True)
        textbutton _("Auto"):
            action Preference("auto-forward", "toggle")
        textbutton _("Save"):
            action ShowMenu('save')
        textbutton _("Hide"):
            action HideInterface()
        textbutton _("Q.Save"):
            action QuickSave()
        textbutton _("Q.Load"):
            action QuickLoad()
        textbutton _("Prefs"):
            action ShowMenu('preferences')
        textbutton _("Cheats"):
            action Show("cheats", transition=dissolve)
        if _in_replay:
            textbutton _("End Replay"):
                action EndReplay(confirm=True)

    screen choice(items):
        $ tooltip = GetTooltip()
        style_prefix "choice"

        default walkthrough = ""
        default hint = ""

        default operators = {
            "<=" : operator.le,   # less than or equal to
            "<"  : operator.lt,   # less than
            ">"  : operator.gt,   # greater than
            ">=" : operator.ge,   # greater than or equal to
            "==" : operator.eq,   # equal tom
            "!=" : operator.ne,   # not equal
            }

        textbutton "?":
            action NullAction() 
            tooltip wt_choice_tooltip
            style "_default"
            text_style "_default"
            text_size 50
            text_outlines [(2, "#0009", 1, 1)]
            text_color "#FFFFFFA3"

        vbox:
            for count, i in enumerate(items, 1):
                $ _choice_wt = ""
                $ _choice_hint = ""
                $ _choice_color = gui.text_color
                $ _choice_size = gui.text_size
                if renpy.loadable("mod/walkthrough.rpy"):
                    $ _choices = WalkthroughData(renpy.get_filename_line(), i.caption)
                    if _choices != (None, None, None, None):
                        $ _choice_wt, _choice_hint, _choice_color, _choice_size = _choices

                if isinstance(_choice_wt, dict):
                    $ var_wt = getattr(store, _choice_wt.get("var"))
                    $ op_wt = operators.get(_choice_wt.get("operator"))
                    $ com_wt = _choice_wt.get("value")
                    $ disp_wt = op_wt(var_wt, com_wt)
                    $ walkthrough = _choice_wt.get('msg') if disp_wt else _choice_wt.get('alt_msg')
                elif isinstance(_choice_wt, list):
                    $ walkthrough = custom_join(_choice_wt, " ")
                elif isinstance(_choice_wt, str):
                    $ walkthrough = _choice_wt

                if isinstance(_choice_hint, dict):
                    $ var_hint = getattr(store, _choice_hint.get("var"))
                    $ op_hint = operators.get(_choice_hint.get("operator"))
                    $ com_hint = _choice_hint.get("value")
                    $ disp_hint = op_hint(var_hint, com_hint)
                    if isinstance(_choice_hint.get('msg'), list):
                        $ _hint = custom_join(_choice_hint.get('msg'))
                    elif isinstance(_choice_hint.get('msg'), str):
                        $ _hint = _choice_hint.get('msg')
                    if isinstance(_choice_hint.get('alt_msg'), list):
                        $ _hint_alt = custom_join(_choice_hint.get('alt_msg'))
                    elif isinstance(_choice_hint.get('alt_msg'), str):
                        $ _hint_alt = _choice_hint.get('alt_msg')
                    $ hint = _hint if disp_hint else _hint_alt
                elif isinstance(_choice_hint, list):
                    $ hint = custom_join(_choice_hint)
                elif isinstance(_choice_hint, str):
                    $ hint = _choice_hint

                $ number = "{size=-5}{alpha=.5}%s{/alpha}{/size}. "%(count % 10) if count < 10 and persistent._choice_hotkeys else ''
                $ wt_data = " {b}{size=[_choice_size]}{color=[_choice_color]}%s{/color}{/size}{/b}"%(walkthrough) if persistent._walkthrough else ""
                $ output = "{}{}{}".format(number, i.caption, wt_data)

                textbutton output:
                    action i.action
                    if hint and persistent._walkthrough and persistent._choice_tooltips:
                        tooltip "{}".format(hint)

                key "K_{}".format(count) action (i.action if persistent._choice_hotkeys else NullAction())
                key "K_KP_{}".format(count) action (i.action if persistent._choice_hotkeys else NullAction())

        ## Uncomment the desired tooltip for desired renpy version
        if tooltip:
            ## Use With Renpy Version Below 7.5 and 8.0
            #frame:
            #    style_prefix "tooltip"
            #    hbox:
            #        text tooltip
            ## Use With Renpy Version Above 7.5 and 8.0
            nearrect:
                focus "tooltip"
                prefer_top True
                frame:
                    at choice_appear(.5)
                    style_prefix "tooltip"
                    hbox:
                        text tooltip

    transform choice_appear(t=1):
        alpha 0.0
        easein t alpha 1.0

    screen input(prompt):
        # renpy.input("Please type the password and press 'Enter'|hint=cw|anotherkeyword=False", default="cw" if persistent._complete_input else '')
        # modify the input to your hearts content whichever keyword you need the above line is a sample of how it will split them
        style_prefix "input"

        window:
            if persistent._textbox_visible:
                background Transform(Frame("gui/textbox.png"),
                    alpha=persistent._textbox_alpha,
                    xysize=(config.screen_width, gui.textbox_height))
            else:
                background None

            vbox:
                xanchor gui.dialogue_text_xalign
                xpos gui.dialogue_xpos
                xsize gui.dialogue_width
                ypos gui.dialogue_ypos

                text prompt style "input_prompt" at input_appear(.5)

                input id "input" at input_appear(.5) length 50

            vbox:
                style_prefix "input_hint"
                textbutton _("Confirm %s")%(u"{font=DejaVuSans.ttf}\u23CE{/font}"):
                    at input_appear(.5)
                    action GetText("input","input"),With(dissolve)

        key "input_enter" action GetText("input","input"),With(dissolve)

    screen file_slots(title):

        default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))
        default savename = VariableInputValue('save_name', False)
        default the_page = VariableInputValue("_go_to_page", False)

        use game_menu(title):

            fixed:
                if persistent._custom_savename:
                    if title.lower() == _("save") and not page_name_value.get_page() in ["auto", "quick"]:
                        button:
                            ypos 10
                            xpos -30
                            style "page_label"

                            key_events True
                            action savename.Toggle()

                            input:
                                id "input"
                                length 26
                                size gui.text_size-10
                                prefix _("Enter A Save Name: ")
                                value savename
                                style "page_label_text"

                ## This ensures the input will get the enter event before any of the
                ## buttons do.
                order_reverse True

                ## The page name, which can be edited by clicking on a button.
                button:
                    ypos -30
                    style "page_label"

                    key_events True
                    xalign 0.5
                    action page_name_value.Toggle()

                    input:
                        style "page_label_text"
                        value page_name_value

                ## The grid of file slots.
                grid gui.file_slot_cols gui.file_slot_rows:
                    style_prefix "slot"

                    xalign 0.5
                    yalign 0.5

                    spacing gui.slot_spacing

                    for i in range(gui.file_slot_cols * gui.file_slot_rows):

                        $ slot = i + 1

                        button:
                            action FileAction(slot)

                            vbox:

                                add FileScreenshot(slot) xalign 0.5 yalign 0.5 #xysize WideRatio(config.thumbnail_width)

                                text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                                    style "slot_time_text"

                                text FileSaveName(slot):
                                    style "slot_name_text"

                                key "save_delete" action FileDelete(slot)
                            if FileLoadable(slot):
                                textbutton _("X"):
                                    action FileDelete(slot)
                                    align (1.0,0.0)
                                    style_prefix "file_slots_delete"

                ## Buttons to access other pages.
                hbox:
                    style_prefix "page"

                    xalign 0.5
                    yalign 1.0

                    spacing gui.page_spacing

                    textbutton _("<"):
                        action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A"):
                            action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q"):
                            action FilePage("quick")

                    ## range(1, 10) gives the numbers from 1 to 9.
                    for page in range(1, 10):
                        textbutton "[page]":
                            action FilePage(page)

                    textbutton _(">"):
                        action FilePageNext()

        button:

            key_events True
            xalign 1.0
            action the_page.Toggle()
            hbox:
                
                xsize 380
                ysize 50
                input:
                    style "page_label_text"
                    align (0.0, 0.5)
                    prefix "Go To Page: "
                    allow [str(i) for i in range(0,10)]
                    length 3
                    value the_page
                textbutton "Go":
                    text_style "page_label_text"
                    align (1.0,0.5)
                    if _go_to_page.isdigit():
                        action FilePage(int(_go_to_page)),SetVariable("_go_to_page",""),the_page.Disable()

                if _go_to_page.isdigit():
                    key "input_enter" action FilePage(int(_go_to_page)),SetVariable("_go_to_page",""),the_page.Disable()

    screen replays_custom():

        tag menu

        default main_girls_replay = ["Ayumi", "Emiko", "Haruka", "Maiya"]
        default girls = ["Ayumi", "Emiko", "Haruka", "Maiya", "Others"]
        default landing_page = 0
        default page_name = girls[landing_page]
        default unlocked = False

        use game_menu(_("Replays"), scroll="viewport"):

            style_prefix "about"

            vpgrid:
                cols 2
                spacing 50

                if girls[landing_page] in main_girls_replay:
                    for i in _cheats_replay:
                        if i.girl == girls[landing_page]:
                            if i.sharing and not persistent._sharing_content:
                                continue
                            else:
                                imagebutton:
                                    style "menu_text_button_custom"
                                    if not persistent._unlocked_gallery:
                                        insensitive "Locked_Replay_idle"
                                    idle i.label + "_idle"
                                    hover i.label + "_hover"
                                    at fzoom
                                    if getattr(persistent, i.flag):
                                        action Replay(i.label, scope=i.dic, locked=False)
                                    else:
                                        action Replay(i.label, scope=i.dic, locked=not persistent._unlocked_gallery)
                else:
                    for i in _cheats_replay:
                        if i.girl not in main_girls_replay:
                            if i.sharing and not persistent._sharing_content:
                                continue
                            else:
                                imagebutton:
                                    style "menu_text_button_custom"
                                    if not persistent._unlocked_gallery:
                                        insensitive "Locked_Replay_idle"
                                    idle i.label + "_idle"
                                    hover i.label + "_hover"
                                    at fzoom
                                    if getattr(persistent, i.flag):
                                        action Replay(i.label, scope=i.dic, locked=False)
                                    else:
                                        action Replay(i.label, scope=i.dic, locked=not persistent._unlocked_gallery)

        vbox:
            spacing 15
            xalign 0.2
            yalign 0.3
            for girl in girls:
                if girl in main_girls_replay:
                    if persistent._show_empty_gallery:
                        imagebutton:
                            style "menu_text_button_custom"
                            idle "images/hud/rounded portraits (students)/" + girl + " idle.png"
                            hover "images/hud/rounded portraits (students)/" + girl + " hover.png"
                            selected_idle "images/hud/rounded portraits (students)/" + girl + " hover.png"
                            at academybookzoom
                            action SetScreenVariable("landing_page", girls.index(girl))
                    elif GetEmptyReplays(girl):
                        imagebutton:
                            style "menu_text_button_custom"
                            idle "images/hud/rounded portraits (students)/" + girl + " idle.png"
                            hover "images/hud/rounded portraits (students)/" + girl + " hover.png"
                            selected_idle "images/hud/rounded portraits (students)/" + girl + " hover.png"
                            at academybookzoom
                            action SetScreenVariable("landing_page", girls.index(girl))
                else:
                    if persistent._show_empty_gallery:
                        imagebutton:
                            style "menu_text_button_custom"
                            idle "images/hud/rounded portraits (students)/Unknown idle.png"
                            hover "images/hud/rounded portraits (students)/Unknown hover.png"
                            selected_idle "images/hud/rounded portraits (students)/Unknown hover.png"
                            at academybookzoom
                            action SetScreenVariable("landing_page", len(girls)-1)
                    elif GetEmptyReplays(girl):
                        imagebutton:
                            style "menu_text_button_custom"
                            idle "images/hud/rounded portraits (students)/Unknown idle.png"
                            hover "images/hud/rounded portraits (students)/Unknown hover.png"
                            selected_idle "images/hud/rounded portraits (students)/Unknown hover.png"
                            at academybookzoom
                            action SetScreenVariable("landing_page", len(girls)-1)

        if girls[landing_page] in main_girls_replay:
            image "images/hud/Replay/" + girls[landing_page] + ".png"

        $ page_name = girls[landing_page]
        $ text_color = "FFFFFF"

        if page_name == "Ayumi":
            $ text_color = ay.who_args['color']
            $ girl_name = ay
        elif page_name == "Emiko":
            $ text_color = em.who_args['color']
            $ girl_name = em
        elif page_name == "Haruka":
            $ text_color = ha.who_args['color']
            $ girl_name = ha
        elif page_name == "Maiya":
            $ text_color = ma.who_args['color']
            $ girl_name = ma
        else:
            $ text_color = "FFFFFF"
            $ girl_name = "Secondary Characters"

        text "{font=[gui.name_text_font]}{color=[text_color]}{size=64}[girl_name]":
            outlines [ (3, "#00000080", 1, 2) ]
            xanchor 0.5
            xalign 0.465
            yalign 0.07
        vbox:
            style_prefix "replay_unlocked"
            textbutton "Sharing %s"%("On".zfill(2) if persistent._sharing_content else "Off") action ToggleField(persistent, "_sharing_content")
            if not Unlock_Replays().get_selected():
                textbutton ("Lock Replays".zfill(4) if persistent._unlocked_gallery else "Unlock Replays"):
                    action ToggleField(persistent, "_unlocked_gallery")
            textbutton "{} Empty Replays".format("View" if not persistent._show_empty_gallery else "Hide") action ToggleField(persistent, "_show_empty_gallery")
            

        key "K_e" action ToggleField(persistent, "_show_empty_gallery")
        key "K_l" action ToggleField(persistent, "_unlocked_gallery")
        key "K_s" action ToggleField(persistent, "_sharing_content")

    transform input_appear(t=1):
        alpha 0.0
        easein t alpha 1.0

    screen callstack():
        $ current_line = renpy.get_filename_line()
        $ callstack = renpy.get_return_stack()
        $ mode = renpy.get_mode()
        vbox:
            ypos 50
            if mode == "menu":
                text _("Current Line: [current_line!q]") outlines [(2, "#0009", 1, 1)] color "#0F0"
                text _("Mode: [mode]") outlines [(2, "#0009", 1, 1)] color "#0F0"
            if callstack:
                text _("CallStack: [callstack!q]") outlines [(2, "#0009", 1, 1)] color "#0F0"
                textbutton "Clear Stack" action Function(renpy.set_return_stack, [])

    screen tooltip(tooltip, **kwargs):
        $ f_align = kwargs.get("align", (0.5, 0.05))
        if isinstance(tooltip, str):
            pass
        elif isinstance(tooltip, list):
            $ tooltip = "\n".join(tooltip)
        if tooltip:
            frame:
                at choice_appear(.5)
                align f_align
                style_prefix "tooltip"
                hbox:
                    text tooltip size gui.text_size

    screen cheat_input():
        modal True
        add "gui/overlay/confirm.png"
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 20
            ypadding 15
            xminimum 400
            yminimum 200
            vbox:
                spacing 10
                xalign 0.5
                text _("Enter Cheat Code"):
                    xalign 0.5
                    size 30

                input default "":
                    pixel_width(500)
                    value VariableInputValue("cheat_input_text")
                    xalign 0.5

                textbutton _("Confirm"):
                    xalign 0.5
                    ypos 15
                    style "menu_text_button_custom"
                    text_style "menu_text_button_custom"
                    action Hide("cheat_input"), Function(cheat_confirm, cheat_code=cheat_input_text)
        
        vbox:
            xalign 0.5
            yalign 0.15
            spacing 50
            text _("{size=44}Cheat Unlock Code:"):
                style "menu_text_button_custom"
                xalign 0.5
                yalign 0.5
            hbox:
                xalign 0.5
                spacing 50
                text "[gui.built_in_cheats]":
                    style "menu_text_button_custom"
                    xalign 0.5
                    yalign 0.5
                    color "#F00"
            vbox:
                ypos -25
                xalign 0.5
                spacing 5
                text _("{size=18}!! Edit Students Stats !!"):
                    style "menu_text_button_custom"
                    xalign 0.5
                    text_align 0.5
                text _("{size=18}!! Unlock Gallery !!"):
                    style "menu_text_button_custom"
                    xalign 0.5
                    text_align 0.5
                text _("{size=18}!! Edit Academy Stats !!"):
                    style "menu_text_button_custom"
                    xalign 0.5
                    text_align 0.5

    screen notify_item(msg, use_atl=True):
        zorder 1500
        tag notify_item

        style_prefix "notify_item"

        frame:

            if use_atl: # ATL not used for history

                at custom_notify_appear

            text msg text_align 0.5

    screen notify_container():
        zorder 1000
        tag notify_container
        fixed:
            align (0.5,0.05)
            #pos (5, 50)

            vbox:
                xalign 0.5
                yalign 0.05
                #xmaximum 250
                spacing 5

                # We index on the time the notification was added as that
                # is unique. Using index helps manage the ATL nicely
                if notify_messages:
                    for msg_info index msg_info[1] in reversed(notify_messages):
                        if msg_info[1] > time.time() - notify_duration:
                            use notify_item(msg_info[0])

    transform custom_notify_appear():
        xalign 0.5
        ypos 130

        yoffset -15.0 yzoom 0.0 zoom 0.7 alpha 0.5

        easein 1.0 yoffset 0.0 yzoom 1.0 zoom 1.0 alpha 1.0

        pause 2.0

        easeout 1.0 yoffset -15.0 yzoom 0.0 zoom 0.1 alpha 0.0

        pause .5

        function finish_notify

init 1:# Screens Cheats

    screen cheats():
        button:
            key "rollback" action NullAction()
            xysize (config.screen_width, config.screen_height)
            action NullAction()
        if not char_dict_female:
            timer .1 action SetVariable("char_dict_female", Generate_Char_Dict(_cheat_chars_data())[0])
        if not char_dict_male:
            timer .1 action SetVariable("char_dict_male", Generate_Char_Dict(_cheat_chars_data())[1])
        on "show" action Show("office_hud_cheats")
        on "hide" action Hide("office_hud_cheats")
        default default_sttrust = academy.sttrust
        default default_grades = academy.grades
        default default_apl = academy.apl
        default default_viewership = academy.viewership
        default default_board = academy.board
        default default_gradesthreshold = academy.gradesthreshold
        default default_outsidepressure = academy.outsidepressure
        default default_focus = academy.focus
        default default_disciplinary = academy.disciplinary 
        default default_lawsuitprogress = academy.lawsuitprogress
        $ tooltip = GetTooltip()
        zorder 160
        modal True
        image "blackoverlay"
        image "students_book"
        default students_book_page = 1
        default students_report_show = False
        #default students_book_example = False
        default perknametext = ""
        default student_replay = ""
        default staff_report_show = False
        default make_sextstat_available_staff = True
        default make_sextstat_available_students = True
        default mc_name = VariableInputValue('mcname', False)

        default management_page = 1
        key ("game_menu", "K_5", "K_KP_5"):
            if students_report_show:
                action SetScreenVariable("rstd", "Student"), SetScreenVariable("students_report_show", False),With(dissolve)
            elif staff_report_show:
                action SetScreenVariable("rstd", "Student"), SetScreenVariable("staff_report_show", False),With(dissolve)
            else:
                action Hide("cheats", transition=d),With(dissolve)
        key ("K_1", "K_KP_1") action SetScreenVariable("students_book_page", 1), SetScreenVariable("management_page", 1), SetScreenVariable("students_report_show", False),With(dissolve)
        key ("K_2", "K_KP_2") action SetScreenVariable("students_book_page", 1), SetScreenVariable("management_page", 2), SetScreenVariable("students_report_show", False),With(dissolve)
        key ("K_3", "K_KP_3") action SetScreenVariable("students_book_page", 3), SetScreenVariable("students_report_show", False),With(dissolve)
        key ("K_4", "K_KP_4") action SetScreenVariable("students_book_page", 2), SetScreenVariable("staff_report_show", False),With(dissolve)

        vbox:
            xpos 1650
            ypos 50
            spacing 10
            textbutton "1. Academy":
                style "menu_text_button_custom"
                text_style "menu_text_button_custom_cheats"
                xalign 0.5
                action SetScreenVariable("students_book_page", 1), SetScreenVariable("management_page", 1), SetScreenVariable("students_report_show", False),With(dissolve)
                selected (students_book_page == 1 and management_page == 1)
            textbutton "2. Management":
                style "menu_text_button_custom"
                text_style "menu_text_button_custom_cheats"
                xalign 0.5
                action SetScreenVariable("students_book_page", 1), SetScreenVariable("management_page", 2), SetScreenVariable("students_report_show", False),With(dissolve)
                selected (students_book_page == 1 and management_page == 2)
            textbutton "3. Students":
                style "menu_text_button_custom"
                text_style "menu_text_button_custom_cheats"
                xalign 0.5
                action SetScreenVariable("students_book_page", 3), SetScreenVariable("students_report_show", False),With(dissolve)
                selected students_book_page == 3
            textbutton "4. Staff/Teachers":
                style "menu_text_button_custom"
                text_style "menu_text_button_custom_cheats"
                xalign 0.5
                action SetScreenVariable("students_book_page", 2), SetScreenVariable("staff_report_show", False),With(dissolve)
                selected students_book_page == 2
            textbutton "5. Return":
                style "menu_text_button_custom"
                text_style "menu_text_button_custom_cheats"
                xalign 0.5
                if students_report_show:
                    action SetScreenVariable("rstd", "Student"), SetScreenVariable("students_report_show", False),With(dissolve)
                elif staff_report_show:
                    action SetScreenVariable("rstd", "Student"), SetScreenVariable("staff_report_show", False),With(dissolve)
                else:
                    action Hide("cheats", transition=d),ClearFocus("diff_drop"),With(dissolve)

        if students_book_page == 1 and students_report_show == False:
            text "{size=-8}{color=000000}Management":
                xalign 0.3
                yalign 0.93
        elif students_book_page == 3 and students_report_show == False:
            text "{size=-8}{color=000000}Students":
                xalign 0.3
                yalign 0.93
        elif students_book_page == 2 and students_report_show == False:
            text "{size=-8}{color=000000}Staff & Teachers":
                xalign 0.3
                yalign 0.93
        elif students_report_show == True and rstd != "":
            text "{color=000000}" + "{size=-12}" + rstd.surname + ",{/size}{size=-8} " + rstd.name + " Summary":
                xalign 0.3
                yalign 0.93

        if students_book_page == 1:
            text "{=cheats_inline_50}Manage Academy":
                xpos 435
                ypos 75
            text "{=cheats_inline_50}{u}".ljust(77):
                xpos 345
                ypos 110
            vbox:
                xpos 345
                ypos 175
                text "{size=38}{color=#000000}Test Difficulty:":
                    xpos 150
                hbox:
                    ypos 50
                    xpos 10
                    spacing 20
                    imagebutton:
                        idle "easy_button idle"
                        hover "easy_button hover"
                        selected_idle "easy_button selected_idle"
                        selected_hover "easy_button selected_hover"
                        style "menu_text_button_custom"
                        action SetVariable("academy.difficulty", 0)
                    imagebutton:
                        idle "normal_button idle"
                        hover "normal_button hover"
                        selected_idle "normal_button selected_idle"
                        selected_hover "normal_button selected_hover"
                        style "menu_text_button_custom"
                        action SetVariable("academy.difficulty", 1)
                    imagebutton:
                        idle "hard_button idle"
                        hover "hard_button hover"
                        selected_idle "hard_button selected_idle"
                        selected_hover "hard_button selected_hover"
                        style "menu_text_button_custom"
                        action SetVariable("academy.difficulty", 2)   
                text "{size=20}{color=#000000}  At the end of each week, the students will perform an exam that will evaluate their Academic Ability.":
                    ypos 70
                    xmaximum 570
                vbox:
                    ypos 85
                    spacing 25
                    text "{size=38}{color=#000000}Academy Policies:":
                        xpos 150
                        xalign 0.5
                    vbox:
                        spacing 20
                        vbox:
                            spacing 10
                            hbox:
                                spacing 10
                                text "{=cheats_inline_25}Teaching Method:"
                                text "{=cheats_inline_15}%s"%("Punishment Focus" if academy.focus == 0\
                                    else "Relaxed" if academy.focus == 1\
                                    else "Teaching Focus" if academy.focus == 2\
                                    else "Corruption Focus"):
                                        yalign 0.6
                            hbox:
                                spacing 10
                                frame:
                                    textbutton "{size=13}Punishment Focus":
                                        yalign 0.5
                                        if currentdate.daytime == 0:
                                            action SetVariable("academy.focus", 0)
                                        else:
                                            tooltip "Some Management options are only available during Early Morning periods!"
                                            action NullAction()
                                frame:
                                    textbutton "{size=15}Relaxed Focus":
                                        xalign 0.5
                                        if currentdate.daytime == 0:
                                            action SetVariable("academy.focus", 1)
                                        else:
                                            tooltip "Some Management options are only available during Early Morning periods!"
                                            action NullAction()
                                frame:
                                    textbutton "{size=15}Teaching Focus":
                                        xalign 0.5
                                        if currentdate.daytime == 0:
                                            action SetVariable("academy.focus", 2)
                                        else:
                                            tooltip "Some Management options are only available during Early Morning periods!"
                                            action NullAction()
                                if academy.apl >= 40:
                                    frame:
                                        textbutton "{size=15}Corruption Focus":
                                            xalign 0.5
                                            if currentdate.daytime == 0:
                                                action SetVariable("academy.focus", 3)
                                            else:
                                                tooltip "Some Management options are only available during Early Morning periods!"
                                                action NullAction()
                        vbox:
                            spacing 10
                            hbox:
                                spacing 10
                                text "{=cheats_inline_25}Disciplinary Method:"
                                text "{=cheats_inline_15}%s"%("Verbal Warning" if academy.disciplinary == 0 else "Spanking"):
                                    yalign 0.6                                                                                         
                            if academy.apl >= 10:
                                hbox:
                                    spacing 5
                                    frame:
                                        textbutton "{size=13}Verbal Warning":
                                            yalign 0.6
                                            action SetVariable("academy.disciplinary", 0)
                                    frame:
                                        textbutton "{size=13}Spanking":
                                            yalign 0.6
                                            action SetVariable("academy.disciplinary", 1)
                            else:
                                hbox:
                                    spacing 5
                                    frame:
                                        textbutton "{size=13}Verbal Warning":
                                            yalign 0.6
                                            action SetVariable("academy.disciplinary", 0)

                        vbox:
                            spacing 2
                            hbox:
                                spacing 10
                                text "{=cheats_inline_25}Academy Perks:"
                            hbox:
                                spacing 5
                                text "{size=20}{color=#000000}Active:"
                                text "{=cheats_inline_15}[perknametext]":
                                    yalign 0.6

                            hbox:
                                spacing 5
                                text "{size=20}{color=#000000}Inactive:"

            vbox:
                xsize 580
                ysize config.screen_height-200
                ypos 100
                xpos 950
                vpgrid:
                    style_prefix "cheat_management"
                    mousewheel True
                    draggable True
                    pagekeys True
                    scrollbars "vertical"
                    cols 1
                    if management_page == 1:
                        vbox:
                            label _("Student Trust:\n{color=#000}%s{/color}"%academy.sttrust)
                            bar:
                                value VariableValue("academy.sttrust",
                                    range=100,
                                    style="slider",
                                    max_is_zero=False,
                                    step=1,
                                    force_step=True)
                            textbutton "Default" action SetVariable("academy.sttrust", default_sttrust)
                        vbox:
                            label _("Grades:\n{color=#000}%s{/color}"%academy.grades)
                            bar:
                                value VariableValue("academy.grades",
                                    range=100,
                                    style="slider",
                                    max_is_zero=False,
                                    step=1,
                                    force_step=True)
                            textbutton "Default" action SetVariable("academy.grades", default_grades)
                        vbox:
                            label _("Academic Perversion Level:\n{color=#000}%s{/color}"%academy.apl)
                            bar:
                                value VariableValue("academy.apl",
                                    range=100,
                                    style="slider",
                                    max_is_zero=False,
                                    step=1,
                                    force_step=True)
                            textbutton "Default" action SetVariable("academy.apl", default_apl)
                        vbox:
                            label _("Viewership:\n{color=#000}%s{/color}"%academy.viewership)
                            bar:
                                value VariableValue("academy.viewership",
                                    range=100000,
                                    style="slider",
                                    max_is_zero=False,
                                    step=1,
                                    force_step=True)
                            textbutton "Default" action SetVariable("academy.viewership", default_viewership)
                        vbox:
                            label _("Board Happiness:\n{color=#000}%s{/color}"%academy.board)
                            bar:
                                value VariableValue("academy.board",
                                    range=100,
                                    style="slider",
                                    max_is_zero=False,
                                    step=1,
                                    force_step=True)
                            textbutton "Default" action SetVariable("academy.board", default_board)

                    elif management_page == 2:
                        vbox:
                            label _("Grades Threshold:\n{color=#000}%s{/color}"%academy.gradesthreshold)
                            bar:
                                value VariableValue("academy.gradesthreshold",
                                    range=100,
                                    style="slider",
                                    max_is_zero=False,
                                    step=1,
                                    force_step=True)
                            textbutton "Default":
                                action SetVariable("academy.gradesthreshold", default_gradesthreshold)

                        vbox:
                            label _("Outside Pressure:\n{color=#000}%s{/color}"%academy.outsidepressure)
                            bar:
                                value VariableValue("academy.outsidepressure",
                                    range=100,
                                    style="slider",
                                    max_is_zero=False,
                                    step=1,
                                    force_step=True)
                            textbutton "Default":
                                action SetVariable("academy.outsidepressure", 0)

                        vbox:
                            textbutton _("Lawsuit Progress:\n{color=#000}%s{/color}"%academy.lawsuitprogress if academy.lawsuit else "MC Lawsuit"):
                                action ToggleVariable("academy.lawsuit") 
                                text_bold False
                            if academy.lawsuit:
                                bar:
                                    value VariableValue("academy.lawsuitprogress",
                                        range=100,
                                        style="slider",
                                        max_is_zero=False,
                                        step=1,
                                        force_step=True)
                                textbutton "Default":
                                    action SetVariable("academy.lawsuitprogress", 0)

        elif students_book_page == 2:
            $ reportbookstaff = []
            for Actor in academy.staff:
                if not Actor in reportbookstaff:
                    $ reportbookstaff.append(Actor)

            $ reportbookstaff.sort(key=lambda x: x.name)
            if staff_report_show:
                text "{=cheats_inline}{u}".ljust(110):
                    xpos 347
                    ypos 338
                image "[rstd.nametag]_portrait":
                    zoom 0.25
                    xpos 345
                    ypos 86
                text "{=cheats_inline_50}{size=25}[rstd.surname],{/size} [rstd.name]":
                    xpos 600
                    ypos 135
                    xmaximum 250

                text "{=cheats_inline_40}{u} PERSONAL INFORMATION {/u}":
                    xpos 1000
                    ypos 80
                vbox:
                    xpos 980
                    ypos 160
                    spacing 15
                    xsize 580
                    hbox:
                        spacing 15
                        text "{=cheats_inline}{u}FULL NAME:{/u}"
                        if rstd.nametag == "protag":
                            text "{=cheats_inline}[rstd.surname]"
                            button:
                                key_events True
                                action mc_name.Toggle()

                                input:
                                    id "input"
                                    style "cheats_inline"
                                    length 26
                                    yoffset -7
                                    value mc_name
                        else:
                            text "{=cheats_inline}[rstd.surname] [rstd.name]"
                    hbox:
                        spacing 15
                        text "{=cheats_inline}{u}GENDER:{/u}"
                        if rstd.gender == 0:
                            text "{=cheats_inline}Female"
                        elif rstd.gender == 1:
                            text "{=cheats_inline}Male"
                        else:
                            text "{=cheats_inline}Other"
                    #hbox:
                    #    spacing 15
                    #    text "{=cheats_inline}{u}AGE:{/u}"
                    #    text "{=cheats_inline}[rstd.age]"
                    #hbox:
                    #    spacing 15
                    #    text "{=cheats_inline}{u}HEIGHT:{/u}"
                    #    text "{=cheats_inline}[rstd.height] m"
                    #hbox:
                    #    spacing 15
                    #    text "{=cheats_inline}{u}WEIGHT:{/u}"
                    #    text "{=cheats_inline}[rstd.weight] kg"
                    if make_sextstat_available_staff and rstd.gender == 0:
                        text "{=cheats_inline_40}{u} SEX STATS {/u}" xalign 0.5
                        for stat, stat_val in rstd.sexstats.items():
                            hbox:
                                spacing 15
                                text "{=cheats_inline}{u}[stat!c]:{/u}"
                                text "{=cheats_inline}[stat_val]"

            else:
                vbox:
                    xpos 345
                    ypos 70
                    spacing 20
                    text "{size=38}{color=#000000}Staff Members:":
                        xpos 150
                    vpgrid:
                        spacing 10
                        style_prefix "cheats_student"
                        ysize config.screen_height-300
                        xsize 560
                        xfill True
                        cols 1
                        mousewheel True
                        draggable True
                        scrollbars "vertical"
                        for Actor in academy.staff:
                            hbox:
                                spacing 20
                                imagebutton:
                                    idle Actor.nametag + "_portrait"
                                    hover Transform(Actor.nametag + "_portrait", matrixcolor=BrightnessMatrix(0.2))
                                    hover_sound "audio/sfx/button_h.mp3"
                                    activate_sound "audio/sfx/page1.mp3"
                                    at academybookzoom
                                    if staff_report_show == False:
                                        action SetScreenVariable("rstd", Actor), SetScreenVariable("staff_report_show", True)
                                    elif rstd <> Actor:
                                        action SetScreenVariable("rstd", Actor)
                                    else:
                                        action SetScreenVariable("rstd", "Student"), SetScreenVariable("staff_report_show", False)
                                vbox:
                                    spacing -5
                                    ypos -35
                                    text "{color=#000000}{u}".ljust(60):
                                        ypos -4
                                    text "{size=15}{color=#000000}{font=gui/fonts/CrimsonText-SemiBold.ttf}{i}[Actor.title]"
                                    text "{size=30}{color=#000000}{font=gui/fonts/CrimsonText-SemiBold.ttf}{size=22}[Actor.surname],{/size} [Actor.c]{/font}{/color}{/size}":
                                        xmaximum 480
                                    if Actor.name in [i.girl for i in _cheats_replay]:
                                            textbutton "Replays ({})".format(sum(1 for i in _cheats_replay if i.girl == Actor.name)):
                                                text_style "replay_cheat"
                                                style "replay_cheat"
                                                action SetScreenVariable("student_replay", Actor.name), CaptureFocus("diff_drop")
                vbox:
                    xpos 970
                    ypos 70
                    spacing 20
                    text "{size=38}{color=#000000}Teachers:":
                        xpos 200
                    vpgrid:
                        spacing 10
                        style_prefix "cheats_student"
                        ysize config.screen_height-300
                        xsize 560
                        xfill True
                        cols 1
                        mousewheel True
                        draggable True
                        scrollbars "vertical"
                        for Teacher in academy.teachers:
                            hbox:
                                spacing 20
                                imagebutton:
                                    idle Teacher.nametag + "_portrait"
                                    hover Transform(Teacher.nametag + "_portrait", matrixcolor=BrightnessMatrix(0.2))
                                    hover_sound "audio/sfx/button_h.mp3"
                                    activate_sound "audio/sfx/page1.mp3"
                                    at academybookzoom
                                    if staff_report_show == False:
                                        action SetScreenVariable("rstd", Teacher), SetScreenVariable("staff_report_show", True)
                                    elif rstd <> Teacher:
                                        action SetScreenVariable("rstd", Teacher)
                                    else:
                                        action SetScreenVariable("rstd", "Student"), SetScreenVariable("staff_report_show", False)
                                vbox:
                                    spacing -5
                                    ypos -35
                                    text "{color=#000000}{u}".ljust(60):
                                        ypos -4
                                    text "{size=15}{color=#000000}{font=gui/fonts/CrimsonText-SemiBold.ttf}{i}[Teacher.title]"
                                    text "{size=30}{color=#000000}{font=gui/fonts/CrimsonText-SemiBold.ttf}{size=22}[Teacher.surname],{/size} [Teacher.name]{/font}{/color}{/size}":
                                        xmaximum 480

        elif students_book_page == 3:
            #$ academy.students.sort(key=lambda x: x.name)
            $ reportbookstudents = []
            for Student in academy.students:
                if Student in academy.targets:
                    pass
                else:
                    $ reportbookstudents.append(Student)
            $ reportbookstudents.sort(key=lambda x: x.name)
            $ academy.targets.sort(key=lambda x: x.name)
            if students_report_show == True:                
                text "{=cheats_inline}{u}".ljust(110):
                    xpos 347
                    ypos 338
                image "[rstd.nametag]_portrait":
                    zoom 0.25
                    xpos 345
                    ypos 86
                text "{=cheats_inline_50}{size=25}[rstd.surname],{/size} [rstd.name]":
                    xpos 600
                    ypos 135
                    xmaximum 250
                if rstd.strikes >= 1:
                    textbutton "{size=20}Correct Behavior":
                        xpos 700
                        ypos 450
                        action NullAction()
                if "Rosette_Award" in rstd.topics:
                    imagebutton:
                        idle "rosetteaward"
                        hover "rosetteaward"
                        at halfzoom
                        xpos 530
                        ypos 90
                        action NullAction()
                vbox:
                    xpos 350
                    ypos 375
                    spacing 15
                    hbox:
                        spacing 10
                        text "{=cheats_inline_40}Grades:"
                        text "%s"%_student_grade_status(rstd)

                    hbox:
                        spacing 10
                        text "{=cheats_inline_40}Strikes:"
                        text "%s"%_student_strike_status(rstd)[0] xalign _student_strike_status(rstd)[1] yalign _student_strike_status(rstd)[2]
                    text "{=cheats_inline_40}Student Report:"
                    vbox:
                        ypos -20
                        if rstd == ayumi:
                            text "{size=18}{color=#000000}{i}  [rstd.surname] [rstd.name] is one of our most distinguished students. She comes from a priviledged background and studied in a very prestigious school. However, due to disagreements with her parents, they stopped paying for her education near its conclusion.":
                                xmaximum 550
                        #elif rstd == emiko:
                            # TODO emiko report
                            #pass
                        #elif rstd == haruka:
                            # TODO haruka report
                            #pass
                        #elif rstd == maiya:
                            # TODO maiya report
                            #pass
                        else:
                            text "%s"%_student_report_status(rstd)[0] xmaximum _student_report_status(rstd)[1]

                        if rstd.intelligence >= 2.5:
                            text "%s"%_student_intelligence_status(rstd,1) xmaximum 550       

                        if "Cheat_Prostitute" in rstd.topics or "BigCheat_Prostitute" in rstd.topics:
                            if rstd == rina:
                                text "{=cheats_inline_itallic}  Ms. [rstd.surname] has been linked with not only exchanging favors of sexual nature with others, but also, being in charge of organizing such unusual encounters between other students and the teachers.":
                                    xmaximum 550
                            else:
                                text "{=cheats_inline_itallic}  Our reports have concluded that this student has been selling favors, of sexual nature, in exchange of attaining higher grading.":
                                    xmaximum 550
                        if "Rosette_Award" in rstd.topics and rstd.testResult < academy.gradesthreshold:
                            text "{=cheats_inline_itallic}  An award has been given to [rstd.name], meaning that they will count as having achieved the minimum score for a success on their weekly exam result.":
                                xmaximum 550
                        elif "Cheated_Exam" in rstd.topics and rstd.testResult == 0:
                            text "{=cheats_inline_itallic}  This student has received a grading of 0 as a consequence of being caught cheating on their weekly exam.":
                                xmaximum 550
                        elif rstd.intelligence < 0.7 and rstd.testResult >= academy.gradesthreshold:
                            text "{=cheats_inline_itallic}  It has been observed that despite having not exceeded in many of our initial examinations, the student is achieving adequate performance in regards to our grading system. Some could argue that [rstd.name] is probably receiving some form of external assistance, in order to gain an advantage.":
                                xmaximum 550
                        elif rstd.intelligence >= 2.0:
                            text "%s"%_student_intelligence_status(rstd,2) xmaximum 550
                        elif rstd.intelligence >= 1.6:
                            text "%s"%_student_intelligence_status(rstd,3) xmaximum 550
                        elif rstd.intelligence >= 1.2:
                            text "{=cheats_inline_itallic}  With their notable aptitude, this student consistently achieves scores that are reliably at or above the average level, maintaining acceptable academic performance.":
                                xmaximum 550
                        elif rstd.intelligence >= 0.9:
                            text "{=cheats_inline_itallic}  This student consistently achieves scores that align with the average level, demonstrating a steady performance with occasional fluctuations both above and below the average range.":
                                xmaximum 550
                        elif rstd.intelligence >= 0.7:
                            text "{=cheats_inline_itallic}  This student typically falls below the average range, occasionally reaching the average mark and rarely exceeding it in specific circumstances.":
                                xmaximum 550
                        elif rstd.intelligence >= 0.5:
                            text "{=cheats_inline_itallic}  This student demonstrates an ongoing difficulty in keeping up with the academic pace of their peers, consistently falling short of expected standards and exhibiting a tendency towards underachievement.":
                                xmaximum 550
                        elif rstd.intelligence < 0.5:
                            text "{=cheats_inline_itallic}  This student demonstrates an evident challenge when it comes to comprehending intricate topics, showcasing either a restrictive capability to learn or a severe lack of interest that would most definitely significantly hurt their academics.":
                                xmaximum 550
                text "{=cheats_inline_40}{u} PERSONAL INFORMATION {/u}":
                    xpos 1000
                    ypos 80
                vbox:
                    xpos 980
                    ypos 160
                    spacing 15
                    hbox:
                        spacing 15
                        text "{=cheats_inline}{u}FULL NAME:{/u}"
                        text "{=cheats_inline}[rstd.surname] [rstd.name]"
                    hbox:
                        spacing 15
                        text "{=cheats_inline}{u}GENDER:{/u}"
                        if rstd.gender == 0:
                            text "{=cheats_inline}Female"
                        elif rstd.gender == 1:
                            text "{=cheats_inline}Male"
                        else:
                            text "{=cheats_inline}Other"
                    hbox:
                        spacing 15
                        text "{=cheats_inline}{u}AGE:{/u}"
                        text "{=cheats_inline}[rstd.age]"
                    hbox:
                        spacing 15
                        text "{=cheats_inline}{u}HEIGHT:{/u}"
                        text "{=cheats_inline}[rstd.height] m"
                    hbox:
                        spacing 15
                        text "{=cheats_inline}{u}WEIGHT:{/u}"
                        text "{=cheats_inline}[rstd.weight] kg"
                    vbox:
                        spacing 10
                        text "{=cheats_inline}{u}".ljust(110):
                            xalign 0.5
                            yalign 0.5
                        text "{=cheats_inline_40}{u} OTHER STATS {/u}":
                            xalign 0.5
                            yalign 0.5
                    hbox:
                        xpos -10
                        spacing 30
                        vbox:
                            spacing 15
                            text "{=cheats_inline_25}Intelligence":
                                xalign 0.5
                                yalign 0.5
                            text "%s"%_student_intelligence_lvl(rstd):
                                xalign 0.5
                                yalign 0.5

                        vbox:
                            spacing 15
                            text "{=cheats_inline_25}|":
                                xalign 0.5
                                yalign 0.5
                            text "{=cheats_inline_25}|":
                                xalign 0.5
                                yalign 0.5
                        vbox:
                            spacing 15
                            text "{=cheats_inline_25}  Affection  ":
                                xalign 0.5
                                yalign 0.5
                            if rstd.gender == 1:
                                text "{=cheats_inline_20}{i}-":
                                    xalign 0.5
                                    yalign 0.5
                                    text_align 0.5
                            else:
                                image "images/hud/heart affct.png":
                                    xalign 0.5
                                    zoom 0.75
                                text "{size=20}[rstd.affection]":
                                    outlines [ (2, "#e2aaaa80", 0, 0) ]
                                    xalign 0.5
                                    text_align 0.5
                                    ypos -83
                                text "%s"%_student_affection_status(rstd):
                                    outlines [ (2, "#00000080", 0, 0) ]
                                    ypos -60
                                    xalign 0.5
                                    text_align 0.5

                        vbox:
                            spacing 15
                            text "{=cheats_inline_25}|":
                                xalign 0.5
                                yalign 0.5
                            text "{=cheats_inline_25}|":
                                xalign 0.5
                                yalign 0.5
                        vbox:
                            spacing 15
                            text "{=cheats_inline_25}Corruption Level":
                                xalign 0.5
                                yalign 0.5
                                text_align 0.5
                            if rstd.gender == 1:
                                text "{=cheats_inline_20}{i}-":
                                    xalign 0.5
                                    yalign 0.5
                                    text_align 0.5
                            else:
                                image "images/hud/heart crrpt.png":
                                    xalign 0.5
                                    zoom 0.75
                                text "{size=20}[rstd.corruption]":
                                    outlines [ (2, "#00000080", 0, 0) ]
                                    xalign 0.5
                                    text_align 0.5
                                    ypos -83
                                text "%s"%_student_corruption_status(rstd):
                                    outlines [ (2, "#00000080", 0, 0) ]
                                    ypos -60
                                    xalign 0.5
                                    text_align 0.5   

                    vbox:
                        xsize 550
                        yoffset (-70 if rstd.gender == 0 else 90)
                        use cheat_modifier(rstd, make_sextstat_available_students)
            else:
                vbox:
                    xpos 345
                    ypos 70
                    spacing 20
                    text "{size=38}{color=#000000}Students:":
                        xpos 195
                    vbox:
                        ypos -30
                        spacing 10
                        text "{size=30}{color=#000000}Main Targets:"
                    vpgrid:
                        ypos -30
                        spacing 10
                        style_prefix "cheats_student"
                        ysize config.screen_height-300
                        xsize 560
                        xfill True
                        cols 1
                        mousewheel True
                        draggable True
                        scrollbars "vertical"
                        for Actor in academy.targets:
                            hbox:
                                spacing 20
                                imagebutton:
                                    idle Actor.nametag + "_portrait idle"
                                    hover Actor.nametag + "_portrait hover"
                                    hover_sound "audio/sfx/button_h.mp3"
                                    activate_sound "audio/sfx/page1.mp3"
                                    if students_report_show == False:
                                        action SetScreenVariable("rstd", Actor), SetScreenVariable("students_report_show", True)
                                    elif rstd <> Actor:
                                        action SetScreenVariable("rstd", Actor)
                                    else:
                                        action SetScreenVariable("rstd", "Student"), SetScreenVariable("students_report_show", False)
                                    at academybookzoom
                                vbox:
                                    spacing -5
                                    ypos -35
                                    text "{color=#000000}{u}".ljust(60):
                                        ypos -4
                                    text "{=cheats_inline_15}{font=gui/fonts/CrimsonText-SemiBold.ttf}{i}[Actor.title]"
                                    text "{=cheats_inline}{size=22}[Actor.surname],{/size} [Actor.name]":
                                        xmaximum 480
                                    if Actor.name in [i.girl for i in _cheats_replay]:
                                        textbutton "Replays ({})".format(sum(1 for i in _cheats_replay if i.girl == Actor.name)):
                                            text_style "replay_cheat"
                                            style "replay_cheat"
                                            action SetScreenVariable("student_replay", Actor.name), CaptureFocus("diff_drop")
                vbox:
                    xpos 970
                    ypos 70
                    spacing 20
                    text "{size=38}{color=#000000}Students:":
                        xpos 202
                    vpgrid:
                        spacing 10
                        style_prefix "cheats_student"
                        ysize config.screen_height-300
                        xsize 560
                        xfill True
                        cols 1
                        mousewheel True
                        draggable True
                        scrollbars "vertical"
                        for Student in reportbookstudents:
                            hbox:
                                spacing 20
                                imagebutton:
                                    at studentszoom
                                    idle Student.nametag + "_portrait idle"
                                    hover Student.nametag + "_portrait hover"
                                    hover_sound "audio/sfx/button_h.mp3"
                                    activate_sound "audio/sfx/page1.mp3"
                                    if students_report_show == False:
                                        action SetScreenVariable("rstd", Student), SetScreenVariable("students_report_show", True), 
                                    elif rstd <> Student:
                                        action SetScreenVariable("rstd", Student)                    
                                    else:
                                        action SetScreenVariable("rstd", "Student"), SetScreenVariable("students_report_show", False)
                                vbox:
                                    spacing -10
                                    ypos -35
                                    text "{color=#000000}{u}".ljust(60):
                                        ypos -4
                                    text "{=cheats_inline_15}{font=gui/fonts/CrimsonText-SemiBold.ttf}{i}[Student.title]"
                                    text "{=cheats_inline}{size=22}[Student.surname],{/size} [Student.name]":
                                        xmaximum 480
                                    if Student.name in [i.girl for i in _cheats_replay]:
                                        textbutton "Replays ({})".format(sum(1 for i in _cheats_replay if i.girl == Student.name)):
                                            text_style "replay_cheat"
                                            style "replay_cheat"
                                            action SetScreenVariable("student_replay", Student.name), CaptureFocus("diff_drop")

        if GetFocusRect("diff_drop"):
            $ replay_ysize = ((config.screen_height//2) if sum(1 for i in _cheats_replay if i.girl == student_replay) > 1 else 270)
            $ mto = sum(1 for i in _cheats_replay if i.girl == student_replay) > 1
            $ mtt = sum(1 for i in _cheats_replay if i.girl == student_replay) > 2
            $ ono = sum(1 for i in _cheats_replay if i.girl == student_replay) == 1
            dismiss action ClearFocus("diff_drop"),SetScreenVariable("student_replay", '')
            key "game_menu" action ClearFocus("diff_drop"),SetScreenVariable("student_replay", '')
            button:
                key "rollback" action NullAction()
                xysize (config.screen_width, config.screen_height)
                action ClearFocus("diff_drop"),SetScreenVariable("student_replay", '')
            nearrect:
                prefer_top False
                focus "diff_drop"
                frame:

                    at choice_appear(.5)
                    style_prefix "tooltip"
                    left_padding (15 if mtt or ono else 5)
                    right_padding 5
                    modal True
                    has vbox
                    vpgrid:
                        id "replays"
                        cols 2
                        mousewheel True
                        draggable True
                        scrollbars ("vertical" if mtt else None)
                        ysize 265
                        xsize (410*2 if mto else 400)
                        xspacing (15 if mto else 0)
                        xfill (True if mto else False)
                        xalign 0.5
                        for rep in _cheats_replay:
                            if student_replay == rep.girl:
                                vbox:
                                    xalign 0.5
                                    imagebutton:
                                        style "menu_text_button_custom"
                                        idle rep.idle
                                        hover rep.hover
                                        insensitive rep.insensitive
                                        action Replay(rep.label, scope=rep.dic, locked=False)
                                        tooltip rep.desc
                                        xalign 0.5
                                        sensitive getattr(persistent, rep.flag)
                                    textbutton ("Unlock" if not getattr(persistent, rep.flag) else "Lock"):
                                        action ToggleField(persistent, rep.flag)
                                        selected getattr(persistent, rep.flag) == None
                                        text_size gui.text_size-7
                                        xalign 0.5
                    textbutton "Close" action ClearFocus("diff_drop"),SetScreenVariable("student_replay", '') xalign 0.5
                    key "game_menu" action ClearFocus("diff_drop"),SetScreenVariable("student_replay", '')

        if tooltip:
            nearrect:
                focus "tooltip"
                prefer_top True
                frame:
                    at choice_appear(.5)
                    style_prefix "tooltip"
                    hbox:
                        text tooltip

    screen office_hud_cheats():
        zorder 170
        image "hud top"
        default expandofficehud = False
        default expandmanagehud = False
        default boardmessagetoggle = False
        default liveEvent = False
        default callstudenthud = False
        default dailyactionhud = False

        hbox:
            spacing 15
            ypos 11
            xpos 15
            hbox:
                image _student_trust_status(academy.sttrust) ypos -6
            image "hudline"
            hbox:
                spacing 14
                image "academicssymbol":
                    ypos -1
                text "%s"%_grades_status(academy.grades) ypos -6
            image "hudline"
            hbox:
                spacing 14
                image "sexsymbol"
                text "%s"%_sex_symbol_status(academy.apl):
                    ypos -3
            image "hudline"
            hbox:
                spacing 14
                image "viewership":
                    zoom 0.19
                    ypos 2
                text "%s"%_viewership_status(academy.viewership) ypos -3

        textbutton "Board Satisfaction:":
            text_outlines [ (2, "#00000080", 0, 1) ]
            action NullAction()
            tooltip "%s"%_board_status(academy.board)
            ypos -2
            xpos 660
        bar:
            value academy.board
            range 100
            xysize (270, 20)
            ypos 15
            xpos 990

        $ currentperiod_output = currentdate.period[currentdate.daytime]
        $ currentweekday_output = currentdate.weekdays[currentdate.weekday]
        $ currentmonth_output = currentdate.months[currentdate.month]
        #$ currentday_output = currentdate.day

        hbox:
            ypos 24
            xpos 1350
            spacing 50
            text "{size=20}{b}[currentperiod_output]":
                outlines [ (2, "#00000080", 0, 1) ]
                yanchor 0.5
            text "{size=20}| ":
                outlines [ (2, "#00000080", 0, 1) ]
                yanchor 0.5
            text "{size=18}[currentweekday_output]":
                outlines [ (2, "#00000080", 0, 1) ]
                #ypos 1
                yanchor 0.5
            text "{size=20}| ":
                outlines [ (2, "#00000080", 0, 1) ]
                yanchor 0.5
            text "{size=15}[currentmonth_output], [currentdate.day]":
                outlines [ (2, "#00000080", 0, 1) ]
                #ypos 5
                yanchor 0.5

    screen gym_intro_girlsstretch:
        image "gym0147"
        text "Pick a girl":
            yalign 0.85
            xalign 0.5
        if q6 == True:
            image "gym0147_0"
        imagebutton:
            focus_mask True
            idle "gym01rina idle"
            hover "gym01rina hover"
            action SetVariable("v6", 1), SetVariable("q8", True), Return(),Hide("tooltip")#, Call("gym_intro_stretch_start")
            hovered Show("tooltip", tooltip="Rina Path")
            unhovered Hide("tooltip")
        if q6 == False:
            imagebutton:
                focus_mask True
                idle "gym01nanami idle"
                hover "gym01nanami hover"
                action SetVariable("q6", True), Return(),Hide("tooltip")
                hovered Show("tooltip", tooltip="Nanami Path")
                unhovered Hide("tooltip")
                #action SetVariable("v7", v7 + 1), Call("gym_intro_stretch_start")
        imagebutton:
            focus_mask True
            idle "gym01yoko idle"
            hover "gym01yoko hover"
            action SetVariable("v8", 1), SetVariable("q8", True), Return(),Hide("tooltip")#, Call("gym_intro_stretch_start")
            hovered Show("tooltip", tooltip="Yoko Path")
            unhovered Hide("tooltip")
        imagebutton:
            focus_mask True
            idle "gym01haruka idle"
            hover "gym01haruka hover"
            action SetVariable("v9", 1), SetVariable("q8", True), Return(),Hide("tooltip")#, Call("gym_intro_stretch_start")
            hovered Show("tooltip", 
                tooltip=["Haruka Path", "Haruka Affection +1", "Board +1","Viewership +50"])
            unhovered Hide("tooltip")

    screen cheat_modifier(rstd, make_sextstat_available_students):
        $ character_selected = (char_dict_female.get(rstd.nametag) if rstd.gender == 0 else char_dict_male.get(rstd.nametag))
        $ thechar = character_selected.get("class")
        vpgrid:
            mousewheel True
            draggable True
            pagekeys True
            style_prefix "cheat_students"
            cols 1
            scrollbars "vertical"
            vbox:
                #vbox:
                #    label _("Personality")
                #    textbutton "{}".format(thechar.personality):
                #        action CyclePersonalities(thechar.personality, thechar)
                #        alternate SetField(rstd, "personality", character_selected.get("personality"))
                #        selected thechar.personality == character_selected.get("personality")
                #        tooltip "Left Click: Cycle Through Personalities\nRight Click Set Default"
                #    null height gui.text_size
                if rstd.gender == 0:
                    #vbox:
                    #    label _("Met")
                    #    textbutton "{}".format(rstd.met):
                    #        action ToggleField(rstd, "met")
                    #        alternate SetField(rstd, "met", character_selected.get("met"))
                    #        selected thechar.met == character_selected.get("met")
                    #        tooltip "Left Click: Toggle Met\nRight Click Set Default"
                    #    null height gui.text_size
                    #vbox:
                    #    label _("Available")
                    #    textbutton "{}".format(rstd.available):
                    #        action ToggleField(rstd, "available")
                    #        alternate SetField(rstd, "available", character_selected.get("available"))
                    #        selected rstd.available == character_selected.get("available")
                    #        tooltip "Left Click: Toggle Available\nRight Click Set Default"
                    #    null height gui.text_size
                    vbox:
                        label _("Virgin")
                        textbutton "{}".format("Pure Maiden" if rstd.virgin else "Horny Slut"):
                            action ToggleField(rstd, "virgin")
                            alternate SetField(rstd, "virgin", character_selected.get("virgin"))
                            selected rstd.virgin == character_selected.get("virgin")
                            tooltip "Left Click: Toggle Virgin\nRight Click Set Default"
                        null height gui.text_size
                    #vbox:
                    #    label _("Lewd: {color=#000}%s{/color}"%round(float(rstd.lewd),2))
                    #    bar:
                    #        value FieldValue(rstd,"lewd",
                    #            range=2.5,
                    #            style="slider",
                    #            max_is_zero=False,
                    #            step=.01,
                    #            force_step=True)
                    #    textbutton "Default":
                    #        action SetField(rstd, "lewd", character_selected.get("lewd"))
                #vbox:
                #    label _("Intelligence: {color=#000}%s{/color}"%round(float(rstd.intelligence),2))
                #    bar:
                #        value FieldValue(rstd,"intelligence",
                #            range=6.0,
                #            style="slider",
                #            max_is_zero=False,
                #            step=.01,
                #            offset=-3.0,
                #            force_step=True)
                #    textbutton "Default":
                #        action SetField(rstd, "intelligence", character_selected.get("intelligence"))
                vbox:#Test Result
                    label _("Test Result: {color=#000}%s{/color}"%rstd.testResult)
                    bar:
                        value FieldValue(rstd,"testResult",
                            range=100,
                            style="slider",
                            max_is_zero=False,
                            step=1,
                            force_step=True)
                    textbutton "Default":
                        action SetField(rstd, "testResult", character_selected.get("testResult"))
                if rstd.gender == 0:
                    vbox:#Affection
                        label _("Affection: {color=#000}%s{/color}"%rstd.affection)
                        bar:
                            value FieldValue(rstd,"affection",
                                range=100,
                                style="slider",
                                max_is_zero=False,
                                step=1,
                                force_step=True)
                        textbutton "Default":
                            action SetField(rstd, "affection", character_selected.get("affection"))
                    vbox:#Corruption
                        label _("Corruption: {color=#000}%s{/color}"%rstd.perversion)
                        bar:
                            value FieldValue(rstd,"perversion",
                                range=100,
                                style="slider",
                                max_is_zero=False,
                                step=1,
                                force_step=True)
                        textbutton "Default":
                            action SetField(rstd, "perversion", character_selected.get("perversion"))
                vbox:#Strikes
                    label _("Strikes: {color=#000}%s{/color}"%rstd.strikes)
                    bar:
                        value FieldValue(rstd,"strikes",
                            range=3,
                            style="slider",
                            max_is_zero=False,
                            step=1,
                            force_step=True)
                    textbutton "Default":
                        action SetField(rstd, "strikes", character_selected.get("strikes"))
                if make_sextstat_available_students and rstd.gender == 0:
                    text "{=cheats_inline_40}{u} SEX STATS {/u}" xalign 0.5
                    for stat, stat_val in rstd.sexstats.items():
                        hbox:
                            spacing 15
                            text "{=cheats_inline}{u}[stat!c]:{/u}"
                            text "{=cheats_inline}[stat_val]"

                if rstd.topics:
                    text "{=cheats_inline_40}{u} TOPICS {/u}" xalign 0.5
                    $ tops = ", ".join(rstd.topics)
                    text "{=cheats_inline}[tops]"
