screen musicroom():
    $ tooltip = GetTooltip()
    default current_loop = False
    default current_track = None
    default return_track = None
    default return_loop = []
    if mr.get_track() not in mr.playlist:
        on "show" action SetLocalVariable("return_track", mr.get_track()), SetLocalVariable("return_loop", renpy.music.get_loop()), Stop("music"),mr.Play()
        on "replace" action SetLocalVariable("return_track", mr.get_track()), SetLocalVariable("return_loop", renpy.music.get_loop()), Stop("music"),mr.Play()

    if not main_menu:
        on "show" action SetLocalVariable("current_track", mr.get_track()), SetLocalVariable("current_loop", renpy.music.get_loop())
        on "replace" action SetLocalVariable("current_track", mr.get_track()), SetLocalVariable("current_loop", renpy.music.get_loop())

    if return_track:
        on "hide" action Play("music", return_loop if return_loop else return_track, loop=True if return_loop else False), Return()
        on "replaced" action Play("music", return_loop if return_loop else return_track, loop=True if return_loop else False), Return()
        key ("K_m", "game_menu") action Play("music", return_loop if return_loop else return_track, loop=True if return_loop else False), Return()
    else:
        key ("K_m", "game_menu") action mr.Stop(), Return()

    if current_track:
        if not mr.get_track() == current_track:
            key ("K_m", "game_menu") action Play("music", current_loop if current_loop else current_track, loop=True if current_loop else False), Return()
        else:
            key ("K_m", "game_menu") action Queue("music", current_loop if current_loop else current_track, loop=True if current_loop else False), Return()
    else:
        key ("K_m", "game_menu") action mr.Stop(), Return()
    
    # Start the music playing on entry to the music room.
    if not renpy.music.is_playing() and persistent._start_music_on_enter:
        on "replace" action mr.Play()

    if not custom_keep_music_playing:
        # Restore the main menu music upon leaving.
        if config.main_menu_music:
            if not mr.get_track() == config.main_menu_music:
                on "replaced" action Play("music", config.main_menu_music, loop=True)
            else:
                on "replaced" action Queue("music", config.main_menu_music, loop=True)
        else:
            on "replaced" action mr.Stop()

    style_prefix "musicroom"
    tag menu
    default barvalue = AdjustableAudioPositionValue()
    default barvalue_active = AudioPositionValue()
    default timer_active = False
    default show_locked = False
    default previoustrack = ""
    default currentTrack = ""
    default nexttrack = ""
    default prog_tt = ""
    default mouse_active = False

    timer .5 action GetMusicPlaying() repeat True

    use game_menu(_("Music"), scroll=None):
        vbox:
            hbox:
                spacing 10
                hbox:
                    xfill True
                    xsize 690
                    spacing 10
                    imagebutton:
                        style "imagebutton_sounds"
                        idle MP_IMG("back")
                        hover MP_IMG("back", "hover")
                        selected "back_button_selected"
                        insensitive "back_button_insensitive"
                        action mr.Previous(),SetLocalVariable("timer_active", True)
                        tooltip _("Previous Track\n[mr.previous_track]")
                    imagebutton:
                        style "imagebutton_sounds"
                        idle MP_IMG("rewind")
                        hover MP_IMG("rewind", "hover")
                        selected "rewind_button_selected"
                        insensitive "rewind_button_insensitive"
                        action mr.Rewind()
                        tooltip _("Rewind\n[mr.current_track]")
                    if renpy.music.is_playing(channel='music'):
                        imagebutton:
                            style "imagebutton_sounds"
                            idle (MP_IMG("play") if mr.get_pause() else MP_IMG("pause"))
                            hover (MP_IMG("play", "hover") if mr.get_pause() else MP_IMG("pause", "hover"))
                            selected ("play_button_selected" if mr.get_pause() else "pause_button_selected")
                            insensitive ("play_button_insensitive" if mr.get_pause() else "pause_button_insensitive")
                            action mr.TogglePause()
                            tooltip _("Pause/Play\n[mr.current_track]")
                    else:
                        imagebutton:
                            style "imagebutton_sounds"
                            idle MP_IMG("play")
                            hover MP_IMG("play", "hover")
                            selected "play_button_selected"
                            insensitive "play_button_insensitive"
                            action mr.Play()
                            tooltip _("Play\n[mr.current_track]")
                    imagebutton:
                        style "imagebutton_sounds"
                        idle MP_IMG("stop")
                        hover MP_IMG("stop", "hover")
                        selected "stop_button_selected"
                        insensitive "stop_button_insensitive"
                        action mr.Stop()
                        tooltip _("Stop\n[mr.current_track]")
                    imagebutton:
                        style "imagebutton_sounds"
                        idle MP_IMG("fast_forward")
                        hover MP_IMG("fast_forward", "hover")
                        selected "fast_forward_button_selected"
                        insensitive "fast_forward_button_insensitive"
                        action mr.Forward()
                        tooltip _("Fast Forward\n[mr.current_track]")
                    imagebutton:
                        style "imagebutton_sounds"
                        idle MP_IMG("next")
                        hover MP_IMG("next", "hover")
                        selected "next_button_selected"
                        insensitive "next_button_insensitive"
                        action mr.Next(),SetLocalVariable("timer_active", True)
                        tooltip _("Next Track\n[mr.next_track]")
                    imagebutton:
                        style "imagebutton_sounds"
                        idle (MP_IMG("repeat_once") if mr.single_track else MP_IMG("repeat"))
                        hover ((MP_IMG("repeat", "hover") if mr.single_track else MP_IMG("repeat_once", "hover"))\
                            if mr.single_track else (MP_IMG("repeat_once", "hover") if not  mr.single_track else MP_IMG("repeat", "hover")))
                        selected ("repeat_once_button_selected" if mr.single_track else "repeat_button_selected")
                        insensitive ("repeat_once_button_insensitive" if mr.single_track else "repeat_button_insensitive")
                        action mr.ToggleSingleTrack()
                        tooltip _("Repeat\n[mr.current_track]")
                    imagebutton:
                        style "imagebutton_sounds"
                        idle (MP_IMG("shuffle") if mr.shuffle else MP_IMG("shuffle_off"))
                        hover ((MP_IMG("shuffle_off","hover") if mr.shuffle else MP_IMG("shuffle","hover"))\
                            if mr.shuffle else (MP_IMG("shuffle","hover") if not mr.shuffle else MP_IMG("shuffle_off","hover")))
                        selected ("shuffle_button_selected" if mr.shuffle else "shuffle_off_button_selected")
                        insensitive ("shuffle_button_insensitive" if mr.shuffle else "shuffle_off_button_insensitive")
                        action mr.ToggleShuffle()
                        tooltip _("Shuffle Playlist")
                    if len(mr.unlocked_playlist()) < sum(len(titles) for titles in music_tracks.values()):
                        imagebutton:
                            style "imagebutton_sounds"
                            idle (MP_IMG("unlocked") if show_locked else MP_IMG("locked"))
                            hover (MP_IMG("unlocked", "hover") if show_locked else MP_IMG("locked","hover"))
                            selected ("unlocked_button_selected" if show_locked else "locked_button_selected")
                            insensitive ("unlocked_button_insensitive" if show_locked else "locked_button_insensitive")
                            action ToggleLocalVariable("show_locked")
                            sensitive len(mr.unlocked_playlist()) < sum(len(titles) for titles in music_tracks.values())
                            tooltip _("Show Locked\n[mr.current_track]")
                    imagebutton:
                        style "imagebutton_sounds"
                        idle MP_IMG("settings")
                        hover MP_IMG("settings", "hover")
                        action Show("color_picker_mr", transition=dissolve)
                        tooltip _("Settings")
                    imagebutton:
                        style "imagebutton_sounds"
                        idle (MP_IMG("silent",size=gui.button_size_mute) if get_mute(channel="music") == 0.0\
                            else MP_IMG("volume_half",size=gui.button_size_mute) if get_mute(channel="music")\
                            > 0.0 and get_mute(channel="music") < 0.6 or get_mute(channel="music")\
                            == 0.6 else MP_IMG("volume",size=gui.button_size_mute))
                        hover (MP_IMG("silent","hover",size=gui.button_size_mute) if get_mute(channel="music") == 0.0\
                            else MP_IMG("volume_half","hover",size=gui.button_size_mute) if get_mute(channel="music")\
                            > 0.0 and get_mute(channel="music") < 0.6 or get_mute(channel="music")\
                            == 0.6 else MP_IMG("volume","hover",size=gui.button_size_mute))
                        selected "mute_player_selected"
                        insensitive "mute_player_insensitive"
                        action MutePlayer()
                        tooltip _("Mute Music")
                hbox:
                    xsize 720
                    spacing 5
                    xalign 1.0
                    add "readablePos" yalign 0.0 yoffset -5
                    bar value (barvalue if not timer_active and renpy.music.is_playing(channel='music') else barvalue_active):
                        if not timer_active:
                            hovered barvalue.hovered
                            unhovered barvalue.unhovered
                            tooltip _("Progress\n[mr.current_track]")
                        base_bar MP_BAR("idle")
                        hover_base_bar MP_BAR("hover")
                        thumb MP_THUMB("hover")
                        hover_thumb MP_THUMB("idle")
                    add "readableDur" yalign 0.0 yoffset -5
            hbox:
                xfill True            
                vbox:
                    xalign 0.0
                    label _("Music Volume: %s"%VolumeDisplay('music')) xalign 0.0 text_color MP_TEXT("idle")
                vbox:
                    xalign 1.0
                    bar value Preference("music volume") xalign 1.0 tooltip _("Volume\n{}".format(VolumeDisplay('music'))):
                        hovered SetLocalVariable("mouse_active", True)
                        unhovered SetLocalVariable("mouse_active", False)
                        base_bar MP_BAR("idle")
                        hover_base_bar MP_BAR("hover")
                        thumb MP_THUMB("hover")
                        hover_thumb MP_THUMB("idle")
            vpgrid:
                id "music"
                scrollbars "vertical"
                xsize config.screen_width - gui.game_menu_navigation_frame_xsize
                mousewheel True
                draggable True
                pagekeys True
                cols 1
                side_yfill True
                side_xfill True
                spacing 5
                xfill True
                vbox:
                    spacing 5
                    for artist in sorted_music_tracks(music_tracks).keys():
                        frame:
                            has vbox
                            text artist
                            for title in sorted(music_tracks[artist].keys()):
                                $ track_info = music_tracks[artist][title]
                                
                                $ track = track_info["musicroom_path"]
                                $ length = track_info.get("length", "0:00")
                                $ get_locked = track_info.get("unlocked") and track in mr.unlocked_playlist()
                                $ locked = _("- locked") if not track_info.get("unlocked") else _("- unlocked")
                                $ custom = _(" (User Music)") if track_info.get("custom") else ""
                                if seen_track(track):
                                    $ track_info["unlocked"] = True
                                if show_locked:
                                    textbutton "{}{}({}){}".format(title," {}".format(locked), length, custom):
                                        action Function(single_unlock, track)#mr.Play(track),SelectedIf(mr.Play(track))
                                        if GetMusicPlaying().filename == track:
                                            at music_playing_trans
                                        text_color ("#F0F" if not get_locked else MP_TEXT("idle"))
                                        text_hover_color MP_TEXT("hover")
                                        text_selected_color gui.selected_color
                                        text_insensitive_color gui.insensitive_color
                                else:
                                    if get_locked:
                                        textbutton "{} {}{}".format(title, length, custom):
                                            action mr.Play(track),SelectedIf(mr.Play(track))
                                            if GetMusicPlaying().filename == track:
                                                at music_playing_trans
                                            text_color MP_TEXT("idle")
                                            text_hover_color MP_TEXT("hover")
                                            text_selected_color gui.selected_color
                                            text_insensitive_color gui.insensitive_color
                                    else:
                                        textbutton _("Locked"):
                                            text_color MP_TEXT("idle")
                                            text_hover_color MP_TEXT("hover")
                                            text_selected_color gui.selected_color
                                            text_insensitive_color gui.insensitive_color

    if timer_active:
        timer 3 action SetLocalVariable("timer_active", False)

    if tooltip:
        nearrect:
            focus "tooltip"
            prefer_top True
            frame:
                at choice_appear(.5)
                style_prefix "tooltip"
                if _("Progress") in tooltip:
                    vbox:
                        text tooltip
                        add "readablePosTT" xalign 0.5
                else:
                    hbox:
                        text tooltip

    if mouse_active:
        key "mousedown_4" action SlowVolUp("music","_fast_vol_music","music")
        key "mousedown_5" action SlowVolDown("music","_fast_vol_music","music")

    text "Now Playing: [mr.current_track]" align (0.99, 0.05)

