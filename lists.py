friends=['Maneesh','Alex','Katraj']
print(range(len(friends)))

for i in range(len(friends)):
    new_friend= friends[i]
    print('Happy New Year:',new_friend)

    # Concatinating lisits using +

a= [1,2,3]
b=[4,5,6]
c=a+b
print(c)

# Lists can be sliced

a=[1,2,3,4,5]
print(a[1:3])

#Adding numbers into lists and taking sum and average using builtin functions.

values=list()

while True:
    list_values=input('Enter the Values:')
    if list_values=='done': break
    float_no=float(list_values)
    values.append(float_no)

average= sum(values)/len(values)
print(sum(values),'Average:',average)
