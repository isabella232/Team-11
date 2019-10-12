# imports multiple clases from the python library and some of our
# own modules.
from sys import exit
from random import randint
from map import Map
from leaderboard import Leaderboard
from scores import Score
from game_engine import Engine
import json

FILE_PATH = "../data/terms.json"

# global variables to keep track of score, player, and leaderboard
moves = 0
name = ""
age = 0
leaderboard = Leaderboard()

def get_word_list(category, min_age):
    """
    Gets a word list from JSON file
    """
    with open(FILE_PATH) as word_data:
        data = json.load(word_data)
        words = []
        age_group = data[category]
        for age_group in data[category]:
            if min_age >= 4:
                words += list(age_group["4"])
            if min_age >= 13:
                words += list(age_group["13"])
            if min_age >= 36:
                words += list(age_group["36"])
            if min_age >= 66:
                words += list(age_group["66"])
        return words

# what happens when the game is over
# takes in a boolean parameter
# should update leaderboard, global variables, and print leaderboard
def game_over(won):
    global name
    global moves
    global leaderboard
    print('NEXT LEVEL STILL UNDER CONSTRUCTION, CHECK BACK SOON\n')

# initializes/updates global variables and introduces the game.
# starts the Map and the engine.
# ends the game if needed.
def play_game():
    while True:
        global name
        global moves
        global difficulty
        print ("Welcome to Fincy Education! To quit, enter :q at any time. Good luck!") # raise ValueError ('todo')
        name = raw_input("\nLet's begin! To begin, please input your name: > ")
        if (name == ':q'):
            exit(1)
        age = raw_input("\n Enter the age you want to work with>") # raise ValueError ('todo')
        # learning_words = get_word_list('budgeting', age)
        a_map = Map('starting_out')
        a_game = Engine(a_map)
        moves = a_game.play()
        game_over(a_game.won())

play_game()
