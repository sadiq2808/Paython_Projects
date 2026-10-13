import random

attempts=5

def display_rules():
    print("welcome to Number Guessing Game of Sadiq Alawi!\n")
    print("IHave selected a number between 1 and 10.")
    print("You have 10 attempts to guess it.\n")


def play_game(number, attempt=1):
    if attempt> attempts:
        print("\nGame Over!")
        print("The correct number was:", number)
        return
    
    guess = input(f"Attempt{attempt}/10 - Enter Your Guess:")

    try:
        guess= int(guess)
    except ValueError:
        print("Plase Enter a Valid Number.\n")
        return play_game(number, attempt)


    if guess<1 or guess>10:
        print("Plaese enter a number between 1 to 150.\n")
        return play_game(number,attempt)
    

    check_guess=lambda x,y: "correct" if x==y else(
    
        "low" if x<y else "high"
    )
    result = check_guess(guess, number)

    if result=="correct":
        print("\nCongratulation! you guessed the correct number!")
        print("You guessed it in", attempt,"attempts(s).")
        return
    
    if result =="low":
        print("Too Low! Try a higher number.\n")
    else:
        print("Too High! Try a Lower number.\n")
    play_game(number, attempt+1)

display_rules()

random_number=random.randint(1,10)

play_game(random_number)
    
    