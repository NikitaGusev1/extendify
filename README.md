````markdown
# Spotify Quick Add to Playlist

A simple macOS script to add the currently playing Spotify track to a chosen playlist with one button press — no need to like songs temporarily.

## Features

- Adds the currently playing track directly to your specified Spotify playlist
- macOS Quick Action integration for easy keyboard shortcut usage
- macOS notifications for success or error feedback
- Uses Spotipy Python library and Spotify Web API
- Configurable via environment variables (secure handling of credentials)

## Setup

1. Clone this repo:
   ```bash
   git clone https://github.com/yourusername/yourrepo.git
   cd yourrepo
````

2. Create and activate a Python virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your Spotify credentials and playlist info:

   ```env
   SPOTIPY_CLIENT_ID=your_spotify_client_id
   SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
   SPOTIPY_REDIRECT_URI=http://127.0.0.1:8888/callback
   PLAYLIST_ID=your_spotify_playlist_id
   PLAYLIST_NAME=Your Playlist Name
   ```

5. Set up the macOS Quick Action to run the `extendify.sh` script (or your preferred shell script).

6. Use your assigned keyboard shortcut to add the current track to your playlist.

## Notes

* Make sure your Spotify app is running and playing a track when you use the action.
* You might need to authorize the app the first time it runs.

## License

MIT License © Nikita Gusev

---
