# Word Jumble/Анаграммы
import random

WORDS = "anagram simple complex answer long question".split()
word = random.choice(WORDS)
correct = word
jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]
print(
    """
            Welcome to the game 'Anagram!'
        It is necessary to rearrange the letter so that there is a meaningful word.
        (To exit the game, press Enter without entering your version.)
    """
)
print(f"My anagramma: {jumble}")
guess = input("\nTry to guess the source word: ")
while guess != correct and guess != "":
    print("Unfortunately, you are wrong.")
    guess = input("\nTry to guess the source word: ")
if guess == correct:
    print("Yes exactly! You guess!\n")
    print("Thanks for playing)")
