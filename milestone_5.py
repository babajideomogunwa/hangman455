import random

class Hangman():
    """A class to represent the Hangman game."""
    def __init__ (self, word_list, num_lives = 5):
        """Initialize the Hangman game with a word list and number of lives.
        
        Args:
            word_list (list): List of words to choose from.
            num_lives (int): Number of lives. Defaults to 5.
        """
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_lives = num_lives
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        """Check if the guessed letter is in the word.
        
        Args:
            guess (str): The letter guessed by the player.
        """
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
        print("Current word progress: ", " ".join(self.word_guessed))
                                                  
    def ask_for_input(self):
        """Prompts the player for input and validates the guess."""
        while True:
            guess = input("Guess a letter: ").lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

def play_game(word_list):
    """Starts the Hangman game session.
    
    Args:
        word_list (list): List of words to choose from for the game.
    """
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break   
play_game(word_list = ["mango", "orange", "lemon", "pear", "plum"])
    



                



 

