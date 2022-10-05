'''  a Python script to create a list of 
     first N natural numbers. '''
 
list_n_natural=[]  
N_natural=int(input("How many numbers you want to print :\n"))
for i in range(1,N_natural+1):
    list_n_natural.append(i)
print(list_n_natural)


