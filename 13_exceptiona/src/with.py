import random


def main():
    try:
        fptr = open("myfile.txt", 'w')
        #some code that causes an exception
    except:
        print("there was an error")
    finally:
        print("finally")
        fptr.close()

    with open("myfile.txt", 'r') as fptr:
        print("in myfile with")

    with open("no.txt", 'r') as fptr:
        print("in no file with")
    print("complete")
main()
