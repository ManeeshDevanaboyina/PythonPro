def string(x):
    k=len(x)
    if k<3:
        return x
    elif x[-3:]=="ing":
        return x + "ly"
    else:
        return x + "ing"

x=input("Enter the value of the String")
print(string(x))