screen color_picker_mr():
    modal True
    default activate = False
    default option = ""
    default field = ""
    default state = "idle"
    use game_menu(_("Music Player Settings")):
        vbox:
            spacing 20
            hbox:
                box_wrap True
                vbox:
                    style_prefix "check"
                    label _("Music Volume\n[jg_s]{}".format("Fast" if persistent._fast_vol_music else "Slow"))
                    textbutton _("Fast"):
                        action SetField(persistent, "_fast_vol_music", True)
                    textbutton _("Slow"):
                        action SetField(persistent, "_fast_vol_music", False)
                vbox:
                    style_prefix "check"
                    label _("Music Buttons\n[jg_s]{}".format("Solid" if persistent._use_outline_music_buttons else "Outline"))
                    textbutton _("Solid"):
                        action SetField(persistent, "_use_outline_music_buttons", True)
                    textbutton _("Outline"):
                        action SetField(persistent, "_use_outline_music_buttons", False)

                vbox:
                    style_prefix "check"
                    label ("Button State\n[jg_s]{}".format("Idle" if state == "idle" else "Hover"))
                    textbutton _("Idle"):
                        action SetLocalVariable("state", "idle"), If(option == "_music_icon_{}_color".format(state), 
                            true=[SetScreenVariable("activate", False), SetScreenVariable("option", ""), SetScreenVariable("field", "")])
                    textbutton _("Hover"):
                        action SetLocalVariable("state", "hover"), If(option == "_music_icon_{}_color".format(state), 
                            true=[SetScreenVariable("activate", False), SetScreenVariable("option", ""), SetScreenVariable("field", "")])

                if len(mr.unlocked_playlist()) < sum(len(titles) for titles in music_tracks.values()):
                    vbox:
                        style_prefix "check"
                        label ("Unlock All\n[jg_s]")
                        textbutton _("Unlock"):
                            action Function(unlock_all_tracks)
            vbox:
                box_wrap True
                style_prefix "check"
                label _("FF and REW time in Seconds: %s"%(round_float(persistent._music_ff_rew)))
                hbox:
                    style_prefix "slider"
                    bar value FieldValue(persistent, "_music_ff_rew", 
                        range=9.0,
                        offset=1.0,
                        style="slider",
                        max_is_zero=False,
                        step=.1,
                        force_step=True
                        ) released SetField(persistent, "_music_ff_rew", round(float(persistent._music_ff_rew),2))
                    textbutton _("Reset") action SetField(persistent, "_music_ff_rew", 1.0) yoffset -8
            hbox:
                spacing 10
                imagebutton:
                    idle MP_IMG("back", state)
                    action NullAction()
                imagebutton:
                    idle MP_IMG("rewind", state)
                    action NullAction()
                imagebutton:
                    idle MP_IMG("play", state)
                    action NullAction()
                imagebutton:
                    idle MP_IMG("pause", state)
                    action NullAction()
                imagebutton:
                    idle MP_IMG("stop", state)
                    action NullAction()
                imagebutton:
                    idle MP_IMG("fast_forward", state)
                    action NullAction()
                imagebutton:
                    idle MP_IMG("next", state)
                    action NullAction()
                imagebutton:
                    idle MP_IMG("repeat_once", state)
                    action NullAction()
                imagebutton:
                    idle MP_IMG("repeat", state)
                    action NullAction()
                imagebutton:
                    idle MP_IMG("shuffle", state)
                    action NullAction()
                imagebutton:
                    idle MP_IMG("shuffle_off", state)
                    action NullAction()
                imagebutton:
                    idle MP_IMG("silent", state, size=gui.button_size_mute)
                    action NullAction()
                imagebutton:
                    idle MP_IMG("volume_half", state, size=gui.button_size_mute)
                    action NullAction()
                imagebutton:
                    idle MP_IMG("volume", state, size=gui.button_size_mute)
                    action NullAction()
            hbox:#Good Choice
                spacing 15
                vbox:
                    textbutton _("Set {} Color".format(state.title())):
                        
                        action If(option == "_music_icon_{}_color".format(state), 
                            true=[SetScreenVariable("activate", False), SetScreenVariable("option", ""), SetScreenVariable("field", "")], 
                            false=[SetScreenVariable("activate", True), SetScreenVariable("option", "_music_icon_{}_color".format(state)), SetScreenVariable("field", "_music_icon_{}_color".format(state))])
                        text_color getattr(persistent,"_music_icon_{}_color".format(state))
                        text_hover_color adjust_brightness(getattr(persistent,"_music_icon_{}_color".format(state)), -50)
                vbox:
                    textbutton _("Reset"):
                        action SetField(persistent, "_music_icon_{}_color".format(state), getattr(persistent,"_music_icon_{}_color_default".format(state)))
                        sensitive getattr(persistent,"_music_icon_{}_color".format(state)) != getattr(persistent,"_music_icon_{}_color_default".format(state))
            
        if activate:
            use color_picker(FieldSimpleValue(persistent,option), field, (1.0,1.0))

