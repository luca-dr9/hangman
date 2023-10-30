import random

class Hangman:
    """
    This class is ued to represent the hangman game.

    Attributes:
        word (str): random word from word_list
        word_list (list): list of different words/strings
        num_lives (int): number of lives left in hangman
        num_letters (int): number of letters left to guess
        word_guessed (list): the word but seperated by each letter, start off with all '_' then adds the letter when guessed
        list_of_guesses (list): list every letter guessed in order of when guessed
    """
    def __init__(self, word_list, num_lives=5):
        """
        See help(Hangman) for accurate signature.
        """
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for i in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def __check_guess(self, guess): # __, so can't be called outside of class
        """
        This function is used to check if the guesses letter is in the word.
        It is a private function so can only be called inside the class.
        If guess in word: puts letters into word_guessed and lowers num_letters by 1
        If wrong, lowers num_lives by 1

        Args:
            guess (str): inputted letter by user to guess the word
        """
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            indices = [i for i, x in enumerate(self.word) if x == guess]
            for i in indices:   # changes mutiple occurances of same letter
                self.word_guessed[i] = guess
            self.num_letters -= 1
        else:
            print(f"Sorry, {guess} is not in the word. Try again. \nYou lose 1 life!")
            self.num_lives -= 1

    def ask_for_input(self):
        """
        This function is used to ask user for a letter to guess to word.
        It makes sure it is a single alphabetical character.
        Appends guess into list_of_guesses
        """
        print(self.word_guessed)
        print(f"Letters guessed: {self.list_of_guesses}")
        print(f"Lives left: {self.num_lives}")
        guess = input("Make a guess: ")
        guess = guess.lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif guess in self.list_of_guesses:
            print("You already tried that letter!")
        else:
            self.__check_guess(guess)
            self.list_of_guesses.append(guess)
            
def play_game(word_list):
    """
    This function is used to start the hangman game.

    Args:
        word_list (list): list of different words/strings
    """
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print(f"You lost! \nThe word was: {game.word}")
            break
        if game.num_letters > 0:
            game.ask_for_input()
        if game.num_lives != 0 and game.num_letters <= 0:
            print(f"Congradulations. You won the game! \nThe word was: {game.word}")
            break

word_list = ["apple","pear","orange","banana","mango"]
play_game(word_list)
