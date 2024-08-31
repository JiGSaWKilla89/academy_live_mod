init python:
    shortcuts = """
{size=75}{color=FB4301}JiG{/color}{color=#000}SaW{/color} Mod Shortcuts{/size}

Toggle Textbox Shortcut: {color=FB4301}T{/color}
Toggle Choice Hotkeys: {color=FB4301}C{/color}
Toggle Custom Savenames: {color=FB4301}Shift+S{/color}
Toggle Fancy Text: {color=FB4301}Shift+F{/color}
Toggle Fancy Text Effect: {color=FB4301}E{/color}
Toggle Fancy Text Always Effect: {color=FB4301}R{/color}
Toggle Walkthrough: {color=FB4301}W{/color}
Toggle Walkthrough Choice Tooltips: {color=FB4301}Shift+T{/color}
Toggle Cheat Mod: {color=FB4301}END{/color}
Toggle Music Room: {color=FB4301}M{/color}
Toggle Notifications Stack/Standard: {color=FB4301}N{/color}
"""

    wt_choice_tooltip = """Each Choice marked with either Good Choice/Bad Choice is
just a recommendation from me.
You play the game the way you want."""

init -5 python:
    
    import operator
    import time
    config.developer = True
    config.console = True
    config.autoreload = True
    config.rollback_length = 300
    config.hard_rollback_limit = 150

    if not persistent._always_effect_title:
        persistent._always_effect_title = "None"

    if not persistent._slow_effect_title:
        persistent._slow_effect_title = "Fade"

    if not persistent._effect_delay:
        persistent._effect_delay = 0.2

    if persistent._fancy_text == None:
        persistent._fancy_text = True

    if persistent._quick_menu_state == None:
        persistent._quick_menu_state = "visible"

    if persistent._quick_menu_layout == None:
        persistent._quick_menu_layout = "bottom_center"

    if persistent._choice_hotkeys == None:
        persistent._choice_hotkeys = True
    
    if persistent._walkthrough == None:
        persistent._walkthrough = True

    if persistent._choice_tooltips == None:
        persistent._choice_tooltips = True

    if persistent._textbox_visible == None:
        persistent._textbox_visible = True

    if persistent._textbox_alpha == None:
        persistent._textbox_alpha = 0.5

    if persistent._custom_savename == None:
        persistent._custom_savename = True

    bypass_list = [
        "ADVCharacter", "ADVSpeaker", "Action", "AddToSet", "Alpha", "AlphaBlend", "AlphaDissolve", 
        "AlphaMask", "AlwaysEffectChange", "AnimatedValue", "Animation", "At", "Attribute", "AudioData", 
        "AudioPositionValue", "AutoForwardTime", "Bar", "BarValue", "Borders", "BrightnessMatrix", "Button", 
        "Call", "Camera", "CaptureFocus", "Character", "ClearFocus", "Color", "ColorMatrix", "ColorizeMatrix", 
        "ComposeTransition", "Composite", "Condition", "ConditionGroup", "ConditionSwitch", "Confirm", 
        "ContrastMatrix", "Crop", "CropMove", "CurrentScreenName", "CycleQuickMenu", "CycleQuickStates", 
        "DictEquality", "DictInputValue", "DictValue", "DisableAllInputValues", "Dissolve", "DownloadSync", 
        "Drag", "DragGroup", "DynamicCharacter", "DynamicDisplayable", "DynamicImage", "EffectDelayDisplay", 
        "EndReplay", "ExecJS", "FactorZoom", "Fade", "FancyCheck", "FancyText", "FieldEquality", "FieldInputValue", 
        "FieldValue", "FileAction", "FileCurrentPage", "FileCurrentScreenshot", "FileDelete", "FileJson", 
        "FileLoad", "FileLoadable", "FileNewest", "FilePage", "FilePageName", "FilePageNameInputValue", 
        "FilePageNext", "FilePagePrevious", "FileSave", "FileSaveName", "FileScreenshot", "FileSlotName", 
        "FileTakeScreenshot", "FileTime", "FileUsedSlots", "Fixed", "Flatten", "FontGroup", "Frame", "Function", 
        "Gallery", "GamepadCalibrate", "GamepadExists", "GetCharacterVolume", "GetFocusRect", "GetMixer", 
        "GetText", "GetTooltip", "Grid", "HBox", "Help", "Hide", "HideInterface", "HueMatrix", "IdentityMatrix", 
        "If", "Image", "ImageButton", "ImageDissolve", "ImageReference", "Input", "InputValue", "InvertMatrix", 
        "InvertSelected", "JSONDB", "Jump", "Language", "Layer", "LayeredImage", "LayeredImageProxy", "Live2D", 
        "LiveComposite", "LiveCrop", "LiveTile", "MainMenu", "Matrix", "MixerValue", "Model", "Motion", 
        "MouseDisplayable", "MouseMove", "Move", "MoveFactory", "MoveIn", "MoveOut", "MoveTransition", "Movie", 
        "MultiPersistent", "MultipleTransition", "MusicRoom", "NVLCharacter", "NVLSpeaker", "NoRollback", "Notify", 
        "Null", "NullAction", "OffsetMatrix", "OldMoveTransition", "OpacityMatrix", "OpenDirectory", "OpenURL", 
        "PY2", "Pan", "ParameterizedText", "Particles", "Pause", "PauseAudio", "Pixellate", "Placeholder", "Play", 
        "PlayCharacterVoice", "Position", "Preference", "PushMove", "Queue", "QueueEvent", "QuickLoad", 
        "QuickPositions", "QuickSave", "Quit", "RemoveFromSet", "Replay", "RestartStatement", "Return", "Revolve", 
        "RevolveInOut", "RollForward", "Rollback", "RollbackToIdentifier", "RotateMatrix", "RotoZoom", "RoundRect", 
        "SaturationMatrix", "ScaleMatrix", "ScreenVariableInputValue", "ScreenVariableValue", "Screenshot", 
        "Scroll", "SelectedIf", "SensitiveIf", "SepiaMatrix", "Set", "SetCharacterVolume", "SetDict", "SetField", 
        "SetLocalVariable", "SetMixer", "SetMute", "SetScreenVariable", "SetVariable", "SetVoiceMute", "Show", 
        "ShowMenu", "ShowTransient", "ShowingSwitch", "SideImage", "SizeZoom", "Skip", "SlottedNoRollback", 
        "SlowEffectChange", "SnowBlossom", "Solid", "Speaker", "SplineMotion", "Sprite", "SpriteManager", "Start", 
        "StaticValue", "Stop", "Style", "StylePreference", "SubTransition", "Swing", "Text", "TextBoxAlpha", 
        "TextButton", "TextSpeed", "Tile", "TintMatrix", "ToggleChoiceHotkeys", "ToggleDict", "ToggleFancyText", 
        "ToggleField", "ToggleFocus", "ToggleLocalVariable", "ToggleMute", "ToggleScreen", "ToggleScreenVariable", 
        "ToggleSetMembership", "ToggleVariable", "ToggleVoiceMute", "Tooltip", "Transform", "TransformMatrix", 
        "Unlock_Replays", "UploadSync", "VBox", "VariableInputValue", "VariableValue", "Viewport", "VoiceInfo", 
        "VoiceReplay", "VolumeDisplay", "WalkthroughData", "Window", "With", "XScrollValue", "YScrollValue", 
        "Zoom", "ZoomInOut", "absolute", "absolute_import", "achievement", "alt", "anim", "audio", "basestring", 
        "bchr", "blinds", "bord", "bubble", "build", "bypass_list", "center", "chr", "collections", "color", 
        "config", "default", "default_transition", "define", "delayed_blink", "dict", "director", "dissolve", 
        "division", "ease", "easeinbottom", "easeinleft", "easeinright", "easeintop", "easeoutbottom", 
        "easeoutleft", "easeoutright", "easeouttop", "eval", "extend", "fade", "flash", "gui", "hpunch", 
        "hyperlink_function", "hyperlink_sensitive", "hyperlink_styler", "iap", "icon", "im", "input", "inspect", 
        "irisin", "irisout", "layeredimage", "layout", "left", "library", "list", "main_menu", "menu", 
        "mouse_visible", "move", "moveinbottom", "moveinleft", "moveinright", "moveintop", "moveoutbottom", 
        "moveoutleft", "moveoutright", "moveouttop", "custom_notify_appear", "nvl_clear", "nvl_clear_next", "nvl_erase", 
        "nvl_hide", "nvl_list", "nvl_menu", "nvl_show", "nvl_show_core", "nvl_variant", "nvl_window", "object", 
        "offscreenleft", "offscreenright", "open", "os", "persistent", "pixellate", "predict_menu", "predict_say", 
        "preferences", "print", "print_function", "pushdown", "pushleft", "pushright", "pushup", "pygame_sdl2", 
        "pystr", "python_dict", "python_list", "python_object", "python_set", "quick_menu", "range", "raw_input", 
        "renpy", "reset", "right", "round", "say", "set", "set_reload", "slideawaydown", "slideawayleft", 
        "slideawayright", "slideawayup", "slidedown", "slideleft", "slideright", "slideup", "small", "sorted", 
        "squares", "store", "str", "style", "suppress_overlay", "sv", "swing", "sys", "theme", "tobytes", 
        "toggle_callstack", "toggle_skipping", "top", "topleft", "topright", "touch", "truecenter", "ui", 
        "unicode", "unicode_literals", "updater", "var_search", "voice", "voice_can_replay", "voice_replay", 
        "voice_sustain", "vpunch", "walkthrough_dict", "wipedown", "wipeleft", "wiperight", "wipeup", 
        "with_statement", "xrange", "zoomin", "zoominout", "zoomout", "always_pulse", "always_shake", "slow_fade", 
        "slow_nonsense", "slow_rotate", "slow_shake", "slow_shaking_slide", "slow_slide_down", "slow_slide_left", 
        "slow_slide_right", "slow_slide_up", "slow_typewriter", "check_dic", "find_closest_menu_before_name",
        "jg_1", "jg_2", "jg_3", "jg_s", "shortcuts", "valid_dic_items", "update_wt", "wt_choice_tooltip",
        "ToggleWalkthrough", "ToggleSavename", "ToggleChoiceToolTips", "ToggleTextbox", "WideRatio", "custom_join",
        ]

    bypass_list.extend(['Academic_Stats', 'Actor', 'Alex_grohl__Flip_phone', 'Alex_productions__Vlog_2_0', 
        'AudioCredits', 'Ayumi_Replay_List', 'Bensound__Badass', 'Bensound__Funky_suspense', 'Bensound__Sexy', 
        'BlocktoCall', 'Calendar', 'CalendarMonth', 'CalendarMonths', 'CalendarWeekstart', 'Count', 
        'Emiko_Replay_List', 'Envy__Tears', 'Foxxy_mulderr__Good_things_ahead', 'Fsm_team_escp__Acceleration', 
        'Fsm_team_escp__Rhythm_boulevard', 'Fsm_team_escp__Small_town_girl', 'Fsm_team_escp__kinetics', 
        'GameEvents', 'GetEmptyReplays', 'H_', 'Haruka_Replay_List', 'Julexar', 'Kane0ne', 'KazutoSensei', 
        'Kevin_macleod__Acid_trumpet', 'Kevin_macleod__Bossa_antigua', 'Kevin_macleod__Chill_wave', 
        'Kevin_macleod__Hard_boiled', 'Kevin_macleod__Hit_list', 'Kevin_macleod__Martini_sunset', 
        'Kevin_macleod__Master_disorder', 'Kevin_macleod__On_the_ground', 'Kevin_macleod__Slow_Jam', 
        'Kevin_macleod__Thief_in_the_night', 'Location_Events', 'Main_Academy', 'Main_Events', 
        'Main_Target_Events', 'Maiya_Replay_List', 'Maxkomusic__Urban_hip_hop', 'Minor_Events', 
        'Others_Replay_List', 'Priority_Events', 'Random_Events', 'Replay_List', 'Replays', 'Screen_Saver_List', 
        'Secondary_Events', 'SpecialThanks', 'Stat_Change', 'Student', 'Teacher', 'Weekend_Date_Dictionary', 
        'Weekend_Date_Events', 'Weekend_Dates_Function', 'Weekend_Event_Checker', 'Weekend_Main_Events', 
        'Weekend_Priority_Events', 'Zantengetsu', 'academy', 'academy_programs', 'academy_stats_dict', 
        'academy_stats_list', 'academybookzoom', 'acceleration', 'add_tolist', 'arrowupbookstudents', 'ayumi', 
        'ayumi_bathroom_0', 'ayumi_bathroom_01', 'ayumi_masturbating_0', 'ayumi_mc_fing_0', 'ayumi_office_0', 
        'ayumi_soushi_00_e', 'ayumi_soushi_00_ev', 'ayumi_soushi_01_e', 'ayumi_soushi_01_ev', 'ayumi_soushi_bj_0', 
        'ayumi_teaching_0', 'ayumi_teaching_01', 'b', 'bad_ass', 'badguy_vibe', 'bensound_sexy', 'blowjob', 
        'boardreq', 'bounties', 'bounties_to_add', 'bounty_check', 'calendar_view', 'calendarshown', 
        'calledstudent', 'calledstudent_list', 'callstudent_fix', 'cdict', 'char_dict', 'char_dict_female', 
        'char_dict_male', 'character_list', 'choice_appear', 'completed_requests', 'completed_tasks', 
        'confiscated_items', 'creampie', 'currentdate', 'currentmonth_output', 'currentperiod_output', 
        'currentweekday_output', 'd', 'd1', 'd2', 'dailyacademic', 'dailyacademics', 'dailyaction', 'dailyevent', 
        'dbug', 'dd', 'ddi', 'di', 'dice_rolled', 'displaytime', 'dscreen', 'emiko', 'emiko_gym_0', 'emiko_gym_00', 
        'emiko_prologue_0', 'emiko_virgin', 'emiko_virgin_shared', 'emiko_volley_0', 'even', 'event_preference', 
        'f', 'f1', 'f2', 'f_in', 'f_out', 'f_scene', 'fingering', 'first_kaori_even', 'first_kaori_event', 
        'fixingnamestuff', 'flipit', 'flipphone', 'fsm_team_escp_kinetics', 'funkysuspense', 'fzoom', 'genpachi', 
        'girl', 'good_things_ahead', 'halfzoom', 'haruka', 'haruka_date0', 'haruka_date01', 'haruka_late_0', 
        'haruka_main_0', 'haruka_main_01', 'haruka_office_0', 'haruka_weekend_0', 'hidetoshi', 'hiroshige', 
        'hit_list', 'humanize', 'initialapl', 'initialboard', 'input_appear', 'izo', 'jazz_ambient', 
        'jazz_loop_office', 'jazzy_discussion', 'key', 'kiyomi', 'koji', 'lower_music', 'lp', 'main', 'main_girl', 
        'maiya', 'maiya_bunny_0', 'maiya_bunny_00', 'maiya_hiro_0', 'maiya_hiro_01', 'maiya_panties', 
        'maiya_panties_0', 'maiya_panties_01', 'mako', 'marcus', 'martini_sunset', 'masaru', 
        'mc_late_main_01_loopintr', 'mc_late_main_01_loopintro', 'mccrpt', 'miyako', 'mrstd', 'nanako', 
        'new_bounties', 'newdayoffice', 'numeric_value', 'officeloop', 'officesprite', 'officesprite_left', 
        'officesprite_right', 'open_url', 'operator', 'perk', 'perkexample', 'photographer_dictionary', 'president', 
        'president_talk_0', 'president_talk_01', 'random_student', 'remove_fromlist', 'report_character_stats', 
        'report_file_chara_stats', 'report_file_stats', 'report_menu_stats', 'req', 'resume_music', 
        'rhythm_boulevard', 'rina', 'rina_blowjob_0', 'rstd', 'rtc', 'ryoichi', 'satoe', 'satsuki', 'sayoko', 
        'scooby', 'script_folder_path', 'sex', 'sex_anal', 'sex_mc', 'sexy_chillwave', 'skippingtime', 'slanted', 
        'slightly_slanted', 'slow_jam', 'small_town_girl', 'smallvpunch', 'sotaro', 'soushi', 'st', 'stat', 
        'story_progression', 'student', 'students_book_page', 'studentszoom', 'sus_dayloopjam', 'sus_jam', 'suzu', 
        'suzu_ba', 'suzu_bat', 'suzu_bat_Kawaguchi_0', 'suzu_bat_MC_0', 'suzu_spanking_0', 'temp_unavailable', 
        'temporary_bounties', 'temporary_list', 'temporary_unavailable_actors', 'threestrikes', 'toggle_cheats', 
        'type_event', 'types_of_event', 'urban_hiphop', 'vlog2', 'weekend_main_event', 'weekendloop', 
        'weekly_exam_e', 'weekly_exam_ev', 'weeklyreport', 'wordcounter', 'wordcounter_character_files', 
        'wordcounter_characters', 'wordcounter_files', 'wordcounter_hidden', 'wordcounter_menu_choices', 
        'wordcounter_same', 'xpr_tag', 'yoko', 'yoko_changing_room_0', 'yoko_dild', 'yoko_dildo', 'yoko_onahole_0', 
        'yoko_prologue_0', 'yuna', "non_finished_tasks", "event", "e", "completed_req", "s", "exam_list", "actor", 
        ])

    bypass_list = sorted(list(set([i.strip() for i in bypass_list])))

    import inspect

    def adj_bri(hex_color, levels):
        def clamp(value):
            return max(0, min(255, value))
        
        # Convert hex to RGB(A)
        hex_color = hex_color.lstrip('#')
        
        # Handle different hex lengths
        if len(hex_color) == 3:  # #RGB
            r, g, b = [int(c*2, 16) for c in hex_color]
            a = None
        elif len(hex_color) == 4:  # #RGBA
            r, g, b, a = [int(c*2, 16) for c in hex_color]
        elif len(hex_color) == 6:  # #RRGGBB
            r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
            a = None
        elif len(hex_color) == 8:  # #RRGGBBAA
            r, g, b, a = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16), int(hex_color[6:8], 16)
        else:
            raise ValueError("Invalid hex color format")
        
        # Adjust brightness
        r = clamp(r + levels)
        g = clamp(g + levels)
        b = clamp(b + levels)
        
        # Convert RGB(A) back to hex
        if a is None:
            return '#{:02X}{:02X}{:02X}'.format(r, g, b)
        else:
            return '#{:02X}{:02X}{:02X}{:02X}'.format(r, g, b, a)
    
    def var_search(name="", default=store):
        if default == persistent:
            ev = "persistent."
        elif default == gui:
            ev = "gui."
        elif default == config:
            ev = "config."
        else:
            ev = ""
        for i in dir(default):
            if not i.startswith(("_","__")):
                if name:
                    if name in i:
                        print("VAR:{} | VALUE:{}".format(i, eval(ev+i)))
                else:
                    if isinstance(eval(ev+i),renpy.character.ADVCharacter):
                        pass
                    elif i in bypass_list:
                        pass
                    else:
                        try:
                            print("VAR:{} | VALUE:{}".format(i, eval(ev+i)))
                        except Exception as e:
                            print("VAR:{}\n{}".format(i,e))

    def set_reload():
        print(config.reload)
        if config.autoreload:
            config.autoreload = False
        else:
            config.autoreload = True

    def TextSpeed():
        _cps_value = int(round(preferences.text_cps))
        _cps_value = '200' if _cps_value == 0 else _cps_value
        return _cps_value

    def AutoForwardTime():
        _auto_forward_time = int(round(preferences.afm_time))
        _auto_forward_time = '1' if _auto_forward_time == 0 else _auto_forward_time
        return _auto_forward_time
    
    def TextBoxAlpha():
        _alpha = float(round(persistent._textbox_alpha,2))
        _alpha = _alpha*100
        _alpha = round(_alpha,0)
        _alpha_out = str(_alpha)
        _alpha_out = _alpha_out.replace(".0"," %")
        return _alpha_out

    def VolumeDisplay(value):
        '''
        Returns the Value Volume Level to Ren'Py.
        '''
        try:
            _volume = float(round(preferences.get_mixer(value),2))
        except:
            _volume = float(round(preferences.get_volume(value),2))
        _volume = _volume*100
        _volume = round(_volume,0)
        _volume_out = str(_volume)
        _volume_out = _volume_out.replace(".0"," %")
        return _volume_out

    def FancyCheck():
        if getattr(persistent, "_fancy_text"):
            if preferences.text_cps == 200 or preferences.text_cps == 0:
                preferences.text_cps = 120
        else:
            preferences.text_cps = 0

    config.after_load_callbacks.append(FancyCheck)

    def WideRatio(width):
        # Take the width of your screen or any size for that matter
        # and you will get an output of width x height
        height = width * 9.0 / 16.0
        return int(width), int(height)

    class SlowEffectChange(Action):
        def __init__(self, bypass=False):
            self.bypass = bypass
            self.effects = {
                "Fade" : slow_fade,
                "Slide Up" : slow_slide_up(20),
                "Slide Down" : slow_slide_down(20),
                "Slide Left" : slow_slide_left(20),
                "Slide Right" : slow_slide_right(20),
                "Shake Slide" : slow_shaking_slide(10,10,20,20),
                "Shake" : slow_shake(10, 10),
                "Typewriter" : slow_typewriter,
                "Rotate" : slow_rotate,
                "Nonsense" : slow_nonsense
            }

            # Convert the dictionary keys to a list for cycling through effects
            self.effect_names = list(self.effects.keys())

            # Initialize the current effect index
            initial_effect_name = persistent._slow_effect_title if hasattr(persistent, '_slow_effect_title') else self.effect_names[0]
            self.current_index = self.effect_names.index(initial_effect_name)

        def __call__(self):
            if main_menu and not self.bypass:
                return
            # Move to the next effect
            self.current_index = (self.current_index + 1) % len(self.effect_names)

            # Get the current effect name
            current_effect_name = self.effect_names[self.current_index]

            # Get the current effect function
            current_effect = self.effects[current_effect_name]

            # Apply the current effect
            persistent._slow_effect = current_effect
            persistent._slow_effect_title = current_effect_name

            # Restart interaction if needed
            renpy.restart_interaction()
            if not main_menu and not self.bypass:
                renpy.notify("Changed Effect to: %s"%persistent._slow_effect_title)

            #return persistent._slow_effect_title

    class AlwaysEffectChange(Action):
        def __init__(self, bypass=False):
            self.bypass = bypass
            self.effects = {
                "None" : None,
                "Fade" : slow_fade,
                "Always Shake" : always_shake(1, 1),
                "Always Pulse" : always_pulse
            }

            # Convert the dictionary keys to a list for cycling through effects
            self.effect_names = list(self.effects.keys())

            # Initialize the current effect index
            initial_effect_name = persistent._always_effect_title if hasattr(persistent, '_always_effect_title') else self.effect_names[0]
            self.current_index = self.effect_names.index(initial_effect_name)

        def __call__(self):
            if main_menu and not self.bypass:
                return
            # Move to the next effect
            self.current_index = (self.current_index + 1) % len(self.effect_names)

            # Get the current effect name
            current_effect_name = self.effect_names[self.current_index]

            # Get the current effect function
            current_effect = self.effects[current_effect_name]

            # Apply the current effect
            persistent._always_effect = current_effect
            persistent._always_effect_title = current_effect_name

            # Restart interaction if needed
            renpy.restart_interaction()
            if not main_menu and not self.bypass:
                renpy.notify("Changed Always Effect to: %s"%persistent._always_effect_title)

            #return persistent._always_effect_title

    def ToggleFancyText():
        if main_menu:
            return
        if persistent._fancy_text:
            if preferences.text_cps == 200 or preferences.text_cps == 0:
                preferences.text_cps = 120
        else:
            preferences.text_cps = 0
        persistent._fancy_text = not persistent._fancy_text
        renpy.run(With(dissolve))
        renpy.notify(_("Fancy Text: %s")%(_("On") if persistent._fancy_text else _("Off")))
        renpy.restart_interaction()

    def EffectDelayDisplay():
        _alpha = float(round(persistent._effect_delay,2))
        _alpha = _alpha*100
        _alpha = round(_alpha,0)
        _alpha_out = str(_alpha)
        _alpha_out = _alpha_out.replace(".0","")
        if _alpha_out == "0":
            _alpha_out = "Off"
        if _alpha_out != "100":
            _alpha_out = _alpha_out.replace("0","")
        else:
            _alpha_out = _alpha_out.replace("00","0")
        return _alpha_out

    def QuickPositions():
        buttons = {
            "bottom_center"  : "Bottom Center",
            "top_center"     : "Top Center"
            }
        return buttons.get(persistent._quick_menu_layout)

    class CycleQuickStates(Action):
        def __init__(self, bypass=False):
            self.bypass = bypass

        def __call__(self):
            if main_menu and not self.bypass:
                return
            if not getattr(store, "quick_menu"):
                setattr(store, "quick_menu", True)
            if persistent._quick_menu_state == "visible":
                persistent._quick_menu_state = "hover"
            elif persistent._quick_menu_state == "hover":
                persistent._quick_menu_state = "hidden"
            elif persistent._quick_menu_state == "hidden":
                persistent._quick_menu_state = "visible"
            renpy.run(With(dissolve))
            if not main_menu and not self.bypass:
                renpy.notify(_("Quick Menu is: %s")%(persistent._quick_menu_state.title()))
            renpy.restart_interaction()

    class CycleQuickMenu(Action):
        def __init__(self, bypass=False):
            self.bypass = bypass
            self.buttons = ["bottom_center", "top_center"]

            self.current_position = self.buttons.index(persistent._quick_menu_layout)

        def __call__(self):
            if main_menu and not self.bypass:
                return
            current_index = self.buttons.index(persistent._quick_menu_layout)
            next_index = (current_index + 1) % len(self.buttons)
            self.current_position = self.buttons[next_index]
            persistent._quick_menu_layout = self.current_position
            renpy.run(With(dissolve))
            if not main_menu and not self.bypass:
                renpy.notify(_("Quick Menu Position: %s")%(QuickPositions()))
            renpy.restart_interaction()

    def ToggleChoiceHotkeys():
        persistent._choice_hotkeys = not persistent._choice_hotkeys
        renpy.run(With(dissolve))
        renpy.notify(_("%sHotkeys: %s")%(_("Choice ") if not main_menu else "",_("On") if persistent._choice_hotkeys else _("Off")))
        renpy.restart_interaction()

    def WalkthroughData(line, caption):
        choices = walkthrough_dict().get(line, None)
        if choices:
            valid = choices.get(caption, None)
            if valid:
                _choice_wt    = valid.get("wt"  , "")
                _choice_hint  = valid.get("hint", "")
                _choice_color = valid.get("color", None)
                _choice_size  = valid.get("size", None)

                if _choice_color in [None, "None", "none"]:
                    _choice_color = gui.text_color
                
                if _choice_size in [None, "None", "none"]:
                    _choice_size = gui.text_size

                if _choice_hint in [None, "None", "none"]:
                    _choice_hint = ""

                return _choice_wt, _choice_hint, _choice_color, _choice_size
        return None, None, None, None

    class GetText(Action):
        def __init__(self,screen_name,input_id):
            self.screen_name=screen_name
            self.input_id=input_id
        def __call__(self):
            if renpy.get_widget(self.screen_name,self.input_id):
                return str(renpy.get_widget(self.screen_name,self.input_id).content)

    class Unlock_Replays(Action):

        reps = [
            ##Name                 #Partner              #Notification             #Variable
            ("ayumi.name",         "",                   "Fingering",              "ayumi_MC_fing_0"), 
            ("ayumi.name",         "",                   "Masturbating",           "ayumi_masturbating_H"), 
            ("ayumi.name",         "",                   "Office",                 "ayumi_office_H"), 
            ("ayumi.name",         "soushi.name",        "BJ",                     "ayumi_soushi_bj_0"), 
            ("emiko.name",         "",                   "Gym",                    "emiko_gym_H_0"), 
            ("emiko.name",         "",                   "Prologue",               "emiko_prologue_H"),
            ("haruka.name",        "",                   "Late",                   "haruka_first_late_H"), 
            ("haruka.name",        "",                   "Office",                 "haruka_first_office_H"), 
            ("haruka.name",        "",                   "First Weekend",          "haruka_first_weekend"), 
            ("rina.name",          "",                   "First Blowjob",          "rina_first_blowjob_H"), 
            ("suzu.name",          "",                   "Suzu Shared",            "suzu_bat_01_Kawaguchi"), 
            ("suzu.name",          "",                   "Suzu Bat",               "suzu_bat_01_MC"),
            ("suzu.name",          "",                   "Spanking",               "suzu_spanking_0"), 
            ("yoko.name",          "",                   "Change Room Sex",        "yoko_changing_room_H"), 
            ("yoko.name",          "",                   "Dildo Quest",            "yoko_onahole_replay"), 
            ("yoko.name",          "",                   "Prologue",               "yoko_prologue_H")
            ]

        def __call__(self):

            for name, partner, notif, var in self.reps:
                if partner:
                    notification = "{} and {} - {} replay Unlocked".format(eval(name), eval(partner), notif)
                    if not getattr(persistent, var):
                        print(notification)
                        #setattr(persistent, var, True)
                        #renpy.notify(notification)
                else:
                    notification = "{} - {} replay Unlocked".format(eval(name), notif)
                    if not getattr(persistent, var):
                        print(notification)
                        #setattr(persistent, var, True)
                        #renpy.notify(notification)

        def get_selected(self):
            return all(getattr(persistent, i[3]) for i in self.reps)

    def GetEmptyReplays(name):
        try:
            return eval("{}_Replay_List".format(name))
        except:
            return []

    def toggle_callstack():
        if main_menu:
            return
        renpy.run(ToggleScreen("callstack", transition=dissolve))

    def ToggleWalkthrough():
        persistent._walkthrough = not persistent._walkthrough
        renpy.run(With(dissolve))
        renpy.notify(_("Walkthrough: %s")%(("On") if persistent._walkthrough else _("Off")))
        renpy.restart_interaction()

    def ToggleSavename():
        persistent._custom_savename = not persistent._custom_savename
        renpy.run(With(dissolve))
        renpy.notify(_("Custom Savenames: %s")%(("On") if persistent._custom_savename else _("Off")))
        renpy.restart_interaction()

    def ToggleChoiceToolTips():
        persistent._choice_tooltips = not persistent._choice_tooltips
        renpy.run(With(dissolve))
        renpy.notify(_("Choice Tooltips: %s")%(("On") if persistent._choice_tooltips else _("Off")))
        renpy.restart_interaction()

    def ToggleTextbox():
        persistent._textbox_visible = not persistent._textbox_visible
        renpy.run(With(dissolve))
        renpy.notify(_("Textbox: %s")%(("On") if persistent._textbox_visible else _("Off")))
        renpy.restart_interaction()

    def _fix_main_name():
        if main.name != mcname:
            main.name = mcname

    def custom_join(items, join_param="\n"):
        fix = []
        for i in items:
            if i:
                fix.append(i)

        return f"{join_param}".join(fix)

    def _adjust_dialogue(direction="+"):
        txt = "Textbox Visibility"
        if direction == "+":
            if persistent._textbox_alpha <= 0.99 :
                persistent._textbox_alpha += 0.01
            else:
                persistent._textbox_alpha = 1.0
                txt = "Textbox Is Completely Visible"
        elif direction == "-":
            if persistent._textbox_alpha > 0.01:
                persistent._textbox_alpha -= 0.01
            else:
                persistent._textbox_alpha = 0.0
                txt = "Textbox Is Completely Invisible"
        renpy.notify("%s: %s"%(txt, TextBoxAlpha()))
    
    def add_notify_message(msg=None):

        if not msg:
            return

        global notify_messages

        add_time = time.time()

        # Just in case multiple notifications are added really really 
        # fast, this gives them minorly different time values so they 
        # do not steal displayables meant for other notifications
        if notify_messages and notify_messages[-1][1] >= add_time:

            add_time = notify_messages[-1][1] + 0.01

        notify_messages.append((msg, add_time))

        # just keep notify_history_length number of messages
        notify_messages = notify_messages[-notify_history_length:]

        renpy.show_screen("notify_container")
        renpy.restart_interaction()

    def finish_notify(trans, st, at):

        max_start = time.time() - notify_duration

        if not [k for k in notify_messages if k[1] > max_start]:

            # If the notification list is now empty, hide the screen
            renpy.hide_screen("notify_container")
            renpy.restart_interaction()

        return None

    def toggle_notify_type():
        if persistent._notify_custom:
            persistent._notify_custom = False
            config.notify = renpy.display_notify
            renpy.notify("Custom Notifications Off")
        else:
            persistent._notify_custom = True
            config.notify = add_notify_message
            renpy.notify("Custom Notifications On")
        
        renpy.restart_interaction()

    #config.python_callbacks.append(_fix_main_name)
    config.after_load_callbacks.append(_fix_main_name)
    config.interact_callbacks.append(_fix_main_name)

    config.keymap[ 'quick_save_button' ] = [ 'K_F5' ]
    config.underlay.append(renpy.Keymap(quick_save_button = QuickSave()))

    config.keymap[ 'quick_load_button' ] = [ 'K_F6' ]
    config.underlay.append(renpy.Keymap(quick_load_button = QuickLoad()))

    config.keymap[ 'toggle_quick_menu_state' ] = [ 'noshift_K_q' ]
    config.underlay.append(renpy.Keymap(toggle_quick_menu_state = CycleQuickStates()))

    config.keymap[ 'toggle_quick_menu_position' ] = [ 'shift_K_q' ]
    config.underlay.append(renpy.Keymap(toggle_quick_menu_position = CycleQuickMenu()))

    config.keymap[ 'toggle_always_effect' ] = [ 'noshift_K_r' ]
    config.underlay.append(renpy.Keymap(toggle_always_effect = AlwaysEffectChange()))

    config.keymap[ 'toggle_slow_effect' ] = [ 'noshift_K_e' ]
    config.underlay.append(renpy.Keymap(toggle_slow_effect = SlowEffectChange()))

    config.keymap[ 'toggle_fancy_text' ] = [ 'shift_K_f' ]
    config.underlay.append(renpy.Keymap(toggle_fancy_text = Function(ToggleFancyText)))

    config.keymap[ 'toggle_choice_hotkeys' ] = [ 'noshift_K_c' ]
    config.underlay.append(renpy.Keymap(toggle_choice_hotkeys = Function(ToggleChoiceHotkeys)))

    config.keymap[ 'toggle_walkthrough' ] = [ 'noshift_K_w' ]
    config.underlay.append(renpy.Keymap(toggle_walkthrough = Function(ToggleWalkthrough)))

    config.keymap[ 'toggle_savename' ] = [ 'shift_K_s' ]
    config.underlay.append(renpy.Keymap(toggle_savename = Function(ToggleSavename)))

    config.keymap[ 'toggle_choice_tooltips' ] = [ 'shift_K_t' ]
    config.underlay.append(renpy.Keymap(toggle_choice_tooltips = Function(ToggleChoiceToolTips)))

    config.keymap[ 'toggle_textbox' ] = [ 'noshift_K_t' ]
    config.underlay.append(renpy.Keymap(toggle_textbox = Function(ToggleTextbox)))

    config.keymap[ 'toggle_callstack' ] = [ 'K_HOME' ]
    config.underlay.append(renpy.Keymap(toggle_callstack = Function(toggle_callstack)))
        
    config.keymap[ 'toggle_visibility_up' ] = [ 'K_KP_PLUS', 'repeat_K_KP_PLUS' ]
    config.underlay.append(renpy.Keymap(toggle_visibility_up = Function(_adjust_dialogue, "+")))

    config.keymap[ 'toggle_visibility_down' ] = [ 'K_KP_MINUS', 'repeat_K_KP_MINUS' ]
    config.underlay.append(renpy.Keymap(toggle_visibility_down = Function(_adjust_dialogue, "-")))

    config.keymap[ 'toggle_notifications' ] = [ 'K_n' ]
    config.underlay.append(renpy.Keymap(toggle_notifications = Function(toggle_notify_type)))

    config.overlay_screens.append("shortcuts")

    if persistent._notify_custom == None:
        persistent._notify_custom = True

    if persistent._notify_custom:
        config.notify = add_notify_message
    else:
        config.notify = renpy.display_notify

