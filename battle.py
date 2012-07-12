from pprint import pprint
import random

aircraft_carrier = []
battle_ship = []
submarine = []
destroyer = []
patrol_boat = []

def new_board(rows = 3, columns = 3, default_value = 0):
	board = [] 
	
	for i in range(rows):
		board.append([default_value] * columns)
	return board


def fire_shot():
	print "Select x, y coordinates to fire a shot."
	fire = input("You may fire when ready: ")
	x = fire[0]
	y = fire[1]
	
	if battleship[x][y] == 1:
		print 'hit!'
	else:
		print 'miss!'
		
	battleship[x][y] = 5
	
	pprint(battleship)
	
	fire_shot()



# new

def transform_board(battleship):
    a = battleship
    battleship = new_board(10, 10)
    for i in range(10):
        for j in range(10):
            battleship[i][j] = a[j][i]

    return battleship

# new


def find_open_spot(row, i, blank_space, ship, first_match=True):
	j = random.randrange(0, 9 - ship)
	while j < len(row):
		if [blank_space]*ship == row[j:j + ship]:
			row[j:j+ship] = [1]*ship
			if first_match:
				break
		else:
			j += 1
	
	placement = [k for k in range(len(row)) if row[k] == 1]
	
	# get the index for this particular ship

	for l in placement:
		if ship == 5:
			aircraft_carrier.append([i, l])
		elif ship == 4:
			battle_ship.append([i, l])
		elif ship == 3:
			if len(submarine) < 3:
				submarine.append([i, l])
			else:
				destroyer.append([i, l])
		elif ship == 2:
			patrol_boat.append([i, l])

	return row

def place_ship(ship):
	i = random.randrange(0, 10)
	row = battleship[i]
	
	add_ship = find_open_spot(row, i, 0, ship)
	battleship[i] = add_ship
	
	return battleship
	
battleship = new_board(10, 10)

ships = [5, 4, 3, 3, 2]

place_ship(ships[0])
battleship = transform_board(battleship)
place_ship(ships[1])
battleship = transform_board(battleship)
place_ship(ships[2])
battleship = transform_board(battleship)
place_ship(ships[3])
battleship = transform_board(battleship)
place_ship(ships[4])

pprint(battleship)

print 'aircraft carrier', aircraft_carrier
print 'battle ship', battle_ship
print 'submarine', submarine
print 'destroyer', destroyer
print 'patrol boat', patrol_boat

fire_shot()

# to do:
# work out vertical placement
# connect over a local network
# detect collision