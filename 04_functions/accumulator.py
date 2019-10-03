def square(x):
    runningtotal = 0
    for counter in range(x):
        runningtotal = runningtotal + x
        print(runningtotal)
    return runningtotal

def main():
    toSquare = 10
    squareResult = square(toSquare)
    print("The result of", toSquare, "squared is", squareResult)
main()
