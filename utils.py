import consts

import os
import logging


def check_dir(path):
    if not os.path.exists(path):
        logging.info("Creating directory " + path)
        os.makedirs(path)


def iso_to_year(iso):
    return int(iso.split("-")[0])


def get_duration(songs):
    return sum(song["duration_ms"] for song in songs)


def latest_change(songs):
    if len(songs) == 0:
        return None
    return max(song["date_added"] for song in songs)


def arist_list(arists):
    return ", ".join(artist["name"] for artist in arists)


def monYR(playlist):
    name = playlist["name"]
    year = "20" + name[-2:]
    try:
        int(year)
    except:
        return (None, playlist)

    month = name[:-2]

    month_num = consts.MONTH_MAP.get(month.lower(), None)
    if month_num == None:
        return (None, playlist)

    return (year + "-" + f"{month_num:02}", playlist)


def monthly_playlists(playlists):
    playlists = list(map(monYR, playlists))

    months = list(
        map(
            lambda x: x[1],
            sorted(
                map(
                    lambda x: (int(x[0].replace('-', '')), x[1]),
                    filter(lambda x: x[0] != None, playlists),
                ),
                key=lambda x: x[0],
                reverse=True,
            ),
        )
    )

    playlists = list(map(lambda x: x[1], filter(lambda x: x[0] == None, playlists)))

    return months, playlists
