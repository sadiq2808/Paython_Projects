import random

name=input("What is your name?")
print("Good Luck!",name)

word=[
    'sadiq','food','computer','programing','python','eat',
    'water','matheatics','player','condition'
]

word=random.choice(word)

print("\n Guess ther Characters")

guesses=''

truns=12

while truns>0:
    failed=0

    for char in word:
        if char in guesses:
            print(char,end=" ")
        else:
            print("_",end=" ")
            failed+=1
    print()

    if failed==0:
        print("You Win")
        print("The word is:", word)
        break
    guess=input("guess a character:").lower()

    if len(guess)!=1:
        print("Please enter a single character.")
        continue
    if guess in guesses:
        print("You already guessed that character.")
        continue

    guesses+=guess

    if guess not in word:
        truns-=1
        print("wrong")
        print("You have,", truns,", more guesses")

    if truns==0:
        print("You lose")
        print("The word was:", word)



        