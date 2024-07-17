import random

correct = False

random_number = random.randint(-1000, 1000)
print(str(random_number))

while(not correct):
    guess = input("\nEnter a guess: ")
    # Checking for low guess
    if(int(random_number) - int(guess)>15):
        print("Your guess is too low")
    elif(int(random_number) - int(guess)<=15 and int(random_number) - int(guess)>=1):
        print("Your guess is low")

    # Checking for high guess
    elif(int(random_number) - int(guess)<-15):
        print("Your guess is too high")
    elif(int(random_number) - int(guess)>=-15 and int(random_number) - int(guess)<=-1):
        print("Your guess is high")

    # Checking for correct guess
    else:
        print("Your guess is correct")
        correct = True