transform music_playing_trans:
    alpha 1.0
    easein .5 alpha 0.5
    pause .5
    easein .5 alpha 1.0
    repeat

screen music_overlay():
    timer .5 action GetMusicPlaying() repeat True
    default shown = False

    mousearea:
        xysize (100,100)
        align (1.0,0.12)
        hovered SetLocalVariable("shown", True), With(dissolve)
        unhovered SetLocalVariable("shown", False), With(dissolve)
    if shown and mr.get_track() and persistent._music_overlay:
        frame:
            align (1.0,0.12)
            padding (20,10,20,10)
            vbox:
                text _("Now Playing") size gui.bar_size+10
                text _("[mr.current_track]") size gui.bar_size
                text _("Looping {}".format(mr.get_track() in renpy.music.get_loop())) size gui.bar_size-5
                hbox:
                    spacing 30
                    text _("Progress") size gui.text_size-10
                    hbox:
                        xalign 1.0
                        yoffset -2
                        add "readablePosTT"
                        text "/" size gui.text_size-10
                        add "readableDurTT"

init python:
    config.overlay_screens.append("music_overlay")

style musicroom_label_text is gui_label_text:
    color gui.bar_left_color
    outlines gui.musicroom_time_text_outlines

style imagebutton_sounds:
    hover_sound "audio/sfx/button_h.mp3"
    activate_sound "audio/sfx/button_a.mp3"

