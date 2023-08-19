import random

hangman_stages = [

"""

""",
""" 
        
        
        
        
        
         _____ 
""",
"""
        |
        |
        |
        |
        |
        |_____ 
""",
"""
         _____
        |
        |
        |
        |
        |
        |_____ 
""",
"""
         _____
        |     |
        |
        |
        |
        |
        |_____ 
""",
"""
         _____
        |     |
        |     0
        |
        |
        |
        |_____ 
""",
"""
         _____
        |     |
        |     0
        |    /
        |
        |
        |_____ 
""",
"""
         _____
        |     |
        |     0
        |    /|
        |
        |
        |_____ 
""",
"""
         _____
        |     |
        |     0
        |    /|\\
        |
        |
        |_____
""",
"""
         _____
        |     |
        |     0
        |    /|\\
        |    / 
        |
        |_____
""",
"""
         _____
        |     |
        |     0
        |    /|\\
        |    / \\
        |
        |_____
"""
]

word_list = ["giraffe", "panda", "bear", "cat", "dog", "horse"]
chosen_word = random.choice(word_list)
guessed_letters = []
MAX_ATTEMPT = 11
incorrect_attempt = 0
diplayed_word = ["_" for _ in chosen_word]

def display_game():
    print(hangman_stages[incorrect_attempt])
    print("Hangman:", incorrect_attempt)
    print("Current word:", " ".join(diplayed_word))
    print("Incorrect guesses:", ", ".join(g for g in guessed_letters if g not in chosen_word))

def get_guess():
    """
    kossher
    """
    guess = input("Guess a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        return None
    if guess in guessed_letters:
        print("You've already guessed that letter.")
        return None
    return guess

while incorrect_attempt < MAX_ATTEMPT:
    display_game()
    guess = get_guess()

    if guess:
        guessed_letters.append(guess)
        if guess in chosen_word:
            print("Good guess!")
            for i, letter in enumerate(chosen_word):
                if letter == guess:
                    diplayed_word[i] = letter
        else:
            print("Incorrect guess.")
            incorrect_attempt += 1

        if all(letter != "_" for letter in diplayed_word):
            print("Congrats, you've guessed the word:", chosen_word)
            break

if incorrect_attempt == MAX_ATTEMPT:
    print("Sorry, you've run out of tries. The answer was:", chosen_word)
