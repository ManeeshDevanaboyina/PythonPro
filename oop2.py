class Geek:
    #def __init__(self, age):
         #self._age = age
         #print(self._age)

    # getter method
    def get_age(self):
        return self.age

    # setter method
    def set_age(self, x):
        self.age = x

raj = Geek()



# setting the age using setter
raj.set_age(21)

# retrieving age using getter
print(raj.get_age())

print(raj.age)
