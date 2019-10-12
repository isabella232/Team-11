# imports random madule form library
from random import randint

# the base class for the scenes. 
# Each scene has one variable name, and three functions: enter(), action(), and exit_scene(). 
# Read through the ones given, feel free to add more using the same template I've given you.
# Change, edit, or completely remove the scenes I gave you. Up to you.
class Scene(object):

	def enter(self):
		print ("This is the base scene class that's inherited by the other scenes, so it is not configured yet.")
		print ("Subclass it and implement enter(), action(), and exit_scene() for each scene.")
		exit(1)

class StartingOut(Scene):
	
	name = 'starting_out'

	def enter(self):
		print ("Hey there! You're about to embark on a journey leading you to different scenes all dependent on your decisions!")
		return self.action()
		
		
	def action(self):
		print ("Oh no! You just came back from school and you're starving! You bite into " +
			 "an apple and see that your tooth fell out! At least that means some extra money to spend, right?")
		print ("You only have a limited amount of money to spend, so you need to decide what to spend it on! " +
			"This is called budgeting, where you set aside money for things you want to do like buy toys or candy")
		print("With that tooth fairy money, are you going to spend your money on a toy or a bunch of candy?")
		print("Choice 1: Toys! That'll take a bite out of your budget though")
		print("Choice 2: Candy! I promise to brush my teeth after eating them though")
		
		choice = input("Please input an int> ")
		if choice == ':q':
			return self.exit_scene(choice)
		# this is some exception handling, you don't need to worry about it, 
		# just accept that it works and keeps the program from falling apart.
		try:
		   choice = int(choice)
		except ValueError:
		   print("That's not an int!")
		   return self.exit_scene(self.name)

		if int(choice) == 1:
			print ("")
			return self.exit_scene('death')
		elif int(choice) == 2:
			print ("Great! You're able to make more money for your family! Now you have less to worry about!")
			return self.exit_scene('boat_dillemma')
		else:
			print ("Come on now, that's not an int! Type :q if you want to drop out... but you should type an int (this is a fun game)!")
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		return outcome

class Savings(Scene):
	
	name = 'savings'

	def enter(self):
		print ("Oh boy... even though you have that extra cash incoming, you see a storm incoming. You find yourself staring at dark clouds; "
			+ "you might have just enough time to get home before they arrive (depending on the winds), however. You also see a boat in the "
			+ "distance, and depending if they are nice enough, the captain might be nice enough to be able to save you and your boat. With "
			+ "Christmas coming, however, you want to buy your family nice gifts; this is only possible if you just continue fishing through the storm. "
			+ "On one hand, you could take your chances with the ship, risk not giving your daughter a gift for Christmas, or attempt to beat the storm "
			+ "to shore")
		return self.action()

	def action(self):
		print ("What do you risk?")
        
		print("Choice 1: Radio the ship for help! Hopefully they pick up!")
		print("Choice 2: I mean, you can always stay and hope for the best!")
		print("Choice 3: Sail for your life! You might be able to reach shore if nothing goes wrong...")
        
        
		choice = input("Please input an int> ")
		if choice == ':q':
			return self.exit_scene(choice)
		# this is some exception handling, you don't need to worry about it, 
		# just accept that it works and keeps the program from falling apart.
		try:
		   choice = int(choice)
		except ValueError:
		   print("That's not an int!")
		   return self.exit_scene(self.name)

		if int(choice) == 1:
			print ("You radio the ship... unsuccessfully. You attempt to sail towards the ship but your sailboat gets destroyed in a rogue wave...")
			return self.exit_scene('death') 
		elif int(choice) == 2:
			print ("You see the storm coming... unfortunately it capsizes your boat but you are able to deploy your liferaft in time!")
			return self.exit_scene('capsize') 
		elif int(choice) == 3:
			print ("As you attempt to race for shore, the inflow of the storm drags you out to sea! You find yourself lost and succumb to the environment.")
			return self.exit_scene('death') 
		else:
			print ("Come on now, that's not an int! Type :q if you want to drop out... but you should type an int (this is a fun game)!") 
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		return outcome
			
class Loan(Scene):
	
	name = 'loan'

	def enter(self):
		print ("You survived! Though you hope you had a lifevest, at least you find yourself alive! As day turns into night, your drenched self starts to "
			+ "shiver, the beginnings of hypothermia...")
		return self.action()
		
		
	def action(self):
		print ("How do you try to stay warm?")
		print("Choice 1: Undress and curl into a fetus position! Your body heat might be able to keep you warm...")
		print("Choice 2: Use your body heat to warm the wet clothes you're wearing. It's only for a couple hours...")
		
		choice = input("Please input an int> ")
		if choice == ':q':
			return self.exit_scene(choice)
		# this is some exception handling, you don't need to worry about it, 
		# just accept that it works and keeps the program from falling apart.
		try:
		   choice = int(choice)
		except ValueError:
		   print("That's not an int!")
		   return self.exit_scene(self.name)

		if int(choice) == 1:
			print ("Success! Your body heat kept you just warm enough to survive a night in the open ocean.")
			return self.exit_scene('drinking_problems')
		elif int(choice) == 2:
			print ("Didn't you mom teach you this? Never keep wet clothes on or you'll get hypothermia!")
			return self.exit_scene('death')
		else:
			print ("Come on now, that's not an int! Type :q if you want to drop out... but you should type an int (this is a fun game)!")
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		return outcome

