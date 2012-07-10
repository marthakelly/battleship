from pprint import pprint
import random

def main():
	def initialize():
		a  = []
		
		for i in xrange(10):
			a.append([])
			for j in xrange(10):
				a[i].append(0)
		return a

	board = initialize()
	temp_board = initialize()
	
	def find_open_spot(row, required_number, num_repeats, stop_after_match=True):
		i = random.randrange(0, 9 - num_repeats)
		while i < len(row):
			if [required_number]*num_repeats == row[i:i + num_repeats]:
				row[i:i+num_repeats] = [1]*num_repeats
				i += num_repeats
				if stop_after_match:
					break
			else:
				i += 1
		return row
	
	def white_space(temp_board, int, x, y):	
		i_start = x - 1
		i_end = x + 2
		j_start = y - 1
		j_end = y + 2
		
		for i in range(i_start, i_end):
			for j in range(j_start, j_end):
				ship = temp_board[i][j]
				
				if ship == 1:
					if int == 0:
						temp_board[i + 1][j] = 2
					elif int == 9:
						temp_board[i - 1][j] = 2
					else:	
						temp_board[i + 1][j] = 2
						temp_board[i - 1][j] = 2
					
					if temp_board[i][j + 1] == 0 and temp_board[i][j + 1] != 2:
						temp_board[i][j + 1] = 2
					
					if temp_board[i][j - 1] == 0 and temp_board[i][j - 1] != 2:
						temp_board[i][j - 1] = 2

		return temp_board

	def format_ship(n):
		int = random.randrange(0, 10)
		init = board[int]
		ship = find_open_spot(init, 0, n)
		temp_board[int] = ship
		
		for j in range(0, 8):
			for k in range(0, 8):
				white_space(temp_board, int, j, k)

		return board

	ship_list = [5, 4, 3, 3, 2]
	
	for i in ship_list:
		new_ship = format_ship(i)
		print i
		board = temp_board
		i = i + 1
			
	pprint(board)
	
if __name__ == "__main__":
	main()
	
	
"""
	Type of ship		Size
	aircraft carrier	5
	battleship			4
	submarine			3
	destroyer			3
	patrol boat			2
	
"""

# find whitespace
# check cols
# connect on a network
# figure out how two boards connect 
# output miss or hit to console
