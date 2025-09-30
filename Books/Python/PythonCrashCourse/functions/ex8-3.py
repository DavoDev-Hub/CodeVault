print('Arguments')
def make_shirt(size, text):
    print('Size: ', size)
    print(f'Text: "{text}"')

make_shirt('M', 'Davodev')

print('\nKeyword arguments')
def make_shirt(size, text):
    print('Size: ', size)
    print(f'Text: "{text}"')

make_shirt(size = 'G', text = 'Fabr0x')
