''' a Python script to print distinct 
    elements along with their frequencies 
    ofoccurrence in the list.'''



list1=['A','A','B','C','C','D','D','a','B']
frequency={}
for item in list1:
    if item in frequency:
        frequency[item]+=1
    else:
        frequency[item]=1
print(frequency)













    