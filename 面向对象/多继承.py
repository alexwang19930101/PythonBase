class BaseA(object):
    def test(self):
        print("a")

class BaseB(object):
    def test(self):
        print("b")
    def test1(self):
        print("b")

class Child(BaseB,BaseA):
    def test1(self):
        print("c")
    pass

child = Child()
child.test()
child.test1()
print(Child.__mro__)