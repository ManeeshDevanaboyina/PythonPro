def list_mul(items):
    value=1
    for x in items:
        value=value*x
    return value


list=list()
while True:
    x=input("Enter the values for list:")
    if x==str("done"):
        break
    else:
            list.append(int(x))
print(list_mul(list))
