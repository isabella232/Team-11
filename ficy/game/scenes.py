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
			 "an apple and see that your tooth fell out! At least that means some extra money to spend from the tooth fairy, right?\n")
		print ("You only have a limited amount of money to spend, so you need to decide what to spend it on! " +
			"This is called budgeting, where you set aside money for things you want to do like buy games or candy\n")
		print ("With $100 to spend, you need to budget your money to last you a while!")
		print("With that tooth fairy money, are you going to spend some of your money on a game or a bunch of candy?")
		print("If you don't want any of the above, just enter 3 to skip!")
		print("Choice 1: Games! That'll take a bite out of your budget though, costing $30")
		print("Choice 2: Candy! A cheaper alternative, this will only cost you $8")
		print("Choice 3: Skip!")
		money=100
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
			money=money-30
			print ("You now have " ,money, " dollars remaining!")
			return self.exit_scene('savings')
		elif int(choice) == 2:
			money=money-8
			print ("You now have " ,money, " dollars remaining!")
			return self.exit_scene('savings')
		elif int(choice)==3:
			return self.exit_scene('savings')
		else:
			print ("Come on now, that's not an int! Type :q if you want to drop out... but you should type an int (this is a fun game)!")
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		return outcome

class Savings(Scene):
	
	name = 'savings'

	def enter(self):
		print ("Looks like you're having with candy or your toys! These are everyday items you can buy, but if unexpected costs (medical bills, emergencies, etc.) come up, "
			+ "you're going to have to get money from somewhere. But where? One option is to store money in savings. Savings "
			+ "are when you set aside a money for the future. You only touch this money when you need this desperately or in "
			+ "an emergency however! ")
		print("*************************************************************")
		return self.action()

	def action(self):
		print ("\nIt's Black Friday and you notice your favorite game is on sale for 50% off, for the price of $95! What a steal! That is, however, until you realize that you do not"
			+ " have enough money to buy it 😬. How will you manage?")
       
		print("Choice 1: Use emergency savings to get your game! What's the worst thing that could happen...")
		print("Choice 2: There's always next black friday... ")
        
        
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
			print ("You better start cutting off certain expenditures because you have no more savings for emergencies!")
			return self.exit_scene('loan') 
		elif int(choice) == 2:
			print ("No games for now :(, but you have a healthy savings account building up!")
			return self.exit_scene('loan') 
		else:
			print ("Come on now, that's not an int! Type :q if you want to drop out... but you should type an int (this is a fun game)!") 
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		return outcome
			
class Loan(Scene):
	
	name = 'loan'

	def enter(self):
		print ("Although savings can be helpful when there are times you need a bit of money quick, it can sometimes be hard to save. "
			+ "As a result, (especially with college) you might be forced to take out loans. Loans are when you go to a bank and they give you "
			+ " a sum of money that you will have to pay back with interest. Interest is what they charge you for taking out the loan, a sort of service fee.")
		print("**************************************************************")
		return self.action()
		
		
	def action(self):
		print("\nUnfortunately, you forgot to realize that although you bought a game, you don't have a console! If you want to play the game you just bought, you're going to"
			+ " have to take out a loan. You want to spend the least amount possible, so which loan is better for you?" )
		print("Choice 1: $500 loan at 10% interest")
		print("Choice 2: $500 loan at 5% interest")
		
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
			print ("Incorrect! Since interest is essentially a service charge, the lower the interest rate the better for you! (and the less you have to pay!)")
			print("MORE SCENES COMING SOON!!")
			return self.exit_scene('finished')
		elif int(choice) == 2:
			print ("Correct! Since interest is essentially a service charge, the lower the interest rate the better for you! (and the less you have to pay!)")
			print("MORE SCENES COMING SOON!!")
			return self.exit_scene('finished')
		else:
			print ("Come on now, that's not an int! Type :q if you want to drop out... but you should type an int (this is a fun game)!")
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		return outcome



class Finale(Scene):
	name = 'finished'


