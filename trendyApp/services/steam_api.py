import requests

STEAM_DETAILS_URL = "https://store.steampowered.com/api/appdetails"
STEAM_RANKING_URL = "https://api.steampowered.com/ISteamChartsService/GetMostPlayedGames/v1/"
STEAM_CURRENT_PLAYERS_URL = "https://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/"

def get_top_appids(limit):

    response = requests.get(STEAM_RANKING_URL)
    data = response.json()
    games = data["response"]["ranks"][:limit]

    return [game["appid"] for game in games]


def get_app_detail(appid):

    params = {"appids":appid,"l":"japanese","cc":"jp"}
    response_detail = requests.get(STEAM_DETAILS_URL, params=params)
    data = response_detail.json()

    data_details = data[str(appid)]["data"]

    response_ranks = requests.get(STEAM_RANKING_URL).json()
    ranks =  response_ranks["response"]["ranks"]

    peak_in_game = 0

    for rank in ranks:
        if rank["appid"] == appid:
            peak_in_game = rank["peak_in_game"]
            break

    response_current_players = requests.get(STEAM_CURRENT_PLAYERS_URL, params={"appid": appid}).json()
    current_players =  response_current_players["response"]["player_count"]

    return {
        "appids": appid,
        "title": data_details["name"],
        "players": peak_in_game,
        "image": data_details["header_image"],
        "description": data_details["short_description"],
        "current_players": current_players
    }


