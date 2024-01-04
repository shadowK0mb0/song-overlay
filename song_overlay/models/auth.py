from typing import Optional, Literal, LiteralString
from datetime import datetime
from pydantic import BaseModel


class RequestAuthCode(BaseModel):
    response_type: Literal["code"]
    client_id: str
    redirect_uri: str
    scope: str
    state: Optional[str]
    code_challenge: str
    code_challenge_method: Literal["S256"]


class AuthCodeResponse(BaseModel):
    code: str
    state: Optional[str]


class RequestAccessToken(BaseModel):
    code: str
    redirect_uri: str
    grant_type: Literal["authorization_code"]
    client_id: str
    code_verifier: str


class AccessTokenResponse(BaseModel):
    access_token: str
    token_type: Literal["Bearer"]
    expires_in: int
    refresh_token: str
    scope: str
    _expire_time: datetime
