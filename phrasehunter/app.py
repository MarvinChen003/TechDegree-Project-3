from game import Game
from phrase import Phrase

def print_phrase(phrase_object):
    print(f"The phrase is: {phrase_object}")

if __name__ == "__main__":
    """ Trial 1 """
    # phrase_trial_instance = Phrase()
    # game_trial_instance  = Game()

    # print(phrase_trial_instance)
    # print(game_trial_instance)
    
    """ Trial 2 """
    # phrase_trial_instance = Phrase("may the force be with you")
    # print(phrase_trial_instance.phrase)

    trial_game_instance = Game()

    """ Trial 3 """
    # for phrase in trial_game_instance.phrases:
    #     print(phrase)

    print_phrase(trial_game_instance.active_phrase)
    # print_phrase(trial_game_instance.create_phrases())