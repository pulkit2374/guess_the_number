import random
num = random.randint(1, 100)

print("I'm guessing a number between 1  to 100, can you help me guessing it???")
ans = input("yes/no: ")
if ans.lower() == 'yes':
    print("Great!!! Let's guess the number")
    while True:
        guess = int(input("make a guess between 1 and 100: "))
    
        if guess == num:
            print("Hurray, you have guessed it right")
            break
        elif guess > num:
            print("Too High, try again!")
        else:
            print("Too Low, try again!")


else:
    print("No worries, Enjoy your day!")
