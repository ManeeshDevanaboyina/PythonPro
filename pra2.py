
#defining an Armstrong no
def Armstrong(n):
    k=len(n)
    j=0
    for i in n:
        i=pow(int(i),k)
        j=j+i
    if j==int(n):
        print("Armstrong no")
    else:
        print("Not")

#Entering the input
n=input("Enter the input");
Armstrong(n);
