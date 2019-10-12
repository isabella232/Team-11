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
        print ("Hey there! You're about to embark on a learning journey to gain" +
         "familiarty with some finance terms! They might look scary but you can do it.")
        return self.action()

    def action(self):
        print ("Are you ready? Hit enter to continue ")
        choice = raw_input("\n > ")
        if choice == ':q':
            return self.exit_scene(choice)
        # this is some exception handling, you don't need to worry about it,
        # just accept that it works and keeps the program from falling apart.
        print ("Great, lets get started!")
        return self.exit_scene('budget')


    def exit_scene(self, outcome):
        return outcome

class Budget(Scene):

    name = 'budget'

    def enter(self):
        print ("Our first word is BUDGET!\n"
            + "A budget is a way to estimate and limit how much money you can / allow yourself to spend.\n"
            + "Sometimes it might be easier than to budget then others, lets see some example scenarios.\n"
            + "Ex 1: So many bills! \n"
            + "Ex 2: Unexpected birthday money from distance relatives! \n")
        return self.action()

    def action(self):
        print ("What do you do?")

        print("Choice 1: Use the money to pay off some previous debt\n")
        print("Choice 2: See if there is anyway to lower your bills\n")


        choice = raw_input("Pick an option, 1 or 2> ")
        if choice == ':q':
            return self.exit_scene(choice)
        # this is some exception handling, you don't need to worry about it,
        # just accept that it works and keeps the program from falling apart.
        try:
           choice = int(choice)
        except ValueError:
           print("That's not an int!")
           return self.exit_scene(self.name)


        print ("Exactly! You are starting to get this!")
        return self.exit_scene('income')

    def exit_scene(self, outcome):
        return outcome

class Income(Scene):

    name = 'income'

    def enter(self):
        print ("On to the next term: Income!\n")
        return self.action()


    def action(self):
        print ("Income is the money you are getting in.\n")
        print("Ex 1: All the money earned from a job is income.\n")
        print("Ex 2: If you get a scholarship this is also considered income.\n")

        choice = raw_input("Enter 1 for more explaining or Enter 2 to continue> ")
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
            print ("Any money made from investments is also income, however, investment is a term for later!\n")
            return self.exit_scene('finished')
        elif int(choice) == 2:
            print ("Congrats! You finished this section, now to put it to practice with the games!\n")
            return self.exit_scene('finished')
        else:
            print ("Come on now, that's not an int! Type :q if you want to drop out... but you should type an int (this is a fun game)!\n")
            return self.exit_scene(self.name)

    def exit_scene(self, outcome):
        return outcome

class Finale(Scene):
    name = 'finished'
