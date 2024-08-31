init 1000 python:
    import os

    #update_wt("events.rpy")
    #update_wt("script.rpy")
    def update_wt(file):
        new_out = []
        with renpy.open_file(file, encoding="utf-8") as readfile:
            return readfile.readlines()

    def walkthrough_dict():
        green = "#0F0"
        blue = "#00F"
        yellow = "#FF0"
        red = "#F00"
        pink = "#F0F"

        _view = "Viewership"
        _aplc = "Academic Perversion Level"
        _sttr = "Student Trust"
        _boar = "Board"
        _dech = "Dealers Choice"
        _goch = "Good Choice"
        _bach = "Bad Choice"
        _recc = "Recommended"
        _poss = "Possible"
        _ffch = "50/50 Choice"
        _bech = "Best Choice"
        _oupr = "Outside Pressure"
        _boun = "Bounty Checks"

        return {
            ("script.rpyc", 2288)  : {
                "Yes, Let's see where this goes" : {
                    "wt" : f"{_recc}",
                    "hint" : [
                        "v2 = 1",
                        "[main.name] Corruption +1"
                        ],
                    "color" : pink
                    },
                "No, I've seen enough" : {
                    "wt" : "",
                    "hint" : [
                        "v2 = 0", 
                        "[main.name] Corruption -1"
                        ],
                    "color" : None
                    }
                },
            ("script.rpyc", 4531)  : {
                "Stay and do Stretches." : {
                    "wt" : f"{_goch}",
                    "hint" : [
                        "[main.name] Topics | Gym_Stretch"
                        f"{_view} +50", 
                        f"{_boar} +1", 
                        f"{_aplc} +1"
                        ],
                    "color" : green
                    },
                "Leave" : {
                    "wt" : f"{_bach}",
                    "hint" : [
                        f"{_view} -50", 
                        "[main.name] Corruption -1"
                        ],
                    "color" : red
                    }
                },
            ("script.rpyc", 5470)  : {
                "Try to touch her butt" : {
                    "wt" : f"{_goch}",
                    "hint" : [
                        "v8 +1",
                        f"{_view} +10",
                        ],
                    "color" : green
                    },
                "Don't try anything" : {
                    "wt" : f"{_bach}",
                    "hint" : [
                        f"{_view} -50",
                        ],
                    "color" : red
                    }
                },
            ("script.rpyc", 5725)  : {
                "Let her continue" : {
                    "wt" : f"{_goch}",
                    "hint" : [
                        "v6 +1",
                        f"{_view} +50",
                        f"{_aplc} +1"
                        ],
                    "color" : green
                    },
                "Stop her" : {
                    "wt" : f"{_bach}",
                    "hint" : [
                        f"{_view} -100",
                        ],
                    "color" : red
                    }
                },
            ("script.rpyc", 5869)  : {
                "Touch her pussy" : {
                    "wt" : f"{_goch}",
                    "hint" : [
                        "[yoko.name] Topics | Gym_Intro_Yoko_Cum"
                        "v8 +1",
                        f"{_view} +150",
                        f"{_poss} {_view} +200",
                        f"{_poss} {_sttr} -2",
                        f"{_poss} {_aplc} +2",
                        f"{_poss} [main.name] Corruption +1"
                        ],
                    "color" : green
                    }
                },
            ("script.rpyc", 6732)  : {
                "Strike her" : {
                    "wt" : f"{_ffch}",
                    "hint" : [
                        "[haruka.name] Strike +1 Later Removed", 
                        f"{_boar} +1", 
                        f"{_sttr} -1",
                        "[haruka.name] Sex Scene Later",
                        "[haruka.name] Topics | Sex_MC, Sex_Vaginal_MC, H_MC",
                        "[haruka.name] Sexstats | Vaginal +1, Creampies +1",
                        f"{_poss} [haruka.name] Topics | Chocked",
                        ],
                    "color" : yellow
                    },
                "Don't do it" : {
                    "wt" : f"{_goch} ",
                    "hint" : [
                        "[haruka.name] Affection +1", 
                        f"{_sttr} +2"
                        ],
                    "color" : green
                    }
                },
            ("script.rpyc", 7138)  : {
                "Interrupt this" : {
                    "wt" : "",
                    "hint" : [
                        "[soushu.name] Topics | MC_Against", 
                        "[soushi.name] Met",
                        "[ryoichi.name] Met",
                        "[izo.name] Met",
                        "[masaru.name] Met",
                        f"{_view} -10",
                        f"{_sttr} +2",
                        "[ayumi.name] Affection +5"
                        ],
                    "color" : None
                    },
                "Let them continue" : {
                    "wt" : f"{_goch}",
                    "hint" : [
                        "[main.name] Topics | Weekly Exams"
                        "[ayumi.name] Corruption +1", 
                        f"{_view} +50"
                        ],
                    "color" : green #Yellow
                    }
                },
            ("script.rpyc", 7274)  : {
                "Interrupt this." : {
                    "wt" : "",
                    "hint" : [
                        "[soushu.name] Topics | MC_Against", 
                        "[soushi.name] Met",
                        "[ryoichi.name] Met",
                        "[izo.name] Met",
                        "[masaru.name] Met",
                        f"{_view} -10",
                        f"{_sttr} +2",
                        "[ayumi.name] Affection +5"
                        ],
                    "color" : green #Yellow
                    },
                "Let them continue" : {
                    "wt" : f"{_goch}",
                    "hint" : [
                        "[ayumi.name] Corruption +5", 
                        f"{_view} +150"
                        ],
                    "color" : green #Yellow
                    }
                },
            ("script.rpyc", 8383)  : {
                "Stay and watch" : {
                    "wt" : f"{_goch}",
                    "hint" : [
                        "[main.name] Topics | Spank", 
                        f"{_view} +100", 
                        f"{_aplc} +1", 
                        f"{_sttr} -1", 
                        f"{_poss} {_view} +15", 
                        f"{_poss} {_sttr} -1", 
                        f"{_poss} [main.name] Corruption +1"
                        ],
                    "color" : green
                    },
                "Just give her a strike, no more spanking" : {
                    "wt" : f"{_bach}",
                    "hint" : [
                        "[suzu.name] Strike+1", 
                        f"{_view} -100", 
                        f"{_sttr} +1"
                        ],
                    "color" : red
                    },
                "I'll leave you to it" : {
                    "wt" : f"{_ffch}",
                    "hint" : [
                        f"{_view} +10", 
                        f"{_sttr} -1"
                        ],
                    "color" : yellow
                    }
                },
            ("script.rpyc", 8659)  : {
                "Soft Spanking" : {
                    "wt" : f"{_dech} ({_recc})" if v8 >= 3 else f'{_dech}',
                    "hint" : "Whack That ass *2" if v8 == 3 else "Whack That ass *1" if v8 == 4 else "",
                    "color" : blue
                    },
                "Normal Spanking" : {
                    "wt" : f"{_dech} ({_recc})" if v8 == 2 else f'{_dech}',
                    "hint" : "Whack That ass *1" if v8 == 2 else "",
                    "color" : blue
                    },
                "Hard Spanking" : {
                    "wt" : f"{_dech} ({_recc})" if v8 < 2 else f'{_dech}',
                    f"hint" : ["Whack That ass *2", "{_view} +3"] if v8 == 0  else ["Whack That ass *1", "{_view} +3"] if v8 == 1 else "{_view} +3",
                    "color" : blue
                    }
                },
            ("script.rpyc", 9600)  : {
                "\"Cool\" hairstyle" : {
                    "wt" : f"{_goch}",
                    "hint" : "[maiya.name] Affection +1",
                    "color" : green
                    }
                },
            ("script.rpyc", 9715)  : {
                "\"Cool\" pose" : {
                    "wt" : f"{_goch}",
                    "hint" : "[maiya.name] Affection +1",
                    "color" : green
                    }
                },
            ("script.rpyc", 10936) : {
                "Blue" : {
                    "wt" : f"{_dech}",
                    "hint" : "",
                    "color" : pink
                    },
                "Red" : {
                    "wt" : f"{_dech}",
                    "hint" : "",
                    "color" : pink
                    }
                },
            ("script.rpyc", 11239) : {
                "How attractive she is" : {
                    "wt" : f"{_recc}",
                    "hint" : "",
                    "color" : pink
                    },
                "A good sense of humor" : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        "[haruka.name] Affection +1"
                        ],
                    "color" : blue
                    }
                },
            ("script.rpyc", 11281) : {
                "5!" : {
                    "wt" : f"{_dech} ({_recc})",
                    "hint" : [
                        "[haruka.name] Affection +1"
                        ],
                    "color" : blue
                    },
                "4" : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        "[haruka.name] Affection +1"
                        ],
                    "color" : blue
                    },
                "1" : {
                    "wt" : f"{_bach}",
                    "hint" : [
                        "[haruka.name] Affection -1"
                        ],
                    "color" : red
                    },
                },
            ("script.rpyc", 11506) : {
                "Yes" : {
                    "wt" : "",
                    "hint" : [
                        "[haruka.name] Dictionary | MC_GF = 1"
                        ],
                    "color" : None
                    },
                "No" : {
                    "wt" : "",
                    "hint" : [
                        "[haruka.name] Dictionary | MC_GF = 0"
                        ],
                    "color" : None
                    }
                },
            ("script.rpyc", 12628) : {
                "Choke her" : {
                    "wt" : f"{_bech}",
                    "hint" : [
                        "[haruka.name] Affection +1",
                        "[haruka.name] Corruption +1",
                        f"{_boar} +1",
                        f"{_view} +100",
                        "[main.name] Corruption +1"
                        ],
                    "color" : green
                    },
                "Finish normally" : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        "[haruka.name] Affection +2",
                        ],
                    "color" : blue
                    }
                },
            
            ("events.rpyc", 1710)  : {
                "Bust [maiya.name]" : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        "[maiya.name] Affection -1",
                        f"{_sttr} -2",
                        ],
                    "color" : blue
                    },
                "Let her Cheat" : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        "[maiya.name] Topics | Favor_MC",
                        "[maiya.name] Affection +3",
                        f"{_sttr} +2",
                        "[hiroshige.name] Topics | Failed_Proposal" if maiya_panties_01.Completed else "",
                        ],
                    "color" : blue
                    },
                },
            ("events.rpyc", 1788)  : {
                "Bust [ri]" : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        "[rina.name] Topics | Useless_Kawaguchi",
                        f"{_sttr} -1",
                        ],
                    "color" : blue
                    },
                "Let her cheat" : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        f"{_sttr} +2",
                        ],
                    "color" : blue
                    },
                },
            ("events.rpyc", 2715)  : {
                "Let [ha] stay" : {
                    "wt" : f"{_bech}",
                    "hint" : [
                        "[haruka.name] Affection +1",
                        f"{_view} +20",
                        ],
                    "color" : green
                    },
                "Send [ha] away" : {
                    "wt" : f"{_bach}",
                    "hint" : [
                        "[haruka.name] Affection -1",
                        f"{_view} -50",
                        ],
                    "color" : red
                    },
                },
            ("events.rpyc", 3152)  : {
                "Ayumi" : {
                    "wt" : "Do Last",
                    "hint" : [
                        
                        ],
                    "color" : pink
                    },
                "Rina" : {
                    "wt" : "Do First",
                    "hint" : [
                        "[rina.name] Topics | Hates_Haruka",
                        ],
                    "color" : pink
                    },
                "Maiya" : {
                    "wt" : "Do Second",
                    "hint" : [
                        ],
                    "color" : pink
                    },
                },
            ("events.rpyc", 3302)  : {
                "Give a 0 to [ri]" : {
                    "wt" : "",
                    "hint" : [
                        "[rina.name] Topics | Cheater_Exam",
                        ],
                    "color" : None
                    },
                "Let [ri] redo the exam" : {
                    "wt" : f"{_goch}",
                    "hint" : [
                        "[rina.name] Topics | Cheater_Exam, Redo_Exam",
                        f"{_sttr} +1",
                        ],
                    "color" : green
                    },
                },
            ("events.rpyc", 3360)  : {
                "Give [ri] a Strike" : {
                    "wt" : "",
                    "hint" : [
                        "[rina.name] Strike +1",
                        ],
                    "color" : green
                    },
                "No Strike" : {
                    "wt" : f"{_goch}",
                    "hint" : [
                        ],
                    "color" : green
                    },
                },
            ("events.rpyc", 3533)  : {
                "Give a 0 to [maiya.name]" : {
                    "wt" : "",
                    "hint" : [
                        "[maiya.name] Topics | Cheater_Exam",
                        "[maiya.name] Affection -2",
                        f"{_sttr} -1"
                        ],
                    "color" : None
                    },
                "Let [maiya.name] redo the exam" : {
                    "wt" : f"{_goch}",
                    "hint" : [
                        "[maiya.name] Topics | Cheater_Exam, Redo_Exam",
                        "[maiya.name] Affection +3",
                        f"{_sttr} +1"
                        ],
                    "color" : green
                    },
                },
            ("events.rpyc", 3583)  : {
                "Give [maiya.name] a strike" : {
                    "wt" : "",
                    "hint" : [
                        "[maiya.name] Strike +1",
                        "[maiya.name] Affection -1",
                        f"{_sttr} -1"
                        ],
                    "color" : red
                    },
                "Don't give her a strike" : {
                    "wt" : f"{_goch}",
                    "hint" : [
                        "[maiya.name] Affection +1",
                        f"{_sttr} +1"
                        ],
                    "color" : green
                    },
                },
            ("events.rpyc", 3633)  : {
                "No" : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        "[hiroshige.name] Topics | Failed_Proposal",
                        ],
                    "color" : blue
                    },
                "Send her to [hiro]'s group" : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        "[maiya.name] Topics | Hiroshige_Group",
                        "[maiya.name] Affection -1" if "Accepted_Proposal" in hiroshige.topics else "",
                        f"{_boar} +3" if not "Accepted_Proposal" in hiroshige.topics else "",
                        "[main.name] Corruption +1" if not "Accepted_Proposal" in hiroshige.topics else "",
                        ],
                    "color" : blue
                    },
                },
            ("events.rpyc", 3783)  : {
                "Give a 0 to [ay]" : {
                    "wt" : "",
                    "hint" : [
                        "[ayumi.name] Topics | Cheater_Exam",
                        "[ayumi.name] Affection -1",
                        f"{_sttr} -2",
                        f"{_boar} +1"
                        ],
                    "color" : None
                    },
                "Let [ay] redo the exam" : {
                    "wt" : f"{_goch}",
                    "hint" : [
                        "[ayumi.name] Topics | Cheater_Exam, Redo_Exam",
                        "[ayumi.name] Affection +5",
                        f"{_sttr} +2",
                        f"{_boar} -10"
                        ],
                    "color" : green
                    },
                },
            ("events.rpyc", 3852)  : {
                "Give a strike to [ay]" : {
                    "wt" : "",
                    "hint" : [
                        "[ayumi.name] Topics | Striked",
                        "[ayumi.name] Affection -2" if "Redo_Exam" not in ayumi.topics else "",
                        f"{_sttr} -1" if "Redo_Exam" not in ayumi.topics else "",
                        f"{_boar} +1",
                        "[ayumi.name] Strike +1" if not "Redo_Exam" not in ayumi.topics else "",
                        ],
                    "color" : None
                    },
                "Don't strike her" : {
                    "wt" : f"{_goch}",
                    "hint" : [
                        "[ayumi.name] Topics | Cheater_Exam, Redo_Exam",
                        "[ayumi.name] Affection +2",
                        f"{_sttr} +2",
                        f"{_boar} -1"
                        ],
                    "color" : green
                    },
                },
            ("events.rpyc", 4090)  : {
                "Choke her" : {
                    "wt" : f"{_goch}",
                    "hint" : [
                        "[haruka.name] Affection +1",
                        "[haruka.name] Corruption +1",
                        f"{_view} +25",
                        f"{_aplc} +1",
                        "[main.name] Corruption +1"
                        ],
                    "color" : green
                    },
                "Don't" : {
                    "wt" : "",
                    "hint" : [
                        "[haruka.name] Affection +1",
                        f"{_view} +15",
                        f"{_aplc} +1",
                        ],
                    "color" : None
                    },
                },
            ("events.rpyc", 4643)  : {
                "Let [sou] redo the exam" : {
                    "wt" : f"{_goch}",
                    "hint" : [
                        "[soushi.name] Topics | Redo_Exam",
                        "[soushi.name] Strike -1",
                        ],
                    "color" : green
                    },
                "Don't help [sou]" : {
                    "wt" : "",
                    "hint" : [
                        "[soushi.name] Topics | Cheater_Exam",
                        ],
                    "color" : None
                    },
                },
            ("events.rpyc", 4747)  : {
                "Accept [ay]'s \'thanks\'" : {
                    "wt" : f"{_goch}",
                    "hint" : [
                        "[ayumi.name] Affection +2",
                        "[ayumi.name] Corruption +2",
                        f"{_boar} +3",
                        f"{_view} +500",
                        f"{_aplc} +1",
                        f"{_oupr} +1"
                        ],
                    "color" : green
                    },
                "Reject [ay]'s \'thanks\'" : {
                    "wt" : "",
                    "hint" : [
                        "[ayumi.name] Affection +1",
                        f"{_boar} -3",
                        f"{_view} -350",
                        ],
                    "color" : None
                    },
                "Help [sou] in exchange for [ay]\'s \'favor\'" : {
                    "wt" : f"{_bech}",
                    "hint" : [
                        "[soushi.name] Topics | Redo_Exam",
                        "[soushi.name] Strikes -1" if soushi.strikes >= 1 else "",
                        "[ayumi.name] Affection +1",
                        "[ayumi.name] Corruption +3",
                        f"{_boar} +3",
                        f"{_view} +500",
                        f"{_aplc} +1",
                        f"{_oupr} +1"
                        ],
                    "color" : green
                    },
                "Don't help [sou] and turn [ay] down." : {
                    "wt" : "",
                    "hint" : [
                        f"{_boar} -3",
                        f"{_view} -350",
                        "[main.name] Corruption -1",
                        ],
                    "color" : None
                    },
                },
            ("events.rpyc", 5797)  : {
                "Let [ay] redo the exam" : {
                    "wt" : f"{_goch}",
                    "hint" : [
                        "[ayumi.name] Topics | Redo_Exam",
                        "[ayumi.name] Affection +2",
                        "[ayumi.name] Corruption +2",
                        f"{_boar} -11",
                        f"{_sttr} +4"
                        ],
                    "color" : green
                    },
                },
            ("events.rpyc", 8351)  : {
                "Let him speak..." : {
                    "wt" : f"{_goch}",
                    "hint" : [
                        "Can Select Sharing On Next Menu"
                        ],
                    "color" : green
                    },
                "Punch him! {size=-8}(Sharing disabled)" : {
                    "wt" : f"{_bach}",
                    "hint" : [
                        "[emiko.name] Topics | Sharing_No",
                        ],
                    "color" : red
                    },
                },
            ("events.rpyc", 8408)  : {
                "Yes, I'll do it. {size=-8}(Sharing enabled)" : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        "Sharing On",
                        f"{_boar} +5",
                        "[main.name] Corruption +5"
                        ],
                    "color" : blue
                    },
                "Yes, but [em]'s virginity is mine. {size=-8}(Sharing enabled)" : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        "Sharing On",
                        "[main.name] Corruption +5",
                        "[emiko.name] Topics | Sharing_No",
                        ],
                    "color" : blue
                    },
                "No, the girls are mine and I'll decide what to do. {size=-8}(Sharing disabled)" : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        "Sharing Off",
                        "\n".join([girl.name + " Topics | Sharing_No" for girl in academy.targets]),
                        "[emiko.name] Topics | Sharing_No",
                        "[main.name] Corruption -2",
                        ],
                    "color" : blue
                    },
                "Punch him! {size=-8}(Sharing disabled)" : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        "Sharing Off",
                        "[main.name] Corruption -2",
                        f"{_boar} +1",
                        "[president.name] Topics | Punched_MC",
                        "[main.name] Topics | Punch_President",
                        "[kiyomi.name] Topics | President_Punched"
                        ],
                    "color" : blue
                    },
                },
            ("events.rpyc", 9079)  : {
                "Get back into it." : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        "[main.name] Corruption +1",
                        "[ayumi.name] Corruption +2",
                        f"{_view} +25"
                        ],
                    "color" : blue
                    },
                },
            ("events.rpyc", 9698)  : {
                "Take a look at [ha] in the bathroom. {size=-8}Light Urination" : {
                    "wt" : "",
                    "hint" : [
                        "[main.name] Corruption +1"
                        ],
                    "color" : blue
                    },
                },
            ("events.rpyc", 11587) : {
                "Send the Picture to [k]" : {
                    "wt" : f"{_recc}",
                    "hint" : [
                        "[haruka.name] Affection +2",
                        "[haruka.name] Dictionary | Shared_Pic = 1", 
                        f"{_boar} +1",
                        f"{_view} +100", 
                        f"{_oupr} +1",
                        "[main.name] Corruption +1",
                        "[haruka.name] Topics | H_MC",
                        f"{_boun} | Blowjob_Haruka_MC, Blowjob_Student",
                        ],
                    "color" : pink
                    }
                },
            ("events.rpyc", 12317) : {
                "Avoid [sou]" : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        "[ayumi.name] Topics | Avoid_Soushi",
                        "[ayumi.name] No NTR",
                        "[ayumi.name] Affection +1",
                        f"{_sttr} +2",
                        ],
                    "color" : blue
                    },
                "Do what [sou] wants {color=#d8d8d8}{size=-8}(Possible NTR)" : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        "[ayumi.name] Topics | Comply_Soushi",
                        "[ayumi.name] NTR",
                        "[ayumi.name] Corruption +5",
                        f"{_boar} +1",
                        f"{_view} +100",
                        f"{_sttr} +2",
                        "[main.name] Corruption +3",
                        ],
                    "color" : blue
                    },
                "Use your best judgement {color=#d8d8d8}{size=-8}(Possible NTR)" : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        "[ayumi.name] Topics | noInfluence_Soushi",
                        "[ayumi.name] Possible NTR",
                        ],
                    "color" : blue
                    },
                },
            ("events.rpyc", 13476) : {
                "Let it happen" : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        "[ayumi.name] Sexstats | Oral +1",
                        "[ayumi.name] Sexstats | Shared +1",
                        "[ayumi.name] Topics | Shared",
                        ],
                    "color" : blue
                    },
                "Stop it" : {
                    "wt" : f"{_dech}",
                    "hint" : [],
                    "color" : blue
                    },
                "Don't watch {size=-8}(skip)" : {
                    "wt" : f"{_dech}",
                    "hint" : [],
                    "color" : blue
                    },
                },
            ("events.rpyc", 15110) : {
                "Yes" : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        "[ayumi.name] Affection +1",
                        "[ayumi.name] Corruption +1",
                        "[ayumi.name] Topics | Mess", 
                        "[main.name] Corruption +1",
                        ],
                    "color" : pink
                    },
                "No" : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        "[ayumi.name] Affection +3",
                        f"{_boar} -1",
                        "[ayumi.name] Topics | Not_Mess", 
                        ],
                    "color" : pink
                    }
                },
            ("events.rpyc", 16176) : {#TODO
                "Punish her" : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        "[kiyomi.name] ",
                        ],
                    "color" : pink
                    },
                "Let her go" : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        "[kiyomi.name] ",
                        ],
                    "color" : pink
                    }
                },
            ("events.rpyc", 16698) : {#TODO
                "Use the massive dildo" : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        "[kiyomi.name] ",
                        ],
                    "color" : pink
                    },
                "Don't" : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        "[kiyomi.name] ",
                        ],
                    "color" : pink
                    }
                },
            ("events.rpyc", 16885) : {#TODO
                "Fuck her ass" : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        "[kiyomi.name] ",
                        ],
                    "color" : pink
                    },
                "Don't" : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        "[kiyomi.name] ",
                        ],
                    "color" : pink
                    }
                },
            ("events.rpyc", 17267) : {#TODO
                "Piss inside her ass" : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        "[kiyomi.name] ",
                        ],
                    "color" : pink
                    },
                "Nah" : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        "[kiyomi.name] ",
                        ],
                    "color" : pink
                    }
                },
            ("events.rpyc", 18063) : {#TODO
                "Let's do this" : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        
                        ],
                    "color" : pink
                    },
                "Maybe some other time" : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        "{_view} -200",
                        ],
                    "color" : pink
                    }
                },
            ("events.rpyc", 18460) : {#TODO
                "Fuck her ass next" : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        
                        ],
                    "color" : pink
                    },
                "Fuck her pussy next" : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        
                        ],
                    "color" : pink
                    },
                "Cum" : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        
                        ],
                    "color" : pink
                    },
                },
            ("events.rpyc", 18471) : {#TODO
                "Fuck her pussy" : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        
                        ],
                    "color" : pink
                    },
                "Fuck her ass" : {
                    "wt" : f"{_dech}",
                    "hint" : [

                        ],
                    "color" : pink
                    }
                },
            ("events.rpyc", 20657) : {#TODO
                "Remove [ay]'s Strike" : {
                    "wt" : f"{_goch}",
                    "hint" : [
                        "[ayumi.name] Affection +2",
                        "[ayumi.name] Strike -1",
                        
                        ],
                    "color" : green
                    },
                },
            ("events.rpyc", 20302) : {
                "Punish [ay] →" : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        "[ayumi.name] Affection -1", 
                        f"{_view} +50", 
                        "Academic Performance -1"
                        ],
                    "color" : blue
                    },
                "← Punish [ri]" : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        f"{_view} +50", 
                        "Grades +1",
                        "[rina.name] Dictionary | Prostitute = 1"
                        ],
                    "color" : blue
                    },
                "Punish both of them" : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        "[ayumi.name] Affection -1", 
                        f"{_view} +100"
                        ],
                    "color" : blue
                    }
                },
            ("events.rpyc", 20857) : {
                "Blowjob from [ri]" : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        f"{_view} +50", 
                        f"{_aplc} +1",
                        f"{_oupr} +1",
                        "[rina.name] Topics | H_MC, Blowjob_MC",
                        f"{_boun} | Blowjob_Rina_MC, Blowjob_Student_MC",
                        ],
                    "color" : blue
                    },
                "No Blowjob, and Strike [ri]" : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        "[rina.name] Strike +1"
                        f"{_view} -50", 
                        "[main.name] Corruption -1",
                        "[rina.name] Topics | MC_Refused",
                        ],
                    "color" : blue
                    }
                },
            ("events.rpyc", 21297) : {
                "Give them both a strike" : {
                    "wt" : f"{_bach}",
                    "hint" : [
                        "[ayumi.name] Affection -2", 
                        "[ayumi.name] Strike +1", 
                        "[rina.name] Strike +1"
                        ],
                    "color" : red
                    },
                "Let Ayumi decide" : {
                    "wt" : f"{_goch}",
                    "hint" : [
                        "[ayumi.name] Topics | Spanker", 
                        "[rina.name] Topics | Spanked [ayumi.name]",
                        "[ayumi.name] Corruption +1", 
                        f"{_boar} +1",
                        f"{_view} +35",
                        f"{_aplc} +1"
                        ],
                    "color" : green
                    }
                },
            ("events.rpyc", 23450) : {
                "Let's do this." : {
                    "wt" : f"{_goch}",
                    "hint" : [
                        f"{_view} +200",
                        f"{_aplc} +2",
                        f"{_sttr} -2",
                        f"{_oupr} +2",
                        "[yoko.name] Topics | Sex_Vaginal_MC, H_MC, Sex_MC",
                        "[yoko.name] Sexstats | Vaginal +1",
                        f"{_boun} | Sex_Vaginal_Student_MC, Sex_Vaginal_Yoko_MC, Virginity_Student, Virginity_Yoko, Orgasm_Student, Orgasm_Yoko_MC",
                        ],
                    "color" : green
                    },
                "Nah, get the panties and get out." : {
                    "wt" : f"{_bach}",
                    "hint" : [
                        "[main.name] Corruption -1",
                        f"{_view} -200",
                        f"{_aplc} +2",
                        f"{_sttr} -2",
                        f"{_oupr} -1",
                        ],
                    "color" : red
                    }
                },
            ("events.rpyc", 23740) : {
                "Kiss her" : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        "[yoko.name] Topics | Kiss_MC, Love_MC",
                        f"{_boun} | Kiss_Student_MC, Kiss_Yoko_MC",
                        ],
                    "color" : blue
                    },
                "Don't" : {
                    "wt" : f"{_dech}",
                    "hint" : "[yoko.name] Topics | Used",
                    "color" : blue
                    }
                },
            ("events.rpyc", 23960) : {
                "Fuck her ass" : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        "[yoko.name] Topics | Sex_Anal_MC",
                        "[yoko.name] Sexstats | Anal +1",
                        f"{_boun} | Sex_Anal_Student_MC, Sex_Anal_Yoko_MC, Anal_Creampie_Student_MC, Anal_Creampie_Yoko_MC",
                        ],
                    "color" : blue
                    },
                "Keep fucking her pussy" : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        "[yoko.name] Topics | Creampie_Panties_Ev1, Love_MC",
                        "[yoko.name] Sexstats | Creampies +1",
                        f"{_boun} | Creampie_Student_MC, Creampie_Yoko_MC",
                        ],
                    "color" : blue
                    },
                },
            ("events.rpyc", 25119) : {
                "Accept his proposal" : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        "[hiroshige.name] Topics | Accepted_Proposal",
                        f"{_boar} +3",
                        "[main.name] Corruption +1"
                        ],
                    "color" : blue
                    },
                "Refuse it." : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        f"{_boar} -3",
                        ],
                    "color" : blue
                    },
                },
            ("events.rpyc", 25792) : {
                "I like them, they look cute" : {
                    "wt" : f"",
                    "hint" : [
                        "[maiya.name] Affection +2",
                        ],
                    "color" : blue
                    },
                "You look hot" : {
                    "wt" : f"",
                    "hint" : [
                        "[maiya.name] Affection +2", 
                        "[maiya.name] Corruption +1", 
                        ],
                    "color" : blue
                    },
                "I prefer them bigger" : {
                    "wt" : f"",
                    "hint" : [
                        "[maiya.name] Topics | big_boobs_pref",
                        "[main.name] Topics | big_boobs_pref",
                        ],
                    "color" : blue
                    },
                },
            ("events.rpyc", 29499) : {
                "Choke her" : {
                    "wt" : "",
                    "hint" : [
                        "[haruka.name] Topics | Choked",
                        "[haruka.name] Corruption +2",
                        "[main.name] Corruption +1"
                        ],
                    "color" : blue
                    },
                },
            ("events.rpyc", 29616) : {
                "Harder {size=-8}(extreme)" : {
                    "wt" : "",
                    "hint" : [
                        "[haruka.name] Topics | Choked_Harder",
                        "[haruka.name] Corruption +3",
                        "[main.name] Corruption +1"
                        ],
                    "color" : blue
                    },
                },
            ("events.rpyc", 30240) : {
                "Yes" : {
                    "wt" : "",
                    "hint" : [
                        "[haruka.name] Topics | is_GF",
                        "[haruka.name] Affection +20",
                        
                        ],
                    "color" : blue
                    },
                "Yes {size=-4}(lie)" : {
                    "wt" : "",
                    "hint" : [
                        "[haruka.name] Topics | is_GF, is_GF_lie",
                        "[main.name] Topics | Haruka_GF, Haruka_GF_lie",
                        "[haruka.name] Affection +20",
                        "[main.name] Corruption +2",
                        ],
                    "color" : blue
                    },
                "It's too soon" : {
                    "wt" : "",
                    "hint" : [
                        "[haruka.name] Topics | Rejected_GF",
                        "[haruka.name] Affection -5",
                        ],
                    "color" : blue
                    },
                },
            ("events.rpyc", 30481) : {
                "Tell the truth" : {
                    "wt" : "",
                    "hint" : [
                        "[haruka.name] Topics | Ayumi_Handjob_First_H",
                        "[haruka.name] Dictionary | Ayumi_Office_First_H = 1",
                        ],
                    "color" : blue
                    },
                },
            ("events.rpyc", 31544) : {#TODO
                "Let [ay] show them her tits" : {
                    "wt" : f"{_goch}",
                    "hint" : [
                        "[ayumi.name] Topics | thugs_tits",
                        "[ayumi.name] Sexstats | Shared +1",
                        
                        ],
                    "color" : green
                    },
                "Just give them money" : {
                    "wt" : f"{_goch}",
                    "hint" : [
                        "[ayumi.name] Affection +2",
                        "[ayumi.name] Strike -1",
                        
                        ],
                    "color" : green
                    },
                },
            ("events.rpyc", 31674) : {#TODO
                "Let them touch her" : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        "[ayumi.name] ",
                        ],
                    "color" : blue
                    },
                "No" : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        "[ayumi.name] ",
                        ],
                    "color" : blue
                    },
                },
            ("events.rpyc", 32309) : {#TODO
                "Go for it" : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        "[ayumi.name] ",
                        ],
                    "color" : blue
                    },
                "Refuse" : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        "[ayumi.name] ",
                        ],
                    "color" : blue
                    },
                },
            ("events.rpyc", 32885) : {#TODO
                "Tell the truth" : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        "[ayumi.name] ",
                        ],
                    "color" : blue
                    },
                "Lie" : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        "[ayumi.name] ",
                        ],
                    "color" : blue
                    },
                },
            ("events.rpyc", 33767) : {#TODO
                "Your Baseball Bat was confiscated." : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        "[ayumi.name] ",
                        ],
                    "color" : blue
                    },
                "Nevermind" : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        "[ayumi.name] ",
                        ],
                    "color" : blue
                    },
                },
            ("events.rpyc", 35468) : {
                "Finger her" : {
                    "wt" : f"{_dech} ({_recc})",
                    "hint" : [
                        "Event Topics | Finger_H",
                        "[main.name] Topics | H_Suzu",
                        "[suzu.name] Topics | Bat_Event_01_MC, H_MC, Like_MC",
                        f"{_view} +200",
                        f"{_aplc} +2",
                        f"{_sttr} {'+2' if academy.apl >= 50 else '-2' if academy.apl >= 10 else '-4'}",
                        f"{_oupr} +1"
                        ],
                    "color" : blue
                    },
                "Send her to [hidetoshi.surname] {size=-8}(Sharing)" : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        "Event Topics | Kawaguchi_H",
                        "[hidetoshi.surname] Topics | H_Suzu",
                        "[suzu.name] Sexstats | Caressing +1, Shared +1",
                        "[suzu.name] Topics | H_{}, Bat_Event_01_Kawaguchi".format(hidetoshi.name),
                        f"{_view} +200",
                        f"{_aplc} +2",
                        f"{_sttr} {'+2' if academy.apl >= 50 else '-5' if academy.apl >=10 else '-10'}",
                        f"{_oupr} +1"
                        ],
                    "color" : blue
                    },
                "Give the bat back and send her away" : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        "Event Topics | Bat_Back",
                        "[suzu.name] Topics | Bat_Event_01_None",
                        f"{_boar} -1",
                        f"{_view} -100",
                        f"{_sttr} +2"
                        ],
                    "color" : blue
                    }
                },
            ("events.rpyc", 35646) : {
                "Stick a finger in her ass" : {
                    "wt" : f"{_dech}",
                    "hint" : [
                        "Event Topics | Finger Ass",
                        ],
                    "color" : red
                    }
                },
            

            #27084
            #27290
            #27462
            #27507
            #27985
            #28140
            #28271
            #28300
            #29203

            }
        
    valid_dic_items = [#Changes Every Update
        ("events.rpyc", 3152), ("events.rpyc", 23450),
        ("script.rpyc", 8659), 
        ]

    script_ignore_lines = [#Changes Every Update
        52, 56, 95, 108, 1557, 2393, 3267, 3285,
        3306, 3509, 4147, 4176, 4610, 11081
        ]

    event_ignore_lines = [#Changes Every Update
        47, 138, 34070, 34276, 34456, 34665, 34897, 
        35052, 35183, 35212, 36115
        ]

    def check_dic(dic, scripts):

        def find_closest_menu_before_name(lines, name, r_count, out=False):
            closest_menu_line = None
            min_distance = float('inf')
            
            for i, line in enumerate(lines):
                line = line.replace("\\","")
                # Check if the name, including double quotes, is in the line
                if name in line:
                    # Check if this `name` line is after `r_count`
                    if i >= r_count:
                        # Search backwards from the current line to find the nearest `menu`
                        for j in range(i, -1, -1):
                            if 'menu' in lines[j]:
                                # Calculate distance from `r_count` to the found `menu`
                                distance = abs(r_count - j)
                                if distance < min_distance:
                                    if out:
                                        print(f"Found {name} in {line.strip()} at {i+1}")
                                    min_distance = distance
                                    closest_menu_line = j + 1  # Convert to 1-indexed
                                break  # Stop searching backwards once we find the closest menu
            return closest_menu_line

        def find_menu_before_name(lines, name, out=False):
            for i, line in enumerate(lines):
                if name in line:
                    # Search backwards from the current line
                    for j in range(i, -1, -1):
                        if 'menu' in lines[j]:
                            if out:
                                print(f"Found {name} in {line.strip()} at {i+1}")
                            # Return the line number (1-indexed)
                            return j + 1
            return None

        def output(line):
            p = os.path.join(config.basedir, "walkthrough_check.txt")
            with open(p, 'a') as file:
                print(line)
                file.write("{}\n".format(line))

        counter = 0
        lst = {}
        
        # Populate the lst dictionary with the script information
        for v, n, file in scripts:
            lst[v] = [n, update_wt(file), file]

        # Iterate over the lst dictionary and the dic dictionary
        for key, value in lst.items():
            for wt_key, wt_value in dic.items():
                r_count = wt_key[1]
                # Check if the name in value[0] is part of the current wt_key[0]
                if value[0] in wt_key[0]:
                    for name in wt_value:
                        # Find the closest menu line number
                        ln = find_closest_menu_before_name(value[1], f'"{name}"', r_count) #Precise Search
                        al = find_menu_before_name(value[1], f'"{name}"') #Fuzzy Search
                        # Create the tuple with the filename and the line number
                        d = ("{}c".format(value[2]), ln)
                        e = ("{}c".format(value[2]), al)
                        # Print the result with the correct key and value
                        if wt_key != d and not wt_key in valid_dic_items:
                            counter += 1
                            output("Current: {}\nNew: {}\nLine: {}\nCould Be Mistaken For a Sub Menu\n".format(wt_key, d, name))
        return counter

    def filter_wt(fil):
        out = []
        for script, i in walkthrough_dict().keys():
            if fil in script:
                out.append(i)
        return out

    class WTDict():
        dic = {}
        def __init__(self, fileline, menu_choice, **kwargs):
            print(type(fileline))
            self.dic[fileline] = {}
            self.dic[fileline][menu_choice] = {}
            
            for k,v in kwargs.items():
                self.dic[fileline][menu_choice][k] = v
                setattr(self, k, v)
            print(self.__dict__)

            print(self.dic)

    #WTDict(("events.rpyc", 28734), "Stick a finger in her ass", wt="Good Choice", hint=["[ayumi.name] Affection +1"], color="#F00")

    def get_menu_lines(filename, ignore_lines):
        
        output_data = []
        data = update_wt(filename)
        p = os.path.join(config.basedir, "menu_finder.txt")

        for i, line in enumerate(data, 1):
            if "menu:" in line and not i in ignore_lines:
                output_data.append((filename, i))

        if output_data:
            with open(p, "a") as file:
                for c, i in enumerate(output_data, 1):
                    file.write(f"{c} {str(i)}\n")
                file.write("\n")

    def update_check_walkthrough():
        get_menu_lines("script.rpy", filter_wt("script")+script_ignore_lines)
        get_menu_lines("events.rpy", filter_wt("events")+event_ignore_lines)
        check_dic(walkthrough_dict(),[("sc", "script", "script.rpy"), ("ev", "events", "events.rpy")])