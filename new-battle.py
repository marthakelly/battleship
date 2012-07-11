from pprint import pprint
import random

def new_board(rows = 3, columns = 3, default_value = 0):
	board = [] 
	
	for i in range(rows):
		board.append([default_value] * columns)
	return board

battleship = new_board(10, 10)

def fire_shot(x, y, default_value, board):
	board[x][y] = default_value

def find_open_spot(row, blank_space, ship, first_match=True):
	i = random.randrange(0, 9 - ship)
	while i < len(row):
		if [blank_space]*ship == row[i:i + ship]:
			row[i:i+ship] = [1]*ship
			i += ship
			if first_match:
				break
		else:
			i += 1
	return row

def place_ship(ship):
	i = random.randrange(0, 10)
	row = battleship[i]
	
	add_ship = find_open_spot(row, 0, ship)
	battleship[i] = add_ship
	
	print ship

ship_list = [5, 4, 3, 3, 2]

for i in ship_list:
	place_ship(i)
	
#place_ship(battleship)

pprint(battleship)

#fire_shot(1, 1, 5, battleship)

# make sure ships dont overlap and have white space around them