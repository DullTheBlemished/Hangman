# Hangman
most likely will not include any refractors

This is a quick brain-break kind of activity i did during a free period at school, took about 1 hour total. This is a prime example of when NOT to use OOP, but honestly i just needed something in OOP that isnt Stock-I-Guess V3 which as of right now i am struggling to track what i need to add in

code:
uses a ChoosenWord class that reqs a word to be passed in `__init__`, then takes the word and makes a list with `self.state = ["_" for word in self.word]` to manage the state, for win logic, it is simply checking for an instance of `"_"` inside `self.state`, also has another `self.` variable to track wrong guesses
