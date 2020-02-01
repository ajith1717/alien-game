import random
def getSecretNum(numDigits):
	numbers = list(range(10))
	random.shuffle(numbers)
	secretNum =''
	for i in range(numDigits):
		secretNum += str(numbers[i])
	return secretNum
def getClues(guess, secretNum):
	if guess == secretNum:
		return 'You got it!'
	clue = []
	for i in range(len(str(guess))):
		if guess[i] == secretNum[i]:
			clue.append('Fermi')
		elif guess[i] in secretNum:
			clue.append('Pico')
		else:
		    clue.append('None')
		if len(clue) == 0:
			return 'None'
	return ' '.join(clue)
def isOnlyDigits(num):
    if len(str((num))) != 3:
    	print 'only 3 digit no is allowed'
        return False
    else:
        return True
def playAgain():
	play = raw_input("Do you want to play again? Yes or No?")
	return play.lower.startswith('y')
NUMDIGITS = 3
MAXGUESS = 10
print('I am thinking of a %s digit number. Try to guess what it is.' % (NUMDIGITS))
print('Here are some clues:')
print('When I say:    That means:')
print('  Pico         One digit is correct but in the wrong position.')
print('  Fermi        One digit is correct and in the right position.')
print('  None       No digit is correct.')
secretNum = getSecretNum(NUMDIGITS)
print('I have thought up a number. You have %s guesses to get it' % (MAXGUESS))
numGuesses = 1
while numGuesses <= MAXGUESS:
    Guess=int(input("enter your guess: "))
    if isOnlyDigits(Guess)==True:
        if len(str(Guess)) == NUMDIGITS:
            print 'Guess : ' ,str(numGuesses)
    else:
        break
    clue = getClues(str(Guess), secretNum)
    print(clue)
    numGuesses += 1
    if int(Guess) == int(secretNum):
        break
    else:
        print 'guess again'
else:
    print 'You ran out of guesses. The answer was ' + secretNum
    playAgain()