class Debt(Scene):
	
	name = 'debt'

	def enter(self):
		print ("This is just like the desert... with the sun beating down on me, how am I going to survive?! I might die of thirst before I "
			+ "am saved by someone... I just need a bit of water to survive on... and it can't be salty oceanwater... "
			+ "As you search the tiny liferaft, you find a solar water filter! With a bit of oceanwater, you can turn it into freshwater! "
			+ "You just need to grab it, however.")
		return self.action()

	def action(self):
		print ("How do you grab it? (or not)")
        
		print("Choice 1: Voluntarily jump into the water and hope you can pull yourself back up with "
			+ "the solar filter in hand!")
		print("Choice 2: Stare at it from the safety of the raft.")
		print("Choice 3: Reach for it!")
        
        
		choice = input("Please input an int> ")
		if choice == ':q':
			return self.exit_scene(choice)
		# this is some exception handling, you don't need to worry about it, 
		# just accept that it works and keeps the program from falling apart.
		try:
		   choice = int(choice)
		except ValueError:
		   print("That's not an int!")
		   return self.exit_scene(self.name)

		if int(choice) == 1:
			print ("The water is freezing... You throw the solar filter up onto the raft and grab onto the side of the ship... Those arm days" 
				+ " in the gym really paid off didn't they. You successfully pull yourself up to the side of the ship!")
			return self.exit_scene('food_problems') 
		elif int(choice) == 2:
			print ("You continue to stare at it... until you die of dehydration :(")
			return self.exit_scene('death') 
		elif int(choice) == 3:
			print ("You reach for it! And you grab it! But you didn't expect to fall in the water. Caught off guard, you unfortunately drown underneath the liferaft...")
			return self.exit_scene('death') 
		else:
			print ("Come on now, that's not an int! Type :q if you want to drop out... but you should type an int (this is a fun game)!") 
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		return outcome

class FoodProblems(Scene):


	name = 'food_problems'

	def enter(self):
		print ("Great! You have just enough water to survive on for a while. But even though you are quenched, you find yourself "
			+ "starving for food. Given that you're in the middle of the ocean, you have very few options... ")
		return self.action()

	def action(self):
		print ("What do you eat?")
        
		print("Choice 1: Turtles! Hopefully you don't get sick... cause you're eating a turtle...")
		print("Choice 2: Fish! Even though its raw... hopefully you don't get sick")
		
        
		choice = input("Please input an int> ")
		if choice == ':q':
			return self.exit_scene(choice)
		# this is some exception handling, you don't need to worry about it, 
		# just accept that it works and keeps the program from falling apart.
		try:
		   choice = int(choice)
		except ValueError:
		   print("That's not an int!")
		   return self.exit_scene(self.name)

		if int(choice) == 1:
			print ("Fool! The shell is preventing you from reaching the meat of the turtle and you starve to death!")
			return self.exit_scene('death') 
		elif int(choice) == 2:
			print ("Yum? You eat the fish unwillingly but at least you are able to eat enough so that you're not hungry anymore!")
			return self.exit_scene('com_problems') 
		else:
			print ("Come on now, that's not an int! Type :q if you want to drop out... but you should type an int (this is a fun game)!") 
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		return outcome

class ComProblems(Scene):

	name = 'com_problems'

	def enter(self):
		print ("Finally... you see a ship! They can save you(hopefully)! You don't know how far away they are from you, as the ocean's "
			+ "mirage distorts distance. You're not sure if they can hear your shouts, if their radio is on, or if you can paddle in time."
			+ "You do know that you only have enough time to make one decision effectively.")
		return self.action()

	def action(self):
		print ("Choose wisely! This can be your way out!")
        
		print("Choice 1: Use your radio skills and hope they pick up!")
		print("Choice 2: Paddle for your life!")
		print("Choice 3: Scream for your life!")
        
        
		choice = input("Please input an int> ")
		if choice == ':q':
			return self.exit_scene(choice)
		# this is some exception handling, you don't need to worry about it, 
		# just accept that it works and keeps the program from falling apart.
		try:
		   choice = int(choice)
		except ValueError:
		   print("That's not an int!")
		   return self.exit_scene(self.name)

		if int(choice) == 1:
			print ("You used your radio skills... but your radio skills can't fix a radio with no batteries, unfortunately")
			return self.exit_scene('death') 
		elif int(choice) == 2:
			print ("You paddle, and paddle, and paddle, and paddle... AND REACH THE BOAT!")
			return self.exit_scene('climbing_problems') 
		elif int(choice) == 3:
			print ("Screaming for your life can only help so much when the boat is a mile away... they cannot hear you and your last hope is gone.")
			return self.exit_scene('death') 
		else:
			print ("Come on now, that's not an int! Type :q if you want to drop out... but you should type an int (this is a fun game)!") 
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		return outcome

class ClimbingProblems(Scene):

	name = 'climbing_problems'

	def enter(self):
		print ("A mile of paddling later... you reach the boat! As you try to get on the boat, you are posed with a decision: use a ladder to climb on "
			+ " or try to jump?")
		return self.action()

	def action(self):
		print ("Choose wisely! This can be your way out!")
        
		print("Choice 1: Use a ladder!")
		print("Choice 2: Jump!")
        
        
		choice = input("Please input an int> ")
		if choice == ':q':
			return self.exit_scene(choice)
		# this is some exception handling, you don't need to worry about it, 
		# just accept that it works and keeps the program from falling apart.
		try:
		   choice = int(choice)
		except ValueError:
		   print("That's not an int!")
		   return self.exit_scene(self.name)

		if int(choice) == 1:
			print ("You grab onto the ladder and start climbing, but the ladder breaks and lets you fall into the abyss below.")
			return self.exit_scene('death') 
		elif int(choice) == 2:
			print ("You prepare yourself for the jump... and are able to climb on to the boat!!")
			return self.exit_scene('finished') 
		else:
			print ("Come on now, that's not an int! Type :q if you want to drop out... but you should type an int (this is a fun game)!") 
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		return outcome

class Finale(Scene):
	name = 'finished'


