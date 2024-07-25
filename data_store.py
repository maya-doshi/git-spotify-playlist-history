import utils

import consts
import shutil
import json
from urllib import request
import logging
import os

data_store  = os.path.join(consts.REPO_PATH, consts.DATA_PATH)

def playlist_data_dir(playlist_id):
    utils.check_dir(data_store)
    res = os.path.join(data_store, playlist_id)
    utils.check_dir(res)
    return res

def playlist_art_download(path, cover):
    if cover == "":
        return
    request.urlretrieve(cover, os.path.join(path, 'cover.jpg'))
    logging.info('Downloaded from ' + cover + ' cover')
    return

def m3u_gen(path, playlist):
    with open(os.path.join(path, 'playlist.m3u'), 'w', newline='') as m3u:
        m3u.writelines([
            "#EXTM3U\n",
            "#PLAYLIST:" + playlist['name'],
        ])
        for song in playlist['songs']:
            m3u.writelines([
                "\n#EXTINF:" + str(int(song['duration_ms'] / 1000)) + "," + song['artists'][0]['name'] + " - " + song['name'] + "\n",
                "#EXTALB:" + song['album']['name'] + " (" + str(song['album']['year']) + ")" + "\n",
                song['url']
            ])
    logging.info('Generated ' + playlist['name'] + ' m3u')

def playlist(id, playlist_data, cover_url):
    playlist_dir = playlist_data_dir(id)
    with open(os.path.join(playlist_dir, 'metadata.json'), 'w') as metadata:
        logging.info('Saving ' + playlist_data['name'] + ' data')
        json.dump(playlist_data, metadata, indent=2)
    m3u_gen(playlist_dir, playlist_data)
    playlist_art_download(playlist_dir, cover_url)

def clear():
    if os.path.exists(data_store):
        logging.info('Removing directory ' + data_store)
        shutil.rmtree(data_store)
    utils.check_dir(data_store)
