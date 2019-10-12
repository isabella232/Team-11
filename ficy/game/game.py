# imports multiple clases from the python library and some of our
# own modules.
from sys import exit
from random import randint
from map import Map
from leaderboard import Leaderboard
from scores import Score
from game_engine import Engine

# global variables to keep track of score, player, and leaderboard
moves =0
name = ""
leaderboard = Leaderboard()

# what happens when the game is over
# takes in a boolean parameter
# should update leaderboard, global variables, and print leaderboard
def game_over(won):
    global name
    global moves
    global leaderboard
    score = Score(name, moves)
    if won == True:
    	print("Money remaining:",moves)
    	print("You won")
    	score = Score(name, moves)
    	if leaderboard.update(score) == True:
    		leaderboard.insert(score)
    else:
    	print ("\nGame Over.")
    	moves =0
    	name =""
    leaderboard.print_board()

# initializes/updates global variables and introduces the game.
# starts the Map and the engine.
# ends the game if needed.
def play_game():
	while True:
		global name 
		global moves 
		global difficulty
		print ("Welcome to the Tooth Fairy! To quit, enter :q at any time. Good luck!") # raise ValueError ('todo')
		name = input("\nLet's begin! To begin, please input your name: > ") # raise ValueError ('todo')
		if (name == ':q'):
			exit(1)
		a_map = Map('starting_out')
		a_game = Engine(a_map)
		moves = a_game.play()
		game_over(a_game.won())

play_game()