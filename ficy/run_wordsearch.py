import json
import wordsearch

FILE_PATH = "../data/terms.json"

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
