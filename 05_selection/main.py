import random

def main():
    num = random.randrange(1,11)
    for i in range(3):
        guess = int(input("Input a number (1-10)"))
        if(guess == num):
            print("correct")
        elif(guess < num):
            print("too low")
        else:
            print("too high")
    print("done")

main()
