
def main():
    nums = ""
    for i in range(1,1000):
        nums += str(i) + ", "
    nums += "1000"
    print(nums)
    b = "Binghamton"
    print(b[:3])
    print(b[4:6]+b[-3])
    print(b[:2]+b[-3]+b[1:4])
    results = 'average:  0.8475'
    results = float(results[results.find(':')+1:].strip())

main()
