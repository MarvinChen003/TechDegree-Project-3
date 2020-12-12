from phrase import Phrase
import random
import sys
# sys imported but not use
import string


class Game():
    missed = 0
    guess_count = 0
    phrases = []
    active_phrase = None
    guesses = [" "]
    # There might better be class property/attributes
    congratulatory_messages = [
            "Nice Job!", 
            "Woohoo, that's great!",
            "Not bad, not bad at all.",
            "Good one!"
            ]
    encouraging_messages = [
            "Oh, that's too bad",
            "Oh no!",
            "Good try, but no dice.",
            "Bad luck!",
    ]

    def __init__(self):
        self.guesses = [" "]
        self.phrases = [
            Phrase('May the Force be with you'),
            Phrase('All roads lead to Rome'),
            Phrase('Life is a box of chocolates'),
            Phrase('Words are wind'),
            Phrase('Winter is coming'),
        ]
        self.active_phrase = self.get_random_phrase()


    def welcome(self):
        print("\n     ==============================")
        print("        Welcome to Phrase Hunter")
        print("     ==============================\n")
        # use variable not function


    def rules(self):
        print("Guidelines:")
        print("  - Identify and complete the famous phrases by guessing its letters.")
        print("  - If you can complete the phrase before making 5 incorrect guesses,you win.") 
        print("  - If you make 5 incorrect guesses, you lose.")
        print("  - You can only input individual letters that you've not previously guessed.\n")
        # use variable not function
   

    def start(self):
        self.welcome()
        self.rules()
        # line 53 - 54
        # Use variable to define rules and message then give it to print as parameter
        check_complete_value = False
        while self.missed < 5 and check_complete_value == False:
            print(f"\nGuess #{self.guess_count + 1}:\n")
            self.active_phrase.display(self.guesses)
            print(f"\nNumber of Incorrect Guesses: {self.missed}")
            user_guess_uppercase, user_guess_lowercase = self.convert_guess_to_both_cases()
            self.guesses.append(user_guess_uppercase)
            self.guesses.append(user_guess_lowercase)
            self.handle_guess(user_guess_uppercase,user_guess_lowercase)
            # Line 60 - 63, user only allowed to input lower cases,
            # check_phrase method should
            # has the ability to check upper and lower cases

            check_complete_value = self.active_phrase.check_complete(self.guesses)
            # you can put line 70 in the condition of line 58
        self.game_over()


    def get_random_phrase(self):
        self.pointer = random.randint(0, 4)
        self.selected_phrase = self.phrases[self.pointer]
        return self.selected_phrase
        # pointer and selected_phrase might not necessarily be a class property/attribute


    def get_guess(self):
        user_guess_input = None
        while not user_guess_input:
            user_guess_input = input("\nInput Guess: What letter would you like to guess next? >>> ")
        return user_guess_input
        # line 81 & 82 might not be required


    def constrain_guess(self):
        user_guess_input = self.get_guess()
        while (user_guess_input not in string.ascii_letters) or (user_guess_input in self.guesses):
            print(f"\nSorry, '{user_guess_input}' isn't a valid option.")
            print(f"Please input a letter (a - z) that you haven't already guessed.\n")
            user_guess_input = self.get_guess()
        return user_guess_input


    def convert_guess_to_both_cases(self):
        user_guess = self.constrain_guess()
        user_guess_uppercase = user_guess.upper()
        user_guess_lowercase = user_guess.lower()
        return user_guess_uppercase, user_guess_lowercase
        # this function would not be required if you update check_phrase method


    def get_random_congratulatory_message(self):
        self.pointer = random.randint(0, 3)
        self.selected_congratulatory_message = self.congratulatory_messages[self.pointer]
        return self.selected_congratulatory_message
        # pointer and selected_congratulatory_message might not necessarily be a class property/attribute


    def get_random_encouraging_messages(self):
        self.pointer = random.randint(0, 3)
        self.selected_encouraging_messages = self.encouraging_messages[self.pointer]
        return self.selected_encouraging_messages
        # pointer and selected_encouraging_messages might not necessarily be a class property/attribute

    def handle_guess(self, user_guess_uppercase, user_guess_lowercase):
        value1 = self.active_phrase.check_phrase(user_guess_uppercase)
        value2 = self.active_phrase.check_phrase(user_guess_lowercase)
        print("Result:", end=" ")

        if value1 == 1 or value2 == 1:
            congratulatory_message = self.get_random_congratulatory_message()
            print(f"{congratulatory_message}", end=" ")
            print("Your guess is correct!\n")
    
        elif value1 == 0 and value2 == 0:
            encouraging_message = self.get_random_encouraging_messages()
            print(f"{encouraging_message}", end=" ")
            print("Your guess is incorrect.\n")
            self.missed += 1
        # if...else... would be fine here
        # but I guess, if you change check_phrase method
        # you would not require check value1/value2

        self.guess_count += 1

    # print(trial_game_instance.active_phrase.phrase)

    # def print_phrase(phrase_object):
        # print(f"The phrase is: {phrase_object}")

    def game_over(self):

        
        if self.missed == 5:
            print("\n\n--------------  Unfortunately... YOU LOSE! -------------- ")
            print("... because you've made 5 incorrect guesses.\n")
            print(f"You've managed to complete this much of the phrase:")
            self.active_phrase.display(self.guesses)

        else:
            print("\n\n-------------- YOU WIN! --------------")
            print(f"You've completed the phrase: \n")
            self.active_phrase.display(self.guesses)
        # extract the message as variable
        # self.active_phrase.display(self.guesses) can be extracted out from if...else...
        # put it after if...else... will be fine