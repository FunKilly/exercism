def recite(start_verse, end_verse):
    with open('twelve-days','r+') as file:
        lyrics = file.read()
        lyrics = lyrics.split('\n\n')
    return lyrics[start_verse-1:end_verse]
    pass


