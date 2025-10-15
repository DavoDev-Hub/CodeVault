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

make_album('Arctic Monkeys', 'AM' )