import lyricwikia

# this is extremely specific, and wont work if there is a typo in the song or author. 
def get_lyrics(author, song):
    lyrics = lyricwikia.get_lyrics(author, song)
    return lyrics
