from pprint import pprint
import random

def new_board(rows = 3, columns = 3, default_value = 0):
	board = [] 
	
	for i in range(rows):
		board.append([default_value] * columns)
	return board

def fire_shot(x, y, default_value, board):
	board[x][y] = default_value

def find_open_spot(row, blank_space, ship, first_match=True):
	i = random.randrange(0, 9 - ship)
	while i < len(row):
		if [blank_space]*ship == row[i:i + ship]:
			row[i:i+ship] = [1]*ship
			#i += ship
			if first_match:
				break
		else:
			i += 1
	
	placement = [j for j in range(len(row)) if row[j] == 1]
	
	# get the index for this particular ship
	
	for k in placement:
		print [i, k]

	return row

def place_ship(ship):
	i = random.randrange(0, 10)
	row = battleship[i]
	
	add_ship = find_open_spot(row, 0, ship)
	battleship[i] = add_ship

battleship = new_board(10, 10)

ships = [5, 4, 3, 3, 2]
#ships = [[5, "destroyer"]]

for ship in ships:
	place_ship(ship)

pprint(battleship)

#fire_shot(1, 1, 5, battleship)

# to do:
# work out vertical placement
# connect over a local network
# detect collision