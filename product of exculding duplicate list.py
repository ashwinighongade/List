# List product excluding duplicates.
list = [6,1,3,5,6,3,1]
# Output: 90
new=[]
i=0
while i<len(list):
    if list[i] not in new:
        new.append(list[i])
    i+=1
print(new)
i=0
product=1
while i<len(new):
    b=new[i]
    product=product*b
    i=i+1
print(product)
    

