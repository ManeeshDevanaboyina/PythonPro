class car:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def milage(self):
        return self.a,self.b


c1=car(85,"BMW")
c2=car(90,"TATA")
print(c1.milage(),c2.milage())
