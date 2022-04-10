list=[12,34,23,16,56,78,98,87,76]
max=0
max1=0
i=0
while i<len(list):
    if max<list[i]:
        max=list[i]
    if max1<list[i]:
        if list[i]!=max:
            max1=list[i]
    i+=1
print(max1)
    