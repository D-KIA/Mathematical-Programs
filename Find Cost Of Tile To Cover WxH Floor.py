# Find Cost of Tile to Cover W x H Floor

'''
Calculate the total cost of tile it would take to cover a floor plan of width and height, using a cost entered by the user.
The seven most common standard tile sizes are : 300*300 mm(0.3*o.3 m), 300*600 mm, 600*600 mm, 610*610 mm, 800*800 mm, 250*350 mm and 350*450 mm.
'''

tiles = {'T1': 0.09, 'T2': 0.18, 'T3': 0.36, 'T4': 0.3721, 'T5': 0.64, 'T6': 0.0875, 'T7': 0.1575}
def TileCount(w, h, tile):
    required_area = w * h
    if tile not in tiles:
        number_of_tiles = round(required_area / tile)
    else:
        number_of_tiles = round(required_area/tiles[tile])
    return number_of_tiles

print('''
    Standard Tile Sizes In Market :-
     T1 : 300*300 mm
     T2 : 300*600 mm
     T3 : 600*600 mm
     T4 : 610*610 mm
     T5 : 800*800 mm
     T6 : 250*350 mm
     T7 : 350*450 mm
     T8 : Custom
     ''')

while True:
    tile_size = input('Pick a Tile Size : ').upper()
    if tile_size in tiles or  tile_size == 'T8':
        break

if tile_size == 'T8':
    while True:
        try:
            t_h = abs(int(input('Enter Tile Height(mm) : ')))
            t_w = abs(int(input('Enter Tile Width(mm) : ')))
            break
        except:
            continue

    tile_size = (t_h/1000 * t_w/1000)

while True:
    try:
        w = int(input('Width of the surface(m): '))
        h = int(input('Height of the surface(m): '))
        break
    except:
        continue

while True:
    try:
        cost = abs(float(input('Enter Cost per tile: ')))
        break
    except:
        continue
print(f'Number of tiles: {TileCount(w , h, tile_size)}')
print('Price : Rs.', TileCount(w , h, tile_size) * cost)

