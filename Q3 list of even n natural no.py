'''  a Python script to create a list of 
     first N even natural numbers. '''
 
i=2
n=int(input("Enter number : "))
list1=[]
while i<=2*n:
    list1.append(i)
    i+=2
print(list1)

