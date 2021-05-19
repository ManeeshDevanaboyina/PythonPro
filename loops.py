i=0
count=0
print('before', i)
for man in [10,20,50,100]:
    count=count+1
    i=man+i
    print(i,man)
print('After',i/count)
