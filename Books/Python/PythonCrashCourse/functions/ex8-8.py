def make_album(artist, title, n_songs = None):

    if n_songs:
        album ={
            'Artist': artist,
            'Title': title,
            'No.Songs': 'No songs'
        }
    else: 
        album ={
            'Artist': artist,
            'Title': title,
            'No.Songs': n_songs
        }

    for v,k in album.items():
        print(f'{v}: {k}')



while True:
    artist = input('Enter an artist:')
    title = input('Enter te title of the album:')
    n_songs = input('Enter de number of the songs:')
    make_album(artist,title, n_songs)
    