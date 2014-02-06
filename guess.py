import random
import os

def guess():
	print "Guess a number between 1 and 1000"
	prevGuess = 0
	counter = 0
	goal = random.randint(1, 1000)
	def loopFx(counter, prevGuess):
		
		guessNum = raw_input()
		if int(guessNum) < goal:
			prevGuess = int(guessNum)
			os.system('cls')
			print prevGuess
			print "\nMore"
			counter +=1
			loopFx(counter, prevGuess)
	
		if int(guessNum, prevGuess) > goal:
			prevGuess = int(guessNum)
			os.system('cls')
			print "\nLess"
			counter +=1
			loopFx(counter, prevGuess)
	
		if int(guessNum, prevGuess) == goal:
			counter +=1 
			os.system('cls')
			print "\nGood Job! You got it in %d turns!" % counter
				
	loopFx(counter, prevGuess)
os.system('cls')
guess()