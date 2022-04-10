list=["mam","dad","anuja","madam"]
i=0
d=[]
e=[]
while i<len(list):
    a=list[i]
    str=""
    
    j=1
    while j<len(list[i])+1:
        str+=list[i][-j]
        
        j+=1
    if a==str:
        d.append(str)
    else:
        e.append(str)
    i+=1

print(d)
print(e)

