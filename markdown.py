import consts
import utils

import logging
import shutil
import os

def playlist(playlist):
    path = os.path.join(consts.REPO_PATH, consts.PLAYLIST_FOLDER)
    utils.check_dir(path)
    path = os.path.join(path, playlist['id'] + '.md')
    description = "_" + playlist['description'] + "_\n\n" if playlist['description'] else ""
    marky = [
        "# [" + playlist['name'] + "](" + playlist['url'] +")\n\n",
        "![Cover](../" + consts.DATA_FOLDER + "/" + playlist['id'] + "/cover.jpg)\n\n",
        description,
        str(playlist['length']) + " songs - " + str(int(playlist['duration'] / 60000)) + " minutes\n\n",
        "[M3U](../"+ consts.DATA_FOLDER + "/" + playlist['id'] + "/playlist.m3u)\n\n",
        "## Songs",
    ]
    for i, song in enumerate(playlist['songs']):
        marky.append("\n" + str(i + 1) + ". [" + song['name'] + "](" + song['url'] + ") - " + utils.arist_list(song['artists']))
    with open(path, 'w', newline='') as md:
        logging.info('Generating playlist md at ' + path)
        md.writelines(marky)
            # "id: " + playlist['id'] + "\n",
            # "name: " + playlist['name'] + "\n",
            # "cover: " + playlist['cover'] + "\n",
            # "length: " + str(playlist['length']) + "\n",
            # "duration: " + str(int(playlist['duration'] / 60000)) + " minutes\n",
            # "owner: " + playlist['owner']['username'] + "\n",
            # "owner_id: " + playlist['owner']['id'] + "\n",
            # "last_modified: " + playlist['last_modified'] + "\n",
            # "last_modified: " + playlist['last_modified'] + "\n",
            # "collaborative: " + str(playlist['collaborative']) + "\n",
            # "public: " + str(playlist['public']) + "\n",
            # "---\n",

def index(playlists, months):
    path = os.path.join(consts.REPO_PATH, consts.BASE_MD)
    marky = [ "## " + consts.INDEX_HEADER  + ":" ]
    for playlist in playlists:
        marky.append("\n- [" + playlist['name'] + "](./" + consts.PLAYLIST_FOLDER + "/" + playlist['id'] + ".md)")

    if months:
        marky.append("\n\n## monthly playlists:")
    for month in months:
        marky.append("\n- [" + month['name'] + "](./" + consts.PLAYLIST_FOLDER + "/" + month['id'] + ".md)")
    with open(path, 'w', newline='') as md:
        logging.info('Generating index at ' + path)
        md.writelines(marky)

def clear():
    path = os.path.join(consts.REPO_PATH, consts.PLAYLIST_FOLDER)
    if os.path.exists(path):
        logging.info('Removing playlist path')
        shutil.rmtree(path)
    utils.check_dir(path)
