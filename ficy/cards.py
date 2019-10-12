import json

FILE_PATH = "../data/imgs.json"

class Card:
    def __init__(self, card_name, img, description):
        self.card_name = card_name
        self.img = img
        self.description = description

    def __str__(self):
        return "Card name:%s, Image path; %s, description: %s" % (self.card_name, self.img, self.description)
def create_word_search_card():
    with open(FILE_PATH) as data:
        loaded_data = json.load(data)
        return Card("Word Search", loaded_data["word search"], 'A word search game!')
