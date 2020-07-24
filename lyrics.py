import lyricwikia


def get_lyrics(author, song):
    lyrics = lyricwikia.get_lyrics(author, song)
    return lyrics
