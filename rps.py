from random import randint

print "Welcome to Rock, Paper, Scissors!"
print "Type (r)ock, (p)aper or (s)cissors to play!"
print "Type (q)uit to quit."


while True:
	x=0
	getU = True

	while getU:
		u = raw_input()
		u = u.lower()
		if (u == "r" or u == "rock"):
			print "You chose Rock."
			x = 1
			getU = False
		elif (u == "p" or u == "paper"):
			print "You chose Paper."
			x = 2
			getU = False
		elif (u == "s" or u == "scissors"):
			print "You chose Scissors."
			x = 3
			getU = False
		elif (u == "q" or u == "quit"):
			getU = False
		else:
			print "Invalid input"

	if (u == "q" or u == "quit"):
		break

	y = randint(1,3)

	if (y==1):
		print "Opponent chose Rock."
		if (x==1):
			print "Tie!"
		elif (x==2):
			print "Paper beats Rock. You win!"
		elif (x==3):
			print "Rock beats scissors. You lose!"

	elif (y==2):
		print "Opponent chose Paper."
		if (x==1):
			print "Paper beats Rock. You lose!"
		elif (x==2):
			print "Tie!"
		elif (x==3):
			print "Scissors beats Paper. You win!"

	elif (y==3):
		print "Opponent chose Scissors."
		if (x==1):
			print "Rock beats Scissors. You win!"
		elif (x==2):
			print "Scissors beats Paper. You lose!"
		elif (x==3):
			print "Tie!"


	print "-------------------------"
	print ""
	print ""
	print ""


