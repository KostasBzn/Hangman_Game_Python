import random

def hangman():
    words = ["python", "chair", "programming", "berlin", "laptop", "bootcamp", "winter"]
    random_word_to_guess = random.choice(words)
    guessed_letters = []
    attempts = 6
    print("Welcome to Hangman!")
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

       if guessed_letter not in random_word_to_guess:
           attempts -= 1
           print(f"Sorry, the letter {guessed_letter} is not in the word")
           print(f"You have {attempts} attempts left.")
       
       if guessed_letter in random_word_to_guess:
           print(f"Good job! The letter {guessed_letter} is in the word")

       if attempts == 0:
           print(f"Sorry you have run out of attempts :(")
           print(f"The word was {random_word_to_guess}")
           restart = input("Press 'Enter' to restart ot type 'exit' to exit the game: ").lower()
           if restart == "exit":
               print("That was fun! Until next time!")
               break
       

       
       


hangman()