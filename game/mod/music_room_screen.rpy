screen musicroom():
    $ tooltip = GetTooltip()
    default current_loop = False
    default current_track = None
    if not main_menu:
        on "replace" action [SetLocalVariable("current_track", mr.get_track()),
            SetLocalVariable("current_loop", renpy.music.get_loop())]
        if current_track:
            if not mr.get_track() == current_track:
                key ("K_m", "game_menu") action Play("music", current_track, loop=current_loop), Function(preferences.set_mixer, "music", 0.5), Return()
            else:
                key ("K_m", "game_menu") action Queue("music", current_track, loop=current_loop), Function(preferences.set_mixer, "music", 0.5), Return()
        else:
            key ("K_m", "game_menu") action mr.Stop(), Return()
    # Start the music playing on entry to the music room.
    if not renpy.music.is_playing() and persistent._start_music_on_enter:
        on "replace" action mr.Play()

    if not custom_keep_music_playing:
        # Restore the main menu music upon leaving.
        if config.main_menu_music:
            if not mr.get_track() == config.main_menu_music:
                on "replaced" action Play("music", config.main_menu_music, loop=True), Function(preferences.set_mixer, "music", 0.5)
            else:
                on "replaced" action Queue("music", config.main_menu_music, loop=True), Function(preferences.set_mixer, "music", 0.5)
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
                xfill True
                imagebutton:
                    style "imagebutton_sounds"
                    idle "back_button_idle"
                    hover "back_button_hover"
                    selected "back_button_selected"
                    insensitive "back_button_insensitive"
                    action mr.Previous(),SetLocalVariable("timer_active", True)
                    tooltip "Previous Track\n[mr.previous_track]"
                imagebutton:
                    style "imagebutton_sounds"
                    idle "rewind_button_idle"
                    hover "rewind_button_hover"
                    selected "rewind_button_selected"
                    insensitive "rewind_button_insensitive"
                    action mr.Rewind()
                    tooltip "Rewind\n[mr.current_track]"
                if renpy.music.is_playing(channel='music'):
                    imagebutton:
                        style "imagebutton_sounds"
                        idle ("play_button_idle" if mr.get_pause() else "pause_button_idle")
                        hover ("play_button_hover" if mr.get_pause() else "pause_button_hover")
                        selected ("play_button_selected" if mr.get_pause() else "pause_button_selected")
                        insensitive ("play_button_insensitive" if mr.get_pause() else "pause_button_insensitive")
                        action mr.TogglePause()
                        tooltip "Pause/Play\n[mr.current_track]"
                else:
                    imagebutton:
                        style "imagebutton_sounds"
                        idle "play_button_idle"
                        hover "play_button_hover"
                        selected "play_button_selected"
                        insensitive "play_button_insensitive"
                        action mr.Play()
                        tooltip "Play\n[mr.current_track]"
                imagebutton:
                    style "imagebutton_sounds"
                    idle "stop_button_idle"
                    hover "stop_button_hover"
                    selected "stop_button_selected"
                    insensitive "stop_button_insensitive"
                    action mr.Stop()
                    tooltip "Stop\n[mr.current_track]"
                imagebutton:
                    style "imagebutton_sounds"
                    idle "fast_forward_button_idle"
                    hover "fast_forward_button_hover"
                    selected "fast_forward_button_selected"
                    insensitive "fast_forward_button_insensitive"
                    action mr.Forward()
                    tooltip "Fast Forward\n[mr.current_track]"
                imagebutton:
                    style "imagebutton_sounds"
                    idle "next_button_idle"
                    hover "next_button_hover"
                    selected "next_button_selected"
                    insensitive "next_button_insensitive"
                    action mr.Next(),SetLocalVariable("timer_active", True)
                    tooltip "Next Track\n[mr.next_track]"
                imagebutton:
                    style "imagebutton_sounds"
                    idle ("repeat_once_button_idle" if mr.single_track else "repeat_button_idle")
                    hover ("repeat_once_button_hover" if mr.single_track else "repeat_button_hover")
                    selected ("repeat_once_button_selected" if mr.single_track else "repeat_button_selected")
                    insensitive ("repeat_once_button_insensitive" if mr.single_track else "repeat_button_insensitive")
                    action mr.ToggleSingleTrack()
                    tooltip "Repeat\n[mr.current_track]"
                imagebutton:
                    style "imagebutton_sounds"
                    idle ("shuffle_button_idle" if mr.shuffle else "shuffle_off_button_idle")
                    hover ("shuffle_button_hover" if mr.shuffle else "shuffle_off_button_hover")
                    selected ("shuffle_button_selected" if mr.shuffle else "shuffle_off_button_selected")
                    insensitive ("shuffle_button_insensitive" if mr.shuffle else "shuffle_off_button_insensitive")
                    action mr.ToggleShuffle()
                    tooltip "Shuffle Playlist"
                #imagebutton:
                #    style "imagebutton_sounds"
                #    idle ("unlocked_button_idle" if show_locked else "locked_button_idle")
                #    hover ("unlocked_button_hover" if show_locked else "locked_button_hover")
                #    selected ("unlocked_button_selected" if show_locked else "locked_button_selected")
                #    insensitive ("unlocked_button_insensitive" if show_locked else "locked_button_insensitive")
                #    action ToggleLocalVariable("show_locked")
                #    tooltip "Show Locked\n[mr.current_track]"
                imagebutton:
                    style "imagebutton_sounds"
                    idle "mute_player_idle"
                    hover "mute_player_hover"
                    selected "mute_player_selected"
                    insensitive "mute_player_insensitive"
                    action MutePlayer()
                    tooltip "Mute Music"
                hbox:
                    
                    spacing 5
                    xalign 1.0
                    add "readablePos" yalign 0.0 yoffset -5
                    bar value (barvalue if not timer_active and renpy.music.is_playing(channel='music') else barvalue_active):
                        if not timer_active:
                            hovered barvalue.hovered
                            unhovered barvalue.unhovered
                            tooltip "Progress\n[mr.current_track]"
                    add "readableDur" yalign 0.0 yoffset -5
            hbox:
                xfill True            
                vbox:
                    xalign 0.0
                    label _("Music Volume: %s"%VolumeDisplay('music')) xalign 0.0
                vbox:
                    xalign 1.0
                    bar value Preference("music volume") xalign 1.0 tooltip "Volume\n{}".format(VolumeDisplay('music')):
                        hovered SetLocalVariable("mouse_active", True)
                        unhovered SetLocalVariable("mouse_active", False)
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
                            for title in sorted_music_tracks(music_tracks[artist]).keys():
                                $ track = music_tracks[artist][title]["musicroom_path"]
                                $ length = music_tracks[artist][title].get("length", "0:00")
                                $ get_locked = music_tracks[artist][title].get("unlocked")
                                $ locked = _("- locked") if not music_tracks[artist][title].get("unlocked") else ""
                                $ custom = _(" (User Music)") if music_tracks[artist][title].get("custom") else ""
                                if seen_track(track):
                                    $ music_tracks[artist][title]["unlocked"] = True
                                if show_locked:
                                    textbutton "{}{}({}){}".format(title," {}".format(locked), length, custom):
                                        action mr.Play(track),SelectedIf(mr.Play(track))
                                else:
                                    if get_locked:
                                        textbutton "{}{}({}){}".format(title," {}".format(locked), length, custom):
                                            action mr.Play(track),SelectedIf(mr.Play(track))
                                    else:
                                        textbutton _("Locked")

    if timer_active:
        timer 3 action SetLocalVariable("timer_active", False)

    if tooltip:
        nearrect:
            focus "tooltip"
            prefer_top True
            frame:
                at choice_appear(.5)
                style_prefix "tooltip"
                if "Progress" in tooltip:
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

screen music_overlay():
    timer .5 action GetMusicPlaying() repeat True
    default shown = False

    mousearea:
        xysize (100,100)
        align (1.0,0.12)
        hovered SetLocalVariable("shown", True), With(dissolve)
        unhovered SetLocalVariable("shown", False), With(dissolve)
    if shown and mr.get_track():
        frame:
            align (1.0,0.12)
            padding (20,10,20,10)
            vbox:
                text "Now Playing" size gui.bar_size+10
                text "[mr.current_track]" size gui.bar_size
                text "Looping {}".format(mr.get_track() in renpy.music.get_loop()) size gui.bar_size-5
                hbox:
                    spacing 30
                    text "Progress" size gui.text_size-10
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
    base_bar Frame(Solid(gui.bar_left_color), gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame(Solid(gui.bar_right_color), gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    hover_base_bar Frame(Solid(gui.bar_right_color), gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    hover_thumb Frame(Solid(gui.bar_left_color), gui.vscrollbar_borders, tile=gui.scrollbar_tile)

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
