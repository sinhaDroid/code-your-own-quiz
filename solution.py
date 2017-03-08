""" Fill in the blanks Quiz.

Ask the user for difficulty level and number of trys to display an approproate quiz.
The quiz has numbered blanks, where user has to fill those blanks with correct answer.
User can try the quiz until number of trys get end.

Example: 
To help you get started, we've provided a sample paragraph that you can use when testing your code.
Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

"""
questions = {
	'easy':
			"""The Android operating system was developed by ___1___, in 2004 backed by Google. Later ___2___ bought it in 2005 at a price of $50 ___3___. Google launched, Android operating system in ___4___ 5, 2007, which is a ___5___ based software system.""",
    'medium':
			"""Except Android ___1___ and ___2___, are name after sweet to name a few. Android is Andy ___3___ who is the co-creater of Android, it was the name given to him at ___4___ before joining ___5___, for his obession, and love for robots.""",
    'hard':
			"""Spirited ___1___ is the ___2___ Award winning film by ___3___ Miyazaki and Studio ___4___. It won Best ___5___ ___6___ Film, and also won the Golden ___7___ at the 2002 ___8___ International Film Festival(among many others). It was adapted by ___9___ for the English speaking audience."""
}

answers = {
	'easy':	[
		['Android Inc.', 'android inc.', 'ANDROID INC.'],
		['Google'],
        ['Million'],
        ['November'],
        ['Linux']
	],
	'medium':	[
		['1.0', '1'],
        ['1.1', 1.10],
        ['Rubin'],
        ['Apple'],
        ['Google']
	],
	'hard':	[
		['Away'],
        ['Academy', 'Oscar'],
        ['Hayao'],
        ['Ghibli'],
        ['Animated'],
        ['Feature'],
        ['Bear'],
        ['Berlin'],
        ['Walt Disney Pictures', 'Disney']
	]
}

alive=True
chances, difficultylevel=1, 'easy'
min_chances=0

def assignedifficulty():
	"""Choose your ``difficulty level``. """

	print "Enter your difficulty level:"
	difficultylevel=raw_input("Enter easy, medium, or hard: ")
	while difficultylevel not in questions:
		difficultylevel = raw_input("Please enter one of the options [easy, medium, hard]: ")

	print "This quiz will be "+difficultylevel
	print ""

def assignedchances():
	""" Assign the number of ```chances``` the player gets per question. """
	global chances

	chances=raw_input("Enter your number of chances per question: ")
	while not chances.isdigit() or int(chances) < min_chances:
		chances = raw_input("Please enter a number greater than 0: ")
	chances=int(chances)
	print ""

def checkanswer(verify, guess):
	for answer in verify:
		if guess.lower()==answer.lower():
			return True
		return False

def answerquestion(index, question):
    global alive
    chance = chances
    answer = answers[difficultylevel][index]

    while chance > 0:
        guess = raw_input("What goes in ___%s___: " % str(index+1))
        if checkanswer(answer, guess):
            print "Correct! \n"
            print '-' * 20
            question = question.replace('___%s___' % str(index+1), guess)
            print question
            print '-' * 20 + '\n'
            break
        elif chance > min_chances:
            print "That is incorrect. Try again."
            chance += -1
            print chance, "chance(s) left. \n"
        else:
            alive = False
            break
    return question

def startquiz():
    """ Shows the quiz and asks the user for answers.
    Returns:
        bool: True if the user completes the quiz, ``False`` if they use
        too many guesses.
    """
    global alive
    alive = True

    print '\n' + "* " * 10
    print "Welcome to the quiz.\n"
    assignedifficulty()
    question = questions[difficultylevel]
    assignedchances()

    print "Let's get started:" + "\n" + "=" * 20 + "\n" + question + "=" * 20 + '\n'

    for index in xrange(len(answers[difficultylevel])):
        question = answerquestion(index, question)
        if not alive: break

    if alive:
        print "Great job completing the %s quiz!\n" % difficultylevel
    else:
        print "Too many wrong guesses. Game over.\n"

    return alive

if __name__ == '__main__':

    # Main
    while True:
        startquiz()

        if raw_input("Would you like to play again: (yes or no)  ") not in ['yes', 'y']:
            print "Okay, good bye. \n"
            break

