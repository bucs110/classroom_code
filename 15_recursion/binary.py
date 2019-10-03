
def binary(slist, num):
    mid = len(slist) // 2
    if(not slist):
        return None
    elif(slist[mid] == num):
        return num
    elif(slist[mid] > num):
        return binary(slist[:mid], num)
    else:
        return binary(slist[mid+1:], num)

def main():
    l = [1,2,3,4,5,6,7,8,9]
    print(binary(l, 3))
    print(binary(l, 2))
    print(binary(l, 6))
    print(binary(l, 9))
    print(binary(l, 10))
    print(binary(l, -1))
main()
