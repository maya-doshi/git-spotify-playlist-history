import utils
import markdown
import data_store
import metadata
import version
import consts

import logging
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

version.check_repo()

data_store.clear()
markdown.clear()

playlists = sp.user_playlists(consts.SPOTIFY_USER)
playlist_datas = []

while playlists:
    for playlist in playlists['items']:
        id = playlist['id']
        url = metadata.get_image_url(playlist['images'])
        playlist_data = metadata.get_playlist(playlist, sp.playlist_items(id), sp)
        data_store.playlist(id, playlist_data, url)
        markdown.playlist(playlist_data)
        playlist_datas.append(playlist_data)
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None

# version.commit_data()
months, playlist_datas = utils.monthly_playlists(playlist_datas)

markdown.index(playlist_datas, months)

if version.stage_all():
    version.commit()
    version.push()
else:
    logging.info('No changes')
