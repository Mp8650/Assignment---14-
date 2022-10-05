'''  Write a Python script to remove all non
     int values from a list..'''


items = ['1','Bareilly','2','Bhopal','3','4','Delhi','Agra','5']
new_items=[]
for item in items:
     if not item.isdigit():
          new_items.append(item)


print (new_items)



    