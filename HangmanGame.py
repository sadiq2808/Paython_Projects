import random

words=["apple","banana","orange","mango",
"grape","watermelon","strawberry","pineapple","peach","cherry","lemon","coconut"]

word=random.choice(words)
guessed=[]
wrong_guesses=0
max_attempts=6

hangman=[
    """
     -----
     |   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
    =========
    """
]

print("Welcome to sadiq Hangman Game!")
print("Hint : The word is a fruit.")

while wrong_guesses<max_attempts:
    display=" "

    for letter in word:
        if letter in guessed:
            display +=letter + " "
        else:
            display +="_"
            
    print(hangman[wrong_guesses])
    print("Word:", display)

    if "_" not in display:
        print("Congratuations ! You Won!")
        print("The Word was:",word)
        break

    guess = input("Guess a letter:").lower()

    if len(guess)!=1 or not guess.isalpha():
        print("Please enter one letter.")
        continue
    
    if guess in guessed:
        print("You already guessed that letter.")
        continue
    guessed.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses +=1
        print("Wrong guess!")
else:
    print(hangman[wrong_guesses -1])
    print("Game Over!")
    print("The word was:",word)
