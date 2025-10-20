import random 
import math

target = random.randrange(0, 777)
attempts = 0

while True:
    try:
        num = int(input("Choose a number between 0–777: "))
    except ValueError:
        print("That’s not a number, try again!")
        continue

    if num < 0 or num > 777:
        print("Oops! That number is not valid. Try again!")
        continue

    attempts += 1

    if num == target:
        print("Well done!")
        optimal = math.ceil(math.log2(778))
        print(f"You used {attempts} guesses. Binary search could have done it in {optimal}.")
        break

    elif num > target:
        print("You have to guess smaller!")

    else:
        print("You have to guess bigger!")
