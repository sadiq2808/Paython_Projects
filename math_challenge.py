import random

while True:
    num1 = random.randint(1, 1000)
    num2 = random.randint(1, 100)

    operation = random.choice(["+", "-", "*", "/", "%"])

    if operation == "+":
        correct_answer = num1 + num2
    elif operation == "-":
        correct_answer = num1 - num2
    elif operation == "*":
        correct_answer = num1 * num2
    elif operation == "/":
        correct_answer = num1 / num2
    else:
        correct_answer = num1 % num2

    print(f"\n{num1}{operation}{num2}=?")

    try:
        answer = float(input("Enter Your Answer: "))
    except ValueError:
        print("Enter valid number!")
        continue

    if answer == correct_answer:
        print("Well Done! Correct Answer!")
    else:
        print(f"Wrong Answer! The Correct Answer is {correct_answer}")

        again = input("Continue? (y/n): ")

        if again.lower() != "y":
            break