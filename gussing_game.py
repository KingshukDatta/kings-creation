# Guessing the number.

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess your number: "))
    guess_count += 1
    if guess == secret_number:
        print("Hurray!!! You won the game.🤩")
        break
else:
    print("Sorry, you lost. 🥲")
