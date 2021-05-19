def Largest_Elements(list,N):
    i=0
    list2=[]
    for j in list:
        if int(j)>int(i):
            i=j
    list2.append(i)
    list.remove(i)
    return list2

list=list()
K=input("How many values you are entering")
count=0
while count<=int(K):
    a=input("Insert the value into the list")
    list.append(a)
    count=count+1
N=int(input("Enter the value of N"))
list2=[]
for n in range(0,N):
    list2.append(Largest_Elements(list,N))
print(list2)
