from trendyApp import app
from flask import render_template,request
from trendyApp.services.steam_api import get_top_appids,get_app_detail,get_genre_top_appids

# 
limit = 10

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/ranking')
def ranking():
    
    appids = get_top_appids(limit)

    games = [get_app_detail(appid) for appid in appids]

    return render_template("ranking.html",games=games)

@app.route('/select_genre', methods=['POST'])
def select_genre():
    genre = request.form['genre']  # HTMLのname="genre" で渡された値を取得
    appids = get_genre_top_appids(limit,genre)

    games = [get_app_detail(appid) for appid in appids]
    
    return render_template("ranking.html",games=games)