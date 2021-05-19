#Entering the inputs and adding,count,average & if we give characters in between error occurs

count=0
value=0
while True:
    m=input("Enter the value of number ")
    if m=='done':
        break
    try:
        num=float(m)
    except:
        print("Invalid number")
        continue
    value=value+num
    count=count+1
print(count,value,value/count)
