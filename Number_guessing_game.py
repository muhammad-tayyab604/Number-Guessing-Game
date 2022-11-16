import random
top_of_range=input("Type a NUMBER (Note this shows the limit. This guessing game will never exceed the number you type):\n")

if top_of_range.isdigit():
    top_of_range=int(top_of_range)

    if top_of_range<=0:
        print("Please type larger number")
        quit()

else:
    print("Type a number next time!")
    quit()

random_number=random.randint(0,top_of_range)

guesses=0

while True:
    guesses+=1

    user_guess=input("Guess a number:\n")

    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("Type a number next time!")
        continue
    if user_guess<=0:
        print("Please type larger number")
        continue

    if user_guess==random_number:
        print("Congratualtions! You Win")
        break

    elif user_guess > random_number:
        print("You are above the number")
    else:
        print("You are below the number")

print(f"you done this in {guesses} guesses")