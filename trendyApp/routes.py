from trendyApp import app
from flask import render_template
from trendyApp.services.steam_api import get_top_appids,get_app_detail

@app.route('/')
def ranking():
    limit = 10

    appids = get_top_appids(limit)

    games = [get_app_detail(appid) for appid in appids]

    return render_template("ranking.html",games=games)