style musicroom_imagebutton:
    align (0.5, 0.5)

style musicroom_vscrollbar is gui_vscrollbar:
    unscrollable "hide"
    #base_bar Frame(Solid(gui.bar_left_color), gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    #thumb Frame(Solid(gui.bar_right_color), gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    #hover_base_bar Frame(Solid(gui.bar_right_color), gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    #hover_thumb Frame(Solid(gui.bar_left_color), gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style musicroom_text:
    properties gui.text_properties("musicroom")

style music_room_time:
    font gui.musicroom_time_text_font
    size gui.musicroom_time_size
    outlines gui.musicroom_time_text_outlines

style musicroom_hbox:
    ysize gui.bar_size*2

style musicroom_button:
    properties gui.button_properties("musicroom_button")
    xfill False
    hover_sound "audio/sfx/button_h.mp3"
    activate_sound "audio/sfx/button_a.mp3"

style musicroom_button_text:
    properties gui.text_properties("musicroom_button")

style musicroom_frame:
    background gui.musicroom_frame_background
    padding gui.musicroom_frame_padding
    xsize gui.musicroom_frame_xsize

style musicroom_bar is gui_bar:
    hover_sound "audio/sfx/button_h.mp3"
    activate_sound "audio/sfx/button_a.mp3"
    xsize 500
    idle_left_bar Transform(
        Frame(
            "mod/images/%s_%s/left.png"%aspect_ratio,
            gui.bar_borders, tile=gui.bar_tile),
        matrixcolor=ColorSingle(gui.musicroom_bar_left_idle_color))
    idle_right_bar Transform(
        Frame(
            "mod/images/%s_%s/right.png"%aspect_ratio,
            gui.bar_borders, tile=gui.bar_tile),
        matrixcolor=ColorSingle(gui.musicroom_bar_right_idle_color))

    hover_left_bar Transform(
        Frame(
            "mod/images/%s_%s/left.png"%aspect_ratio,
            gui.bar_borders, tile=gui.bar_tile),
        matrixcolor=ColorSingle(gui.musicroom_bar_left_hover_color))
    hover_right_bar Transform(
        Frame(
            "mod/images/%s_%s/right.png"%aspect_ratio,
            gui.bar_borders, tile=gui.bar_tile),
        matrixcolor=ColorSingle(gui.musicroom_bar_right_hover_color))

style musicroom_slider is gui_slider:
    base_bar Frame(Solid(gui.bar_left_color), gui.slider_borders, tile=gui.slider_tile)
    hover_base_bar Frame(Solid(gui.bar_right_color), gui.slider_borders, tile=gui.slider_tile)
    thumb Transform(Solid(gui.bar_right_color),ysize=gui.slider_size, xsize=30)
    hover_thumb Transform(Solid(gui.bar_left_color),ysize=gui.slider_size, xsize=30)
    xsize 500
    xalign 1.0