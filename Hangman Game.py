import random
import string
from words import words

Life_Points = 6
Win_Points = 0


def get_valid_word(words):
    word = random.choice(words)

    while '_' in word or ' ' in word:
        word = random.choice(words)

    return word


def hangman_game():
    global Life_Points
    global Win_Points
    hidden_word = get_valid_word(words).upper()
    password = ['-'] * len(hidden_word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    # I don't think you need Win_Points, when you can just check to see if 
    # you've lost, of if you have no more hidden letters
    Win_Points = sum(1 for char in hidden_word if char != ' ')

    # while Win_Points > 0 and Life_Points > 0: # You can use this
    while "-" in password and Life_Points > 0:  # or this
        print("You have", Life_Points, "Life Points and you have used these letters:", ''.join(used_letters))
        print(''.join(password))

        guess_letter = input("Guess a letter: ").upper()

        if guess_letter in alphabet - used_letters:
            used_letters.add(guess_letter) # Good so far

            if guess_letter not in set(hidden_word):
                Life_Points -= 1
                print("This letter is incorrect")
            else:
                Win_Points -= 1
                
                for i in range(len(hidden_word)):
                    if hidden_word[i] == guess_letter:
                        password[i] = guess_letter
                    if hidden_word[i] == " ":
                        password[i] = " "
        else:
            print("You've already guessed this letter or it's not a valid letter.")

        print(f"Life_Points:\t{Life_Points}")
        print(f"Win_Points:\t{Win_Points}")
    if Life_Points <= 0:
        print("You've run out of Life Points. Game Over.")
        print("The correct answer was", hidden_word)

    # elif Win_Points == 0: # You can use this
    else:                   # or this
        print("Congratulations! You've guessed the word:", hidden_word)


hangman_game()


