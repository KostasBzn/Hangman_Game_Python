import random

def hangman():
    words = ["python", "hangman", "programming", "development", "challenge", "bootcamp", "winter"]
    random_word_to_guess = random.choice(words)
    guessed_letters = []
    attempts = 6
    print("Welcome to hangman!")
    print("Try to guess the word..you have 6 wrong attempts!")
    while attempts > 0:
       guessed_letter = input("Please guess a letter:").lower()
       
       if not guessed_letter.isalpha() or len(guessed_letter) != 1:
            print("Please type a valid alphabetic character.")
            continue
       if guessed_letter in guessed_letters:
           print(f"You have already guessed the letter {guessed_letter}")
           continue
       guessed_letters.append(guessed_letter)

hangman()