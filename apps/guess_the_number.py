from random import randint

random_number = randint(1, 20)
secret_number = random_number
print(secret_number)

score = 20

while True:
    try:
        guess = int(input("Enter your guess: "))
        if score < 2:
            print(f"You lost, try another time")
            break
        elif guess > 20:
            print("Your number is not between 1 and 20")
        elif guess < 1:
            print("Your number is not between 1 and 20")
        elif guess > secret_number:
            print("Too high")
            score -= 1
            print(f"You have {score} attempt(s)")
        elif guess == secret_number:
            print("Correct number! Congrats!")
            score -= 1
            print(f"Your score is {score}")
            break
        else:
            print("Too low")
            score -= 1
            print(f"You have {score} attempt(s)")
    except ValueError:
        print("Enter a number from 1 to 20")