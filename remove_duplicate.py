# Write a Python program to remove duplicates from a list.
list=[12,8,11,15,12,5,23,12,11,8,11,2,8,9,3]

b=[]
i=0
while i<len(list):
    j=0
    c=0
    while j<len(list):
        if list[i]==list[j] and i!=j:
            c+=1
        j+=1
    if c>1:
        if list[i] not in b:
            b.append(list[i])
    i+=1
print(b)

 