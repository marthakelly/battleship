from pprint import pprint
import random

def new_board(rows = 3, columns = 3, default_value = 0):
	board = [] 
	
	for i in range(rows):
		board.append([default_value] * columns)
	return board
	
def fire_shot(x, y, default_value, board):
	board[x][y] = default_value

def place_ship(size, board):
	rand_row = random.randrange(0, 9 - size)
	rand_col = random.randrange(0, 9 - size)

	count = 0
	while count < size:
		board[rand_row][rand_col + count] = 1
		count += 1
		
		
	

battleship = new_board(10, 10, 0)

fire_shot(1, 1, 5, battleship)

place_ship(3, battleship)

pprint(battleship)