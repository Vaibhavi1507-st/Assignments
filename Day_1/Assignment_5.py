import random

number = random.randint(1, 50)
chances = 5

while chances > 0:
    guess = int(input("Enter your guess number: "))

    if guess == number:
        print("Right answer")
        break
    elif guess < number:
        print("Too low")
    else:
        print("Too high")

    chances = chances - 1

    if chances > 0:
        print("Chances left are:", chances)
    else:
        print("You ran out of chances. The number was:", number)
