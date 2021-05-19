a=list()
for i in range(1,5):
    b=input("Enter the values:")
    a.append(b)
print(a)

for j in a:
    if int(j)<0:
        print(j)
