man=dict()
man['money']=21
man[22]=25
man['choco']=28
print(man)

ma1={}
ma1
print(ma1)


counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    counts[name] = counts.get(name, 0) + 1
    print(counts[name])
print(counts)