label splashscreen:
    scene black
    with Pause(1)

    show splashText with dissolve
    with Pause(15)

    hide text with dissolve
    with Pause(1)

    return

init 100:# Defaults
    # Academy Live
    define d = Dissolve(0.1)
    define d1 = Dissolve (0.5)
    define d2 = Dissolve (1.0)

init 1:# Defaults
    image splashText = Text(shortcuts.strip(), style="splash")
    default preferences.text_cps = 120
    default persistent._unlocked_gallery = False
    default persistent._show_empty_gallery = False
    define gui.slot_delete_text_idle_color = "#F00"
    define gui.slot_delete_text_outlines = [(2, "#0009", 1, 1)]
    define gui.input_prompt_text_outlines = [ (2, "#00000080", 0, 0) ]
    define gui.input_button_text_outlines = [ (2, "#00000080", 0, 0) ]
    define gui.quick_button_text_outlines = [(2, "#0009", 1, 1)]

    default _go_to_page = ""
    default jg_s = "{size=24}"
    default jg_1 = "{color=#FB4301}"
    default jg_2 = "{color=#000000}"
    default jg_3 = "{/color}"
    define config.end_game_transition = dissolve
    define config.end_splash_transition = dissolve
    define config.enter_replay_transition = dissolve
    define config.exit_replay_transition = dissolve
    define config.after_load_transition = dissolve
    define config.end_game_transition = dissolve
    define config.game_main_transition = dissolve
    define config.main_game_transition = dissolve

    define gui.jg_mod_version = '0.06.2.1_alpha'
    define gui.built_in_cheats = "IWBUWS"

    default notify_messages = []
    default notify_duration = 4.0
    default notify_history_length = 5
    define gui.mod_dev = "JiGSaW Games Studios"

