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
	#pprint(board)
	
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
	
	def white_space(temp_board, x, y):
		counter = 0
		
		i_start = x-1
		i_end = x+2
		j_start = y-1
		j_end = y+2

		if i_start < 0:
			i_start = 0

		if i_end > 9:
			i_end = 9

		if j_start < 0:
			j_start = 0

		if j_end > 9:
			j_end = 9

		for i in range(i_start, i_end):
			for j in range(j_start, j_end):
				if i==x and j==y: 
					pass
				elif temp_board[i][j] == 1:
					temp_board[i][j] = 2
					counter += 1
					
		pprint(temp_board)	
	
	def format_ship(n):
		i = random.randrange(0, 9)
		init = board[i]
		ship = find_open_spot(init, 0, n)
		temp_board[i] = ship
		
		for i in xrange(10):
		      for j in xrange(10):
		        white_space(temp_board, i, j)
		
		# board = white_space(temp_board, i)
		
		return board

	new_ship = format_ship(3)
	
	#pprint(new_ship)
	
	"""
	row = [1,  ,  ,  , 0,  ,  ,  ,  , 0]
	row = [1,  , 1, 1,  , 1, 1, 1, 1,  ]
	row = [1,  ,  ,  , 1,  ,  ,  ,  , 0]
	row = [1,  , 0,  , 1,  , 0, 0, 0, 0]
	row = [1,  , 0,  , 1,  , 0, 0, 0, 0]
	row = [ , 0, 0, 0,  , 0, 0, 0,  ,  ]
	row = [0, 0, 0, 0, 0, 0, 0,  , 1,  ]
	row = [0, 0, 0,  ,  ,  ,  ,  , 1,  ]
	row = [0, 0,  , 0, 0, 0, 0,  , 1,  ]
	row = [0, 0, 0,  ,  ,  ,  , 0,  , 0]
	"""
	
	#row = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
		
	#print find_open_spot(row, 0, 4)
	
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

# [2, 2, 2]