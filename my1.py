# Угадай число/Guess the number
import random


print("\tWelcome to guess the number game!")
print("\nI guessed a natural number from the range from 1 to 100.")
print("Try to guess it in the minimum number of attempts.\n")
the_number = random.randint(1, 100)
guess = int(input("Your guess: "))
tries = 0
while guess != the_number:
    if guess > the_number:
        print("Less...")
    else:
        print("More...")
    guess = int(input("Your guess: "))
    tries += 1
print("You managed to guess the number! It's really", the_number)
print("You spent only", tries, "attempts to guess!\n")
input("\n\nPress Enter to exit.")
