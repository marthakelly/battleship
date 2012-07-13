from pprint import pprint
import random
import sys

def main():

	aircraft_carrier = []
	battle_ship = []
	submarine = []
	destroyer = []
	patrol_boat = []

	def new_board(rows = 10, columns = 10, default_value = 0):
		board = []

		for i in xrange(rows):
			board.append([default_value] * columns)

		return board

	def fire_shot():
		print "Select x, y coordinates to fire a shot."
		
		fire = input("You may fire when ready: ")
		
		x = fire[0]
		y = fire[1]
		
		if battleship[x][y] == 1:
			print "\033[95m" + "hit!" + "\033[0m"		
		else:
			print "\033[93m" + "miss!" + "\033[0m"
		
		track_hits(x, y)
		battleship[x][y] = 5
		pprint(battleship)
		fire_shot()

	def track_hits(x, y):
		all_ships = [aircraft_carrier] + [battle_ship] + [submarine] + [destroyer] + [patrol_boat]
		
		if battleship[x][y] == 1:
			for ship in all_ships:
				for spot in ship:
					if spot == [x, y]:
						ship.remove(spot)
			
			for ship in all_ships:
				if len(ship) == 0:
					if all_ships.index(ship) == 0:
						print "You sunk the aircraft carrier!"
					elif all_ships.index(ship) == 1:
						print "You sunk the battle ship!"
					elif all_ships.index(ship) == 2:
						print "You sunk the submarine!"
					elif all_ships.index(ship) == 3:
						print "You sunk the destroyer!"
					elif all_ships.index(ship) == 4:
						print "You sunk the patrol boat!"

			if len(all_ships) == 0:
				print "You Win!"
				sys.exit()

	def find_open_spot(row, row_number, required_number, num_repeats, stop_after_match=True):
		i = random.randrange(0, 9 - num_repeats)
		while i < len(row):                   
			if [required_number]*num_repeats == row[i:i + num_repeats]:
				row[i:i+num_repeats] = [1]*num_repeats                  
				
				placement = [k for k in range(len(row)) if row[k] == 'x']
				
				if num_repeats == 5:
					for coords in xrange(5):
						aircraft_carrier.append([row_number, i+coords])
				elif num_repeats == 4:
					for coords in xrange(4):
						battle_ship.append([row_number, i+coords])
				elif num_repeats == 3:
					if len(submarine) < 3:
						for coords in xrange(3):
							submarine.append([row_number, i+coords])
					else:
						for coords in xrange(3):
							destroyer.append([row_number, i+coords])
				elif num_repeats == 2:
					for coords in xrange(2):
						patrol_boat.append([row_number, i+coords])
				
				i += num_repeats                                                  
				if stop_after_match:
					break
			else:
				i += 1
		
		return row
	
	def transform_board(battleship):
		a = battleship
		battleship = new_board()
		for i in range(10):
			for j in range(10):
				battleship[i][j] = a[j][i]

		return battleship

	def place_ship(ship):
		i = random.randrange(0, 10)
		row = battleship[i]
	
		add_ship = find_open_spot(row, i, 0, ship)
		battleship[i] = add_ship
	
		return battleship

	#init battleship board
	battleship = new_board(10, 10)

	ships = [5, 4, 3, 3, 2]

	place_ship(ships[0])
	battleship = transform_board(battleship)

	for item in aircraft_carrier:
		item.reverse()

	place_ship(ships[1])
	place_ship(ships[2])

	#battleship = transform_board(battleship)

	#for item in submarine:
	#	item.reverse()

	place_ship(ships[3])
	place_ship(ships[4])

	pprint(battleship)

	print 'aircraft carrier', aircraft_carrier
	print 'battle ship', battle_ship
	print 'submarine', submarine
	print 'destroyer', destroyer
	print 'patrol boat', patrol_boat

	fire_shot()

if __name__ == "__main__":
    main()