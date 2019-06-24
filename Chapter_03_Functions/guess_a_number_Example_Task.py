import random

secret_number = random.randint(1, 20)
print("I'm thinking  of  a number between 1 and 20.")
count = 0

while True:
    user_number = int(input("Please take a guess. \n"))
    count += 1
    if user_number < secret_number:
        print("Your guess is too low.")
    elif user_number > secret_number:
        print("Your guess is too high.")
    else:
        print(f"It is correct! You guessed it in {count} tries")
        break
