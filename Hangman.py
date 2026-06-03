import random
import time
import os

class InvalidInputError(Exception):
    pass

class WrongInput(Exception):
    pass

class Win(Exception):
    pass

class Loose(Exception):
    pass

class AlreadyGuessed(Exception):
    pass

class ChoosenWord():
    def __init__(self, word):
        self.word = word
        self.state = ["_" for char in word]
        self.wrong_guess = []
        self.lives = 6

    def printself(self):
        print(*self.state)

    def guess(self, letter):
        letter = letter.lower()
        if letter not in alphabet or len(letter) != 1:
            raise InvalidInputError
        
        if letter.upper() in self.state or letter in self.wrong_guess:
            raise AlreadyGuessed
        
        if letter not in self.word:
            self.wrong_guess.append(letter)
            self.lives -= 1
            if self.lives == 0:
                raise Loose
            raise WrongInput
        
        for index, char in enumerate(self.word):
            if letter == char:
                self.state[index] = letter.capitalize()
        
        if any(thingy == "_" for thingy in self.state):
            pass
        else:
            raise Win
        
    def reset(self):
        self.word = random.choice(hangman_words)
        self.state = ["_" for word in self.word]
        self.lives = 6
        self.wrong_guess = []

        


hangman_words = [
    "supercalifragilisticexpialidocious", 
    "pneumonoultramicroscopicsilicovolcanoconiosis",
    
    "blizzard", "mystique", "paradoxe", "quadrant", "sapphire",
    "gargoyle", "jugglerx", "vanguard", "infinity", "phantoms",
    "mischief", "corridor", "absolute", "badgered", "bimonthly",
    "catapult", "daydream", "eccentric", "flamingo", "glitchy",
    "gossamer", "hologram", "illusion", "jeopardy", "knapsack",
    "luminous", "marathon", "nocturnal", "oblivion", "perplexo",
    "quizzing", "ramshack", "scavenge", "suburban", "tentacle",
    "umbrella", "velocity", "whiplash", "xenolith", "zeppelin"
]

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

chosen_word = ChoosenWord(random.choice(hangman_words))

while True:
    os.system("cls")
    print(f"Lives: {chosen_word.lives}")
    print(f"Wrong Guesses: {chosen_word.wrong_guess}")
    print("Word:")
    chosen_word.printself()

    print("")
    user_input = input("Input a letter: ")
    try:
        chosen_word.guess(user_input)
    
    except InvalidInputError:
        print("Invalid Input!")
        time.sleep(0.7)
        continue

    except WrongInput:
        print("Guess again")
        time.sleep(0.7)

    except Win:
        os.system("cls")
        time.sleep(0.5)
        print(f"The word was: {chosen_word.word.upper()}")
        time.sleep(0.5)
        print("You Win!")
        input("'ENTER' to restart")
        chosen_word.reset()
        continue

    except Loose:
        os.system("cls")
        time.sleep(0.5)
        print(f"The word was: {chosen_word.word.upper()}")
        time.sleep(0.5)
        print("You Loose...")
        input("'ENTER' to restart")
        chosen_word.reset()
        continue
    
    except AlreadyGuessed:
        print("Already Guessed!")
        time.sleep(0.75)
        continue
