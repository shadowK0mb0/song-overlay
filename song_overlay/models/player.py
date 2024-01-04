from typing import List, Dict, Optional
from pydantic import BaseModel

class Device(BaseModel):
    id: Optional[str] = None
    is_active: Optional[bool] = False
    is_private_session: Optional[bool] = False
    is_restricted: Optional[bool] = False
    name: Optional[str] = "Unknown Device"
    type: Optional[str] = "Unknown Type"
    volume_percent: Optional[int] = 0
    supports_volume: Optional[bool] = False

class ExternalUrls(BaseModel):
    spotify: Optional[str] = None

class Image(BaseModel):
    height: Optional[int] = 0
    url: Optional[str] = None
    width: Optional[int] = 0

class Followers(BaseModel):
    href: Optional[str] = None
    total: Optional[int] = 0

class Artist(BaseModel):
    external_urls: Optional[ExternalUrls] = ExternalUrls()
    followers: Optional[Followers] = Followers()
    genres: Optional[List[str]] = []
    href: Optional[str] = None
    id: Optional[str] = None
    images: Optional[List[Image]] = []
    name: Optional[str] = "Unknown Artist"
    popularity: Optional[int] = 0
    type: Optional[str] = "Unknown Type"
    uri: Optional[str] = None

class Album(BaseModel):
    album_type: Optional[str] = "Unknown Type"
    total_tracks: Optional[int] = 0
    available_markets: Optional[List[str]] = []
    external_urls: Optional[ExternalUrls] = ExternalUrls()
    href: Optional[str] = None
    id: Optional[str] = None
    images: Optional[List[Image]] = []
    name: Optional[str] = "Unknown Album"
    release_date: Optional[str] = "Unknown Date"
    release_date_precision: Optional[str] = "Unknown Precision"
    restrictions: Optional[Dict[str, str]] = {}
    type: Optional[str] = "Unknown Type"
    uri: Optional[str] = None
    artists: Optional[List[Artist]] = []

class ExternalIds(BaseModel):
    isrc: Optional[str] = None
    ean: Optional[str] = None
    upc: Optional[str] = None

class Item(BaseModel):
    album: Optional[Album] = Album()
    artists: Optional[List[Artist]] = []
    available_markets: Optional[List[str]] = []
    disc_number: Optional[int] = 0
    duration_ms: Optional[int] = 0
    explicit: Optional[bool] = False
    external_ids: Optional[ExternalIds] = ExternalIds()
    external_urls: Optional[ExternalUrls] = ExternalUrls()
    href: Optional[str] = None
    id: Optional[str] = None
    is_playable: Optional[bool] = False
    linked_from: Optional[Dict[str, str]] = {}
    restrictions: Optional[Dict[str, str]] = {}
    name: Optional[str] = "Unknown Track"
    popularity: Optional[int] = 0
    preview_url: Optional[str] = None
    track_number: Optional[int] = 0
    type: Optional[str] = "Unknown Type"
    uri: Optional[str] = None
    is_local: Optional[bool] = False

class Context(BaseModel):
    type: Optional[str] = "Unknown Type"
    href: Optional[str] = None
    external_urls: Optional[ExternalUrls] = ExternalUrls()
    uri: Optional[str] = None

class Actions(BaseModel):
    interrupting_playback: Optional[bool] = False
    pausing: Optional[bool] = False
    resuming: Optional[bool] = False
    seeking: Optional[bool] = False
    skipping_next: Optional[bool] = False
    skipping_prev: Optional[bool] = False
    toggling_repeat_context: Optional[bool] = False
    toggling_shuffle: Optional[bool] = False
    toggling_repeat_track: Optional[bool] = False
    transferring_playback: Optional[bool] = False

class CurrentlyPlaying(BaseModel):
    device: Optional[Device] = Device()
    repeat_state: Optional[str] = "off"
    shuffle_state: Optional[bool] = False
    context: Optional[Context] = Context()
    timestamp: Optional[int] = 0
    progress_ms: Optional[int] = 0
    is_playing: Optional[bool] = False
    item: Optional[Item] = Item()
    currently_playing_type: Optional[str] = "track"
    actions: Optional[Actions] = Actions()
