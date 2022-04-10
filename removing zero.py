list1=[10,101,10000,10101]
i=0
a=[]
while i<len(list1):
    b=str(list1[i])
    c=""
    j=0
    while j<len(b):
        if b[j]!="0":
            c+=b[j]
        j+=1
    a.append(int(c))
    i+=1
print(a)
    