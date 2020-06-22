#
# #Accumulator Pattern
# accumulator = starting_value
# for i in list:
#     #code
#     accumulator = accumulator + increment
#     #code

def square(x):
    #docstrings
    '''
        this function squares stuff
        args: (int) to be squared
        return: (int)
    '''
    runningtotal = 0
    for counter in range(x):
        runningtotal = runningtotal + x
    return runningtotal

def main(): #driver
    to_square = 10
    result = square(to_square)
    print(result)
main()
