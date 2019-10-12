# importing random int maker module
from random import randint

# class defines what happens when a player dies.
# in this case, it has a list of phrases to be displayed
# randomly, and returns the string 'died' to let the engine know.
class Death(object):
	quips = ["Not quite, lets try again!",
			"Looks like this needs some refreshing...",
			"Almost there! Look at the notes again",
			"So close!",
			]
	def enter(self):
		print (Death.quips[randint(0, len(self.quips)- 1)])
		return 'died'
