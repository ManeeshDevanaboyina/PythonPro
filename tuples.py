s=open('new_file.txt')
counts=dict()
for line in s:
    line.rstrip()
    words=line.split()
    for word in words:
         counts[word]=counts.get(word,0)+1
         print(counts)
