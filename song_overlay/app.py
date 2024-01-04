import os
from datetime import datetime

import httpx
from flask import Flask, redirect, request, session, render_template

from song_overlay.clients.spotify_client import SpotifyClient
from song_overlay.in_memory_cache import InMemoryCache
from song_overlay.models.auth import (
    AccessTokenResponse,
    AuthCodeResponse,
    RequestAccessToken,
    RequestAuthCode,
)

app = Flask(__name__)

cache = InMemoryCache()

client = SpotifyClient(
    client_id=os.environ["CLIENT_ID"],
    client_secret=os.environ["CLIENT_SECRET"],
    redirect_uri=os.environ.get("REDIRECT_URI", "http://localhost:5000/callback"),
    state=os.environ.get("STATE", "A random string"),
)


@app.route("/")
def current_playing_song():
    if cache.get("access_token") is None:
        return login()
    elif cache.get("access_token")._expire_time < datetime.now():
        refresh_token()
    return redirect("/current_playing_song")


def login():
    auth_code_url, code_verifier = client.request_auth_code_url(
        scope="user-read-currently-playing"
    )
    cache.set("code_verifier", code_verifier)
    return redirect(auth_code_url)


@app.route("/callback")
def callback():
    code = request.args.get("code", None)
    if not code:
        error = request.args.get("error", None)
        return error
    state = request.args.get("state", None)
    if not state:
        error = request.args.get("error", None)
        return error if error else "State is missing"
    if state != os.environ.get("STATE", "A random string"):
        return "State is invalid"
    code_verifier = cache.get("code_verifier")
    access_token: AccessTokenResponse = client.request_access_token(code, code_verifier)
    cache.set("access_token", access_token)
    return redirect("/current_playing_song")


def refresh_token():
    pass


@app.route("/current_playing_song")
def get_current_playing_song():
    access_token = cache.get("access_token")
    if not access_token:
        return login()
    return client.get_current_playing_song(access_token).model_dump()

@app.route("/current_playing")
def get_current_playing():
    access_token = cache.get("access_token")
    if not access_token:
        return login()
    curr_song = client.get_current_playing_song(access_token)
    if not curr_song:
        return render_template("current-playing.html", song_playing=False)
    return render_template("current-playing.html", song_playing=True, title=curr_song.item.name, artist=", ".join(artist.name for artist in curr_song.item.artists), image=curr_song.item.album.images[0].url)


