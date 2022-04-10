list1 = ['a','b','c','d','e','f']
list2 = ['d','e','f','g','h']
b=[]
c=[]

for x in list1:
    if x not in list2:
        b.append(x)
for y in list2:   
    if y not in list1:
        c.append(y)
                
print("missing value",b)
print("adding value",c)

