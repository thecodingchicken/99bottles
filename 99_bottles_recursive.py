#!/bin/bash python3
# 99 Bottles of Beer
# Python 3 Edition
# Joshua Bowe

import sys, time
def constrain(number):
	if number < 2:
		return number
	return 2
def beer_song(number,delay=1):
	print("%d bottle%s of beer on the wall, %d bottle%s of beer"%
				(number, (['', 's'][number == 1]),
				number, ['', 's'][number == 1]))
	print("Take one down, pass it around, %s on the wall"%
			(['no more beer', '1 bottle of beer',
			'%d bottles of beer'%number][constrain(number)]))
	if number:
		time.sleep(delay)
		print("--")
		beer_song(int(number-1),delay)
	return None
	
	
if __name__ == '__main__':
	number = 99
	if len(sys.argv)>1:
		number = int(sys.argv[1])
	if len(sys.argv)>2:
		delay = int(sys.argv[2])
	beer_song(number, delay)
