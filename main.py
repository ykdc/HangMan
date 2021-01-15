import words
import random

from words import word_list

def get_word():
  word = random.choice(word_list)
  # convert word to uppercase
  return word.upper()

def play(word):
  # create word w/underscores w/length of word to guess
  word_completion = "_" * len(word)
  guessed = False
  guessed_letters = []
  guessed_words = []
  tries = 6
  
  print("Let's play Hangman!")
  # image of hangman at current try
  print(display_hangman(tries))
  print(word_completion)
  print("The word is ", len(word), "letters long.")
  print("\n")

  while not guessed and tries > 0:
    guess = input("Guess a letter or word: ").upper()
    # guess is a letter
    if len(guess) == 1 and guess.isalpha():
      if guess in guessed_letters:
       print("You already guessed the letter " + guess)
      elif guess not in word:
        print("Sorry, " + guess + " is not in the word.")
        tries -= 1
        guessed_letters.append(guess)
      else:
        print("Good job! " + guess + " is in the word.")
        guessed_letters.append(guess)
        # convert word_completeion from string to list so can index into it
        word_as_list = list(word_completion)
        # find all indices where guess appears in word; call enumerate on word to get index i & letter at index at each iteration,  append i to list if letter = guess
        indices = [i for i, letter in enumerate(word) if letter == guess]
        # replace underscore w/guess to show correctly guessed letters
        for index in indices:
          word_as_list[index] = guess
        # convert back to string
        word_completion = "".join(word_as_list)
        # check if guess completes word - if no underscore then all letters guessed
        if "_" not in word_completion:
          guessed = True
    # check if word already guessed is correct or not
    elif len(guess) == len(word) and guess.isalpha():
      if guess in guessed_words:
        print("You already guessed the word "+ guess)
      elif guess != word:
        print("Sorry! " + guess + " is not in the word.")
        tries -= 1
        guessed_words.append(guessed_words)
      else:
        guessed = True
        word_completion = word
    else:
      print("Not a valid guess.")
    
    print(display_hangman(tries))
    print(word_completion)
    print("Already guessed letters: ", guessed_letters)
    print("\n")
     
  if guessed:
    print("Great! You guessed the word!")
  else:
    print("Sorry, you ran out of tries. The word was " + word)


def display_hangman(tries):
  stages = [
       """
       ---------
       |        |
       |        O
       |       \|/
       |        |
       |       / \\
       -
       """,
       """
       ---------
       |        |
       |        O
       |       \|/
       |        |
       |       /
       -
       """,
       """
       ---------
       |        |
       |        O
       |       \|/
       |        |
       |
       -
       """,
       """
       ---------
       |        |
       |        O
       |       \|
       |        |
       |
       -
       """,
       """
       ---------
       |        |
       |        O
       |        |
       |        |
       |
       -
       """,
       """
       ---------
       |        |
       |        O
       |
       |
       |
       -
       """,
       """
       ---------
       |        |
       |        
       |
       |
       |
       -
       """
  ]
  return stages[tries]
 

def main():
  word = get_word()
  play(word)
  while input("Would you like to play again? [Y/N] ").upper() == "Y":
    word = get_word()
    play(word)

main()
