word='maneesh'

if word < 'banana':
    print('Your word,' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word,' + word + ', comes after banana.')
else:
    print('All right, bananas.')

print('new_word'.upper())





data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
new= data.find('s')
print(new)
new1=data.find(' ',new)
print(new1)
man=data[new:new1]
print(man)
