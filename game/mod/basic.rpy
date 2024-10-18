##################################################################################################
## Check Screens to make sure we do not overwrite developers original                           ##
## screens                                                                                      ##
## Modify the following:                                                                        ##
##    'gui.jg_mod_version'                                                                      ##
##    'gui.dev_mod_page'                                                                        ##
##    'gui.mod_update_date'                                                                     ##
##    'gui.built_in_cheats' if it changes                                                       ##
##    'gui.developer_name'                                                                      ##
##    'gui.developer_support'                                                                   ##
##################################################################################################
init 1:#Mod Defaults
    define gui.mod_dev = "JiGSaW Games Studios"
    define gui.jg_mod_version = '0.06.2.1_alpha'
    define gui.mod_update_version = 1
    define gui.dev_mod_page = "academy_live_mod"
    define gui.mod_update_date = "11/10/2024"
    define gui.built_in_cheats = "IWBUWS"
    define gui.mod_update_url = "https://github.com/JiGSaWKilla89/{}/releases".format(gui.dev_mod_page)
    define gui.mod_check_url = 'https://raw.githubusercontent.com/JiGSaWKilla89/{}/main/version'.format(gui.dev_mod_page)
    define gui.donate_mod = "https://buymeacoffee.com/jigsawgames"
    define gui.mod_issues = "https://github.com/JiGSaWKilla89/{}/issues/new/choose".format(gui.dev_mod_page)
    define gui.developer_name = "passhonQ"
    define gui.developer_support = "https://www.patreon.com/passhonQ"
    default mod_changelog = read_changelog()
    default mod_updated = "None", gui.jg_mod_version

    define gui.mod_info_size = gui.title_text_size-20
    define gui.mod_savename_input_size = gui.text_size-10
    define gui.mod_savename_input_ypos = 10
    define gui.mod_savename_input_xpos = -30
    define gui.mod_save_page_input_ypos = -30
    define gui.mod_save_goto_page_xsize = 380
    define gui.mod_save_goto_page_ysize = 50

    define gui.use_custom_caret = False

    define gui.textbox_location = "gui/textbox.png"

default persistent._support_mod_display = True

style donate_mod_text:
    text_align 0.5
    align (0.5,0.5)
    outlines [(2, "#fff9", 1, 1)]

style donate_mod_vbox:
    align (0.5,0.5)
    spacing 10

style donate_mod_hbox:
    align (0.5,0.5)
    spacing 20

style donate_mod_button:
    align (0.5,0.5)

style donate_mod_button_text:
    text_align 0.5
    align (0.5,0.5)


screen support_mod_developer():
    style_prefix "donate_mod"
    default closing = 30

    button:
        action Return()
    if closing > 0:
        timer 1 action SetLocalVariable("closing", closing-1) repeat True
    if closing == 0:
        timer .1 action Return()
    text "Window Will Close in: %s"%closing align (0.01, 0.01)
    vbox:
        spacing 200
        vbox:
            text "{b}{u}[jg_1]JiG[jg_3][jg_2]SaW[jg_3] Multi-Mod{/u}{/b}" size gui.name_text_size
            text "for [config.name] Version: [gui.jg_mod_version]"
            text "Current Game Version: [config.version]" size gui.text_size-10 color "#FF0"
            text "If you enjoy using my mod please consider buying me a beer."
        hbox:
            textbutton "Buy Me a Beer" action OpenURL(gui.donate_mod)
            text " | "
            textbutton "Return to Game" action Return()

label before_main_menu:
    if persistent._support_mod_display:
        show screen support_mod_developer
        $ renpy.pause(hard=True)
    return

init 100:# Defaults
    # Academy Live
    define d = Dissolve(0.1)
    define d1 = Dissolve (0.5)
    define d2 = Dissolve (1.0)

init 1:#Defines
    define gui.slot_delete_text_idle_color = "#F00"
    define gui.slot_delete_text_outlines = [(2, "#0009", 1, 1)]
    define gui.input_prompt_text_outlines = [ (2, "#00000080", 0, 0) ]
    define gui.input_button_text_outlines = [ (2, "#00000080", 0, 0) ]
    define gui.quick_button_text_outlines = [(2, "#0009", 1, 1)]
    
    define config.end_game_transition = dissolve
    define config.end_splash_transition = dissolve
    define config.enter_replay_transition = dissolve
    define config.exit_replay_transition = dissolve
    define config.after_load_transition = dissolve
    define config.end_game_transition = dissolve
    define config.game_main_transition = dissolve
    define config.main_game_transition = dissolve

init -5 python:
    import requests
    import json
    from datetime import datetime

    def read_changelog():
        path = os.path.join(config.gamedir, "mod", "MODCHANGELOG")

        try:
            with open(path, "r") as f:
                return f.readlines()
        except:
            return []

    def write_changelog(line):
        path = os.path.join(config.gamedir, "mod", "MODCHANGELOG")

        data = read_changelog()

        with open(path, "a") as f:
            if not f"{line}\n" in data:
                f.write(f"{line}\n")

    def get_latest_mod():
        global mod_changelog
        # URL of the file containing the dictionary
        response = None  # Initialize response to None

        # Fetch the file from the URL
        try:
            response = requests.get(gui.mod_check_url)

            # Check if the request was successful
            if response.status_code == 200:
                try:
                    # Load the JSON data into a Python dictionary
                    data = json.loads(response.text)

                    web_date = data["date_update"]
                    web_version_game = data["version_game"]
                    web_version = data["version_update"]

                    for i in data["changelog"]:
                        write_changelog(i)

                    mod_changelog = read_changelog()

                    if gui.jg_mod_version != web_version_game:
                        return "Mod game version changed"
                    elif gui.mod_update_version != web_version:
                        return "Mod version changed", web_version_game
                    elif gui.mod_update_date != web_date:
                        return "Update date has changed", web_version_game
                    elif config.version > web_version_game:
                        return "Game Version Newer Than Mod", config.version
                    else:
                        return "Mod up-to-date", gui.jg_mod_version
                except json.JSONDecodeError as e:
                    return "JSON Error", gui.jg_mod_version
            else:
                return "Could Not Connect to Host"
        except requests.ConnectionError as ce:
            if response is not None:
                renpy.write_log(f"HTTP Error: Received status code {response.status_code}: {ce}")
            else:
                renpy.write_log(f"Connection Error: {ce}")
            return "HTTP Error", gui.jg_mod_version

        except requests.Timeout as rto:
            renpy.write_log(f"Timeout: The request timed out {rto}")
            return "Timeout", gui.jg_mod_version

        except requests.RequestException as e:
            renpy.write_log(f"Request Error: {e}")
            return "Request Error", gui.jg_mod_version