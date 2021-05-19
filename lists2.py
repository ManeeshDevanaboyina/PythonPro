# Using split function to change the strings to Lists
fhand = open('new_file2.txt')

for line in fhand:
        line = line.rstrip()
        if not line.startswith('From ') : continue
        words = line.split()
        print(words[2])
