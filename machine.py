from fsm import TocMachine


def create_machine():
    machine = TocMachine(
        states=["user", "menu", "showFSM",
            "voteStats", "voteStatsRegion",
            "visualData", "visualDataRegion",
            "multiAnalysis", "selectItem",
            "funcIntro", 
            ],
        transitions=[
            {
                "trigger": "advance",
                "source": "user",
                "dest": "menu",
                "conditions": "is_going_to_menu",
            },
            {
                "trigger": "advance",
                "source": ["user", "menu"],
                "dest": "showFSM",
                "conditions": "is_going_to_showFSM",
            },
            {
                "trigger": "advance",
                "source": "menu",
                "dest": "voteStats",
                "conditions": "is_going_to_voteStats",
            },
            {
                "trigger": "advance",
                "source": "voteStats",
                "dest": "voteStatsRegion",
                "conditions": "is_going_to_voteStatsRegion",
            },
            {
                "trigger": "advance",
                "source": "voteStatsRegion",
                "dest": "voteStatsRegion",
                "conditions": "is_going_to_voteStatsRegion",
            },
            {
                "trigger": "advance",
                "source": "menu",
                "dest": "visualData",
                "conditions": "is_going_to_visualData",
            },
            {
                "trigger": "advance",
                "source": "visualData",
                "dest": "visualDataRegion",
                "conditions": "is_going_to_visualDataRegion",
            },
            {
                "trigger": "advance",
                "source": "visualDataRegion",
                "dest": "visualDataRegion",
                "conditions": "is_going_to_visualDataRegion",
            },
            {
                "trigger": "advance",
                "source": "menu",
                "dest": "multiAnalysis",
                "conditions": "is_going_to_multiAnalysis",
            },
            {
                "trigger": "advance",
                "source": "multiAnalysis",
                "dest": "selectItem",
                "conditions": "is_going_to_selectItem",
            },
            {
                "trigger": "advance",
                "source": "selectItem",
                "dest": "selectItem",
                "conditions": "is_going_to_selectItem",
            },
            {
                "trigger": "advance",
                "source": "selectItem",
                "dest": "selectNum",
                "conditions": "is_going_to_selectNum",
            },
            {
                "trigger": "advance",
                "source": "selectNum",
                "dest": "selectNum",
                "conditions": "is_going_to_selectNum",
            },
            {
                "trigger": "advance",
                "source": "menu",
                "dest": "funcIntro",
                "conditions": "is_going_to_funcIntro",
            },
            {
                "trigger": "advance",
                "source": ["voteStats", "visualData", "multiAnalysis",
                    "voteStatsRegion", "visualDataRegion", "selectItem", "selectNum", "funcIntro"],
                "dest": "menu",
                "conditions": "is_go_back_to_menu",
            },
            {"trigger": "go_back", "source": ["menu", "showFSM"], "dest": "user"},
            #{"trigger": "go_back", "source": "voteStatsRegion", "dest": "voteStats"},
            #{"trigger": "go_back", "source": "visualDataRegion", "dest": "visualData"},
            #{"trigger": "go_back", "source": "selectItem", "dest": "multiAnalysis"},

        ],
        initial="user",
        auto_transitions=False,
        show_conditions=True,
    )

    return machine