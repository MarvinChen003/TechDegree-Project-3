
class Phrase():

    def __init__(self, phrase):
        self.phrase = phrase

    def display(self, guesses): 
        for letter in self.phrase:
            if letter == " ":
                print(" ", end=" ")
            else:
                matches_guess = False
                for guess in guesses:
                    if guess == letter:
                        print(f"{letter}", end=" ")
                        matches_guess = True
                if matches_guess == False:
                    print("_", end=" ")
                # matches_guess might not necessary here
                # if guess == letter:
                #    print(f"{letter}", end=" ")
                # else：
                #    print("_", end=" ")

    def check_phrase(self, guess):
        value = 0
        if guess in self.phrase:
            value += 1
        return value
        # From the code it looks like a counter, but it is kind of a boolean
        # if guess in lower(self.phrase):
        #       return True
        # might be enough

    def check_complete(self, guesses):
            check_complete_value = True
            for letter in self.phrase:
                if letter not in guesses:
                    check_complete_value = False
            return check_complete_value

        # line 28 -32, indent
        # might change to something like following:
        # ===
        # for letter in self.phrase:
        #   if letter not in guesses:
        #       return False
        # return True