import random

class NoAnswerError(Exception):
    pass
class WrongAnswerError(Exception):
    pass

def main():
    done = False
    while not done:
        try:
            food = input("What is your favorite food: ")
            if(not food):
                raise NoAnswerError()
            if(food != "Whiskey"):
                raise WrongAnswerError()
        except NoAnswerError as err:
            print("Please enter something")
        except WrongAnswerError as err:
            print("Wrong, the correct answer is Whiskey")
            done = True
        else:
            print("Correct answer!")

main()
