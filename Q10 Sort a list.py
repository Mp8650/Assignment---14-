'''a python script to sort a list. '''

city_list=[]
i=int(input("How many city you to print: \n"))
while i:
   city_list.append(str(input("Enter a city name :\n")))
   
   i-=1
print("List in sorted form: ",sorted(city_list))
print()












