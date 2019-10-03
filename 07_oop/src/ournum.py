class OurNum:
    num = 0
    def __init__(self):
        OurNum.num += 1
        print("Nums:", self.num)

def main():
    p = OurNum()
    q = OurNum()
    print("p num:", p.num, "id:", id(p.num))
    print("q num:", q.num, "id:", id(q.num))
    print("OurNum num:", OurNum.num, "id:", id(OurNum.num))
    # p.num += 1
    # print("p num:", p.num, "id:", id(p.num))
    # print("q num:", q.num, "id:", id(q.num))
    # print("OurNum num:", OurNum.num, "id:", id(OurNum.num))
    # q.num += 2
    # print("p num:", p.num, "id:", id(p.num))
    # print("q num:", q.num, "id:", id(q.num))
    # print("OurNum num:", OurNum.num, "id:", id(OurNum.num))

if __name__ == '__main__':
    main()
