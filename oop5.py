class car:
    def __init__(self):
        self.mil=10
        self.rpm=1000

    def compare(self,other):
        if self.mil==other.mil:
            return True
        else:
            return False
c1=car()
c1.mil=20
c2=car()

#evry object should undergo through init method and there the values for the objects will be assigned

if c1.compare(c2):
    print("They are same")
else:
    print("different")
