def make_album(artist, title):
    album ={
        'Artist': artist,
        'Title': title
    }
    for v,k in album.items():
        print(f'{v}: {k}')

make_album('Arctic Monkeys', 'AM')