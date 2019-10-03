
class TempClass:
    a = 1
    def __init__(self, num):
        self.instance_var = num

def main():
    obj1 = TempClass(1)
    print(type(obj1.__dict__))
    print(obj1.instance_var, obj1.__dict__)

    obj2 = TempClass(2)
    print(obj2.instance_var, obj2.__dict__)

    obj2.__dict__ = {k:v for k,v in obj1.__dict__.items()}
    obj1.instance_var = 10
    print("Object 1: ", obj1.instance_var, obj1.__dict__)
    print("Object 2: ", obj2.instance_var, obj2.__dict__)

main()
