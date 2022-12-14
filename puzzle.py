import random

class Puzzle:
    """The game puzzle . 
    
    The responsibility of Puzzle is to have the guess word and display it 
.
    """
    
    def __init__(self):
        """stes the attribus of the class"""
      self._word = ["banana", "potato", "cheese", "mango"]
      self._selected_word = ""
      self._guess = ""
      
    def guess(self):
        """checks the player guess"""
        self.guess = input("Guess a letter [a-z]: ")
        return self.guess
      
    def check_letter(self):
        """checks to see if letter is in selected word"""
      self._selected_word = random.choice(self._word)      
      letter = list(self._selected_word)
      while not True:
          print ("______")
      else:
          print (letter)
    