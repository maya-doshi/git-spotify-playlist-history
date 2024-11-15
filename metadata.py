import utils


def get_image_url(images):
    if images == None:
        return ""
    return images[0]["url"]


def get_user(user):
    return {
        "username": user["display_name"],
        "id": user["id"],
    }


def get_artist(artist):
    return {
        "name": artist["name"],
        "id": artist["id"],
        "url": artist["external_urls"]["spotify"],
    }


def get_artists(artists):
    res = []
    for artist in artists:
        res.append(get_artist(artist))
    return res


def get_album(album):
    return {
        "id": album["id"],
        "name": album["name"],
        "artists": get_artists(album["artists"]),
        "year": utils.iso_to_year(album["release_date"]),
        "track_count": album["total_tracks"],
        "url": album["external_urls"]["spotify"],
    }


def get_song(song):
    track = song["track"]
    return {
        "date_added": song["added_at"],
        "added_by": {
            #'name': song['added_by']['display_name'],
            "id": song["added_by"]["id"],
        },
        "name": track["name"],
        "id": track["id"],
        "url": track["external_urls"]["spotify"],
        "disc_number": track["disc_number"],
        "track_number": track["track_number"],
        "artists": get_artists(track["artists"]),
        "duration_ms": track["duration_ms"],
        "isrc": track["external_ids"]["isrc"],
        "album": get_album(track["album"]),
    }


def get_songs(songs, sp):
    songs_out = []

    tracks = songs["items"]
    while songs["next"]:
        songs = sp.next(songs)
        tracks.extend(songs["items"])

    for song in tracks:
        songs_out.append(get_song(song))
    return songs_out


def get_playlist(playlist, songs, sp):
    songs = get_songs(songs, sp)
    return {
        "id": playlist["id"],
        "url": playlist["external_urls"]["spotify"],
        "name": playlist["name"],
        "description": playlist["description"],
        "length": playlist["tracks"]["total"],
        "duration": utils.get_duration(songs),
        "last_modified": utils.latest_change(songs),
        "owner": get_user(playlist["owner"]),
        "collaborative": playlist["collaborative"],
        "public": playlist["public"],
        "songs": songs,
    }
