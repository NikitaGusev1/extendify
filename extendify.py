import sys
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Load environment variables from a .env file
load_dotenv()

# Load config from environment
SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = os.getenv('SPOTIPY_REDIRECT_URI')
PLAYLIST_ID = os.getenv('PLAYLIST_ID')  # Format: spotify:playlist:xxxxxxxx
PLAYLIST_NAME = os.getenv('PLAYLIST_NAME')  # Just for display

# Scopes
scope = "user-read-playback-state user-read-currently-playing playlist-modify-public playlist-modify-private"

try:
    # Authenticate with Spotify
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI,
        scope=scope,
        cache_path='.cache',
        open_browser=False
    ))

    # Get current playback
    current = sp.current_playback()

    if current and current.get('is_playing') and current.get('item'):
        track = current['item']
        track_uri = track['uri']
        track_name = track['name']
        artist_name = track['artists'][0]['name']

        # Add to playlist
        sp.playlist_add_items(playlist_id=PLAYLIST_ID, items=[track_uri])

        print(f"✅ Added: '{track_name}' by {artist_name} to '{PLAYLIST_NAME}'")
    else:
        print("❌ No track is currently playing.")
        sys.exit(1)

except Exception as e:
    print(f"❌ Error: {str(e)}")
    sys.exit(1)
