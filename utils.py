import consts

import os
import logging

def check_dir(path):
    if not os.path.exists(path):
        logging.info('Creating directory ' + path)
        os.makedirs(path)

def iso_to_year(iso):
    return int(iso.split('-')[0])

def get_duration(songs):
    return sum(song['duration_ms'] for song in songs)

def latest_change(songs):
    if len(songs) == 0:
        return None
    return max(song['date_added'] for song in songs)

def arist_list(arists):
    return ", ".join(artist['name'] for artist in arists)

def monYR_conv(name):
    year = "20" + name[-2:]
    try:
        int(year)
    except:
        return None

    month = name[:-2]

    month_num = consts.MONTH_MAP.get(month.lower(), None)
    if month_num == None:
        return None

    return year + "-" + str(month_num)

def monthly_playlists(playlists):
    playlists = [(monYR_conv(playlist['name']), playlist) for playlist in playlists]
    # months = filter(lambda x: x[0] != None, months)
    months = []
    non_months = []
    for playlist in playlists:
        if playlist[0] == None:
            non_months.append(playlist[1])
        else:
            months.append(playlist[1])
    return months, non_months