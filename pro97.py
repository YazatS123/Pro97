import random
number = random.randint(1, 10)
tries = 0
guess = 0
while tries < 5 or guess == number:
    guess = int(input("Guess a number between 1 and 10. "))
    if guess > number:
        print("No! " + str(guess) + " is too big! " + str(4 - tries) + " more tries to go!")
    elif guess < number:
        print("Nope! " + str(guess) + " is not big enough! " + str(4 - tries) + " more tries to go!")
    elif guess == number:
        print("Good job! You got it right in " + str(tries + 1) + " tries!")
        break
    tries = tries + 1
if guess != number:
    print("You lose! The number was " + str(number) + ". You'll get it next time!")