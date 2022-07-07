import random

def Number_guess(x):
        random_number = random.randint(1, x)
        Number_guess = 0
        while Number_guess != random_number:
            Number_guess = int(input(f"Guess a Number Between 1 to {x}:"))
            if Number_guess < random_number:
                print("Sorry too low, Please try again")
            elif Number_guess > random_number:
                print("Sorry too High, Please try again")
        print("Congration!! You have Guessed the correct Number")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            Number_guess = random.randint(low, high)
        else:
            Number_guess = low
        feedback = input(f"Is Your Number is {Number_guess}, Too High (H)< Too Low (L) or correctlly (C):").lower()
        if feedback == 'h':
            high = Number_guess - 1
        if feedback == 'l':
            low = Number_guess + 1
    print(f"Congrats!!!, You guessed My Number {Number_guess}!!!")

computer_guess(10)

