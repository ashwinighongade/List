#  Write a Python program to get the frequency of the elements in a list.
# List :  [10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]
# Frequency of the elements in the List :  Counter(10: 4, 20: 4, 40: 2, 50: 2, 30: 1)
b=[10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30]
a=[]
d=[]
i=0
while i<len(b):
    j=0
    count=0
    # d=[]
    while j<len(b):
        if b[i] in b:
            if b[i]==b[j]:
                count+=1
        j+=1
    print(b[i],":",count)    
    # d.append(b[i])
    # d.append(count)
    # if d not in a:
    #     a.append(d)
    i+=1
print(b[i],count)   
