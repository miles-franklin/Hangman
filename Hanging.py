import random
import string
from words import words

Life_Points = 6
Win_Points = 0


def get_valid_word(words):
    word = random.choice(words)

    while '_' in word or '' in word:
        word = random.choice(words)

    return word


def hangman_game():
    global Life_Points
    global Win_Points
    # hidden_word = get_valid_word(words)
    hidden_word = input("Input your secret word: ").upper()
    hint = input("give a hint: ")
    password = ['-'] * len(hidden_word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    Win_Points = sum(1 for char in hidden_word if char != ' ')

    while Win_Points > 0 and Life_Points > 0:
        print("You have", Life_Points, "Life Points and you have used these letters:", ''.join(used_letters))
        print(''.join(password))
        print(hint)

        guess_letter = input("Guess a letter: ").upper()
        if guess_letter in alphabet - used_letters:
            used_letters.add(guess_letter)
            for i in range(len(hidden_word)):
                if hidden_word[i] == guess_letter:
                    password[i] = guess_letter
                    if hidden_word[i] != ' ':  # Check if the guessed letter is not a space
                        Win_Points -= 1
            if guess_letter not in hidden_word:
                Life_Points -= 1
                print("This letter is incorrect")
        else:
            print("You've already guessed this letter or it's not a valid letter.")

    if Life_Points <= 0:
        print("You've run out of Life Points. Game Over.")
        print("The correct answer was", ''.join(password))
        print("The correct answer was", hidden_word)

    elif Win_Points == 0:
        print("Congratulations! You've guessed the word:", ''.join(password))


hangman_game()
