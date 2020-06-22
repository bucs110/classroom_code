import random
def main():
    percentage = random.randrange(1, 100)
    if(percentage >= 90):
        letter = 'A'
    elif(percentage >= 80):
        letter = 'B'
    elif(percentage >= 70):
        letter = 'C'
    elif(percentage >= 60):
        letter = 'D'
    elif(percentage < 60):
        letter = 'F'
    return letter


main()
