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
		
	def white_space(board):
		
		for row in board: 
			print row
			for item in row:
				if item == 1:
					print row[item]
			
	def place_ship(n):
		i = random.randrange(0, 10)
		init = board[i]
		add_ship = find_open_spot(init, 0, n)
		board[i] = add_ship
		
		white_space(board)

	ship_list = [5]
	
	for i in ship_list:
		place_ship(i)

if __name__ == "__main__":
	main()