init 5:# Screens

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
                    action ShowMenu("replays")

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
                
                
                    #textbutton _("{font=gui/fonts/JosefinSans-SemiBold.ttf}{size=64}Start{/size}{/font}"):
                        #text_outlines [ (2, "#00000080", 0, 1) ]
                        #action Start()

                else:

                    textbutton _("History") action ShowMenu("history") style "menu_text_button_custom" text_style "menu_text_button_custom"

                    textbutton _("Save") action ShowMenu("save") style "menu_text_button_custom" text_style "menu_text_button_custom"

                textbutton _("Load") action ShowMenu("load") style "menu_text_button_custom" text_style "menu_text_button_custom"

                if main_menu:

                    textbutton _("Replays") action ShowMenu("replays") style "menu_text_button_custom" text_style "menu_text_button_custom"

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

        #vbox:
            #style_prefix "navigation"

            #xpos gui.navigation_xpos
            #yalign 0.5

            #spacing gui.navigation_spacing

            #if main_menu:

                #textbutton _("Start") action Start()
            
            
                ##textbutton _("{font=gui/fonts/JosefinSans-SemiBold.ttf}{size=64}Start{/size}{/font}"):
                    ##text_outlines [ (2, "#00000080", 0, 1) ]
                    ##action Start()

            #else:

                #textbutton _("History") action ShowMenu("history")

                #textbutton _("Save") action ShowMenu("save")

            #textbutton _("Load") action ShowMenu("load")

            #textbutton _("Preferences") action ShowMenu("preferences")

            #if _in_replay:

                #textbutton _("End Replay") action EndReplay(confirm=True)

            #elif not main_menu:

                #textbutton _("Main Menu") action MainMenu()

            #textbutton _("About") action ShowMenu("about")

            #if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

                ### Help isn't necessary or relevant to mobile devices.
                #textbutton _("Help") action ShowMenu("help")

            #if renpy.variant("pc"):

                ### The quit button is banned on iOS and unnecessary on Android and
                ### Web.
                #textbutton _("Quit") action Quit(confirm=not main_menu)

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

                #text "[config.name!t]":
                    #style "main_menu_title"

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
        $ mod_version = "[gui.jg_mod_version]" if gui.jg_mod_version == config.version else "Incompatible Mod"
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

    screen mod_features():
        tag menu

        use game_menu("Mod Features", scroll="viewport"):
            vbox:
                spacing 10
                if gui.jg_mod_version == config.version:
                    text "Custom Cheat Menu Toggled Using {color=#f00}(END){/color} or button in Quick Menu"
                    text "1. Manage Academy Options" xoffset 50
                    text "2. Modify Student/Teacher Traits" xoffset 50
                    text "Walkthrough"
                    text "1. Walkthrough Suggestions Toggled using {color=#f00}(W){/color} or in preferences menu" xoffset 50
                    text "2. Walkthrough Tooltips Toggled using {color=#f00}(Shift+T){/color} or in preferences menu" xoffset 50
                    text "Music Player"
                    text "1. Music Player can be Toggled ingame using {color=#f00}(M){/color}" xoffset 50
                    text "Override Replays"
                    text "1. View Empty Replays {color=#f00}(E){/color} or button in Replays" xoffset 50
                    text "2. View Locked Replays {color=#f00}(L){/color} or button in Replays" xoffset 50
                    text "Quick Menu Options"
                    text "1. Quick Menu Visibility Options Toggled using {color=#f00}(Q){/color} or in preferences menu" xoffset 50
                    text "2. Quick Menu Position Options Toggled Using {color=#f00}(Shift+Q){/color} or in preferences menu" xoffset 50
                    text "Say Dialogue"
                    text "1. Textbox Visibility Toggled using {color=#f00}(T){/color} or in preferences menu" xoffset 50
                    text "2. Slider in Preferences or NUM {color=#f00}(+/-){/color}" xoffset 50
                    text "3. Fancy Text Toggled using {color=#f00}(F){/color} or in preferences menu" xoffset 50
                    text "4. Text Effect Toggled using {color=#f00}(E){/color} or in preferences menu" xoffset 50
                    text "5. Text Always Effect Toggled using {color=#f00}(R){/color} or in preferences menu" xoffset 50
                    text "Credit to {a=https://github.com/yukinogatari/Ren-Py-FancyText}yukinogatari{/a} for the Fancytext Module Modified by\n[gui.mod_dev] for newer Ren'Py Compatibility" xoffset 50
                    text "Custom Save Names"
                    text "1. Toggle Custom Savenames using {color=#f00}(Shift+S){/color} or in preferences menu" xoffset 50
                    text "Hotkeys"
                    text "1. Toggle Choice Hotkeys using {color=#f00}(C){/color} or in preferences menu" xoffset 50
                    text "Notifications"
                    text "1. Toggle Notification Stack/Standard using {color=#f00}(N){/color} or in preferences menu" xoffset 50
                    text "Credit to {a=https://github.com/RenpyRemix/multi-notify}RenpyRemix{/a} for stackable notifications" xoffset 50
                    text ""
                    text "And lastly {a=https://www.patreon.com/passhonQ}passhonQ{/a} for developing [config.name!t]"
                else:
                    text "Mod is outdated {a=https://github.com/JiGSaWKilla89/academy_live_mod}Click Here To Check for New Version{/a}"

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
                        label _("Music Buttons\n[jg_s]{}".format("Solid" if persistent._use_outline_music_buttons else "Outline"))
                        textbutton _("Solid"):
                            action SetField(persistent, "_use_outline_music_buttons", True)
                        textbutton _("Outline"):
                            action SetField(persistent, "_use_outline_music_buttons", False)
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
                    
                    
                null height (4 * gui.pref_spacing)

                hbox:
                    box_wrap True
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
                    
                    vbox:
                        style_prefix "check"
                        label _("Notifictions\n[jg_s](N)")
                        textbutton _("{size=-10}%s{/size}"%("Notification Stack" if persistent._notify_custom else "Notification Standard")):
                            action ToggleField(persistent, "_notify_custom")


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

    screen replays():
    
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


                    for i_replay in Replay_List:
                        if i_replay.girl == girls[landing_page]:
                            imagebutton:
                                style "menu_text_button_custom"
                                if not persistent._unlocked_gallery:
                                    insensitive "Locked_Replay_idle"
                                idle i_replay.block + "_idle"
                                hover i_replay.block + "_hover"
                                at fzoom
                                if i_replay.flag == True:
                                    action Replay(i_replay.block, scope=i_replay.dict, locked=False)
                                else:
                                    action Replay(i_replay.block, scope=i_replay.dict, locked=not persistent._unlocked_gallery)
                else:
                    for i_replay in Replay_List:
                        if i_replay.girl not in main_girls_replay:
                            imagebutton:
                                style "menu_text_button_custom"
                                if not persistent._unlocked_gallery:
                                    insensitive "Locked_Replay_idle"
                                idle i_replay.block + "_idle"
                                hover i_replay.block + "_hover"
                                at fzoom
                                if i_replay.flag == True:
                                    action Replay(i_replay.block, scope=i_replay.dict, locked=False)
                                else:
                                    action Replay(i_replay.block, scope=i_replay.dict, locked=not persistent._unlocked_gallery)

    
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
            textbutton "{} Empty Replays".format("View" if not persistent._show_empty_gallery else "Hide") action ToggleField(persistent, "_show_empty_gallery")
            if not Unlock_Replays().get_selected():
                textbutton ("Lock Replays".zfill(4) if persistent._unlocked_gallery else "Unlock Replays"):
                    action ToggleField(persistent, "_unlocked_gallery")

        key "K_e" action ToggleField(persistent, "_show_empty_gallery")
        key "K_l" action ToggleField(persistent, "_unlocked_gallery")

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

