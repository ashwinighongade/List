list1=[12,54,78,43,98,3,54,9,34]
min=list1[0]
i=0
while i<len(list1):
    if min>list1[i]:
        min=list1[i]
    i+=1
print(min)
min1=list1[1]
i=0
while i<len(list1):
    if min1>list1[i]:
        if list1[i]!=min:
            min1=list1[i]
    i+=1
print(min1)
                