str = 'X-DSPAM-Confidence: 0.8475 '

new_str=str.find('X')

another_str=str.find(' ',new_str)

one_more=str.find(' ',another_str+1)

print(one_more)

final_str=str[new_str:one_more]
 
print(final_str)
