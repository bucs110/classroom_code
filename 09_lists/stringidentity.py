

def main():
    strA1 = list("Hello")
    strA2 = list("Hello")
    strB1 = "Goodbye"
    strB2 = "Goodbye"

    print(id(strA1), id(strA2))
    print(id(strB1), id(strB2))

main()
