def getGrade(percentage):
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

def isPassing(letter):
    return letter in ['A', 'B', 'C']

def main():
    grade = getGrade(95)
    print(isPassing(grade))
    print(isPassing(getGrade(65)))
    print(isPassing(getGrade(110)))
    print(isPassing(getGrade(-1)))

main()
