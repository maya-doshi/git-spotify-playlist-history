# git-spotify-playlist-history
track spotify playlists with git.

Run with a cron job to keep in sync.

[Here's mine](https://codeberg.org/maya-doshi/public-spotify-playlists)

## Usage:
1. Install all dependencies from `requirements.txt`
2. Create and clone a blank repo from a remote
3. Edit the variables in `consts.py`
4. Get Spotify API keys from [here](https://developer.spotify.com/dashboard) and add to environment
5. Run script on loop somehow

### Environment Variables
- `SPOTIPY_CLIENT_ID`
- `SPOTIPY_CLIENT_SECRET`

### Modification
Editing the monthly playlist detection should be trivial just replace
`monthly_playlists` in [utils](utils.py)
