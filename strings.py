x="banana"
print(x[1])
y=len(x)
print(y)
index=0
count=0

#Using while loop
while index < y:
    print(index,x[index])
    index=index+1

#Usinng for Loop
for letter in x:
    print(letter)

#Looping and counting
for letter in x:
    if letter=='a':
        count=count+1
print(count)
