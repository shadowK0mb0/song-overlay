from typing import Optional

import httpx
from datetime import datetime, timedelta
from song_overlay.models.auth import (
    RequestAuthCode,
    RequestAccessToken,
    AuthCodeResponse,
    AccessTokenResponse,
)
from song_overlay.models.player import CurrentlyPlaying, Item, Artist, Image, Album
from song_overlay.utils import generate_random_string, sha256, base64encode

AUTH_CODE_URL = "https://accounts.spotify.com/authorize"
ACCESS_TOKEN_URL = "https://accounts.spotify.com/api/token"

class SpotifyClient:
    def __init__(self, client_id: str, client_secret: str, redirect_uri: str, state: str):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.state = state
        self.client = httpx.Client()
    
    def request_auth_code_url(self, scope: str) -> tuple[str, str]:
        code_verifier = generate_random_string(64)
        hashed = sha256(code_verifier)
        code_challenge = base64encode(hashed)
        auth_code = RequestAuthCode(
            response_type="code",
            client_id=self.client_id,
            redirect_uri=self.redirect_uri,
            scope=scope,
            state=self.state,
            code_challenge=code_challenge,
            code_challenge_method="S256",
        )
        auth_code_url = httpx.URL(AUTH_CODE_URL, params=auth_code.model_dump(exclude_none=True))
        return auth_code_url, code_verifier
    
    def request_access_token(self, code: str, code_verifier: str) -> AccessTokenResponse:
        access_token = RequestAccessToken(
            grant_type="authorization_code",
            code=code,
            code_verifier=code_verifier,
            redirect_uri=self.redirect_uri,
            client_id=self.client_id,
            client_secret=self.client_secret,
        )
        # perform logic of request_access_token function
        response = self.client.post(
            ACCESS_TOKEN_URL, data=access_token.model_dump(exclude_none=True)
        )
        response.raise_for_status()
        response_json = response.json()
        return AccessTokenResponse(
            **response_json,
            _expire_time=datetime.now() + timedelta(seconds=response_json["expires_in"])
        )
    
    def get_current_playing_song(self, access_token: AccessTokenResponse) -> Optional[CurrentlyPlaying]:
        headers = {"Authorization": f"Bearer {access_token.access_token}"}
        response = self.client.get(
            "https://api.spotify.com/v1/me/player/currently-playing",
            headers=headers,
        )
        response.raise_for_status()
        if response.status_code == 204:
            return None
        return CurrentlyPlaying.model_validate(response.json())

