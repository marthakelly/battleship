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
	#pprint(board)
	
	def find_open_spot(row, required_number, num_repeats, stop_after_match=True):
		i = 0
		while i < len(row):
			if [required_number]*num_repeats == row[i:i + num_repeats]:
				row[i:i+num_repeats] = [1]*num_repeats
				i += num_repeats
				if stop_after_match:
					break
			else:
				i += 1
		return row
	
	def test():
		i = random.randrange(0, 9)
		init = board[i]
		x = find_open_spot(init, 0, 4)
		board[i] = x
		return board

	new_board = test()
	
	pprint(new_board)
	
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