## Cheats ######################################################################################################################
init python:
    def toggle_cheats():
        if main_menu:
            return
        renpy.run(ToggleScreen("cheats", transition=dissolve))
    config.keymap[ 'toggle_cheats' ] = [ 'K_END' ]
    config.underlay.append(renpy.Keymap(toggle_cheats = Function(toggle_cheats)))

default char_dict_female = {}
default char_dict_male = {}

init python:# Init Cheats

    def _cheat_chars_data():
        return [ayumi, emiko, haruka, maiya, genpachi, hiroshige, izo, miyako, nanako, rina, ryoichi, sayoko, satsuki, soushi, sotaro, suzu, yoko, yuna]

    def Generate_Char_Dict(lst):
        char_dic_female = {}
        char_dic_male = {}
        for i in lst:
            if i.gender == 0:
                if not i.nametag in char_dic_female:
                    char_dic_female[i.nametag] = {
                        "name" : i.name,
                        "surname" : i.surname,
                        "class" : i,
                        "outfit" : i.outfit,
                        "available" : i.available,
                        "met" : i.met,
                        "virgin" : i.virgin,
                        "personality" : i.personality,
                        "intelligence" : i.intelligence,
                        "testResult" : i.testResult,
                        "strikes" : i.strikes,
                        "affection" : i.affection,
                        "perversion" : i.perversion,
                        "lewd" : i.lewd
                    }
            elif i.gender == 1:
                if not i.nametag in char_dic_male:
                    char_dic_male[i.nametag] = {
                        "name" : i.name,
                        "surname" : i.surname,
                        "class" : i,
                        "outfit" : i.outfit,
                        "available" : i.available,
                        "met" : i.met,
                        "virgin" : i.virgin,
                        "personality" : i.personality,
                        "intelligence" : i.intelligence,
                        "testResult" : i.testResult,
                        "strikes" : i.strikes,
                        "affection" : i.affection,
                        "perversion" : i.perversion,
                        "lewd" : i.lewd
                    }
        return char_dic_female, char_dic_male

    #renpy.run(CyclePersonalities("Pure"))
    class CyclePersonalities(Action):
        def __init__(self, personality, char):
            self.buttons = ["Pure", "Outgoing", "Shy", "Charming", "Cold", "Delinquent", "Nerd"]

            self.char = char
            self.personality = personality

            self.current_position = self.buttons.index(personality)

        def __call__(self):
            current_index = self.buttons.index(self.personality)
            next_index = (current_index + 1) % len(self.buttons)
            self.current_position = self.buttons[next_index]
            self.char.personality = self.current_position
            renpy.restart_interaction()

    class CycleOutfits(Action):
        def __init__(self, outfit, char):
            self.buttons = ["School", "Swim", "Gym", "Casual", "Naked"]

            self.char = char
            self.outfit = outfit

            self.current_position = self.buttons.index(outfit)

        def __call__(self):
            current_index = self.buttons.index(self.outfit)
            next_index = (current_index + 1) % len(self.buttons)
            self.current_position = self.buttons[next_index]
            image = "images/characters/%s/%s.png"%(self.char.nametag,self.current_position)
            if renpy.loadable(image):
                self.char.outfit = self.current_position
            else:
                self.char.outfit = "School"
            renpy.restart_interaction()
    #Generate_Char_Dict([ayumi, emiko, haruka, maiya, genpachi, hiroshige, izo, miyako, nanako, rina, ryoichi, sayoko, satsuki, soushi, sotaro, suzu, yoko, yuna])
    #Personalities : "Pure", "Outgoing", "Shy", "Charming", "Cold", "Delinquent"
    #print_stats([ayumi, emiko, haruka, maiya, genpachi, hiroshige, izo, miyako, nanako, rina, ryoichi, sayoko, satsuki, soushi, sotaro, suzu, yoko, yuna])
    def print_stats(lst):
        print()
        for i in lst:
            if i.gender == 0:
                print("'{}' : {{".format(i.name.lower()))
                print("    'class' : {},".format(i.nametag))
                print("    'outfit' : '{}',".format(i.outfit))
                print("    'available' : {},".format(i.available))
                print("    'met' : {},".format(i.met))
                print("    'virgin' : {},".format(i.virgin))
                print("    'personality' : '{}',".format(i.personality))
                print("    'intelligence' : {},".format(i.intelligence))
                print("    'testResult' : {},".format(i.testResult))
                print("    'strikes' : {},".format(i.strikes))
                print("    'affection' : {},".format(i.affection))
                print("    'perversion' : {},".format(i.perversion))
                print("    'lewd' : {}".format(i.lewd))
                print("    },")

    bypass_list.extend(["CyclePersonalities", "CycleOutfits", "print_stats", "Generate_Char_Dict"])

    def _sex_symbol_status(value):
        if value >= 95:
            return "{size=22}{color=#ff002e}Corrupted!"
        elif value >= 75:
            return "{size=22}{color=#ff0049}Perverted"
        elif value >= 55:
            return "{size=22}{color=#ff008f}Lustful"
        elif value >= 30:
            return "{size=22}{color=#ff9300}Slutty"
        elif value >= 10:
            return "{size=22}{color=#ffe000}Curious"
        elif value < 10:
            return "{size=22}{color=#7cffe1}Pure"
        else:
            return "{size=22}{color=#FFFFFF}None"

    def _viewership_status(value):
        if value >= 100000:
            return "{size=22}Very High!"
        elif value >= 50000:
            return "{size=22}High"
        elif value >= 15000:
            return "{size=22}Normal"
        elif value >= 5000:
            return "{size=22}Low"
        elif value < 5000:
            return "{size=22}Very Low"
        else:
            return "{size=22}No Data!!"

    def _board_status(value):
        if value >= 90:
            return "{size=20}The Board is Delighted with your performance!"
        elif value >= 75:
            return "{size=20}The Board is Happy with the way you run the Academy."
        elif value >= 60:
            return "{size=20}The Board is Satisfied with the way the Academy is functioning."
        elif value >= 40:
            return "{size=20}The Board is Dissatisfied with your directing of the Academy."
        elif value >= 11:
            return "{size=20}The Board is Incredibly Frustrated with your performance!"
        elif value < 11:
            return "{size=20}The Board is considering removing you from your position. Do something fast!"

    def _grades_status(value):
        if value >= 96:
            return "{size=25}{b}A{/b}+"               
        elif value >= 90:
            return "{size=25}{b}A{/b}"               
        elif value >= 85:
            return "{size=25}{b}A{/b}-"                   
        elif value >= 80:
            return "{size=25}{b}B{/b}+"                   
        elif value >= 75:
            return "{size=25}{b}B{/b}"                   
        elif value >= 70:
            return "{size=25}{b}B{/b}-"                   
        elif value >= 65:
            return "{size=25}{b}C{/b}+"                  
        elif value >= 60:
            return "{size=25}{b}C"                  
        elif value >= 55:
            return "{size=25}{b}C{/b}-"                  
        elif value >= 50:
            return "{size=25}{b}D{/b}+"                 
        elif value >= 45:
            return "{size=25}{b}D"                
        elif value >= 40:
            return "{size=25}{b}D{/b}-"                  
        elif value < 40:
            return "{size=25}{b}F{/b}"
    
    def _student_trust_status(value):
        if value >= 90:
            return "veryhappysymbol"
        elif value >= 63:# and sttrust >= 63:
            return "happysymbol"
        elif value >= 38:# and sttrust >= 38:
            return "neutralsymbol"
        elif value >= 15:# and sttrust >= 15:
            return "sadsymbol"
        elif value < 15:
            return "verysadsymbol"

    def _student_grade_status(rstd):
        if "Cheated_Exam" in rstd.topics and rstd.testResult == 0:
            return "{size=40}{color=#c30000}{font=gui/fonts/CrimsonText-SemiBold.ttf}{i}0"
        elif rstd.testResult >= 96:
            return "{=cheats_inline_40}A+"
        elif rstd.testResult >= 90:
            return "{=cheats_inline_40}A"
        elif rstd.testResult >= 85:
            return "{=cheats_inline_40}A-" 
        elif rstd.testResult >= 80:
            return "{=cheats_inline_40}B+"
        elif rstd.testResult >= 75:
            return "{=cheats_inline_40}B"
        elif rstd.testResult >= 70:
            return "{=cheats_inline_40}B-"
        elif rstd.testResult >= 65:
            return "{=cheats_inline_40}C+"
        elif rstd.testResult >= 60:
            return "{=cheats_inline_40}C"
        elif rstd.testResult >= 55:
            return "{=cheats_inline_40}C-"
        elif rstd.testResult >= 50:
            return "{=cheats_inline_40}D+"
        elif rstd.testResult >= 45:
            return "{=cheats_inline_40}D"
        elif rstd.testResult >= 40:
            return "{=cheats_inline_40}D-"
        elif rstd.testResult < 40:
            return "{=cheats_inline_40}F"

    def _student_strike_status(rstd):
        if rstd.strikes >= 3:
            return "{color=#000000} /  /  /", 0, 0
        elif rstd.strikes == 2:
            return "{color=#000000} /  /", 1.5, 0
        elif rstd.strikes == 1:
            return "{color=#000000} /", 0, 0
        else:
            return "{color=#000000}{size=20}{i}(clean record){/i}",0 , 0.55

    def _student_report_status(rstd):
        if rstd.personality == "Pure":
            if rstd.gender == 0:
                return "{size=18}{color=#000000}{i}  [rstd.surname] [rstd.name] is a student that possesses a genuinely friendly and warm personality. Her inviting and authentic nature naturally attracts others to be around. As a result, forming social connections comes easily to her.", 550
            elif rstd.gender == 0:
                return "{size=18}{color=#000000}{i}  [rstd.surname] [rstd.name] is a student that possesses a genuinely friendly and warm personality. His inviting and authentic nature naturally attracts others to be around. As a result, forming social connections comes easily to Him.", 550
            else:
                return "{size=18}{color=#000000}{i}  [rstd.surname] [rstd.name] is a student that possesses a genuinely friendly and warm personality. Their inviting and authentic nature naturally attracts others to be around. As a result, forming social connections comes easily to this student.", 550                                                        
        elif rstd.personality == "Outgoing":
            if rstd.gender == 0:
                return "{size=18}{color=#000000}{i}  [rstd.surname] [rstd.name] is a student that embodies a lively and authentic personality, naturally engaging in social situations, often speaking with enthusiasm and a noticeable volume. Her unreserved approach might have a polarizing effect, prompting swift judgements from others regarding whether they enjoy her company or not.", 550
            elif rstd.gender == 1:
                return "{size=18}{color=#000000}{i}  [rstd.surname] [rstd.name] is a student that embodies a lively and authentic personality, naturally engaging in social situations, often speaking with enthusiasm and a noticeable volume. His unreserved approach might have a polarizing effect, prompting swift judgements from others regarding whether they enjoy his company or not.", 550
            else:
                return "{size=18}{color=#000000}{i}  [rstd.surname] [rstd.name] is a student that embodies a lively and authentic personality, naturally engaging in social situations, often speaking with enthusiasm and a noticeable volume. Their unreserved approach might have a polarizing effect, prompting swift judgements from others regarding whether they enjoy their company or not.", 550                
        elif rstd.personality == "Shy":
            if rstd.gender == 0:
                return "{size=18}{color=#000000}{i}  [rstd.surname] [rstd.name] is a student that often displays an introverted and reserved nature. She tends to exhibit reticence in social interactions and may feel uncomfortable or apprehensive in group settings.", 550
            elif rstd.gender == 1:
                return "{size=18}{color=#000000}{i}  [rstd.surname] [rstd.name] is a student that often displays an introverted and reserved nature. He tends to exhibit reticence in social interactions and may feel uncomfortable or apprehensive in group settings.", 550
            else:
                return "{size=18}{color=#000000}{i}  [rstd.surname] [rstd.name] is a student that often displays an introverted and reserved nature. They tend to exhibit reticence in social interactions and may feel uncomfortable or apprehensive in group settings.", 550
        elif rstd.personality == "Charming":
            if rstd.gender == 0:
                return "{size=18}{color=#000000}{i}  [rstd.surname] [rstd.name] possesses a charismatic magnetism that captivates others. Her ability to effortlessly appear persuasive allows her to influence and win favors from peers, making her stand out in the student community. As a result, she is often seen surrounded by admirers and occupies an elevated social standing among the students", 550
            elif rstd.gender == 1:
                return "{size=18}{color=#000000}{i}  [rstd.surname] [rstd.name] possesses a charismatic magnetism that captivates others. His ability to effortlessly appear persuasive allows him to influence and win favors from peers, making him stand out in the student community. As a result, he is often seen surrounded by admirers and occupies an elevated social standing among the students", 550
            else:
                return "{size=18}{color=#000000}{i}  [rstd.surname] [rstd.name] possesses a charismatic magnetism that captivates others. Their ability to effortlessly appear persuasive allows them to influence and win favors from peers, making them stand out in the student community. As a result, they are often seen surrounded by admirers and occupies an elevated social standing among the students", 550                                                               
        elif rstd.personality == "Cold":
            if rstd.gender == 0:
                return "{size=18}{color=#000000}{i}  [rstd.surname] [rstd.name] displays a cautions and cynical personality. She carefully navigates through social situations with sharp wit and a guarded mindset. It is unusual for her to open up about herself or to provide more information that was required for most interactions", 500
            elif rstd.gender == 1:
                return "{size=18}{color=#000000}{i}  [rstd.surname] [rstd.name] displays a cautions and cynical personality. He carefully navigates through social situations with sharp wit and a guarded mindset. It is unusual for him to open up about herself or to provide more information that was required for most interactions", 500
            else:
                return "{size=18}{color=#000000}{i}  [rstd.surname] [rstd.name] is a student that displays a cautions and cynical personality. They carefully navigate through social situations with sharp wit and a guarded mindset. It is unusual for them to open up about themselves or to provide more information that was required for most interactions", 500
        elif rstd.personality == "Nerd":
            if rstd.gender == 0:
                return "{size=18}{color=#000000}{i}  [rstd.surname] [rstd.name] is a student who often displays social awkwardness and introversion. She is almost always immersed in her own peculiar hobbies and subjects. Although these diverse interests might lead to increased curiosity about these niche subjects, it might also renders the student potentially vulnerable in certain social situations.", 500
            elif rstd.gender == 1:
                return "{size=18}{color=#000000}{i}  [rstd.surname] [rstd.name] is a student who often displays social awkwardness and introversion. He is almost always immersed in his own peculiar hobbies and subjects. Although these diverse interests might lead to increased curiosity about these niche subjects, it might also renders the student potentially vulnerable in certain social situations.", 500
            else:
                return "{size=18}{color=#000000}{i}  [rstd.surname] [rstd.name] is a student who often displays social awkwardness and introversion. They are almost always immersed in their own peculiar hobbies and subjects. Although these diverse interests might lead to increased curiosity about these niche subjects, it might also renders the student potentially vulnerable in certain social situations.", 500
        elif rstd.personality == "Delinquent":
            if rstd.gender == 0:
                return "{size=18}{color=#000000}{i}  [rstd.surname] [rstd.name] is a student who presents a rebellious and nonconforming nature, frequently clashing with others due to her defiance towards rules and authorities. Her confrontational behavior may lead to increased disciplinary issues, and she is viewed as a typical 'troublemaker' based on our earlier observations.", 500
            elif rstd.gender == 1:
                return "{size=18}{color=#000000}{i}  [rstd.surname] [rstd.name] is a student who presents a rebellious and nonconforming nature, frequently clashing with others due to his defiance towards rules and authorities. His confrontational behavior may lead to increased disciplinary issues, and he is viewed as a typical 'troublemaker' based on our earlier observations.", 500
            else:
                return "{size=18}{color=#000000}{i}  [rstd.surname] [rstd.name] is a student who presents a rebellious and nonconforming nature, frequently clashing with others due to their defiance towards rules and authorities. Their confrontational behavior may lead to increased disciplinary issues, and they are viewed as a typical 'troublemaker' based on our earlier observations.", 500
        else:
            return "{=cheats_inline_itallic}  [rstd.surname] [rstd.name] is one of the students at {b}ReLive Academy{/b}.", 550

    def _student_intelligence_status(rstd,lvl=1):
        if lvl == 1:
            if rstd.gender == 0:
                return "{size=18}{color=#000000}{i}  It should be noted that Ms. [rstd.surname] is a very gifted student, having passed many of our initial examinations with flying colors. It is with no caution, that our experts consider her level of intellect to be more than spectacular. Some would even use the word \'Genius\'."
            elif rstd.gender == 1:
                return "{=cheats_inline_itallic}  It should be noted that Mr. [rstd.surname] is a very gifted student, having passed many of our initial examinations with flying colors. It is with no caution, that our experts consider his level of intellect to be more than spectacular. Some would even use the word \'Genius\'."
            else:
                return "{=cheats_inline_itallic}  It should be noted that [rstd.surname] is a very gifted student, having passed many of our initial examinations with flying colors. It is with no caution, that our experts consider their level of intellect to be more than spectacular. Some would even use the word \'Genius\'."

        if lvl == 2:
            if rstd.testResult <= academy.gradesthreshold:
                if rstd.gender == 0:
                    return"{=cheats_inline_itallic} Despite having exceeded many of our initial reports, this student has failed to achieve a significant positive result in their last weekly exam."
            else:
                if rstd.gender == 0:
                    return "{=cheats_inline_itallic} Due to such an unusually intelligent student, it should be very hard to challenge her without severly impacting our other students grades."
                elif rstd.gender == 1:
                    return "{=cheats_inline_itallic} Due to such an unusually intelligent student, it should be very hard to challenge him without severly impacting our other students grades."
                else:
                    return "{=cheats_inline_itallic} Due to such an unusually intelligent student, it should be very hard to challenge them without severly impacting our other students grades."
        if lvl == 3:
            if rstd.gender == 0:
                return "{=cheats_inline_itallic}  She has demonstrated to be a very intelligent student and, under normal circumstances, should have no problem navigating through her academics."
            elif rstd.gender == 1:
                return "{=cheats_inline_itallic}  He has demonstrated to be a very intelligent student and, under normal circumstances, should have no problem navigating through his academics."
            else:
                return "{=cheats_inline_itallic}  They have demonstrated to be a very intelligent student and, under normal circumstances, should have no problem navigating through their academics."
    
    def _student_corruption_status(rstd):
        if rstd.corruption >= 95:
            return "{=cheats_inline_random}{color=#ff002e}Corrupted!"
        elif rstd.corruption >= 75:
            return "{=cheats_inline_random}{color=#ff0049}Perverted"
        elif rstd.corruption >= 55:
            return "{=cheats_inline_random}{color=#ff008f}Lustful"
        elif rstd.corruption >= 30:
            return "{=cheats_inline_random}{color=#ff9300}Slutty"
        elif rstd.corruption >= 10:
            return "{=cheats_inline_random}{color=#ffe000}Curious"
        elif rstd.corruption < 10:
            return "{=cheats_inline_random}{color=#000000}Pure"
    
    def _student_affection_status(rstd):
        if rstd.affection >= 91:
            return "{=cheats_inline_random}{color=#ff4edc}Passion!"
        elif rstd.affection >= 70:
            return "{=cheats_inline_random}{color=#e04646}Love"
        elif rstd.affection >= 40:
            return "{=cheats_inline_random}{color=#ff714e}Warm"
        elif rstd.affection >= 5:
            return "{=cheats_inline_random}{color=#46e0ad}Like"
        elif rstd.affection >= 0:
            return "{=cheats_inline_random}{color=#ffe000}Indifference"
        elif rstd.affection >= -20:
            return "{=cheats_inline_random}{color=#000000}Dislike"
        elif rstd.affection < -20:
            return "{=cheats_inline_random}{color=#000000}Hate"

    def _student_intelligence_lvl(rstd):
        if rstd.intelligence >= 2.5:
            return "{=cheats_inline_20}Genius"
        elif rstd.intelligence >= 1.6:
            return "{=cheats_inline_20}Smart"
        elif rstd.intelligence >= 1.2:
            return "{=cheats_inline_20}Apt"
        elif rstd.intelligence >= 0.9:
            return "{=cheats_inline_20}Average"
        elif rstd.intelligence >= 0.7:
            return "{=cheats_inline_20}Limited"
        elif rstd.intelligence >= 0.5:
            return "{=cheats_inline_20}Slow"
        elif rstd.intelligence < 0.5:
            return "{=cheats_inline_20}Dim" 

    def update_wt(file):
        new_out = []
        with renpy.open_file(file, encoding="utf-8") as readfile:
            return readfile.readlines()

    def find_replays(script):
        replacements = [
            ("Ayumi", "[ayumi.name]"), ("Haruka", "[haruka.name]"),
            ("Emiko", '[emiko.name]'), ("Yoko", '[yoko.name]'),
            ("Rina", '[rina.name]'), ("Suzu", "[suzu.name]"),
            ("Kawaguchi", "[hidetoshi.surname]"), ("Yusuke", "[main.name]")
        ]

        #Flag, Girl, Name, Block, Dict, Desc
        out = []

        data = update_wt(script)

        for line in data:
            line = line.strip()
            line = line.replace('"', '').replace("\\","")
            if "Replays(persistent." in line:
                start_index = line.find("Replays(persistent.") + len("Replays(persistent.")
                s = line[start_index:].replace(")", "")
                d = s.split(", ")
                if len(d) > 6:
                    fix = ", ".join([d[-2],d[-1]])
                    d = [i for i in d[0:5]]
                    d.append(fix)
                #print(len(d), d )

                var = d[0]
                char = d[1]
                for og, rp in replacements:
                    d[1] = d[1].replace(og,rp)
                girl = d[1]
                for og, rp in replacements:
                    d[2] = d[2].replace(og,rp)
                name = d[2]
                label = d[3].strip()
                button_idle = label +"_idle"
                button_hover = label + "_hover"
                dic = eval(d[4])
                for og, rp in replacements:
                    d[5] = d[5].replace(og, rp)
                desc = d[5]
                #Variable, Girl, Girl_Name, Replay Name, Label, Desc
                out.append(ReplayCheat(var, char, name, label, dic, desc, button_idle, button_hover, WideRatio(384)))


        return out

    class ReplayCheat():
        def __init__(self, flag, girl, name, label, dic, desc, idle, hover, size):
            self.flag  = flag
            self.girl  = girl
            self.name  = name
            self.label = label
            self.dic   = dic
            self.desc  = desc
            self.idle = Transform(idle, xysize=size)
            self.hover = Transform(hover, xysize=size)
            self.insensitive = Transform(idle, xysize=size, matrixcolor=SaturationMatrix(0.2))

    _cheats_replay = find_replays("Replay System.rpy")

    bypass_list.extend(["ReplayCheat", "find_replays", "_cheats_replay", 
        "valid_dic_items", "walkthrough_dict", "wt_update", "filter_wt", 
        "update_check_walkthrough", "script_ignore_lines", 
        "event_ignore_lines"])

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
                text "{=cheats_inline}{u}                                                            ":
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
                                    if renpy.variant("mobile"):
                                        text "{color=#000000}{u}                                    ":
                                            ypos -4
                                    else:
                                        text "{color=#000000}{u}                                           ":
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
                                    if renpy.variant("mobile"):
                                        text "{color=#000000}{u}                                    ":
                                            ypos -4
                                    else:
                                        text "{color=#000000}{u}                                           ":
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
                text "{=cheats_inline}{u}                                                            ":
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
                        text "{=cheats_inline}{u}                                                                                        ":
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
                                    if renpy.variant("mobile"):
                                        text "{color=#000000}{u}                                    ":
                                            ypos -4
                                    else:                                 
                                        text "{color=#000000}{u}                                           ":
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
                                    text "{color=#000000}{u}                                           ":
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


#######################################################################################
