ADMIN_NAVIGATION_GRAPH = {
    "AdminInitial": [
        "AdminGames",
        "AdminGamers",
        "Profile",
    ],
    "AdminGames": [
        "AddGame",
        "EditGame",
        "DeleteGame",
        "AdminInitial"
    ],
    "AddGame": [
        "AdminGames"
    ],
    "EditGame": [
        "AdminGames"
    ],
    "DeleteGame": [
        "AdminGames"
    ],
    "AdminGamers": [
        "AddGamer",
        "BanUser",
        "AdminInitial"
    ],
    "AddGamer": [
        "AdminGamers"
    ],
    "BanUser": [
        "AdminGamers"
    ],
    "Profile": [
        "AdminInitial"
    ]
}
