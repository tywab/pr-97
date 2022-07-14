from mimetypes import guess_all_extensions
import numbers
import random
number=random.randint(1, 9)
chance=0

print("Number guessing game")
while chance<5:
    guess=int(input("Guess the number between 1-9: "))
    if guess == number:
        print('Congratulation! YOU WON!')
        break
    if not chance<5:
        print('YOU LOSE!')
    chance=chance+1