import random

class Game():

    def __init__(self):
        self.missed = 0
        self.guesses = [" "]
        self.phrases = [
            "may the force be with you",
            "all roads lead to rome",
            "life is a box of chocolates",
            "words are wind",
            "winter is coming",
        ]
        self.active_phrase = get_random_phrase(self.phrases)

    """ How do I get this to work?"""
    # @property
    # def create_phrases(self):
    #     list_of_phrases = [
    #         "may the force be with you",
    #         "all roads lead to rome",
    #         "life is a box of chocolates",
    #         "words are wind",
    #         "winter is coming",
    #     ]
    #     return self.list_of_phrases
    # @property
    def get_random_phrase(self):
        random_phrase = random.choice(self.phrases)
        return self.random_phrase

